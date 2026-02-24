(async function(){
  const params = new URLSearchParams(location.search);
  const gameKey = params.get('game') || localStorage.getItem('meta_game') || 'warzone';
  try {
    const cfg = await (await fetch('config/games.json', {cache:'no-store'})).json();
    const game = cfg[gameKey] || cfg.warzone;
    localStorage.setItem('meta_game', Object.keys(cfg).includes(gameKey) ? gameKey : 'warzone');

    document.documentElement.style.setProperty('--accent', game.themeColor || '#00ff99');

    const brandEls = document.querySelectorAll('[data-brand]');
    brandEls.forEach(el => el.textContent = `${game.name} ${game.brandLabel || 'Meta Hub'}`);

    const t = document.querySelector('title');
    if (t) t.textContent = t.textContent.replace(/Warzone/gi, game.name);

    const desc = document.querySelector('meta[name="description"]');
    if (desc && desc.content) desc.setAttribute('content', desc.content.replace(/Warzone/gi, game.name));

    window.__GAME_CONFIG__ = game;
  } catch(e) {
    console.warn('[app-config] failed', e);
  }
})();
