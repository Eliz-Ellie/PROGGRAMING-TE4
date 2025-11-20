# samebuttdiffrent — local dev servers

- This folder contains three demo apps and small PowerShell helper scripts organized for local development.

Project layout (inside this folder)
- `apps/php/` — PHP app (docroot)
- `apps/flask/` — Flask app
- `apps/fastapi/` — FastAPI app
- `scripts/` — helper PowerShell scripts to start/stop apps
- `data/` — SQLite databases (php.db, flask.db, fastapi.db)
- `var/pids/` — runtime pid files created by the scripts

Apps and ports
- PHP (apps/php) — http://localhost:8000
- Flask (apps/flask) — http://127.0.0.1:5000
- FastAPI (apps/fastapi) — http://127.0.0.1:8001

Quick start
1. Open PowerShell and change to this folder:
    ```powershell
    Set-Location 'C:\Users\Albin\github\PROGGRAMING-TE4\samebuttdiffrent'
    ```
2. Initialize the databases (one-time):
    ```powershell
    python data/init_dbs.py
    ```
3. Start all servers (they run detached and write pid files):
    - Recommended (ensures script runs even if your session blocks scripts):
       ```powershell
       powershell -NoProfile -ExecutionPolicy Bypass -Command "& '$PWD\\scripts\\start-all.ps1'"
       ```
    - Or (if your PowerShell allows running scripts):
       ```powershell
       .\scripts\start-all.ps1
       ```
4. Verify in your browser:
    - http://localhost:8000/n1.php
    - http://127.0.0.1:5000/
    - http://127.0.0.1:8001/

Stopping servers
- Stop all (recommended):
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -Command "& '$PWD\\scripts\\stop-all.ps1'"
   ```
- Or:
   ```powershell
   .\scripts\stop-all.ps1
   ```
- Or stop individual servers with `.\stop-php-server.ps1`, `.\stop-flask.ps1`, or `.\stop-fastapi.ps1`.

Notes
- The PHP script requires `php` on your PATH for `start-php-server.ps1` to work. (You can use the user-level Scoop install or other installer.)
- The Python scripts prefer the workspace virtualenv at `../.venv`. If it exists, the start scripts will use it; otherwise they fall back to `python` on PATH.
- Each start script writes a pid file in this folder (e.g., `flask-server.pid`). Stop scripts use those files to stop the correct processes.

If you want, I can add a small `Makefile` or a single master script to control everything from the repository root.
