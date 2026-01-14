# Verum Website - Claude Code Guidelines

## Project Overview

Verum is a B2B data enrichment company. This website has ~200 programmatic SEO pages for different industries and services. The high-value industry pages are being rewritten from thin templates (~84 lines) to rich, conversion-focused content (~300+ lines).

## Current Progress

### Completed Industry Pages (13 pages, 300+ lines each)
1. Healthcare - NPI verification, provider data, HIPAA considerations
2. Professional Services - Client data across systems, cross-sell opportunities
3. Fintech - KYC/AML compliance, regulatory accuracy
4. SaaS - Tech stack detection, funding signals, SDR productivity
5. Legal - Bar numbers, practice areas, attorney CRM adoption
6. Real Estate - License data, brokerage info, transaction history
7. Insurance - Agent licensing, claims data, fraud prevention
8. Manufacturing - Long sales cycles, distributor networks, supply chain
9. Cybersecurity - CISO mobility, conference leads, vendor consolidation
10. HR Tech - Title normalization, HRIS stack data, job changes
11. Consulting - Partner relationships, alumni tracking, proposal prep
12. Accounting - Practice management, busy season outreach, advisory services
13. Government - Vendor databases, grant recipients, legacy system exports

### Remaining Industry Pages (15 pages, still thin templates)
1. AdTech
2. AI/ML
3. B2B Services
4. Construction
5. E-commerce
6. Education
7. Energy
8. Logistics
9. MarTech
10. Media
11. Nonprofit
12. Retail
13. Technology
14. Telecommunications
15. Travel

---

## Programmatic SEO Page Template

When creating or editing industry data enrichment pages, follow these guidelines:

### Pain Stats Formatting Rules

**CRITICAL: Stat numbers must NEVER contain spaces**

Spaces in `.pain-stat__number` values cause line wrapping on mobile/tablet.

**THE RULE: No spaces inside stat values. Ever.**

✅ GOOD (no spaces):
- `30%` - percentages are always safe
- `$12.9M` - currency with abbreviation
- `24-48hr` - hyphenated, no spaces
- `84-day` - hyphenated, no spaces
- `13` - just the number, move "hours" to label
- `5+` - just the number with modifier
- `50+` - just the number with modifier

❌ BAD (contains spaces - WILL WRAP):
- `13 hrs` - HAS SPACE, will wrap to two lines
- `84 days` - HAS SPACE, will wrap
- `15+ hrs` - HAS SPACE, will wrap
- `5+ hrs` - HAS SPACE, will wrap

**Pattern for time-based stats:**
Instead of `13 hrs` in the number, use:
- Number: `13`
- Label: `Hours lost weekly to data hunting`

### MANDATORY: Run Verification Before Committing

**YOU MUST run this command before committing any page changes:**

```bash
grep -r "pain-stat__number" /Users/rome/Documents/projects/verum-website/solutions/*/index.html | grep -E ">[^<]+ [^<]+<"
```

If this returns ANY results, you have stats with spaces that will wrap. Fix them before committing.

### Pain Stats Checklist

Before committing any page with `.pain-stats`:
- [ ] Ran verification command above - returned no results
- [ ] Each stat number contains NO SPACES
- [ ] Stat numbers are 6 characters or fewer

---

## Full Page Template Structure

Each industry page should follow this structure (~300 lines, 1200-1500 words):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Standard meta tags, canonical URL, favicon -->
  <!-- Open Graph and Twitter cards -->
  <!-- Google Analytics and Clarity -->
  <!-- FAQ Schema markup (3 questions minimum) -->
  <link rel="stylesheet" href="/css/styles.css?v=2">
</head>
<body>
  <header id="site-header"></header>

  <main>
    <!-- HERO SECTION -->
    <section class="page-hero">
      <div class="container">
        <h1 class="page-hero__title">[Industry] Data Enrichment That Actually Works</h1>
        <p class="page-hero__subtitle">[Pain-first subtitle - specific to industry]</p>

        <!-- Pain Stats - 3 industry-specific stats -->
        <div class="pain-stats">
          <div class="pain-stat">
            <span class="pain-stat__number">[NO SPACES]</span>
            <span class="pain-stat__label">[Label]</span>
          </div>
          <!-- 2 more stats -->
        </div>

        <!-- CTAs Below Stats -->
        <div class="hero-cta-group">
          <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>
          <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Data Assessment</a>
        </div>
      </div>
    </section>

    <!-- CONTENT SECTION -->
    <section class="content">
      <div class="container" style="max-width: 800px;">

        <!-- THE PAIN (300-400 words) -->
        <h2>The [Industry] Data Problem</h2>
        <p>[Opening scenario - specific, relatable, shows we understand]</p>
        <h3>[Pain point 1]</h3>
        <p>[With stats and sources]</p>
        <h3>[Pain point 2]</h3>
        <p>[With stats and sources]</p>
        <h3>[Pain point 3]</h3>
        <p>[With stats and sources]</p>
        <h3>[Pain point 4]</h3>
        <p>[With stats and sources]</p>
        <p>[Consequences paragraph]</p>

        <div class="text-center mt-xl">
          <a href="/#contact" class="btn btn--secondary">See How Clean Data Transforms Operations</a>
        </div>

        <!-- THE SOLUTION (300-400 words) -->
        <h2>How Verum Solves [Industry] Data Challenges</h2>
        <p>[Opening paragraph]</p>
        <h3>Contact Data That Stays Fresh</h3>
        <p>[General explanation]</p>
        <p><strong>For [industry] teams:</strong> [Industry-specific benefit]</p>
        <h3>[Industry-specific solution 2]</h3>
        <p>[Explanation + industry benefit]</p>
        <h3>[Industry-specific solution 3]</h3>
        <p>[Explanation + industry benefit]</p>
        <h3>Human QA on Everything</h3>
        <p>[Explanation]</p>

        <!-- Solution Stats -->
        <div class="solution-stats">
          <div class="solution-stat">
            <span class="solution-stat__number">93%</span>
            <span class="solution-stat__label">Deliverability guarantee</span>
          </div>
          <div class="solution-stat">
            <span class="solution-stat__number">24-48hr</span>
            <span class="solution-stat__label">Typical turnaround</span>
          </div>
          <div class="solution-stat">
            <span class="solution-stat__number">50+</span>
            <span class="solution-stat__label">Data sources</span>
          </div>
        </div>

        <div class="text-center">
          <a href="/#contact" class="btn btn--primary btn--lg">Ready to Get Started?</a>
        </div>

        <!-- USE CASES (200-300 words) -->
        <h2>What [Industry] Teams Do With Clean Data</h2>
        <ul class="feature-list">
          <li><strong>[Outcome 1]</strong> [Specific benefit]</li>
          <li><strong>[Outcome 2]</strong> [Specific benefit]</li>
          <li><strong>[Outcome 3]</strong> [Specific benefit]</li>
          <li><strong>[Outcome 4]</strong> [Specific benefit]</li>
          <li><strong>[Outcome 5]</strong> [Specific benefit]</li>
        </ul>

        <!-- PROCESS (200-300 words) -->
        <h2>Getting Started Takes Less Time Than Your Average Meeting</h2>
        <p><strong>Step 1: Free Assessment (5 minutes)</strong><br>[Description]</p>
        <p><strong>Step 2: Discovery Call (30 minutes)</strong><br>[Description with industry tech stack mentions]</p>
        <p><strong>Step 3: Data Analysis (on us)</strong><br>[Description]</p>
        <p><strong>Step 4: Full Engagement</strong><br>[Description]</p>
        <p><strong>Step 5: Ongoing (if you want it)</strong><br>[Description]</p>

        <!-- WHY VERUM (150-250 words) -->
        <h2>Why [Industry] Leaders Choose Verum</h2>
        <ul class="feature-list">
          <li><strong>We do the work.</strong> [Explanation]</li>
          <li><strong>Fast turnaround.</strong> [Explanation]</li>
          <li><strong>Human verification.</strong> [Explanation]</li>
          <li><strong>No long-term contracts.</strong> [Explanation]</li>
          <li><strong>We understand [industry].</strong> [Industry-specific terminology proof]</li>
        </ul>

        <!-- COMPARISON TABLE -->
        <h2>Verum vs. Manual Data Management</h2>
        <table class="comparison-table">
          <thead>
            <tr>
              <th>The Old Way</th>
              <th>With Verum</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>[Pain]</td><td>[Solution]</td></tr>
            <!-- 4 more rows -->
          </tbody>
        </table>

        <!-- FAQ (200-300 words) -->
        <h2>Common Questions About [Industry] Data Enrichment</h2>
        <div class="faq-section">
          <h3>How long does implementation take?</h3>
          <p>[Standard answer]</p>
          <h3>[Industry-specific question]</h3>
          <p>[Answer]</p>
          <h3>[Industry-specific question]</h3>
          <p>[Answer]</p>
          <h3>How is this different from buying a ZoomInfo license?</h3>
          <p>[Standard 3-part answer: different problem, different pricing, different ownership]</p>
          <h3>[Security/compliance question]</h3>
          <p>[Answer]</p>
          <h3>Do you work with companies of our size?</h3>
          <p>[Standard answer]</p>
        </div>

        <!-- FINAL CTA -->
        <h2>Ready to Stop Fighting Your Data?</h2>
        <p>Two paths forward:</p>
        <p><strong>Not sure yet?</strong> [Assessment pitch]</p>
        <p><strong>Ready to fix this?</strong> [Sample file pitch]</p>

        <div class="cta-group mt-xl">
          <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Assessment</a>
          <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>
        </div>

        <p class="mt-lg text-muted">Related: [3-4 internal links to related pages]</p>

      </div>
    </section>
  </main>

  <footer id="site-footer"></footer>

  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>
```

---

## Writing Style

See `/docs/WRITING-GUIDELINES.md` for full anti-AI detection guidelines.

Key points:
- Use contractions ("we're" not "we are")
- Vary sentence length dramatically
- Avoid em-dashes (heavily flagged as AI)
- No performative interjections ("That's not a typo", "Let that sink in")
- Industry-specific details and stats with source links
- Second-person "you" that speaks directly to reader

---

## CSS Cache-Busting

**IMPORTANT: When modifying CSS, increment the version parameter**

GitHub Pages caches CSS for 4 hours. To ensure users see updated styles immediately:

1. All HTML files link to CSS with a version param: `styles.css?v=2`
2. When you modify `/css/styles.css`, increment the version: `?v=3`, `?v=4`, etc.
3. Update ALL HTML files with the new version (use find/sed)

```bash
# Example: Increment from v=2 to v=3 across all HTML files
find /Users/rome/Documents/projects/verum-website -name "*.html" \
  -exec sed -i '' 's|styles.css?v=2|styles.css?v=3|g' {} \;
```

This prevents the "design issues" where new pages show with old cached CSS.

---

## CSS Classes Reference

- `.page-hero` - Hero section container
- `.page-hero__title` - H1 title
- `.page-hero__subtitle` - Subtitle paragraph
- `.pain-stats` - Container for hero stats (grid, 3 columns)
- `.pain-stat` - Individual stat card
- `.pain-stat__number` - Large teal number (4.5rem desktop) - NO SPACES
- `.pain-stat__label` - Small label below number
- `.solution-stats` - Mid-page stats with card background
- `.solution-stat__number` - 2.75rem with `white-space: nowrap`
- `.solution-stat__label` - Label for solution stat
- `.comparison-table` - Red/green styled comparison table
- `.hero-cta-group` - Button group below hero stats
- `.cta-group` - Button group for final CTA
- `.feature-list` - Styled list with bold lead-ins
- `.faq-section` - FAQ container
- `.content` - Main content section
- `.text-center` - Center-aligned text
- `.mt-xl` - Large top margin
- `.mt-lg` - Medium top margin
- `.text-muted` - Gray text for related links

---

## FAQ Schema Markup

Each page must include FAQ schema for rich snippets. Minimum 3 questions:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does implementation take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There isn't really an implementation. Send us a file, we send back clean data. First project typically completes in 24-48 hours."
      }
    },
    // 2+ more questions
  ]
}
```

---

## Standard Content Blocks

### ZoomInfo Comparison (use in every FAQ)
Three fundamental differences:
1. **Different problem.** ZoomInfo sells net-new contacts; Verum cleans existing data
2. **Different pricing.** ZoomInfo: $15K-$50K+/year recurring; Verum: per project
3. **Different ownership.** ZoomInfo requires deletion on cancel; Verum data is yours forever

### Solution Stats (use on every page)
- 93% deliverability guarantee
- 24-48hr typical turnaround
- 50+ data sources

### Process Steps (use on every page)
1. Free Assessment (5 minutes)
2. Discovery Call (30 minutes)
3. Data Analysis (on us)
4. Full Engagement
5. Ongoing (if you want it)

---

## File Locations

- Industry pages: `/solutions/[industry]-data-enrichment/index.html`
- Main CSS: `/css/styles.css`
- Writing guidelines: `/docs/WRITING-GUIDELINES.md`
- This file: `/CLAUDE.md`
- Solutions index: `/solutions/index.html`
