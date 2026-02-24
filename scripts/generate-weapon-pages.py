#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEAPONS = ROOT / 'assets' / 'weapons.json'
OUT = ROOT / 'weapons'
OUT.mkdir(exist_ok=True)

TPL = """<!DOCTYPE html>
<html lang=\"en\"><head>
<meta charset=\"UTF-8\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
<title>{title}</title>
<meta name=\"description\" content=\"{desc}\" />
<link rel=\"stylesheet\" href=\"../style.css\" />
<link rel=\"icon\" type=\"image/png\" href=\"../assets/logo-wm.png\" />
</head><body>
<nav><div class=\"nav-logo\"><img src=\"../assets/logo-shield.png\" alt=\"logo\" class=\"nav-logo-img\"/><span data-brand>Warzone Meta Hub</span></div>
<ul class=\"nav-links\"><li><a href=\"../index.html\">Tier List</a></li><li><a href=\"../patch-notes.html\">Patch Notes</a></li><li><a href=\"../shop.html\">Shop</a></li></ul></nav>
<div class=\"section\"><div class=\"section-head\"><h1>{h1}</h1><p class=\"muted\">{sub}</p></div>
<div class=\"content-card\"><h2>Weapon Stats</h2><ul><li>Tier: {tier}</li><li>Class: {klass}</li><li>Mode: {mode}</li><li>Damage: {damage}</li><li>Range: {range}</li><li>Mobility: {mobility}</li><li>Control: {control}</li></ul></div>
<div class=\"content-card\"><h2>Best Attachments</h2><ul>{atts}</ul></div>
<div class=\"content-card seo-copy\"><h2>Meta Explanation</h2><p>{explain}</p><p><a href=\"../index.html\">Back to tier list</a> · <a href=\"../patch-notes.html\">See patch notes</a> · <a href=\"../shop.html\">Build setup gear</a></p></div>
</div>
<script src=\"../assets/app-config.js\"></script>
</body></html>"""


def slug(s):
    return re.sub(r'(^-|-$)', '', re.sub(r'[^a-z0-9]+', '-', s.lower()))


def li(items):
    if not items: return '<li>No recommended attachments listed</li>'
    return ''.join(f'<li>{i}</li>' for i in items)


def main():
    data = json.loads(WEAPONS.read_text())
    for w in data.get('weapons', []):
        s = slug(w['name'])
        atts = li(w.get('attachments', []))
        explain = (w.get('strengths') or ['Competitive pick in the current season meta.'])[0]

        pages = [
            (f'best-loadouts-{s}.html', f"Best Loadout for {w['name']} ({w['class']})", f"Best {w['name']} loadout with attachments and stat profile.", f"Best Loadout: {w['name']}"),
            (f'{s}-meta-build.html', f"{w['name']} Meta Build & Attachments", f"Meta build for {w['name']} with top attachment setup.", f"{w['name']} Meta Build"),
            (f'{s}-ttk-guide.html', f"{w['name']} TTK Guide", f"TTK guide and control profile for {w['name']} in current meta.", f"{w['name']} TTK Guide"),
        ]

        for fname, title, desc, h1 in pages:
            html = TPL.format(
                title=title, desc=desc, h1=h1, sub=f"Updated profile for {w['name']}",
                tier=w.get('tier','-'), klass=w.get('class','-'), mode=w.get('mode','-'),
                damage=w.get('damage','-'), range=w.get('range','-'), mobility=w.get('mobility','-'), control=w.get('control','-'),
                atts=atts, explain=explain
            )
            (OUT / fname).write_text(html)

    print(f"generated {len(list(OUT.glob('*.html')))} weapon pages")


if __name__ == '__main__':
    main()
