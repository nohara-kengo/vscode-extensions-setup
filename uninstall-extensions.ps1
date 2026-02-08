$scriptDir = Join-Path -Path $PSScriptRoot -ChildPath "scripts\extensions\uninstall"

if (!(Test-Path $scriptDir)) {
    Write-Error "scripts\\extensions\\uninstall が見つかりません: $scriptDir"
    exit 1
}

$scripts = Get-ChildItem -Path $scriptDir -Filter "*.ps1" | Sort-Object Name

if (-not $scripts) {
    Write-Warning "実行対象のアンインストールスクリプトが見つかりません ($scriptDir)"
    exit 0
}

foreach ($s in $scripts) {
    Write-Host "Running $($s.Name)..."
    & $s.FullName
}

Write-Host "Extension uninstall completed."