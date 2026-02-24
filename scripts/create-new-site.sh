#!/bin/zsh
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: ./scripts/create-new-site.sh <game-key>"
  exit 1
fi

GAME_KEY="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${ROOT}/../site-${GAME_KEY}"

mkdir -p "$TARGET_DIR"
rsync -a --exclude '.git' --exclude 'node_modules' "$ROOT/" "$TARGET_DIR/"

# switch default game in app-config by storing local preference at build-time hint
python3 - <<PY
from pathlib import Path
p=Path('$TARGET_DIR/README.md')
t=p.read_text() if p.exists() else ''
if 'Default game key:' not in t:
    t += f"\n\nDefault game key: { '$GAME_KEY' }\n"
p.write_text(t)
print('cloned to', '$TARGET_DIR')
PY

echo "Created: $TARGET_DIR"
echo "Next: update config/games.json dataSource for '$GAME_KEY' and deploy."
