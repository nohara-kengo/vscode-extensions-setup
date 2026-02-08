$ext = "mhutchie.git-graph"
$installed = code --list-extensions
if ($installed -contains $ext) { Write-Host "Already installed: $ext"; exit 0 }
Write-Host "Installing $ext..."
code --install-extension $ext
