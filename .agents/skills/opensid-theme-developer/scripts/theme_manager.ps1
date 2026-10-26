<#
.SYNOPSIS
    OpenSID Theme Generator, Packager & Deployer Wrapper
.DESCRIPTION
    Wrapper PowerShell untuk theme_manager.py
.EXAMPLE
    .\theme_manager.ps1 -Action new -Name "tema-starter-minsel" -Title "Tema Starter Minsel"
    .\theme_manager.ps1 -Action package -Name "tema-starter-minsel"
    .\theme_manager.ps1 -Action list
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

$scriptPy = Join-Path $PSScriptRoot "theme_manager.py"
$params = @($scriptPy, $Action)

if ($Name) { $params += @("--name", $Name) }
if ($Title) { $params += @("--title", $Title) }
if ($Author) { $params += @("--author", $Author) }
if ($Target) { $params += @("--target", $Target) }

python @params
