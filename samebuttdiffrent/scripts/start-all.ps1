<#
Start all apps (php, flask, fastapi)
#>
$scriptRoot = $PSScriptRoot
& (Join-Path $scriptRoot 'start-php.ps1')
& (Join-Path $scriptRoot 'start-flask.ps1')
& (Join-Path $scriptRoot 'start-fastapi.ps1')
Write-Output "All start scripts invoked."
