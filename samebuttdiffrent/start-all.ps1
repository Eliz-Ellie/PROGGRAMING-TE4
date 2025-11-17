<#
Start all demo servers (PHP, Flask, FastAPI) in this folder.
Usage: .\start-all.ps1
This will call each start-*.ps1. Servers will run detached and write pid files.
#>
& "$PSScriptRoot\start-php-server.ps1"
& "$PSScriptRoot\start-flask.ps1"
& "$PSScriptRoot\start-fastapi.ps1"
Write-Output "All start scripts invoked. Check individual pid files in this folder."
