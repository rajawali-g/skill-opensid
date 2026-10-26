<#
.SYNOPSIS
    Shortcut Pengelola Tema OpenSID
.DESCRIPTION
    Jalankan untuk mengelola pembuatan tema di themes_output/:
    - Buat tema baru: .\manage-theme.ps1 -Action new -Name "nama-tema" -Title "Judul Tema"
    - Kemas ke ZIP:   .\manage-theme.ps1 -Action package -Name "nama-tema"
    - Daftar tema:    .\manage-theme.ps1 -Action list
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("new", "package", "deploy", "list")]
    [string]$Action,

    [Parameter(Mandatory = $false)]
    [string]$Name,

    [Parameter(Mandatory = $false)]
    [string]$Title = "Tema Desa Modern",

    [Parameter(Mandatory = $false)]
    [string]$Author = "Tim Pengembang Desa",

    [Parameter(Mandatory = $false)]
    [string]$Target
)

$managerScript = Join-Path $PSScriptRoot ".agents\skills\opensid\scripts\theme_manager.ps1"
& $managerScript @PSBoundParameters
