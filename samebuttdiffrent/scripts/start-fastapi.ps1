<#
Start FastAPI via uvicorn (uses project venv if present). Writes PID to ../var/pids/fastapi-server.pid
#>
$scriptRoot = $PSScriptRoot
$root = Split-Path -Parent $scriptRoot
$appDir = Join-Path $root 'apps\fastapi'
$pidDir = Join-Path $root 'var\pids'
New-Item -Path $pidDir -ItemType Directory -Force | Out-Null

$venvCandidate = Join-Path $root '.venv\Scripts\python.exe'
if (Test-Path $venvCandidate) { $python = (Resolve-Path $venvCandidate).Path } else { $python = 'python' }
 $uvArgs = @('-m','uvicorn','n3FastAPI:app','--host','127.0.0.1','--port','8001')
try {
    $p = Start-Process -FilePath $python -ArgumentList $uvArgs -WorkingDirectory $appDir -PassThru
    $pidFile = Join-Path $pidDir 'fastapi-server.pid'
    if ($p -and $p.Id) { $p.Id | Out-File -FilePath $pidFile -Encoding ascii }
    Write-Output "Started FastAPI (working dir: $appDir)"
} catch {
    Write-Error "Failed to start FastAPI app: ${_}"
}
