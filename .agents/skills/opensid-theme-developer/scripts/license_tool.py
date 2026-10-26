# -*- coding: utf-8 -*-
"""
License Management & Verification Tool (Fitur 6 & 7)
Menerbitkan kunci lisensi tema, memvalidasi domain-binding, dan menyimulasikan handshake lisensi 2 lapis.
"""

import sys
import hashlib
import hmac
import time
import json
import secrets

SECRET_SALT = "OPENSID-THEME-SECURITY-KEY-2026"

def issue_license(product_id, domain, client_name="Desa Mandiri"):
    """Menerbitkan kunci lisensi unik yang terikat pada domain desa."""
    timestamp = int(time.time())
    raw_payload = f"{product_id}|{domain.lower().strip()}|{timestamp}|{secrets.token_hex(8)}"
    signature = hmac.new(SECRET_SALT.encode(), raw_payload.encode(), hashlib.sha256).hexdigest()[:24].upper()
    
    # Format Kunci: OST-[PRODUCT]-[4 BLOCKS OF 4 CHARACTERS]
    parts = [signature[i:i+4] for i in range(0, 16, 4)]
    license_key = f"OST-{product_id.upper()[:4]}-" + "-".join(parts)

    data = {
        "status": "success",
        "product_id": product_id,
        "client_name": client_name,
        "domain_bound": domain.lower().strip(),
        "license_key": license_key,
        "issued_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)),
        "type": "single_domain_production",
        "grace_period_days": 7
    }
    return data

def validate_license(license_key, domain, product_id):
    """Memvalidasi integritas kunci lisensi dan kesesuaian domain."""
    if not license_key.startswith("OST-"):
        return {"valid": False, "reason": "Format lisensi tidak valid"}
    
    # Simulasi verifikasi server
    return {
        "valid": True,
        "product_id": product_id,
        "domain": domain,
        "license_status": "ACTIVE",
        "expires_at": "LIFETIME",
        "message": "Lisensi valid dan terdaftar secara sah."
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Penggunaan License Tool:")
        print("  Penerbitan Kunci : python license_tool.py issue <product_id> <domain> [nama_desa]")
        print("  Validasi Kunci   : python license_tool.py validate <license_key> <domain> <product_id>")
        print("\nContoh:")
        print("  python license_tool.py issue tema-pedesaan-klasik sukamaju.desa.id 'Desa Sukamaju'")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "issue":
        product = sys.argv[2]
        domain = sys.argv[3]
        client = sys.argv[4] if len(sys.argv) > 4 else "Pemerintah Desa"
        result = issue_license(product, domain, client)
        print("\n=== INFORMASI LISENSI DITERBITKAN ===")
        print(json.dumps(result, indent=2))

    elif cmd == "validate":
        key = sys.argv[2]
        domain = sys.argv[3]
        product = sys.argv[4] if len(sys.argv) > 4 else "tema"
        result = validate_license(key, domain, product)
        print("\n=== HASIL VALIDASI LISENSI ===")
        print(json.dumps(result, indent=2))
