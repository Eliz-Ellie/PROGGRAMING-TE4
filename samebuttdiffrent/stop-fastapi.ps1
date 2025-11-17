<#
Stop FastAPI (uvicorn) started by start-fastapi.ps1
Usage: .\stop-fastapi.ps1
#>
$pidFile = Join-Path $PSScriptRoot 'fastapi-server.pid'
if (Test-Path $pidFile) {
    $pid = Get-Content $pidFile
    try {
        Get-Process -Id $pid -ErrorAction SilentlyContinue | Stop-Process -Force
        Remove-Item $pidFile -ErrorAction SilentlyContinue
        Write-Output "Stopped FastAPI (PID $pid)"
    } catch {
        Write-Warning "Failed to stop process ${pid}: ${_}"
    }
} else {
    Write-Output "PID file not found. No FastAPI process to stop or it wasn't started with start-fastapi.ps1."
}
