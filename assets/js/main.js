/* Tiny progressive enhancements. The portfolio works without JS. */
(() => {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.nav-links');
  if (toggle && menu) {
    // Las etiquetas accesibles del menú provienen de content/{es,en,pt}.json.
    const label = [toggle.dataset.labelOpen || toggle.getAttribute('aria-label'),
                   toggle.dataset.labelClose || toggle.getAttribute('aria-label')];
    toggle.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.setAttribute('aria-label', isOpen ? label[1] : label[0]);
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false');toggle.setAttribute('aria-label',label[0]);
    }));
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') { menu.classList.remove('open'); toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label',label[0]); }
    });
  }
  const back = document.querySelector('.back-to-top');
  if (back) {
    const update = () => back.classList.toggle('show', window.scrollY > 650);
    window.addEventListener('scroll', update, {passive:true}); update();
  }
})();
