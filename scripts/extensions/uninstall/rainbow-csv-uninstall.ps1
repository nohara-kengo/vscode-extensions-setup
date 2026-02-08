$ext = "mechatroner.rainbow-csv"
$installed = code --list-extensions
if ($installed -notcontains $ext) { Write-Host "Not installed: $ext"; exit 0 }
Write-Host "Uninstalling $ext..."
code --uninstall-extension $ext
Write-Host "Uninstall completed: $ext"