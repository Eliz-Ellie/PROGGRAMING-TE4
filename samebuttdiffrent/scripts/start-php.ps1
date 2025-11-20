<#
Start PHP built-in server for the php app. Writes PID into ../var/pids/php-server.pid
Usage: run from any folder: powershell -NoProfile -ExecutionPolicy Bypass -Command "& '...\\scripts\\start-php.ps1'"
#>
$scriptRoot = $PSScriptRoot
$root = Split-Path -Parent $scriptRoot
$appDir = Join-Path $root 'apps\php'
$dataDir = Join-Path $root 'data'
$pidDir = Join-Path $root 'var\pids'
New-Item -Path $pidDir -ItemType Directory -Force | Out-Null

$port = 8000

# Resolve php executable
$phpExe = $null
$cmd = Get-Command php -ErrorAction SilentlyContinue
if ($cmd) { $phpExe = $cmd.Source }
elseif (Test-Path "$env:USERPROFILE\scoop\shims\php.exe") { $phpExe = "$env:USERPROFILE\scoop\shims\php.exe" }
elseif (Test-Path 'C:\ProgramData\chocolatey\bin\php.exe') { $phpExe = 'C:\ProgramData\chocolatey\bin\php.exe' }
elseif (Test-Path 'C:\tools\php\php.exe') { $phpExe = 'C:\tools\php\php.exe' }

if (-not $phpExe) {
    Write-Error "'php' not found. Install PHP or add to PATH."
    return
}

try {
    $p = Start-Process -FilePath $phpExe -ArgumentList "-S localhost:$port -t `"$appDir`"" -WorkingDirectory $appDir -PassThru
    $pidFile = Join-Path $pidDir 'php-server.pid'
    if ($p -and $p.Id) { $p.Id | Out-File -FilePath $pidFile -Encoding ascii }
    else {
        Start-Sleep -Milliseconds 200
        $conn = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
        if ($conn -and $conn.OwningProcess) { $conn.OwningProcess | Out-File -FilePath $pidFile -Encoding ascii }
    }
    Write-Output "Started PHP server on http://localhost:$port (app dir: $appDir)"
} catch {
    Write-Error "Failed to start PHP server: ${_}"
}
