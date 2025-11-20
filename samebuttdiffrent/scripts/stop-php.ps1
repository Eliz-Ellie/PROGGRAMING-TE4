<#
Stop PHP server started by scripts\start-php.ps1
#>
$scriptRoot = $PSScriptRoot
$root = Split-Path -Parent $scriptRoot
$pidFile = Join-Path $root 'var\pids\php-server.pid'
if (Test-Path $pidFile) {
    $thePid = Get-Content $pidFile
    try {
       Get-Process -Id $thePid -ErrorAction SilentlyContinue | Stop-Process -Force
        Remove-Item $pidFile -ErrorAction SilentlyContinue
       Write-Output "Stopped PHP server (PID ${thePid})"
    } catch {
       Write-Warning "Failed to stop process ${thePid}: ${_}"
    }
} else {
    Write-Output "PID file not found: $pidFile"
}
