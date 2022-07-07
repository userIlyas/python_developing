from datetime import date
from pathlib import Path

if Path('new.txt').exists():
    print('All correct! File if in directory!')
else:
    print('File is not in directory. Creating...')
    new = Path('new.txt').touch()


