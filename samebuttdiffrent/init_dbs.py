"""
Wrapper: run the data/init_dbs.py initializer (locations moved).
Usage: python init_dbs.py
"""
import runpy
import sys
from pathlib import Path

root = Path(__file__).parent
target = root / 'data' / 'init_dbs.py'
if not target.exists():
  print(f"Initializer not found: {target}")
  sys.exit(1)
runpy.run_path(str(target), run_name='__main__')