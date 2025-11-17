<#
Start PHP built-in server for this folder and record its PID so it can be stopped later.
Usage: Open PowerShell in this folder and run: .\start-php-server.ps1
#>
$port = 8000
$docroot = $PSScriptRoot

# Resolve php executable: prefer command on PATH, then common user-level locations
$phpExe = $null
$cmd = Get-Command php -ErrorAction SilentlyContinue
if ($cmd) { $phpExe = $cmd.Source }
elseif (Test-Path "$env:USERPROFILE\scoop\shims\php.exe") { $phpExe = "$env:USERPROFILE\scoop\shims\php.exe" }
elseif (Test-Path 'C:\ProgramData\chocolatey\bin\php.exe') { $phpExe = 'C:\ProgramData\chocolatey\bin\php.exe' }
elseif (Test-Path 'C:\tools\php\php.exe') { $phpExe = 'C:\tools\php\php.exe' }

if (-not $phpExe) {
    Write-Error "Failed to start PHP server. 'php' not found on PATH and no known install detected. Please install PHP or add it to PATH."
    return
}

try {
    $p = Start-Process -FilePath $phpExe -ArgumentList "-S localhost:$port" -WorkingDirectory $docroot -PassThru
    $pidFile = Join-Path $PSScriptRoot 'php-server.pid'
    # Try to write the returned PID. If Start-Process didn't return an Id in this context, try to discover the pid by the listening port.
    if ($p -and $p.Id) {
        $p.Id | Out-File -FilePath $pidFile -Encoding ascii
        Write-Output "Started PHP server (PID $($p.Id)) on http://localhost:$port using $phpExe"
    } else {
        Start-Sleep -Milliseconds 200
        $conn = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
        if ($conn -and $conn.OwningProcess) {
            $conn.OwningProcess | Out-File -FilePath $pidFile -Encoding ascii
            Write-Output "Started PHP server (detected PID $($conn.OwningProcess)) on http://localhost:$port using $phpExe"
        } else {
            Write-Warning "Started PHP server but could not determine PID. The server may be running on http://localhost:$port"
        }
    }
} catch {
    Write-Error "Failed to start PHP server using $phpExe. Error: ${_}"
}
