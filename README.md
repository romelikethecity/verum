# Verum Website

Marketing website for Verum - B2B data cleaning, enrichment, and analysis services.

**Live site:** https://veruminc.com

**Repository:** https://github.com/romelikethecity/verum

## Tech Stack

- **Static HTML/CSS/JS** - No framework, GitHub Pages native
- **Hosting:** GitHub Pages with Cloudflare DNS
- **Forms:** Formspree (https://formspree.io/f/xaqqywlb)
- **Analytics:** Google Analytics 4 (G-R416JZ91B1)
- **Heatmaps:** Microsoft Clarity (uzzgoxxnof)
- **Fonts:** Inter (Google Fonts)

## Project Structure

```
verum-website/
├── index.html                    # Homepage
├── about.html                    # About page
├── contact.html                  # Contact page
├── pricing.html                  # Pricing page
├── services/
│   ├── index.html               # Services overview
│   ├── data-cleaning.html       # Data cleaning service
│   ├── data-enrichment.html     # Data enrichment service
│   └── data-analysis.html       # Data analysis service
├── solutions/
│   └── index.html               # Solutions hub
│   └── [industry]-data-[service]/  # 50 industry pages
├── enrichment/                   # 44 enrichment type pages
├── cleaning/                     # 20 cleaning type pages
├── use-cases/                    # 29 use case pages
├── find/                         # 25 business discovery pages
├── analysis/                     # 19 analysis pages
├── compare/                      # 5 competitor comparison pages
├── alternatives/                 # 4 alternative pages
├── css/
│   └── styles.css               # All styles (dark theme)
├── js/
│   └── main.js                  # Mobile nav, smooth scroll
├── assets/
│   ├── logos/                   # SVG and PNG logos
│   └── social-preview.png       # OG image (1200x630)
├── generate_pages.py            # Programmatic page generator
├── sitemap.xml                  # Auto-generated sitemap
├── robots.txt                   # SEO robots file
├── CNAME                        # Custom domain config
└── docs/                        # Documentation
```

## Local Development

Just open any HTML file in a browser. No build step required.

For local server with live reload:
```bash
npx serve .
```

## Generating Programmatic Pages

The site includes 195 programmatic SEO pages generated from templates:

```bash
python3 generate_pages.py
```

This regenerates all pages in `/solutions/`, `/enrichment/`, `/cleaning/`, `/use-cases/`, `/find/`, `/analysis/`, `/compare/`, and `/alternatives/`.

## Deployment

Push to `main` branch. GitHub Pages auto-deploys.

```bash
git add -A
git commit -m "Your message"
git push
```

## Documentation

- [Brand Guidelines](docs/BRAND.md)
- [Pricing Strategy](docs/PRICING.md)
- [SEO Configuration](docs/SEO.md)
- [Site Architecture](docs/ARCHITECTURE.md)

## Key URLs

- Homepage: https://veruminc.com
- Pricing: https://veruminc.com/pricing.html
- Solutions: https://veruminc.com/solutions/
- Contact: https://veruminc.com/contact.html
