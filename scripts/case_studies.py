#!/usr/bin/env python3
"""Generate case study pages and hub for Verum website."""
import os

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"

def generate_case_study(slug, title, meta_desc, hero_subtitle, meta_items, results, challenge_html, approach_html, finding_html, additional_html, recommendations_html, cta_headline, cta_text, cta_button, breadcrumb_name):
    """Generate a case study page."""
    results_cards = "\n".join(f'''        <div class="result-card">
          <div class="result-card__value">{r[0]}</div>
          <div class="result-card__label">{r[1]}</div>
        </div>''' for r in results)

    meta_divs = "\n".join(f'''        <div class="case-study-meta__item">
          <div class="case-study-meta__label">{m[0]}</div>
          <div class="case-study-meta__value">{m[1]}</div>
        </div>''' for m in meta_items)

    og_title = title.split(" | ")[0] if " | " in title else title
    og_desc = meta_desc[:200]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Verum</title>
  <meta name="description" content="{meta_desc}">

  <link rel="canonical" href="https://veruminc.com/case-studies/{slug}/">
  <link rel="icon" type="image/svg+xml" href="/assets/favicons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicons/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicons/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#00b894">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css?v=6">

  <meta property="og:type" content="article">
  <meta property="og:url" content="https://veruminc.com/case-studies/{slug}/">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="https://veruminc.com/assets/social/twitter-card.png">

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R416JZ91B1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-R416JZ91B1');
  </script>
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "uzzgoxxnof");
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://veruminc.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "Case Studies", "item": "https://veruminc.com/case-studies/"}},
      {{"@type": "ListItem", "position": 3, "name": "{breadcrumb_name}"}}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{og_title}",
    "description": "{og_desc}",
    "author": {{
      "@type": "Organization",
      "name": "Verum"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Verum"
    }}
  }}
  </script>

  <style>
    .case-study-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: var(--space-xl);
      margin-bottom: var(--space-2xl);
      padding-bottom: var(--space-xl);
      border-bottom: 1px solid var(--color-border);
    }}
    .case-study-meta__item {{
      flex: 1;
      min-width: 150px;
    }}
    .case-study-meta__label {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-text-muted);
      margin-bottom: 0.25rem;
    }}
    .case-study-meta__value {{
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--color-text-primary);
    }}
    .results-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: var(--space-lg);
      margin: var(--space-xl) 0;
    }}
    .result-card {{
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-xl);
      text-align: center;
    }}
    .result-card__value {{
      font-size: 2.5rem;
      font-weight: 700;
      color: var(--color-teal);
      line-height: 1;
    }}
    .result-card__label {{
      font-size: 0.875rem;
      color: var(--color-text-secondary);
      margin-top: var(--space-sm);
    }}
    .insight-box {{
      background: linear-gradient(135deg, rgba(0, 184, 148, 0.1) 0%, rgba(0, 184, 148, 0.05) 100%);
      border: 1px solid var(--color-teal);
      border-radius: var(--radius-lg);
      padding: var(--space-xl);
      margin: var(--space-xl) 0;
    }}
    .insight-box__title {{
      font-weight: 600;
      color: var(--color-teal);
      margin-bottom: var(--space-sm);
    }}
    .segment-table {{
      width: 100%;
      border-collapse: collapse;
      margin: var(--space-lg) 0;
    }}
    .segment-table th,
    .segment-table td {{
      padding: var(--space-md);
      text-align: left;
      border-bottom: 1px solid var(--color-border);
    }}
    .segment-table th {{
      font-weight: 600;
      color: var(--color-text-muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .segment-table td {{
      color: var(--color-text-secondary);
    }}
    .segment-table tr:hover td {{
      background: var(--color-bg-card);
    }}
    .highlight-row td {{
      background: rgba(0, 184, 148, 0.1);
      color: var(--color-text-primary);
      font-weight: 500;
    }}
  </style>
</head>
<body>
  <header id="site-header"></header>
  <noscript>
    <nav style="background:#1a1a2e;padding:1rem;text-align:center;">
      <a href="/" style="color:#fff;margin:0 1rem;">Home</a>
      <a href="/services/" style="color:#fff;margin:0 1rem;">Services</a>
      <a href="/solutions/" style="color:#fff;margin:0 1rem;">Solutions</a>
      <a href="/resources/" style="color:#fff;margin:0 1rem;">Blog</a>
      <a href="/about.html" style="color:#fff;margin:0 1rem;">About</a>
      <a href="/contact.html" style="color:#fff;margin:0 1rem;">Contact</a>
    </nav>
  </noscript>

  <section class="page-hero">
    <div class="container">
      <p style="font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-teal); margin-bottom: var(--space-md);">Case Study</p>
      <h1 class="page-hero__title">{og_title}</h1>
      <p class="page-hero__subtitle">{hero_subtitle}</p>
    </div>
  </section>

  <section class="content">
    <div class="container" style="max-width: 800px;">

      <div class="case-study-meta">
{meta_divs}
      </div>

      <div class="results-grid">
{results_cards}
      </div>

{challenge_html}

{approach_html}

{finding_html}

{additional_html}

{recommendations_html}

      <h2>{cta_headline}</h2>
      <p>{cta_text}</p>

      <div class="text-center mt-xl">
        <a href="/#contact" class="btn btn--primary btn--lg">{cta_button}</a>
      </div>
    </div>
  </section>

  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


# ── Case Study 1: CRM Cleaning for Staffing Agency ──────────────────────────

CS_CRM_CLEANING = {
    "slug": "crm-cleaning-staffing-agency",
    "title": "CRM Data Cleaning: How a Staffing Agency Cut 42% of Dead Records and Doubled Email Response Rates",
    "meta_desc": "A staffing agency had 85,000 CRM records with duplicate contacts, outdated emails, and inconsistent formatting. Verum cleaned the entire database in 5 days.",
    "hero_subtitle": "85,000 records cleaned in 5 days. Duplicate contacts merged, dead emails removed, and job titles standardized across three acquired company databases.",
    "breadcrumb_name": "CRM Cleaning for Staffing Agency",
    "meta_items": [
        ("Industry", "Staffing & Recruiting"),
        ("Service", "Data Cleaning"),
        ("Records Processed", "85,000"),
        ("Turnaround", "5 days"),
    ],
    "results": [
        ("42%", "Duplicate and dead records removed"),
        ("2x", "Email response rate after cleaning"),
        ("91%", "Email deliverability (up from 62%)"),
    ],
    "challenge_html": """      <h2>The Challenge</h2>
      <p>A regional staffing agency had acquired two smaller firms over the previous 18 months. Each acquisition brought a separate CRM database with its own formatting conventions, duplicate records, and data quality issues.</p>

      <p>The combined database held 85,000 contact records. The sales team had stopped trusting it. Reps were calling the same candidate twice, emailing addresses that bounced, and finding three different records for a single hiring manager with slightly different name spellings.</p>

      <p>They tried assigning an intern to clean it manually. After two weeks, the intern had processed 1,200 records and quit.</p>""",

    "approach_html": """      <h2>Our Approach</h2>
      <p>We ran the full database through a four-stage cleaning pipeline:</p>

      <h3>Stage 1: Deduplication</h3>
      <p>Fuzzy matching across name, email, phone, and company identified 18,400 duplicate clusters. Each cluster was merged into a single golden record, preserving the most recent contact information and the most complete field set.</p>

      <h3>Stage 2: Email Validation</h3>
      <p>Every email address was checked via SMTP verification. We flagged bounced addresses, catch-all domains, and role-based emails (info@, admin@). 23% of emails were invalid.</p>

      <h3>Stage 3: Phone Verification</h3>
      <p>Phone numbers were validated against carrier databases. Landlines, disconnected numbers, and VoIP lines were flagged separately so the team could prioritize direct dials and mobile numbers.</p>

      <h3>Stage 4: Standardization</h3>
      <p>Job titles were normalized to a consistent taxonomy (e.g., "VP of HR," "Vice President Human Resources," and "VP, People" all became "VP of Human Resources"). Company names, addresses, and industry codes were standardized to match.</p>""",

    "finding_html": """      <h2>The Key Finding</h2>

      <div class="insight-box">
        <div class="insight-box__title">35,700 records were actively harming outreach performance</div>
        <p style="margin: 0;">Of the 85,000 records, 18,400 were duplicates, 12,300 had invalid emails, and 5,000 had disconnected phone numbers. The sales team was spending roughly 40% of their outreach effort on records that could never convert.</p>
      </div>

      <table class="segment-table">
        <thead>
          <tr>
            <th>Issue Type</th>
            <th>Records</th>
            <th>% of Total</th>
            <th>Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Duplicate clusters</td>
            <td>18,400</td>
            <td>21.6%</td>
            <td>Same person contacted multiple times</td>
          </tr>
          <tr>
            <td>Invalid emails</td>
            <td>12,300</td>
            <td>14.5%</td>
            <td>Bounces hurting sender reputation</td>
          </tr>
          <tr>
            <td>Disconnected phones</td>
            <td>5,000</td>
            <td>5.9%</td>
            <td>Wasted call time</td>
          </tr>
          <tr>
            <td>Non-standard titles</td>
            <td>31,200</td>
            <td>36.7%</td>
            <td>Broken list segmentation</td>
          </tr>
          <tr class="highlight-row">
            <td>Clean, usable records</td>
            <td>49,300</td>
            <td>58%</td>
            <td>Ready for outreach</td>
          </tr>
        </tbody>
      </table>""",

    "additional_html": """      <h2>Results After 30 Days</h2>
      <p>Within a month of deploying the cleaned database, the staffing agency saw measurable improvements:</p>
      <ul>
        <li><strong>Email deliverability jumped from 62% to 91%</strong> after removing invalid addresses</li>
        <li><strong>Response rates doubled</strong> because reps were reaching real people at correct addresses</li>
        <li><strong>Call connect rates improved 35%</strong> with verified phone numbers</li>
        <li><strong>List segmentation started working</strong> because job titles were consistent enough to filter</li>
      </ul>

      <p>The sales manager reported that reps stopped complaining about "bad data" within the first week. They went from dreading CRM updates to actually using the system for territory planning.</p>""",

    "recommendations_html": """      <h2>What We Recommended Next</h2>
      <ol>
        <li><strong>Quarterly cleaning cycles</strong> to catch data decay before it compounds</li>
        <li><strong>Standardized import rules</strong> for future acquisitions</li>
        <li><strong>Email validation on inbound forms</strong> to prevent bad data from entering the CRM</li>
        <li><strong>Enrichment pass</strong> to fill missing fields on the 49,300 clean records</li>
      </ol>""",

    "cta_headline": "Your CRM Probably Has the Same Problems",
    "cta_text": "B2B databases decay at roughly 30% per year. If you haven't cleaned your CRM in the last 12 months, you're likely spending a significant portion of outreach effort on records that will never convert.",
    "cta_button": "Get a Free Data Audit",
}


# ── Case Study 2: Contact Enrichment for Insurance Brokerage ─────────────────

CS_ENRICHMENT = {
    "slug": "contact-enrichment-insurance-brokerage",
    "title": "Contact Enrichment: How a B2B Insurance Brokerage Added Direct Dials to 73% of Their Target Accounts",
    "meta_desc": "An insurance brokerage had company names but no contacts. Verum enriched 4,200 accounts with verified decision-maker emails, direct dials, and titles in 48 hours.",
    "hero_subtitle": "4,200 target accounts enriched with decision-maker contact data. 73% direct dial coverage, 89% email coverage, all verified before delivery.",
    "breadcrumb_name": "Contact Enrichment for Insurance Brokerage",
    "meta_items": [
        ("Industry", "Insurance"),
        ("Service", "Data Enrichment"),
        ("Accounts Enriched", "4,200"),
        ("Turnaround", "48 hours"),
    ],
    "results": [
        ("73%", "Direct dial phone coverage"),
        ("89%", "Verified email coverage"),
        ("48hrs", "From submission to delivery"),
    ],
    "challenge_html": """      <h2>The Challenge</h2>
      <p>A commercial insurance brokerage had built a target account list of 4,200 mid-market companies. They knew the company names, addresses, and industries. What they didn't have: the names, titles, emails, and phone numbers of the people who actually make insurance purchasing decisions.</p>

      <p>Their producers had been trying to find contacts manually through LinkedIn and Google searches. It was taking each producer roughly 15 minutes per company to find a CFO or risk manager contact. At that rate, covering their entire territory would take over a year.</p>

      <p>They'd tried two self-serve data platforms. One returned mostly generic info@ emails. The other had decent email coverage but phone numbers that rang receptionists instead of decision-makers.</p>""",

    "approach_html": """      <h2>Our Approach</h2>
      <p>We ran a multi-source enrichment process targeting specific decision-maker personas:</p>

      <h3>Persona Definition</h3>
      <p>We worked with the brokerage to define their buyer personas by priority:</p>
      <ol>
        <li><strong>Primary:</strong> CFO, VP of Finance, Controller</li>
        <li><strong>Secondary:</strong> Risk Manager, Director of Operations, Office Manager</li>
        <li><strong>Tertiary:</strong> Owner, President, CEO (for companies under 50 employees)</li>
      </ol>

      <h3>Multi-Source Enrichment</h3>
      <p>Each account was enriched through a waterfall of data sources. We didn't stop at the first match. Instead, we cross-referenced multiple providers to find the highest-confidence contact for each persona, prioritizing direct dial numbers over main lines.</p>

      <h3>Verification</h3>
      <p>Every email was SMTP-verified. Phone numbers were checked against carrier databases to confirm they were active direct dials rather than main office lines or fax numbers. Contacts with LinkedIn profiles were cross-referenced for current employment.</p>""",

    "finding_html": """      <h2>The Key Finding</h2>

      <div class="insight-box">
        <div class="insight-box__title">Single-source enrichment was leaving 40% of contacts on the table</div>
        <p style="margin: 0;">No single data provider covered more than 52% of these mid-market accounts. By waterfall-enriching across multiple sources, we increased total coverage to 89% for emails and 73% for direct dials. The brokerage's previous vendors had been giving them less than half of what was available.</p>
      </div>

      <table class="segment-table">
        <thead>
          <tr>
            <th>Data Point</th>
            <th>Source 1 Only</th>
            <th>Multi-Source</th>
            <th>Improvement</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Decision-maker identified</td>
            <td>58%</td>
            <td>94%</td>
            <td>+36 pts</td>
          </tr>
          <tr>
            <td>Verified email</td>
            <td>52%</td>
            <td>89%</td>
            <td>+37 pts</td>
          </tr>
          <tr class="highlight-row">
            <td>Direct dial phone</td>
            <td>31%</td>
            <td>73%</td>
            <td>+42 pts</td>
          </tr>
          <tr>
            <td>Job title confirmed</td>
            <td>48%</td>
            <td>91%</td>
            <td>+43 pts</td>
          </tr>
        </tbody>
      </table>""",

    "additional_html": """      <h2>Results After 60 Days</h2>
      <p>The brokerage armed their producers with the enriched data and tracked outcomes over two months:</p>
      <ul>
        <li><strong>Meeting-set rate tripled</strong> compared to cold calling main office lines</li>
        <li><strong>Producers covered 4x more accounts per week</strong> because they stopped researching contacts manually</li>
        <li><strong>12 new policies written</strong> directly attributed to enriched contacts in the first 60 days</li>
        <li><strong>Estimated ROI of 8:1</strong> on the enrichment investment based on first-year premiums</li>
      </ul>

      <h3>Coverage by Company Size</h3>
      <p>Enrichment coverage varied by company size, which informed their outreach strategy:</p>
      <ul>
        <li><strong>Under 50 employees:</strong> 68% direct dial coverage (often owner/CEO is the buyer)</li>
        <li><strong>50-200 employees:</strong> 79% direct dial coverage (dedicated finance roles)</li>
        <li><strong>200-500 employees:</strong> 71% direct dial coverage (larger teams, more titles to try)</li>
      </ul>""",

    "recommendations_html": """      <h2>What We Recommended Next</h2>
      <ol>
        <li><strong>Quarterly refresh</strong> on the full list to catch job changes and new hires</li>
        <li><strong>Expand to 8,000 accounts</strong> by adding adjacent territories with the same enrichment process</li>
        <li><strong>Add trigger monitoring</strong> for leadership changes at existing target accounts</li>
        <li><strong>Score accounts by enrichment depth</strong> to prioritize producers' time on accounts with full contact data</li>
      </ol>""",

    "cta_headline": "Stop Calling Main Lines",
    "cta_text": "Your sales team shouldn't spend their time researching contacts. Tell us your target market and buyer persona, and we'll deliver verified decision-maker data you can load directly into your CRM.",
    "cta_button": "See What We'll Find",
}


# ── Case Study 3: Prospect List Building for Commercial Real Estate ──────────

CS_LIST_BUILDING = {
    "slug": "prospect-list-building-commercial-real-estate",
    "title": "Prospect List Building: How a CRE Firm Found 2,800 Property Managers No One Else Was Calling",
    "meta_desc": "A commercial real estate services firm needed property manager contacts in 12 markets. Verum built a verified prospect list of 2,800 decision-makers from scratch.",
    "hero_subtitle": "2,800 verified property management contacts across 12 metro areas, built from scratch in 10 days. 87% email deliverability on first campaign.",
    "breadcrumb_name": "Prospect List Building for CRE Firm",
    "meta_items": [
        ("Industry", "Commercial Real Estate"),
        ("Service", "Data Discovery"),
        ("Contacts Delivered", "2,800"),
        ("Markets Covered", "12 metros"),
    ],
    "results": [
        ("2,800", "Verified property manager contacts"),
        ("87%", "Email deliverability on first send"),
        ("12", "Metro markets covered"),
    ],
    "challenge_html": """      <h2>The Challenge</h2>
      <p>A commercial real estate services company was expanding into property management maintenance contracts. Their target buyer was straightforward: property managers at commercial buildings with 50,000+ square feet in 12 metro areas.</p>

      <p>The problem? Property managers don't show up on standard B2B data platforms. They're not publicly listed executives. Many work for small management companies that don't appear in enterprise databases. Some manage properties for family offices with no web presence.</p>

      <p>The firm had tried buying lists from three different data vendors. The best one delivered 900 contacts with 34% bounce rates. Most of the "property managers" turned out to be leasing agents or maintenance supervisors with no purchasing authority.</p>""",

    "approach_html": """      <h2>Our Approach</h2>
      <p>Standard data platforms aren't built for this kind of niche prospecting. We used a multi-channel discovery process:</p>

      <h3>Source 1: Property Records</h3>
      <p>We started with commercial property databases to identify buildings matching the size criteria in each metro. This gave us property addresses and management company names, but rarely direct contacts.</p>

      <h3>Source 2: Business Registration Cross-Reference</h3>
      <p>Management company names were cross-referenced against state business registrations, professional licensing databases, and industry association directories to identify the people behind each company.</p>

      <h3>Source 3: Multi-Source Contact Enrichment</h3>
      <p>Once we had names and companies, we ran our standard enrichment waterfall to find verified emails and direct dial phone numbers. For smaller firms where the owner is the property manager, we pulled ownership records.</p>

      <h3>Quality Filter</h3>
      <p>Every contact was verified for title accuracy. We removed leasing agents, maintenance staff, and anyone whose role didn't include vendor purchasing decisions. The final list only included people who could sign a maintenance contract.</p>""",

    "finding_html": """      <h2>The Key Finding</h2>

      <div class="insight-box">
        <div class="insight-box__title">78% of the delivered contacts weren't available from any single data vendor</div>
        <p style="margin: 0;">We cross-checked our final list against the three vendors the firm had already tried. Only 22% of our contacts appeared in any of those databases. The remaining 78% were only discoverable through the multi-source approach, which is exactly why the firm's previous list-buying efforts had fallen short.</p>
      </div>

      <table class="segment-table">
        <thead>
          <tr>
            <th>Metro Area</th>
            <th>Contacts Found</th>
            <th>Email Coverage</th>
            <th>Phone Coverage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Dallas-Fort Worth</td>
            <td>380</td>
            <td>91%</td>
            <td>74%</td>
          </tr>
          <tr>
            <td>Atlanta</td>
            <td>340</td>
            <td>88%</td>
            <td>71%</td>
          </tr>
          <tr>
            <td>Phoenix</td>
            <td>290</td>
            <td>90%</td>
            <td>69%</td>
          </tr>
          <tr>
            <td>Denver</td>
            <td>250</td>
            <td>87%</td>
            <td>72%</td>
          </tr>
          <tr class="highlight-row">
            <td>All 12 metros combined</td>
            <td>2,800</td>
            <td>87%</td>
            <td>71%</td>
          </tr>
        </tbody>
      </table>""",

    "additional_html": """      <h2>Results After 90 Days</h2>
      <p>The firm launched a multi-channel outreach campaign using the delivered list:</p>
      <ul>
        <li><strong>87% email deliverability</strong> on the first campaign (industry average for purchased lists is around 70%)</li>
        <li><strong>4.2% reply rate</strong> on cold email sequences, well above the 1-2% industry benchmark</li>
        <li><strong>47 qualified meetings booked</strong> in the first quarter</li>
        <li><strong>8 signed contracts</strong> worth $340K in annual recurring revenue</li>
      </ul>

      <h3>Why the Reply Rates Were High</h3>
      <p>The firm attributed the strong response rates to two factors:</p>
      <ul>
        <li><strong>Correct titles:</strong> Every email went to someone who actually makes vendor decisions, not a gatekeeper</li>
        <li><strong>Low competition:</strong> Because 78% of these contacts weren't in standard databases, most had never received a cold email from a competitor</li>
      </ul>""",

    "recommendations_html": """      <h2>What We Recommended Next</h2>
      <ol>
        <li><strong>Expand to 8 additional metros</strong> using the same discovery methodology</li>
        <li><strong>Add building-level data</strong> (square footage, building age, current maintenance contracts) for better targeting</li>
        <li><strong>Monthly net-new monitoring</strong> to catch new property management companies entering each market</li>
        <li><strong>Quarterly contact refresh</strong> to update job changes and add new hires</li>
      </ol>""",

    "cta_headline": "Need Contacts That Don't Exist in Standard Databases?",
    "cta_text": "If your target buyer is in a niche role or underserved industry, off-the-shelf data platforms won't cut it. Tell us who you're trying to reach and we'll build the list from scratch.",
    "cta_button": "See What We'll Find",
}


# ── Case Study 4: CRM Migration for Manufacturing Company ───────────────────

CS_CRM_MIGRATION = {
    "slug": "crm-migration-data-prep-manufacturing",
    "title": "CRM Migration: How a Manufacturer Moved 120K Records to HubSpot Without Losing a Single Contact",
    "meta_desc": "A manufacturing company migrated 120,000 records from Salesforce to HubSpot. Verum cleaned, deduplicated, and reformatted every record before import. Zero data loss.",
    "hero_subtitle": "120,000 records cleaned, deduplicated, and reformatted for a Salesforce-to-HubSpot migration. Zero contacts lost. 14 custom field mappings preserved.",
    "breadcrumb_name": "CRM Migration for Manufacturer",
    "meta_items": [
        ("Industry", "Manufacturing"),
        ("Service", "Data Cleaning & Validation"),
        ("Records Migrated", "120,000"),
        ("Turnaround", "8 days"),
    ],
    "results": [
        ("0", "Records lost during migration"),
        ("28%", "Duplicates removed pre-migration"),
        ("14", "Custom field mappings preserved"),
    ],
    "challenge_html": """      <h2>The Challenge</h2>
      <p>A mid-market industrial parts manufacturer was switching from Salesforce to HubSpot. Their Salesforce instance had been in use for 7 years and contained 120,000 contact and company records across 14 custom fields.</p>

      <p>The problem wasn't the migration tool. HubSpot's import works fine for clean data. The problem was that the data wasn't clean. Seven years of manual entry by dozens of sales reps had created a mess:</p>

      <ul>
        <li>Company names entered inconsistently ("ABC Manufacturing" vs. "ABC Mfg" vs. "A.B.C. Manufacturing Inc.")</li>
        <li>Phone numbers in 8 different formats</li>
        <li>34,000 duplicate records from years of trade show lead imports</li>
        <li>Custom picklist values that didn't match HubSpot's field types</li>
        <li>5,200 contacts with no email or phone (just a name and company)</li>
      </ul>

      <p>Their IT team estimated the cleanup would take 3-4 months of manual work. The HubSpot contract was starting in 3 weeks.</p>""",

    "approach_html": """      <h2>Our Approach</h2>
      <p>We ran the migration prep in three parallel workstreams:</p>

      <h3>Workstream 1: Deduplication</h3>
      <p>Fuzzy matching on company names, contact names, emails, and phone numbers identified 34,000 duplicate records in 15,200 clusters. We built merge rules that preserved the most recent activity date, the most complete field set, and all associated deal history.</p>

      <h3>Workstream 2: Standardization & Field Mapping</h3>
      <p>We mapped all 14 Salesforce custom fields to their HubSpot equivalents. Picklist values were translated. Phone numbers were reformatted to E.164. Company names were standardized. State abbreviations were normalized. Every record was validated against HubSpot's import requirements before export.</p>

      <h3>Workstream 3: Enrichment of Skeleton Records</h3>
      <p>The 5,200 name-only records were enriched to add email addresses and phone numbers where possible. We recovered usable contact data for 3,800 of them (73%), turning dead records into reachable contacts.</p>""",

    "finding_html": """      <h2>The Key Finding</h2>

      <div class="insight-box">
        <div class="insight-box__title">28% of all records were duplicates that would have created chaos in HubSpot</div>
        <p style="margin: 0;">Importing 34,000 duplicates into a fresh CRM would have immediately recreated the same data quality problems they were trying to escape. Cleaning before migration meant the HubSpot instance started with a trustworthy foundation instead of inheriting seven years of accumulated data debt.</p>
      </div>

      <table class="segment-table">
        <thead>
          <tr>
            <th>Category</th>
            <th>Before</th>
            <th>After</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Total records</td>
            <td>120,000</td>
            <td>89,600</td>
            <td>Duplicates merged, dead records removed</td>
          </tr>
          <tr>
            <td>Duplicate clusters</td>
            <td>15,200</td>
            <td>0</td>
            <td>Merged into golden records</td>
          </tr>
          <tr>
            <td>Skeleton records (name only)</td>
            <td>5,200</td>
            <td>1,400</td>
            <td>73% enriched with contact data</td>
          </tr>
          <tr class="highlight-row">
            <td>Migration-ready records</td>
            <td>0</td>
            <td>89,600</td>
            <td>Clean, standardized, HubSpot-formatted</td>
          </tr>
        </tbody>
      </table>""",

    "additional_html": """      <h2>Migration Outcome</h2>
      <p>The cleaned dataset was imported into HubSpot over a single weekend:</p>
      <ul>
        <li><strong>Zero records lost</strong> during import. Every legitimate contact was preserved.</li>
        <li><strong>All 14 custom fields mapped correctly</strong> with matching picklist values</li>
        <li><strong>Sales team was productive on Day 1</strong> instead of spending weeks fixing data in the new CRM</li>
        <li><strong>HubSpot deduplication tools confirmed 0 duplicates</strong> on the imported dataset</li>
      </ul>

      <h3>The Hidden Benefit</h3>
      <p>By recovering 3,800 skeleton records through enrichment, the migration actually increased the company's usable contact count. They moved to HubSpot with fewer total records but more actionable contacts than they'd ever had in Salesforce.</p>

      <p>The VP of Sales said it was the first time in years that a rep could search the CRM and trust what came back.</p>""",

    "recommendations_html": """      <h2>What We Recommended Next</h2>
      <ol>
        <li><strong>Set up HubSpot deduplication rules</strong> to prevent new duplicates from forming</li>
        <li><strong>Implement required field validation</strong> on new contact creation</li>
        <li><strong>Schedule quarterly data hygiene reviews</strong> to maintain the clean baseline</li>
        <li><strong>Enrich the remaining 1,400 skeleton records</strong> as more data becomes available</li>
      </ol>""",

    "cta_headline": "Migrating Your CRM?",
    "cta_text": "Don't import dirty data into a clean system. We'll deduplicate, standardize, and validate every record before it touches your new CRM.",
    "cta_button": "Get Migration-Ready Data",
}


# ── Case Study 5: Ongoing Database Maintenance for Marketing Agency ──────────

CS_MAINTENANCE = {
    "slug": "database-maintenance-marketing-agency",
    "title": "Database Maintenance: How a Marketing Agency Kept 93% Deliverability Across 200K Contacts",
    "meta_desc": "A B2B marketing agency sends campaigns for 40+ clients. Verum's monthly data maintenance keeps their shared database at 93% deliverability and catches decay before it hurts.",
    "hero_subtitle": "Monthly maintenance on a 200,000-contact database serving 40+ clients. Decay caught early, deliverability held at 93%, sender reputation protected.",
    "breadcrumb_name": "Database Maintenance for Marketing Agency",
    "meta_items": [
        ("Industry", "Marketing Agency"),
        ("Service", "Ongoing Maintenance"),
        ("Database Size", "200,000 contacts"),
        ("Frequency", "Monthly"),
    ],
    "results": [
        ("93%", "Email deliverability maintained"),
        ("6,200", "Decayed records caught per month"),
        ("$0", "Blacklist incidents since starting"),
    ],
    "challenge_html": """      <h2>The Challenge</h2>
      <p>A B2B marketing agency manages email campaigns for 40+ clients. Their shared contact database holds over 200,000 records across multiple industries. Each month, they send roughly 800,000 emails on behalf of their clients.</p>

      <p>The agency had been burned twice by deliverability crises. The first time, a batch of 15,000 decayed emails tanked their sender reputation and got their primary sending domain blacklisted. It took three weeks to recover. The second time, a client uploaded 8,000 purchased contacts without verification, causing a 12% bounce rate on the next campaign.</p>

      <p>After the second incident, the agency decided to invest in proactive maintenance rather than keep reacting to crises.</p>""",

    "approach_html": """      <h2>Our Approach</h2>
      <p>We set up a monthly maintenance cycle with four components:</p>

      <h3>Component 1: Full Email Re-Verification</h3>
      <p>Every contact is re-verified via SMTP each month. Emails that have gone invalid since the last check are flagged and suppressed before the next campaign send. This catches job changes, company closures, and deactivated mailboxes.</p>

      <h3>Component 2: Bounce Analysis</h3>
      <p>We analyze the previous month's bounce logs to identify patterns. Domains with rising bounce rates are investigated. Contacts at those domains are re-verified or suppressed before they trigger ISP penalties.</p>

      <h3>Component 3: New Record Validation</h3>
      <p>Any contacts added during the month (from client uploads, form submissions, or list purchases) are validated before they enter the active sending pool. This prevents the "bad upload" scenario that caused the agency's second blacklisting.</p>

      <h3>Component 4: Quarterly Deep Clean</h3>
      <p>Every quarter, we run a full deduplication pass, standardize new records, and re-enrich contacts that are missing key fields. This keeps the database in shape as it grows and prevents the gradual accumulation of data quality issues.</p>""",

    "finding_html": """      <h2>The Key Finding</h2>

      <div class="insight-box">
        <div class="insight-box__title">B2B email data decays at roughly 3% per month</div>
        <p style="margin: 0;">On average, we catch 6,200 newly-invalid records each month in the 200,000-contact database. That's a 3.1% monthly decay rate, consistent with industry benchmarks of 2-3% monthly turnover in B2B roles. Without monthly cleaning, the agency would accumulate over 35,000 bad records per six-month period.</p>
      </div>

      <table class="segment-table">
        <thead>
          <tr>
            <th>Month</th>
            <th>Records Checked</th>
            <th>Newly Invalid</th>
            <th>Decay Rate</th>
            <th>Deliverability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Month 1</td>
            <td>200,000</td>
            <td>8,400</td>
            <td>4.2%</td>
            <td>89%</td>
          </tr>
          <tr>
            <td>Month 2</td>
            <td>193,200</td>
            <td>5,800</td>
            <td>3.0%</td>
            <td>92%</td>
          </tr>
          <tr>
            <td>Month 3</td>
            <td>191,500</td>
            <td>5,900</td>
            <td>3.1%</td>
            <td>93%</td>
          </tr>
          <tr class="highlight-row">
            <td>Months 4-12 avg</td>
            <td>195,000</td>
            <td>6,200</td>
            <td>3.1%</td>
            <td>93%</td>
          </tr>
        </tbody>
      </table>""",

    "additional_html": """      <h2>Results After 12 Months</h2>
      <p>One year of monthly maintenance transformed the agency's operations:</p>
      <ul>
        <li><strong>Zero blacklisting incidents</strong> in 12 months (compared to two in the previous year)</li>
        <li><strong>Deliverability stabilized at 93%</strong> after the initial cleanup brought it up from 89%</li>
        <li><strong>Client retention improved</strong> because campaign performance became predictable</li>
        <li><strong>New client onboarding accelerated</strong> because every uploaded list was validated before first send</li>
      </ul>

      <h3>The Math on Proactive vs. Reactive</h3>
      <p>The agency calculated the cost comparison:</p>
      <ul>
        <li><strong>Reactive approach (previous year):</strong> Two blacklisting incidents cost roughly $45,000 in lost revenue, recovery fees, and client credits</li>
        <li><strong>Proactive maintenance:</strong> Monthly cleaning costs a fraction of a single incident</li>
        <li><strong>Net savings:</strong> The maintenance program paid for itself within the first quarter</li>
      </ul>""",

    "recommendations_html": """      <h2>What We Deliver Each Month</h2>
      <ol>
        <li><strong>Updated suppression list</strong> of newly-invalid contacts, ready for import</li>
        <li><strong>Decay report</strong> showing trends by domain, industry, and client segment</li>
        <li><strong>New record validation results</strong> for any contacts added that month</li>
        <li><strong>Quarterly deep clean summary</strong> with deduplication and enrichment stats</li>
      </ol>""",

    "cta_headline": "Protect Your Sender Reputation",
    "cta_text": "A single blacklisting incident costs more than a year of proactive maintenance. Don't wait for your deliverability to drop.",
    "cta_button": "Set Up Monthly Maintenance",
}


ALL_CASE_STUDIES = [CS_CRM_CLEANING, CS_ENRICHMENT, CS_LIST_BUILDING, CS_CRM_MIGRATION, CS_MAINTENANCE]


def build_hub_page():
    """Generate the case studies index/hub page."""
    cards = []
    for cs in ALL_CASE_STUDIES:
        # Extract a short summary from meta_desc
        summary = cs["meta_desc"]
        cards.append(f'''          <a href="/case-studies/{cs["slug"]}/" class="alt-card">
            <h3 class="alt-card__title">{cs["results"][0][0]} {cs["results"][0][1].lower()}</h3>
            <p class="alt-card__text">{summary}</p>
          </a>''')

    # Add the existing ICP case study
    icp_card = '''          <a href="/case-studies/icp-analysis-series-a-saas/" class="alt-card">
            <h3 class="alt-card__title">4x LTV difference found between segments</h3>
            <p class="alt-card__text">See how a B2B SaaS company used ICP analysis to discover that RevOps team size predicted 4x differences in customer lifetime value. Real data, real results.</p>
          </a>'''
    cards.insert(0, icp_card)

    cards_html = "\n\n".join(cards)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Case Studies: Real Data Cleaning & Enrichment Results | Verum</title>
  <meta name="description" content="See how companies use Verum for CRM cleaning, contact enrichment, prospect list building, CRM migration, and database maintenance. Real numbers, real outcomes.">

  <link rel="canonical" href="https://veruminc.com/case-studies/">
  <link rel="icon" type="image/svg+xml" href="/assets/favicons/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicons/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicons/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#00b894">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css?v=6">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://veruminc.com/case-studies/">
  <meta property="og:title" content="Case Studies | Data Cleaning & Enrichment Results | Verum">
  <meta property="og:description" content="See how companies use Verum for CRM cleaning, contact enrichment, prospect list building, and database maintenance. Real numbers, real outcomes.">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Case Studies | Data Cleaning & Enrichment Results | Verum">
  <meta name="twitter:description" content="See how companies use Verum for CRM cleaning, contact enrichment, prospect list building, and database maintenance. Real numbers, real outcomes.">
  <meta name="twitter:image" content="https://veruminc.com/assets/social/twitter-card.png">

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R416JZ91B1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-R416JZ91B1');
  </script>
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "uzzgoxxnof");
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://veruminc.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "Case Studies"}}
    ]
  }}
  </script>

  <style>
    .alt-card {{
      padding: var(--space-xl);
      background-color: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      transition: all var(--transition-fast);
      display: block;
      text-decoration: none;
    }}
    .alt-card:hover {{
      border-color: var(--color-teal);
      transform: translateY(-3px);
    }}
    .alt-card__title {{
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: var(--space-sm);
      color: var(--color-text-primary);
    }}
    .alt-card__text {{
      color: var(--color-text-secondary);
      margin-bottom: 0;
      font-size: 0.9375rem;
      line-height: 1.6;
    }}
  </style>
</head>
<body>
  <header id="site-header"></header>
  <noscript>
    <nav style="background:#1a1a2e;padding:1rem;text-align:center;">
      <a href="/" style="color:#fff;margin:0 1rem;">Home</a>
      <a href="/services/" style="color:#fff;margin:0 1rem;">Services</a>
      <a href="/solutions/" style="color:#fff;margin:0 1rem;">Solutions</a>
      <a href="/resources/" style="color:#fff;margin:0 1rem;">Blog</a>
      <a href="/about.html" style="color:#fff;margin:0 1rem;">About</a>
      <a href="/contact.html" style="color:#fff;margin:0 1rem;">Contact</a>
    </nav>
  </noscript>

  <main>
    <section class="page-hero">
      <div class="container">
        <h1 class="page-hero__title">Case Studies</h1>
        <p class="page-hero__subtitle">Real results from real data projects. See how companies fix, complete, and grow their databases.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <p>Every project starts with a different problem. Some companies have 100,000 records full of duplicates. Others have a target market but no way to reach them. A few just need someone to keep their database from rotting.</p>
        <p>Here's what the numbers look like when the work is done.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem; max-width: 900px; margin: 0 auto;">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container text-center">
        <h2>Ready for your own results?</h2>
        <p class="mb-lg" style="max-width: 600px; margin-left: auto; margin-right: auto;">Tell us what you're working with and we'll show you what's possible.</p>
        <a href="/#contact" class="btn btn--primary btn--lg">See What We'll Find</a>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <p class="text-muted">Related: <a href="/services/">Our Services</a> | <a href="/solutions/">Industry Solutions</a> | <a href="/pricing.html">Pricing</a></p>
      </div>
    </section>
  </main>

  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


if __name__ == "__main__":
    # Generate individual case study pages
    for cs in ALL_CASE_STUDIES:
        slug = cs["slug"]
        out_dir = os.path.join(SITE_ROOT, "case-studies", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = generate_case_study(**cs)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Created: case-studies/{slug}/index.html")

    # Generate hub page
    hub_html = build_hub_page()
    hub_path = os.path.join(SITE_ROOT, "case-studies", "index.html")
    with open(hub_path, "w") as f:
        f.write(hub_html)
    print(f"Created: case-studies/index.html (hub)")
    print(f"\nTotal: {len(ALL_CASE_STUDIES)} new case studies + 1 hub page")
