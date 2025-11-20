import sqlite3
from pathlib import Path

folder = Path(__file__).parent
dbs = {
    'php.db': folder / 'php.db',
    'flask.db': folder / 'flask.db',
    'fastapi.db': folder / 'fastapi.db',
}
schema = """
CREATE TABLE IF NOT EXISTS names (
  name TEXT PRIMARY KEY,
  count INTEGER NOT NULL
);
"""

for name, path in dbs.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print(f"Initialized {path}")
