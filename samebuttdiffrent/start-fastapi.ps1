<#
Start the FastAPI app (n3FastAPI.py) with uvicorn using the workspace venv python if present.
Usage: .\start-fastapi.ps1
#>
$venvCandidate = Join-Path $PSScriptRoot '..\.venv\Scripts\python.exe'
if (Test-Path $venvCandidate) {
    $python = (Resolve-Path $venvCandidate).Path
} else {
    $python = 'python'
}
$args = @('-m','uvicorn','n3FastAPI:app','--host','127.0.0.1','--port','8001')
try {
    $p = Start-Process -FilePath $python -ArgumentList $args -WorkingDirectory $PSScriptRoot -PassThru
    $p.Id | Out-File -FilePath (Join-Path $PSScriptRoot 'fastapi-server.pid') -Encoding ascii
    Write-Output "Started FastAPI (PID $($p.Id)) on http://127.0.0.1:8001"
} catch {
    Write-Error "Failed to start FastAPI app. Error: $_"
}
