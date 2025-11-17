<#
Start the Flask app (n2FLASK.py) using the workspace virtualenv Python if present.
Usage: .\start-flask.ps1
#>
$venvCandidate = Join-Path $PSScriptRoot '..\.venv\Scripts\python.exe'
if (Test-Path $venvCandidate) {
    $python = (Resolve-Path $venvCandidate).Path
} else {
    $python = 'python'
}
try {
    $p = Start-Process -FilePath $python -ArgumentList 'n2FLASK.py' -WorkingDirectory $PSScriptRoot -PassThru
    $p.Id | Out-File -FilePath (Join-Path $PSScriptRoot 'flask-server.pid') -Encoding ascii
    Write-Output "Started Flask (PID $($p.Id)) on http://127.0.0.1:5000"
} catch {
    Write-Error "Failed to start Flask app. Error: $_"
}
