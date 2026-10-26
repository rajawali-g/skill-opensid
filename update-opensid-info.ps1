<#
.SYNOPSIS
    Shortcut Pembaruan Informasi Versi OpenSID dari GitHub
.DESCRIPTION
    Menjalankan fetch_opensid_info.py untuk menyinkronkan data rilis umum OpenSID
    (versi, backend, frontend, kebutuhan PHP) langsung dari GitHub resmi OpenSID/OpenSID.
#>

Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "  Update Informasi Versi OpenSID dari GitHub     " -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

$scriptPath = Join-Path $PSScriptRoot ".agents\skills\opensid\scripts\fetch_opensid_info.py"
if (Test-Path $scriptPath) {
    python $scriptPath
    Write-Host "`n✅ Informasi versi OpenSID berhasil diperbarui!" -ForegroundColor Green
    Write-Host "Lihat berkas: .agents/skills/opensid/references/opensid-version-info.md" -ForegroundColor Yellow
} else {
    Write-Error "Berkas skrip tidak ditemukan: $scriptPath"
}
