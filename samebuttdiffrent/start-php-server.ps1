<#
Start PHP built-in server for this folder and record its PID so it can be stopped later.
Usage: Open PowerShell in this folder and run: .\start-php-server.ps1
#>
$port = 8000
$docroot = $PSScriptRoot
try {
    $p = Start-Process -FilePath php -ArgumentList "-S localhost:$port" -WorkingDirectory $docroot -PassThru
    $p.Id | Out-File -FilePath (Join-Path $PSScriptRoot 'php-server.pid') -Encoding ascii
    Write-Output "Started PHP server (PID $($p.Id)) on http://localhost:$port"
} catch {
    Write-Error "Failed to start PHP server. Ensure 'php' is on PATH or install PHP. Error: $_"
}
