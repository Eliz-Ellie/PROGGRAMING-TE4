<#
Stop Flask started by scripts\start-flask.ps1
#>
$scriptRoot = $PSScriptRoot
$root = Split-Path -Parent $scriptRoot
$pidFile = Join-Path $root 'var\pids\flask-server.pid'
if (Test-Path $pidFile) {
    $thePid = Get-Content $pidFile
    try {
        Get-Process -Id $thePid -ErrorAction SilentlyContinue | Stop-Process -Force
        Remove-Item $pidFile -ErrorAction SilentlyContinue
        Write-Output "Stopped Flask (PID ${thePid})"
    } catch {
        Write-Warning "Failed to stop process ${thePid}: ${_}"
    }
} else {
    Write-Output "PID file not found: $pidFile"
}
