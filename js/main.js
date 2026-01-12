/**
 * Verum Website - Main JavaScript
 *
 * Note: Mobile navigation toggle is handled in components.js
 * for pages using the shared header component.
 */

(function() {
  'use strict';

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.header').offsetHeight;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // Header scroll effect
  const header = document.querySelector('.header');
  let lastScrollY = window.scrollY;

  function updateHeader() {
    const currentScrollY = window.scrollY;

    if (currentScrollY > 100) {
      header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
      header.style.boxShadow = 'none';
    }

    lastScrollY = currentScrollY;
  }

  window.addEventListener('scroll', updateHeader, { passive: true });

  // Form submission handling
  const forms = document.querySelectorAll('form');
  forms.forEach(function(form) {
    form.addEventListener('submit', function(e) {
      const submitBtn = form.querySelector('[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
      }
    });
  });

})();
