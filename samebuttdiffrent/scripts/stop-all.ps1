<#
Stop all apps
#>
$scriptRoot = $PSScriptRoot
& (Join-Path $scriptRoot 'stop-php.ps1')
& (Join-Path $scriptRoot 'stop-flask.ps1')
& (Join-Path $scriptRoot 'stop-fastapi.ps1')
Write-Output "All stop scripts invoked."
