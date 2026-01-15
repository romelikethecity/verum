# Verum Website - Claude Code Guidelines

## Project Overview

Verum is a B2B data enrichment company. This website has ~200 programmatic SEO pages for different industries and services. The high-value industry pages have been rewritten from thin templates (~84 lines) to rich, conversion-focused content (~300+ lines).

**Site URL:** https://veruminc.com/

---

## Current Progress

### Completed Industry Data Enrichment Pages (28 pages, 300+ lines each)

All industry data enrichment pages are now complete with full content:

**Batch 1 (Original 13):**
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

**Batch 2 (15 additional, completed January 2026):**
14. AdTech - DSP/SSP contacts, programmatic buying, campaign data
15. AI/ML - Research teams, technical decision-makers, vendor landscape
16. B2B Services - Client relationship tracking, proposal data, referral networks
17. Construction - Project managers, contractor licensing, bid management
18. E-commerce - Customer data, cart abandonment, address verification. Stats: 25%, 70%, $260B
19. Education - Alumni/donor data, development teams, FERPA. Stats: 30%, 8%, 40%
20. Energy - Utility M&A, long sales cycles, energy transition. Stats: 30%, $2T, 200+
21. Logistics - Carrier data, driver turnover (91%), FMCSA verification. Stats: 91%, 30%, 17K
22. MarTech - CMO turnover, tech stack data, marketing leader movement. Stats: 30%, 18mo, 11K+
23. Media - Agency turnover (25%), advertiser relationships, brand-agency tracking. Stats: 30%, 25%, $600B
24. Nonprofit - Donor databases, address decay, major gift prospects. Stats: 30%, 45%, 10%
25. Retail - Buyer turnover (60%), category manager changes, CPG sales. Stats: 30%, 60%, $5T
26. Technology - Startup mortality, M&A activity, tech layoffs. Stats: 30%, 90%, $5T
27. Telecommunications - IT leader turnover, corporate restructuring, enterprise sales. Stats: 30%, $1.5T, 18mo
28. Travel & Hospitality - Travel manager instability, post-pandemic restructuring. Stats: 30%, $1.9T, 73%

### Next Priority: Services Section Rewrite

**Current Services Pages (all thin, ~100-130 lines):**
- `/services/index.html` - Grid of 3 service cards (114 lines)
- `/services/data-cleaning.html` - Basic content (113 lines)
- `/services/data-enrichment.html` - Basic content (134 lines)
- `/services/data-analysis.html` - Basic content (134 lines)
- `/services/icp-analysis.html` - Most complete, has custom CSS (257 lines)

**Services Section Strategy Needed:**
The services pages need the same treatment as industry pages - expanded from thin templates to rich, conversion-focused content with:
- Pain-first messaging
- Specific use cases and outcomes
- FAQ with schema markup
- Comparison tables (Verum vs alternatives)
- Case study integration
- Industry-specific examples

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
- `18mo` - combined unit, no space
- `11K+` - abbreviated number with modifier

❌ BAD (contains spaces - WILL WRAP):
- `13 hrs` - HAS SPACE, will wrap to two lines
- `84 days` - HAS SPACE, will wrap
- `15+ hrs` - HAS SPACE, will wrap
- `5+ hrs` - HAS SPACE, will wrap
- `18 mo` - HAS SPACE, will wrap

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

### Anti-AI Detection Guidelines

To ensure authentic, human-sounding copy:

1. **Use contractions** - "we're" not "we are", "doesn't" not "does not"
2. **Vary sentence length dramatically** - Mix punchy 4-word sentences with longer, flowing ones
3. **Add natural pauses** - Organic breaks that let thoughts breathe
4. **Include occasional tangents** - Brief detours that show personality
5. **Use relatable metaphors** - Compare data problems to everyday frustrations
6. **Show you understand the reader** - Acknowledge their reality, frustrations, and constraints

### What to AVOID (AI Detection Flags)

- **Em-dashes** - Use very rarely. Heavily flagged as AI-generated
- **Performative interjections** - "That's not a typo." "Good question." "And honestly?"
- **Commentary after stats** - "Let that sink in" or "You read that right"
- **Forced casual phrases** - "Here's the thing:" or "Spoiler alert:"
- **Rhetorical questions followed by answers** - "What does this mean? It means..."
- **Overly parallel structure** - Three bullets that all start the same way

### What WORKS (Human Patterns)

- Short sentences that just end. No commentary needed.
- Thoughts that trail into the next paragraph naturally
- Varied paragraph lengths. Some long. Some just one sentence.
- Specific details only someone in the industry would know
- Admitting uncertainty or limitations occasionally
- Second-person "you" that speaks directly to the reader's situation

**Voice check**: Read it out loud. If it sounds like a person talking to a colleague, you're on track.

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

### Key Files
- **Main CSS:** `/css/styles.css`
- **Writing guidelines:** `/docs/WRITING-GUIDELINES.md`
- **This file:** `/CLAUDE.md`
- **Solutions index:** `/solutions/index.html`

### Industry Pages Location
All at: `/solutions/[industry]-data-enrichment/index.html`

Complete list (28 pages):
- accounting-data-enrichment
- adtech-data-enrichment
- ai-ml-data-enrichment
- b2b-services-data-enrichment
- construction-data-enrichment
- consulting-data-enrichment
- cybersecurity-data-enrichment
- e-commerce-data-enrichment
- ecommerce-data-enrichment (duplicate - check if needed)
- education-data-enrichment
- energy-data-enrichment
- fintech-data-enrichment
- government-data-enrichment
- healthcare-data-enrichment
- hr-tech-data-enrichment
- insurance-data-enrichment
- legal-data-enrichment
- logistics-data-enrichment
- manufacturing-data-enrichment
- martech-data-enrichment
- media-data-enrichment
- nonprofit-data-enrichment
- professional-services-data-enrichment
- real-estate-data-enrichment
- retail-data-enrichment
- saas-data-enrichment
- technology-data-enrichment
- telecommunications-data-enrichment
- travel-data-enrichment

### Services Pages Location
- `/services/index.html` - Main services grid
- `/services/data-cleaning.html` - Data cleaning service
- `/services/data-enrichment.html` - Data enrichment service
- `/services/data-analysis.html` - Data analysis service
- `/services/icp-analysis.html` - ICP analysis (most complete)

---

## Services Section - Next Steps

The services section needs strategic planning before rewrite:

### Current State
- Services index: Simple 3-card grid (114 lines)
- Data Cleaning: Basic problem/solution (~113 lines)
- Data Enrichment: Basic what we do (~134 lines)
- Data Analysis: Links to ICP, basic content (~134 lines)
- ICP Analysis: Most complete with custom CSS, pricing ($2,500), case study link (~257 lines)

### Questions to Address
1. **Page structure:** Should services follow same template as industry pages?
2. **Differentiation:** How to make each service page unique (not just feature lists)?
3. **Pricing:** ICP has pricing ($2,500). Should other services show pricing?
4. **Case studies:** How to integrate case studies effectively?
5. **Cross-linking:** How to connect services to industry pages?
6. **Schema markup:** Service schema vs FAQ schema?

### Potential Service Page Structure
- Pain-first opening (different from industry pages)
- Specific deliverables with examples
- Process with timeline expectations
- Pricing or "starting at" ranges
- Case study snippets
- FAQ with schema
- Related industries that use this service

---

## Analytics & Tracking

All pages include:
- Google Analytics: `G-R416JZ91B1`
- Microsoft Clarity: `uzzgoxxnof`

---

## Git Workflow

**Never commit without running stat verification:**
```bash
grep -r "pain-stat__number" /Users/rome/Documents/projects/verum-website/solutions/*/index.html | grep -E ">[^<]+ [^<]+<"
```

If output is empty, stats are clean. If any results appear, fix before committing.
