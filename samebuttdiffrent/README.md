# samebuttdiffrent — local dev servers

This folder contains three demo apps and small PowerShell helper scripts to run them locally for development.

Apps and ports
- `n1.php` — PHP built-in server on http://localhost:8000
- `n2FLASK.py` — Flask app on http://127.0.0.1:5000
- `n3FastAPI.py` — FastAPI (uvicorn) on http://127.0.0.1:8001

Quick start
1. Open PowerShell and change to this folder:
   ```powershell
   Set-Location 'C:\Users\Albin\github\PROGGRAMING-TE4\samebuttdiffrent'
   ```
2. Start all servers (they run detached and write pid files):
   ```powershell
   .\start-all.ps1
   ```
3. Verify in your browser:
   - http://localhost:8000/n1.php
   - http://127.0.0.1:5000/
   - http://127.0.0.1:8001/

Stopping servers
- Stop all:
  ```powershell
  .\stop-all.ps1
  ```
- Or stop individual servers with `.\stop-php-server.ps1`, `.\stop-flask.ps1`, or `.\stop-fastapi.ps1`.

Notes
- The PHP script requires `php` on your PATH for `start-php-server.ps1` to work. (You can use the user-level Scoop install or other installer.)
- The Python scripts prefer the workspace virtualenv at `../.venv`. If it exists, the start scripts will use it; otherwise they fall back to `python` on PATH.
- Each start script writes a pid file in this folder (e.g., `flask-server.pid`). Stop scripts use those files to stop the correct processes.

If you want, I can add a small `Makefile` or a single master script to control everything from the repository root.
