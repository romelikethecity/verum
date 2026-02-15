/**
 * Verum Website - Shared Components
 *
 * This file contains the site header and footer HTML.
 * To update navigation or footer links site-wide, edit this file
 * and all pages will automatically reflect the changes.
 *
 * Usage: Include this script and add elements with id="site-header" and id="site-footer"
 */

(function() {
  'use strict';

  // Chevron down SVG icon for dropdown
  const chevronDownSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" /></svg>`;

  // Site Header HTML
  const headerHTML = `
    <div class="container header__inner">
      <a href="/" class="header__logo">
        <img src="/assets/logos/logo-horizontal-transparent-dark.svg" alt="Verum" width="160" height="44">
      </a>

      <nav class="nav nav--desktop">
        <ul class="nav__list">
          <li><a href="/services/" class="nav__link">Services</a></li>
          <li><a href="/solutions/" class="nav__link">Solutions</a></li>
          <li class="nav__item--dropdown">
            <button class="nav__dropdown-toggle" aria-expanded="false" aria-haspopup="true">
              Resources ${chevronDownSVG}
            </button>
            <div class="nav__dropdown">
              <a href="/resources/" class="nav__dropdown-item">Blog</a>
              <a href="/assessment/" class="nav__dropdown-item">Free Assessment</a>
              <a href="/pricing.html" class="nav__dropdown-item">Pricing</a>
            </div>
          </li>
          <li><a href="/about.html" class="nav__link">About</a></li>
        </ul>
      </nav>

      <a href="/#contact" class="btn btn--primary btn--sm header__cta">See What We'll Find</a>

      <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span class="menu-toggle__icon"></span>
      </button>
    </div>
  `;

  // Mobile Navigation HTML (separate from header to avoid backdrop-filter containment issue)
  const mobileNavHTML = `
    <nav class="nav nav--mobile">
      <ul class="nav__list">
        <li><a href="/services/" class="nav__link">Services</a></li>
        <li><a href="/solutions/" class="nav__link">Solutions</a></li>
        <li class="nav__item--dropdown">
          <button class="nav__dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Resources ${chevronDownSVG}
          </button>
          <div class="nav__dropdown">
            <a href="/resources/" class="nav__dropdown-item">Blog</a>
            <a href="/assessment/" class="nav__dropdown-item">Free Assessment</a>
            <a href="/pricing.html" class="nav__dropdown-item">Pricing</a>
          </div>
        </li>
        <li><a href="/about.html" class="nav__link">About</a></li>
      </ul>
      <a href="/#contact" class="btn btn--primary">See What We'll Find</a>
    </nav>
  `;

  // Site Footer HTML
  const footerHTML = `
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="/assets/logos/logo-horizontal-transparent-dark.svg" alt="Verum" class="footer__logo" width="160" height="44">
          <p class="footer__tagline">Sales data you actually trust.</p>
        </div>

        <div>
          <h4 class="footer__heading">Services</h4>
          <ul class="footer__links">
            <li><a href="/services/data-cleaning.html">Data Cleaning</a></li>
            <li><a href="/services/data-enrichment.html">Data Enrichment</a></li>
            <li><a href="/services/data-validation.html">Data Validation</a></li>
            <li><a href="/services/data-discovery.html">Data Discovery</a></li>
            <li><a href="/services/data-analysis.html">Data Analysis</a></li>
            <li><a href="/services/data-maintenance.html">Data Maintenance</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__heading">Solutions</h4>
          <ul class="footer__links">
            <li><a href="/solutions/">By Industry</a></li>
            <li><a href="/for/">By Role</a></li>
            <li><a href="/use-cases/">Use Cases</a></li>
            <li><a href="/find/">Find Businesses</a></li>
            <li><a href="/healthcare/">Healthcare</a></li>
            <li><a href="/compare/">Compare</a></li>
            <li><a href="/alternatives/">Alternatives</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__heading">Resources</h4>
          <ul class="footer__links">
            <li><a href="/resources/">Blog</a></li>
            <li><a href="/glossary/">Glossary</a></li>
            <li><a href="/assessment/">Free Assessment</a></li>
            <li><a href="/pricing.html">Pricing</a></li>
            <li><a href="https://datastackguide.com/" target="_blank" rel="noopener noreferrer">DataStackGuide</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__heading">Company</h4>
          <ul class="footer__links">
            <li><a href="/about.html">About</a></li>
            <li><a href="/team/">Team</a></li>
            <li><a href="/contact.html">Contact</a></li>
            <li><a href="https://www.linkedin.com/company/verumai/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
          </ul>
        </div>
      </div>

      <div class="footer__bottom">
        <p>&copy; ${new Date().getFullYear()} Verum Inc. All rights reserved.</p>
        <div class="footer__legal">
          <a href="/privacy.html">Privacy</a>
          <a href="/terms.html">Terms</a>
        </div>
      </div>
    </div>
  `;

  // Inject header
  const headerEl = document.getElementById('site-header');

  if (headerEl) {
    headerEl.classList.add('header');
    headerEl.innerHTML = headerHTML;

    // Inject mobile nav as sibling after header (outside header to avoid backdrop-filter containment)
    headerEl.insertAdjacentHTML('afterend', mobileNavHTML);

    // Initialize mobile navigation toggle
    const menuToggle = headerEl.querySelector('.menu-toggle');
    const mobileNav = document.querySelector('.nav--mobile');

    if (menuToggle && mobileNav) {
      menuToggle.addEventListener('click', function(e) {
        e.preventDefault();
        const isExpanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !isExpanded);
        this.classList.toggle('active');
        mobileNav.classList.toggle('active');

        // Prevent body scroll when menu is open
        document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
      });

      // Close mobile menu when clicking a link (but not dropdown toggles)
      mobileNav.addEventListener('click', function(e) {
        if (e.target.tagName === 'A') {
          menuToggle.classList.remove('active');
          menuToggle.setAttribute('aria-expanded', 'false');
          mobileNav.classList.remove('active');
          document.body.style.overflow = '';
        }
      });

      // Mobile dropdown toggle
      const mobileDropdownToggles = mobileNav.querySelectorAll('.nav__dropdown-toggle');
      mobileDropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          const dropdownItem = this.closest('.nav__item--dropdown');
          const isExpanded = this.getAttribute('aria-expanded') === 'true';

          // Close other dropdowns
          mobileDropdownToggles.forEach(function(otherToggle) {
            if (otherToggle !== toggle) {
              otherToggle.setAttribute('aria-expanded', 'false');
              otherToggle.closest('.nav__item--dropdown').classList.remove('active');
            }
          });

          // Toggle current dropdown
          this.setAttribute('aria-expanded', !isExpanded);
          dropdownItem.classList.toggle('active');
        });
      });
    }
  }

  // Inject footer
  const footerEl = document.getElementById('site-footer');
  if (footerEl) {
    footerEl.classList.add('footer');
    footerEl.innerHTML = footerHTML;
  }

})();
