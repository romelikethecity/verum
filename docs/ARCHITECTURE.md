# Verum Site Architecture

## Overview

The Verum website is a static HTML site with 203 pages:
- 8 hand-crafted core pages
- 195 programmatically generated SEO pages

## Why Static HTML?

- **No build step** - GitHub Pages serves files directly
- **Fast load times** - No JavaScript framework overhead
- **Simple maintenance** - Edit HTML directly
- **SEO-friendly** - Full HTML content for crawlers
- **Free hosting** - GitHub Pages at no cost

## Directory Structure

```
verum-website/
├── index.html              # Homepage
├── about.html              # About page
├── contact.html            # Contact page
├── pricing.html            # Pricing page
├── services/
│   ├── index.html          # Services hub
│   ├── data-cleaning.html
│   ├── data-enrichment.html
│   └── data-analysis.html
├── solutions/
│   ├── index.html          # Solutions hub (hand-crafted)
│   └── {industry}-data-{service}/
│       └── index.html      # Generated pages
├── enrichment/
│   └── {type}/
│       └── index.html      # Generated pages
├── cleaning/
│   └── {type}/
│       └── index.html      # Generated pages
├── use-cases/
│   └── {case}/
│       └── index.html      # Generated pages
├── find/
│   └── {type}/
│       └── index.html      # Generated pages
├── analysis/
│   └── {type}/
│       └── index.html      # Generated pages
├── compare/
│   └── verum-vs-{competitor}/
│       └── index.html      # Generated pages
├── alternatives/
│   └── {competitor}-alternative/
│       └── index.html      # Generated pages
├── css/
│   └── styles.css          # All styles
├── js/
│   └── main.js             # Mobile nav, smooth scroll
├── assets/
│   ├── logos/
│   │   ├── logos-svg/      # SVG logo files
│   │   └── logos-png/      # PNG logo files
│   ├── social-preview.png  # OG image
│   └── social-preview.html # Template for OG image
├── docs/                   # Documentation
├── generate_pages.py       # Page generator script
├── sitemap.xml             # Auto-generated
├── robots.txt
└── CNAME                   # Custom domain
```

## URL Structure

Using `/page-name/index.html` for clean URLs:
- `veruminc.com/solutions/healthcare-data-enrichment/` ✓
- `veruminc.com/solutions/healthcare-data-enrichment.html` ✗

## Core Pages

### Homepage (`index.html`)
- Hero with value proposition
- Problem section (3 pain points)
- How it works (3 steps)
- Services overview (3 cards)
- Social proof (personas, founder note, metrics)
- Contact form (Formspree)

### Pricing (`pricing.html`)
- 3 pricing tiers (Starter, Growth, Enterprise)
- Per-record pricing breakdown
- Competitor comparison table
- FAQ section
- CTA

### Solutions Hub (`solutions/index.html`)
- Solutions by Team (Sales, Marketing, RevOps)
- Solutions by Industry (25 industries grid)
- Solutions by Use Case (categorized)
- Data types we enrich

### Services (`services/`)
- Overview page with 3 service cards
- Individual pages for each service
- Feature lists and CTAs

## Programmatic Pages

### Generator Script (`generate_pages.py`)

The script generates 195 pages from data arrays:

```python
python3 generate_pages.py
```

### Data Sources

| Array | Count | Output Path |
|-------|-------|-------------|
| INDUSTRIES | 25 | `/solutions/{industry}-data-{service}/` (x2 = 50) |
| ENRICHMENT_TYPES | 44 | `/enrichment/{type}/` |
| CLEANING_TYPES | 20 | `/cleaning/{type}/` |
| USE_CASES | 29 | `/use-cases/{case}/` |
| BUSINESS_FIND | 25 | `/find/{type}/` |
| ANALYSIS_TYPES | 19 | `/analysis/{type}/` |
| COMPARISONS | 5 | `/compare/verum-vs-{competitor}/` |
| ALTERNATIVES | 4 | `/alternatives/{competitor}-alternative/` |

### Template Structure

Each generated page includes:
- Full HTML document with meta tags
- Header with navigation
- Page hero with H1
- Content section (unique per page type)
- CTA button
- Footer
- Tracking code

### Adding New Pages

1. Add entry to appropriate array in `generate_pages.py`
2. Run `python3 generate_pages.py`
3. Sitemap auto-updates
4. Commit and push

## CSS Architecture

### Single File (`css/styles.css`)

All styles in one file for simplicity:
- CSS variables for theming
- Base/reset styles
- Layout components
- UI components (buttons, cards, forms)
- Section-specific styles
- Utility classes
- Responsive breakpoints

### Breakpoints

```css
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
```

### Dark Theme

The site uses a dark-first design:
- Background: `#1a1d1e` (primary), `#2d3436` (secondary)
- Text: `#ffffff` (primary), `#b2bec3` (secondary)
- Accent: `#00b894` (teal)

## JavaScript (`js/main.js`)

Minimal JS for:
- Mobile navigation toggle
- Smooth scroll for anchor links
- Header background on scroll

No frameworks or build tools required.

## Forms

### Formspree Integration

Contact forms submit to Formspree:
- **Endpoint:** `https://formspree.io/f/xaqqywlb`
- **Method:** POST
- **Honeypot:** `_gotcha` field for spam prevention

### Form Fields

| Field | Type | Required |
|-------|------|----------|
| name | text | Yes |
| email | email | Yes |
| company | text | Yes |
| company_size | select | No |
| message | textarea | Yes (homepage) / No (contact) |

## Assets

### Logos

Two versions for different backgrounds:
- `verum-logo-horizontal-dark.svg` - White text (for dark backgrounds)
- `verum-logo-horizontal-light.svg` - Dark text (for light backgrounds)

Current site uses dark theme, so `*-dark.svg` is used everywhere.

### Social Preview

- **File:** `assets/social-preview.png`
- **Size:** 1200 x 630 px
- **Used for:** Open Graph and Twitter Card images

## Deployment

### GitHub Pages

1. Push to `main` branch
2. GitHub Actions builds and deploys
3. Live at veruminc.com within ~60 seconds

### Custom Domain (Cloudflare)

DNS records in Cloudflare:
```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  romelikethecity.github.io
```

CNAME file contains: `veruminc.com`

## Maintenance Tasks

### Regular

- [ ] Check form submissions in Formspree
- [ ] Review analytics in GA4/Clarity
- [ ] Monitor Google Search Console for issues

### When Adding Content

- [ ] Run `generate_pages.py` if adding programmatic pages
- [ ] Update sitemap if adding manual pages
- [ ] Test all internal links

### When Changing Design

- [ ] Update `css/styles.css`
- [ ] Update `generate_pages.py` template if needed
- [ ] Regenerate all programmatic pages
- [ ] Test responsive design at all breakpoints
