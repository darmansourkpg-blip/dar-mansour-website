/* Eden & Beyond — interactions (vanilla JS, no dependencies) */
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
})();
