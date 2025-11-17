<#
Stop PHP built-in server started by `start-php-server.ps1`.
Usage: .\stop-php-server.ps1
#>
$pidFile = Join-Path $PSScriptRoot 'php-server.pid'
if (Test-Path $pidFile) {
    $pid = Get-Content $pidFile
    try {
        Get-Process -Id $pid -ErrorAction SilentlyContinue | Stop-Process -Force
        Remove-Item $pidFile -ErrorAction SilentlyContinue
        Write-Output "Stopped PHP server (PID $pid)"
    } catch {
        Write-Warning "Failed to stop process ${pid}: ${_}"
    }
} else {
    Write-Output "PID file not found. No PHP server to stop or it wasn't started with start-php-server.ps1."
}
