/* Dar Mansour — interactions (vanilla JS, no dependencies) */
(function () {
  'use strict';

  /* 1. Header: transparent over hero, solid after scroll */
  const header = document.getElementById('header');
  const onScroll = () => {
    if (window.scrollY > 40) header.classList.add('is-solid');
    else header.classList.remove('is-solid');
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* 2. Full-screen menu */
  const toggle = document.getElementById('menuToggle');
  const body = document.body;
  const closeMenu = () => {
    body.classList.remove('menu-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  };
  if (toggle) {
    toggle.addEventListener('click', () => {
      const open = body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }
  document.querySelectorAll('[data-nav] a').forEach((a) =>
    a.addEventListener('click', closeMenu)
  );
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });

  /* 3. Scroll reveal */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            io.unobserve(entry.target);
          }
        });
      },
      // threshold 0 so even very tall elements (long articles) reveal as soon
      // as they scroll into view — 12% of a 10,000px block never fits a screen.
      { threshold: 0, rootMargin: '0px 0px -8% 0px' }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('in'));
  }

  /* 4. Smooth-scroll offset for sticky header on in-page links */
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const y = target.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top: y, behavior: 'smooth' });
    });
  });

  /* 5. Lightbox — read press-feature pages in an overlay (flip with arrows,
        close with ✕ / Escape / backdrop). Falls back to the plain image
        links when JS is unavailable. */
  document.querySelectorAll('.pressgallery').forEach((gallery) => {
    const links = Array.from(gallery.querySelectorAll('a'));
    if (!links.length) return;
    const items = links.map((a) => ({
      href: a.getAttribute('href'),
      alt: (a.querySelector('img') || {}).alt || '',
    }));
    let idx = 0;
    let box = null;

    const render = () => {
      const it = items[idx];
      box.querySelector('.lb__img').src = it.href;
      box.querySelector('.lb__img').alt = it.alt;
      box.querySelector('.lb__count').textContent = idx + 1 + ' / ' + items.length;
      box.querySelector('.lb__full').href = it.href;
      box.querySelector('.lb__prev').style.visibility = items.length > 1 ? '' : 'hidden';
      box.querySelector('.lb__next').style.visibility = items.length > 1 ? '' : 'hidden';
    };
    const go = (d) => { idx = (idx + d + items.length) % items.length; render(); };
    const close = () => {
      document.body.classList.remove('lb-open');
      if (box) box.classList.remove('is-open');
    };
    const open = (i) => {
      idx = i;
      if (!box) {
        box = document.createElement('div');
        box.className = 'lb';
        box.innerHTML =
          '<button class="lb__close" aria-label="Close">&times;</button>' +
          '<button class="lb__nav lb__prev" aria-label="Previous">&#8249;</button>' +
          '<img class="lb__img" src="" alt="">' +
          '<button class="lb__nav lb__next" aria-label="Next">&#8250;</button>' +
          '<div class="lb__bar"><span class="lb__count"></span>' +
          '<a class="lb__full" target="_blank" rel="noopener">Open full size ↗</a></div>';
        document.body.appendChild(box);
        box.querySelector('.lb__close').addEventListener('click', close);
        box.querySelector('.lb__prev').addEventListener('click', (e) => { e.stopPropagation(); go(-1); });
        box.querySelector('.lb__next').addEventListener('click', (e) => { e.stopPropagation(); go(1); });
        box.addEventListener('click', (e) => { if (e.target === box) close(); });
      }
      render();
      document.body.classList.add('lb-open');
      box.classList.add('is-open');
    };

    links.forEach((a, i) =>
      a.addEventListener('click', (e) => { e.preventDefault(); open(i); })
    );
    window.addEventListener('keydown', (e) => {
      if (!box || !box.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') go(-1);
      else if (e.key === 'ArrowRight') go(1);
    });
  });
})();
