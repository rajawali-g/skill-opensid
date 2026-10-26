# -*- coding: utf-8 -*-
"""
Theme Validator & QA Certification Tool (Fitur 6)
Memeriksa kepatuhan struktur, sintaks Blade, manifest, dan kelayakan rilis tema OpenSID.
"""

import os
import sys
import json
import re

def validate_theme(theme_path):
    theme_name = os.path.basename(os.path.normpath(theme_path))
    print(f"[*] Menjalankan Validasi QA untuk Tema: '{theme_name}'")
    print(f"[*] Lokasi: {theme_path}")
    print("=" * 60)

    issues = []
    warnings = []
    passed = []

    # 1. Cek Berkas Manifes Wajib
    mandatory_files = [
        "config.json",
        "composer.json",
        "catatan_rilis.md",
        "index.html",
        os.path.join("resources", "views", "template.blade.php")
    ]

    for rel_file in mandatory_files:
        fpath = os.path.join(theme_path, rel_file)
        if os.path.exists(fpath):
            passed.append(f"Berkas wajib ditemukan: {rel_file}")
        else:
            issues.append(f"Berkas wajib hilang: {rel_file}")

    # 2. Cek Validitas JSON config.json & composer.json
    config_path = os.path.join(theme_path, "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                json.load(f)
            passed.append("config.json valid JSON")
        except Exception as e:
            issues.append(f"config.json corrupt: {str(e)}")

    composer_path = os.path.join(theme_path, "composer.json")
    if os.path.exists(composer_path):
        try:
            with open(composer_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            passed.append("composer.json valid JSON")
            if data.get("type") not in ["opensid-theme", "library"]:
                warnings.append("composer.json 'type' disarankan bernilai 'opensid-theme'")
        except Exception as e:
            issues.append(f"composer.json corrupt: {str(e)}")

    # 3. Pengecekan Sintaks Blade & Namespace theme::
    views_dir = os.path.join(theme_path, "resources", "views")
    if os.path.exists(views_dir):
        include_pattern = re.compile(r"@include(?:If)?\s*\(\s*['\"]([^'\"]+)['\"]")
        for root, _, files in os.walk(views_dir):
            for file in files:
                if file.endswith(".blade.php"):
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, theme_path)
                    try:
                        with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                        
                        # Cek include tanpa prefix theme::
                        matches = include_pattern.findall(content)
                        for m in matches:
                            if not m.startswith("theme::") and not m.startswith("$") and "{" not in m:
                                issues.append(f"{rel_p}: Pemanggilan '@include(\"{m}\")' tidak menggunakan namespace 'theme::'")
                    except Exception as e:
                        warnings.append(f"Gagal membaca berkas {rel_p}: {str(e)}")
        passed.append("Pemeriksaan namespace 'theme::' pada direktif Blade selesai")

    # 4. Cek Keberadaan Aset CSS & JS
    css_dir = os.path.join(theme_path, "assets", "css")
    if os.path.exists(css_dir) and any(f.endswith(".css") for f in os.listdir(css_dir)):
        passed.append("Aset stylesheet CSS tersedia")
    else:
        warnings.append("Tidak ditemukan file .css di assets/css/")

    # 5. Rekapitulasi Status Kelayakan
    print("\n--- HASIL PEMERIKSAAN QA ---")
    for p in passed:
        print(f"  [PASS] {p}")
    
    if warnings:
        print("\n--- PERINGATAN (WARNING) ---")
        for w in warnings:
            print(f"  [WARN] {w}")

    if issues:
        print("\n--- ISU / MASALAH KRITIS (FAIL) ---")
        for i in issues:
            print(f"  [FAIL] {i}")
        print("\n=> STATUS AKHIR: REVISION REQUIRED (Belum memenuhi kriteria rilis)")
        return False
    else:
        print("\n=> STATUS AKHIR: APPROVED (Lolos seluruh kriteria kelayakan rilis)")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan: python validate_theme.py <path_to_theme_folder>")
        print("Contoh: python validate_theme.py d:\\project_opensid\\themes_output\\tema-pedesaan-klasik")
        sys.exit(1)

    target_path = sys.argv[1]
    if not os.path.isdir(target_path):
        print(f"Error: Direktori tidak ditemukan: {target_path}")
        sys.exit(1)

    success = validate_theme(target_path)
    sys.exit(0 if success else 1)
