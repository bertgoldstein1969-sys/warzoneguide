# FPS Meta Site Engine (Warzone instance)

This instance runs a config-driven FPS meta site with monetization + retention features.

## Engine components
- Game registry: `config/games.json`
- Branding/data bootstrap: `assets/app-config.js`
- Weapon SEO page generator: `scripts/generate-weapon-pages.py`
- Clone helper: `scripts/create-new-site.sh <game-key>`
- CSS minifier helper: `scripts/minify-css.sh`

## Data dependencies
- Trend/snapshot feed (primary): `warzone-data/weapon-trends.json`
- News/patch feed: `warzone-data/warzone-data.json`

## Commands
```bash
python3 scripts/generate-weapon-pages.py
./scripts/minify-css.sh
./scripts/create-new-site.sh bo7
```
