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

  // Site Header HTML
  const headerHTML = `
    <div class="container header__inner">
      <a href="/" class="header__logo">
        <img src="/assets/logos/logos-svg/verum-logo-horizontal-dark.svg" alt="Verum" width="120" height="32">
      </a>

      <nav class="nav nav--desktop">
        <ul class="nav__list">
          <li><a href="/services/" class="nav__link">Services</a></li>
          <li><a href="/solutions/" class="nav__link">Solutions</a></li>
          <li><a href="/assessment/" class="nav__link">Free Assessment</a></li>
          <li><a href="/pricing.html" class="nav__link">Pricing</a></li>
          <li><a href="/about.html" class="nav__link">About</a></li>
        </ul>
      </nav>

      <a href="/#contact" class="btn btn--primary btn--sm header__cta">Clean My Data</a>

      <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span class="menu-toggle__icon"></span>
      </button>

      <nav class="nav nav--mobile">
        <ul class="nav__list">
          <li><a href="/services/" class="nav__link">Services</a></li>
          <li><a href="/solutions/" class="nav__link">Solutions</a></li>
          <li><a href="/assessment/" class="nav__link">Free Assessment</a></li>
          <li><a href="/pricing.html" class="nav__link">Pricing</a></li>
          <li><a href="/about.html" class="nav__link">About</a></li>
        </ul>
        <a href="/#contact" class="btn btn--primary">Clean My Data</a>
      </nav>
    </div>
  `;

  // Site Footer HTML
  const footerHTML = `
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="/assets/logos/logos-svg/verum-logo-horizontal-dark.svg" alt="Verum" class="footer__logo" width="120" height="32">
          <p class="footer__tagline">Enterprise data cleaning and enrichment you can trust.</p>
        </div>

        <div>
          <h4 class="footer__heading">Services</h4>
          <ul class="footer__links">
            <li><a href="/services/data-cleaning.html">Data Cleaning</a></li>
            <li><a href="/services/data-enrichment.html">Data Enrichment</a></li>
            <li><a href="/services/data-analysis.html">Data Analysis</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__heading">Resources</h4>
          <ul class="footer__links">
            <li><a href="/assessment/">Free Assessment</a></li>
            <li><a href="/pricing.html">Pricing</a></li>
            <li><a href="/solutions/">Solutions</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__heading">Company</h4>
          <ul class="footer__links">
            <li><a href="/about.html">About</a></li>
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

    // Initialize mobile navigation toggle immediately after injection
    const menuToggle = headerEl.querySelector('.menu-toggle');
    const mobileNav = headerEl.querySelector('.nav--mobile');

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

      // Close mobile menu when clicking a link
      mobileNav.addEventListener('click', function(e) {
        if (e.target.tagName === 'A') {
          menuToggle.classList.remove('active');
          menuToggle.setAttribute('aria-expanded', 'false');
          mobileNav.classList.remove('active');
          document.body.style.overflow = '';
        }
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
