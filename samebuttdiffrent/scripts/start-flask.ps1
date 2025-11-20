<#
Start the Flask app using the project venv if available. Writes PID to ../var/pids/flask-server.pid
#>
$scriptRoot = $PSScriptRoot
$root = Split-Path -Parent $scriptRoot
$appDir = Join-Path $root 'apps\flask'
$pidDir = Join-Path $root 'var\pids'
New-Item -Path $pidDir -ItemType Directory -Force | Out-Null

$venvCandidate = Join-Path $root '.venv\Scripts\python.exe'
if (Test-Path $venvCandidate) { $python = (Resolve-Path $venvCandidate).Path } else { $python = 'python' }

try {
    $p = Start-Process -FilePath $python -ArgumentList 'n2FLASK.py' -WorkingDirectory $appDir -PassThru
    $pidFile = Join-Path $pidDir 'flask-server.pid'
    if ($p -and $p.Id) { $p.Id | Out-File -FilePath $pidFile -Encoding ascii }
    Write-Output "Started Flask (working dir: $appDir)"
} catch {
    Write-Error "Failed to start Flask app: ${_}"
}
