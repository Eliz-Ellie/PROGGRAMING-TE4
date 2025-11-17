<#
Stop Flask app started by start-flask.ps1
Usage: .\stop-flask.ps1
#>
$pidFile = Join-Path $PSScriptRoot 'flask-server.pid'
if (Test-Path $pidFile) {
    $pid = Get-Content $pidFile
    try {
        Get-Process -Id $pid -ErrorAction SilentlyContinue | Stop-Process -Force
        Remove-Item $pidFile -ErrorAction SilentlyContinue
        Write-Output "Stopped Flask (PID $pid)"
    } catch {
        Write-Warning "Failed to stop process ${pid}: ${_}"
    }
} else {
    Write-Output "PID file not found. No Flask process to stop or it wasn't started with start-flask.ps1."
}
