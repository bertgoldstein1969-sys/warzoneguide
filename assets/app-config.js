(async function(){
  const params = new URLSearchParams(location.search);
  const routeKey = location.pathname.split('/').filter(Boolean)[0] || '';
  const gameKey = params.get('game') || (['warzone','bo7','bf6','fortnite'].includes(routeKey) ? routeKey : (localStorage.getItem('meta_game') || 'warzone'));
  try {
    const cfg = await (await fetch('config/games.json', {cache:'no-store'})).json();
    const game = cfg[gameKey] || cfg.warzone;
    localStorage.setItem('meta_game', Object.keys(cfg).includes(gameKey) ? gameKey : 'warzone');

    const primary = game.primary || game.themeColor || '#00ff99';
    const secondary = game.secondary || '#61f500';
    const glow = game.glow || 'rgba(0,255,153,0.35)';
    document.documentElement.style.setProperty('--accent', primary);
    document.documentElement.style.setProperty('--accent-primary', primary);
    document.documentElement.style.setProperty('--accent-secondary', secondary);
    document.documentElement.style.setProperty('--accent-glow', glow);
    document.documentElement.style.setProperty('--button-bg', primary);
    document.documentElement.style.setProperty('--badge-color', secondary);

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
