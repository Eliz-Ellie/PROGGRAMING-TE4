<#
Stop all demo servers (PHP, Flask, FastAPI) started by the start scripts.
Usage: .\stop-all.ps1
#>
& "$PSScriptRoot\stop-php-server.ps1"
& "$PSScriptRoot\stop-flask.ps1"
& "$PSScriptRoot\stop-fastapi.ps1"
Write-Output "All stop scripts invoked."
