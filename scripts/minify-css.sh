#!/bin/zsh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
from pathlib import Path
p=Path('style.css')
out=Path('style.min.css')
css=p.read_text()
# simple minify
import re
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
css=re.sub(r'\s+',' ',css)
css=re.sub(r'\s*([{}:;,])\s*',r'\1',css)
css=css.strip()
out.write_text(css)
print('wrote',out)
PY
