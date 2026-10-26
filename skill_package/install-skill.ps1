# ==============================================================================
# Skrip Pemasangan Otomatis AI Skill OpenSID Theme Developer untuk Antigravity
# ==============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [ValidateSet("all", "global", "workspace")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"

$currentDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$skillSourceDir = Join-Path $currentDir "opensid-theme-developer"

# Fallback jika dijalankan dari root repository
if (-not (Test-Path $skillSourceDir)) {
    $skillSourceDir = Join-Path $currentDir ".agents\skills\opensid"
}

if (-not (Test-Path $skillSourceDir)) {
    Write-Error "Direktori sumber skill tidak ditemukan di: $skillSourceDir"
    exit 1
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  INSTALLER: AI SKILL OPENSID THEME DEVELOPER             " -ForegroundColor Cyan
Write-Host "  Platform: Google Antigravity / Gemini CLI / AI Agent    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Lokasi Global Antigravity
$globalConfigDir = Join-Path $env:USERPROFILE ".gemini\config\skills\opensid-theme-developer"

# 2. Lokasi Workspace Aktif
$workspaceDir = Join-Path (Get-Location) ".agents\skills\opensid-theme-developer"

function Install-Skill([string]$destPath, [string]$label) {
    Write-Host "`n[*] Memasang ke $label..." -ForegroundColor Yellow
    Write-Host "    Target: $destPath" -ForegroundColor Gray
    
    if (Test-Path $destPath) {
        Remove-Item -Path $destPath -Recurse -Force
    }
    
    New-Item -ItemType Directory -Path $destPath -Force | Out-Null
    Copy-Item -Path "$skillSourceDir\*" -Destination $destPath -Recurse -Force
    Write-Host "    [OK] Berhasil dipasang ke $label!" -ForegroundColor Green
}

if ($Target -eq "all" -or $Target -eq "global") {
    Install-Skill -destPath $globalConfigDir -label "Global Antigravity (~/.gemini/config/skills/)"
}

if ($Target -eq "all" -or $Target -eq "workspace") {
    Install-Skill -destPath $workspaceDir -label "Workspace Lokal (.agents/skills/)"
}

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host "  INSTALASI SELESAI & SKILL TELAH SIAP DIGUNAKAN!        " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "Cara menggunakan skill di Antigravity IDE:" -ForegroundColor White
Write-Host "1. Buka sesi chat Antigravity." -ForegroundColor Gray
Write-Host "2. Ketik prompt seperti:" -ForegroundColor Yellow
Write-Host "   - 'Tolong buatkan tema baru OpenSID nuansa islami modern'" -ForegroundColor Gray
Write-Host "   - 'Periksa rilis OpenSID Free terbaru dari GitHub'" -ForegroundColor Gray
Write-Host "   - 'Validasi tema di folder themes_output/tema-desa-modern'" -ForegroundColor Gray
Write-Host "   - 'Terbitkan lisensi untuk domain desa-sukamaju.desa.id'" -ForegroundColor Gray
Write-Host "==========================================================`n" -ForegroundColor Cyan
