<#
.SYNOPSIS
    Skrip Otomatisasi Versi (TAG & RELEASE) untuk GitHub skill-opensid
.DESCRIPTION
    Menghasilkan versi berformat v[TAG].[RELEASE] (Contoh: v2610.002)
    - TAG = Tahun (2 digit) + Bulan (2 digit) -> 2610
    - RELEASE = Nomor urut 3 digit berurutan pada bulan tersebut -> 001, 002, dst.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [string]$Message = "Pembaruan rilis Skill OpenSID",

    [Parameter(Mandatory = $false)]
    [switch]$NoPush
)

$ErrorActionPreference = "Stop"

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  Automated Versioning: TAG & RELEASE System " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# 1. Hitung TAG
$now = Get-Date
$tag = $now.ToString("yyMM")

Write-Host "Periode TAG saat ini: $tag ($($now.ToString('MMMM yyyy')))" -ForegroundColor Yellow

# 2. Cari nomor RELEASE terakhir di git tag pada bulan ini
$allTags = @()
try {
    $allTags = git tag --list "v$($tag).*" 2>$null
} catch {}

$maxRelease = 0
foreach ($t in $allTags) {
    if ($t -match "^v$($tag)\.(\d+)$") {
        $num = [int]$matches[1]
        if ($num -gt $maxRelease) {
            $maxRelease = $num
        }
    }
}

$nextReleaseNum = $maxRelease + 1
$releaseStr = "{0:D3}" -f $nextReleaseNum
$fullVersion = "v$($tag).$($releaseStr)"

Write-Host "Versi Baru Dihasilkan: $fullVersion" -ForegroundColor Green
Write-Host "   - TAG     : $tag" -ForegroundColor Gray
Write-Host "   - RELEASE : $releaseStr" -ForegroundColor Gray
Write-Host "   - Catatan : $Message" -ForegroundColor Gray

# 3. Update Badge di README.md
$readmePath = Join-Path $PSScriptRoot "README.md"
if (Test-Path $readmePath) {
    $readmeContent = [System.IO.File]::ReadAllText($readmePath, [System.Text.Encoding]::UTF8)
    $readmeUpdated = $readmeContent -replace 'Release-v\d{4}\.\d{3}-brightgreen', "Release-$($fullVersion)-brightgreen"
    [System.IO.File]::WriteAllText($readmePath, $readmeUpdated, [System.Text.Encoding]::UTF8)
    Write-Host "README.md diperbarui dengan versi $fullVersion." -ForegroundColor Green
}

# 4. Git Commit & Tag
Write-Host "`nMenjalankan Git Commit & Tag..." -ForegroundColor Yellow
git add .
git commit -m "release: $fullVersion - $Message"
git tag -a "$fullVersion" -m "Release ${fullVersion}: $Message"

Write-Host "Git tag $fullVersion berhasil dibuat!" -ForegroundColor Green

# 5. Git Push
if (-not $NoPush) {
    Write-Host "`nMelakukan Push ke Remote GitHub (origin main --tags)..." -ForegroundColor Yellow
    try {
        git push origin main --tags
        Write-Host "Berhasil dipublikasikan ke https://github.com/rajawali-g/skill-opensid !" -ForegroundColor Green
    } catch {
        Write-Warning "Push otomatis gagal atau remote belum terotorisasi. Jalankan manual:`n  git push origin main --tags"
    }
} else {
    Write-Host "Flag -NoPush aktif. Push ke remote dilewati." -ForegroundColor Cyan
}

Write-Host "`nSelesai! Versi aktif saat ini: $fullVersion" -ForegroundColor Cyan
