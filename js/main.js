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

  function updateHeader() {
    if (window.scrollY > 100) {
      header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.25)';
    } else {
      header.style.boxShadow = 'none';
    }
  }

  window.addEventListener('scroll', updateHeader, { passive: true });

  // ============================================
  // Scroll-triggered reveal animations
  // ============================================
  const revealElements = document.querySelectorAll(
    '.problem-card, .service-card, .step, .persona, .pricing-card, ' +
    '.feature-card, .pipeline-step, .testimonial-card, .faq-item, ' +
    '.comparison-card, .founder-note, .metric, .solution-stats, ' +
    '.pain-stats .pain-stat, .content-figure, .faq-section h3'
  );

  if (revealElements.length > 0 && 'IntersectionObserver' in window) {
    // Add initial hidden state
    revealElements.forEach(function(el) {
      el.classList.add('reveal');
    });

    var revealObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          // Stagger siblings for grid layouts
          var parent = entry.target.parentElement;
          var siblings = parent ? Array.from(parent.querySelectorAll('.reveal:not(.revealed)')) : [];
          var index = siblings.indexOf(entry.target);
          var delay = Math.max(0, index) * 80;

          setTimeout(function() {
            entry.target.classList.add('revealed');
          }, delay);

          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(function(el) {
      revealObserver.observe(el);
    });
  }

  // Section header reveals
  var sectionHeaders = document.querySelectorAll(
    '.problems__header, .how-it-works__header, .pipeline-section__header, ' +
    'section > .container > .text-center, .cta-section__header'
  );

  if (sectionHeaders.length > 0 && 'IntersectionObserver' in window) {
    sectionHeaders.forEach(function(el) {
      el.classList.add('reveal-up');
    });

    var headerObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          headerObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.2,
      rootMargin: '0px 0px -20px 0px'
    });

    sectionHeaders.forEach(function(el) {
      headerObserver.observe(el);
    });
  }

  // ============================================
  // Form submission handling with success state
  // ============================================
  var forms = document.querySelectorAll('form');
  forms.forEach(function(form) {
    form.addEventListener('submit', function(e) {
      var submitBtn = form.querySelector('[type="submit"]');
      if (!submitBtn) return;

      var originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<span class="btn-spinner"></span> Sending...';
      submitBtn.classList.add('btn--sending');

      // Listen for successful submission (Formspree redirects or fetch)
      // Since Formspree uses standard form POST, handle via fetch
      if (form.action && form.action.includes('formspree.io')) {
        e.preventDefault();
        var formData = new FormData(form);

        fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'Accept': 'application/json' }
        }).then(function(response) {
          if (response.ok) {
            submitBtn.innerHTML = '&#10003; Sent!';
            submitBtn.classList.remove('btn--sending');
            submitBtn.classList.add('btn--success');
            form.reset();
            setTimeout(function() {
              submitBtn.innerHTML = originalText;
              submitBtn.disabled = false;
              submitBtn.classList.remove('btn--success');
            }, 3000);
          } else {
            submitBtn.innerHTML = 'Error - Try Again';
            submitBtn.classList.remove('btn--sending');
            submitBtn.classList.add('btn--error');
            setTimeout(function() {
              submitBtn.innerHTML = originalText;
              submitBtn.disabled = false;
              submitBtn.classList.remove('btn--error');
            }, 3000);
          }
        }).catch(function() {
          submitBtn.innerHTML = 'Error - Try Again';
          submitBtn.classList.remove('btn--sending');
          submitBtn.classList.add('btn--error');
          setTimeout(function() {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            submitBtn.classList.remove('btn--error');
          }, 3000);
        });
      }
    });
  });

  // ============================================
  // Floating CTA bar on scroll (homepage only)
  // ============================================
  var contactSection = document.getElementById('contact');
  var floatingCta = document.querySelector('.floating-cta');

  if (contactSection && floatingCta) {
    var ctaObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          floatingCta.classList.remove('visible');
        } else if (window.scrollY > 600) {
          floatingCta.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    ctaObserver.observe(contactSection);

    // Also show after scrolling past hero
    window.addEventListener('scroll', function() {
      if (!contactSection) return;
      var contactRect = contactSection.getBoundingClientRect();
      if (contactRect.top > window.innerHeight && window.scrollY > 600) {
        floatingCta.classList.add('visible');
      }
    }, { passive: true });
  }

})();
