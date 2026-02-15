#!/usr/bin/env python3
"""Update glossary hub page with all terms."""
import os

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"
HUB_PATH = os.path.join(SITE_ROOT, "glossary", "index.html")

# All terms in alphabetical order with short descriptions
ALL_TERMS = [
    ("abm", "Account-Based Marketing (ABM)", "A B2B strategy that focuses sales and marketing resources on a defined set of target accounts with personalized campaigns."),
    ("address-validation", "Address Validation", "Confirms a physical address exists, is deliverable, and conforms to postal standards like USPS CASS certification."),
    ("batch-enrichment", "Batch Enrichment", "Appending missing data fields to a large set of records all at once, rather than enriching them one at a time."),
    ("bounce-rate", "Bounce Rate (Email)", "The percentage of sent emails that fail to reach the recipient's inbox due to invalid addresses or server issues."),
    ("buyer-intent-data", "Buyer Intent Data", "Tracks online research behavior to identify companies actively evaluating solutions in your category."),
    ("buying-signals", "Buying Signals", "Observable actions or events that suggest a company is moving toward a purchase decision."),
    ("catch-all-domain", "Catch-All Domain", "A domain configured to accept email sent to any address, making individual mailbox verification impossible."),
    ("contact-waterfall", "Contact Data Waterfall", "A sequential enrichment strategy that queries multiple data providers in order, using each source's strengths to maximize coverage while minimizing cost."),
    ("crm-hygiene", "CRM Hygiene", "The ongoing practice of maintaining clean, accurate, and complete data in a customer relationship management system through regular deduplication, validation, and enrichment."),
    ("customer-data-platform", "Customer Data Platform (CDP)", "Software that collects customer data from every touchpoint and unifies it into a single customer profile."),
    ("customer-lifetime-value", "Customer Lifetime Value (CLV)", "The total revenue a customer is expected to generate over the entire duration of their relationship with your company."),
    ("customer-segmentation", "Customer Segmentation", "Dividing your customer base into groups that share common characteristics for targeted messaging and strategy."),
    ("data-append", "Data Append", "Adding missing fields to existing records by matching them against external data sources."),
    ("data-decay", "Data Decay", "The rate at which business data becomes inaccurate over time. B2B data decays at roughly 30% per year due to job changes, company closures, and acquisitions."),
    ("data-deduplication", "Data Deduplication", "The process of identifying and removing duplicate records from your CRM or database to improve data quality and prevent redundant outreach."),
    ("data-enrichment", "Data Enrichment", "The process of appending missing information to existing records using external data sources. Adds emails, phone numbers, job titles, company size, and other fields to CRM records."),
    ("data-governance", "Data Governance", "The set of policies, processes, roles, and standards that control how data is collected, stored, maintained, and used."),
    ("data-hygiene", "Data Hygiene", "The ongoing practice of maintaining clean, accurate, and usable data through regular deduplication, verification, and standardization."),
    ("data-integration", "Data Integration", "Combining data from multiple systems into a unified and consistent view across your organization."),
    ("data-migration", "Data Migration", "Moving data from one system to another, typically during a CRM switch or platform upgrade."),
    ("data-normalization", "Data Normalization", "Standardizing data formats and values so records can be accurately compared, deduplicated, and analyzed."),
    ("data-profiling", "Data Profiling", "Examining your database to understand its quality, structure, and content before cleaning."),
    ("data-quality-management", "Data Quality Management", "The ongoing discipline of measuring, monitoring, and improving data accuracy, completeness, and consistency."),
    ("data-standardization", "Data Standardization", "Converting data values into consistent, predefined formats so records can be compared and analyzed."),
    ("data-validation", "Data Validation", "Checking whether data meets predefined rules for format, type, range, and accuracy."),
    ("demand-generation", "Demand Generation", "The marketing discipline of creating awareness, interest, and pipeline across your total addressable market."),
    ("duplicate-detection", "Duplicate Detection", "Identifying records in your database that represent the same person or company through exact and fuzzy matching."),
    ("email-deliverability", "Email Deliverability", "The measure of whether your emails successfully reach the inbox rather than bouncing or landing in spam."),
    ("email-validation", "Email Validation", "The process of verifying that email addresses are valid, deliverable, and belong to real inboxes. Reduces bounce rates and protects sender reputation."),
    ("entity-resolution", "Entity Resolution", "Determining whether records from different sources refer to the same real-world person or company."),
    ("fill-rate", "Fill Rate", "The percentage of records in your database that have a value in a specific field."),
    ("firmographic-data", "Firmographic Data", "Descriptive attributes of a business, including company size, industry, revenue, location, and founding date."),
    ("first-party-data", "First-Party Data", "Information your organization collects directly from customers and prospects through your own channels."),
    ("fuzzy-matching", "Fuzzy Matching", "Finding records that are similar but not identical using algorithms that measure string similarity."),
    ("golden-record", "Golden Record", "The single, most complete and accurate version of an entity after duplicate records have been merged."),
    ("ideal-customer-profile", "Ideal Customer Profile (ICP)", "A data-driven description of the companies most likely to become your best customers, based on analysis of firmographic, technographic, and behavioral attributes."),
    ("industry-classification", "Industry Classification", "Assigning standardized NAICS or SIC codes to businesses based on their primary economic activity."),
    ("job-title-normalization", "Job Title Normalization", "Standardizing the wide variety of job titles in your database into a consistent taxonomy of roles and seniority levels."),
    ("lead-qualification", "Lead Qualification", "Evaluating whether a prospect has the budget, authority, need, and timeline to become a customer."),
    ("lead-routing", "Lead Routing", "Automatically assigning incoming leads to the correct sales rep based on territory, company size, or other criteria."),
    ("lead-scoring", "Lead Scoring", "Assigning a numerical value to each lead based on ICP fit and engagement behavior to prioritize sales outreach."),
    ("lookalike-modeling", "Lookalike Modeling", "Analyzing your best customers' attributes and finding new prospects that share the same characteristics."),
    ("market-sizing", "Market Sizing (TAM/SAM/SOM)", "Quantifying the revenue opportunity for your product using Total Addressable, Serviceable, and Obtainable market metrics."),
    ("master-data-management", "Master Data Management", "Creating and maintaining a single authoritative source of truth for critical business entities across all systems."),
    ("match-rate", "Match Rate", "The percentage of records a data provider can successfully find and enrich from your submitted list."),
    ("mql", "MQL (Marketing Qualified Lead)", "A lead that has met predefined criteria combining demographic fit and behavioral engagement."),
    ("net-new-contact", "Net-New Contact", "A person who does not currently exist in your CRM or marketing database."),
    ("pipeline-management", "Pipeline Management", "Tracking, analyzing, and optimizing the deals moving through your sales process to predict revenue."),
    ("prospect-list-building", "Prospect List Building", "Creating a targeted list of companies and contacts matching your ideal customer profile for outreach."),
    ("record-matching", "Record Matching", "Comparing records from one or more datasets to determine which ones refer to the same real-world entity."),
    ("revenue-intelligence", "Revenue Intelligence", "Using data from across the revenue team to surface insights on pipeline health, deal risks, and forecast accuracy."),
    ("revenue-operations", "Revenue Operations (RevOps)", "The function that aligns sales, marketing, and success teams around shared data, processes, and metrics."),
    ("sales-intelligence", "Sales Intelligence", "Data, insights, and signals that help sales teams identify, prioritize, and engage prospects more effectively."),
    ("sender-reputation", "Sender Reputation", "A score ISPs assign to your sending domain and IP based on email behavior, controlling inbox placement."),
    ("suppression-list", "Suppression List", "A set of contacts that must be excluded from outreach campaigns for compliance, deliverability, or strategic reasons."),
    ("tech-stack-data", "Tech Stack Data", "The specific software tools and technologies a company uses, collected through website scanning and other signals."),
    ("technographic-data", "Technographic Data", "Information about the technology stack a company uses, including CRM, marketing automation, analytics tools, and other software."),
    ("territory-planning", "Territory Planning", "Dividing your addressable market among sales reps to maximize coverage and ensure fair opportunity distribution."),
]

def build_hub():
    # Group terms by first letter
    groups = {}
    for slug, name, desc in ALL_TERMS:
        letter = name[0].upper()
        if letter == '"':
            letter = name[1].upper()
        groups.setdefault(letter, []).append((slug, name, desc))

    # Build entries HTML
    entries = []
    for letter in sorted(groups.keys()):
        entries.append(f'\n        <h2 id="{letter.lower()}" style="color: var(--color-teal); margin-top: var(--space-2xl); margin-bottom: var(--space-lg); font-size: 1.5rem;">{letter}</h2>\n')
        for slug, name, desc in sorted(groups[letter], key=lambda x: x[1]):
            entries.append(f'''        <div style="margin-bottom: var(--space-xl);">
          <h3 style="font-size: 1.125rem; margin-bottom: var(--space-xs);"><a href="/glossary/{slug}/">{name}</a></h3>
          <p style="color: var(--color-text-secondary); margin: 0;">{desc}</p>
        </div>
''')

    # Build letter nav
    letters = sorted(groups.keys())
    letter_nav = " ".join(f'<a href="#{l.lower()}" style="color: var(--color-teal); text-decoration: none; font-weight: 600;">{l}</a>' for l in letters)

    entries_html = "\n".join(entries)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>B2B Data Quality Glossary: 58 Key Terms | Verum</title>
  <meta name="description" content="Definitions of 58 key terms in B2B data quality, CRM management, data enrichment, and sales intelligence. From ABM and data append to tech stack data and territory planning.">

  <link rel="canonical" href="https://veruminc.com/glossary/">
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
  <meta property="og:url" content="https://veruminc.com/glossary/">
  <meta property="og:title" content="B2B Data Quality Glossary: 58 Key Terms | Verum">
  <meta property="og:description" content="Definitions of 58 key terms in B2B data quality, CRM management, data enrichment, and sales intelligence.">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="B2B Data Quality Glossary: 58 Key Terms | Verum">
  <meta name="twitter:description" content="Definitions of 58 key terms in B2B data quality, CRM management, data enrichment, and sales intelligence.">
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
      {{"@type": "ListItem", "position": 2, "name": "Glossary"}}
    ]
  }}
  </script>
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
      <h1 class="page-hero__title">Data Quality Glossary</h1>
      <p class="page-hero__subtitle">58 key terms in B2B data quality, CRM management, data enrichment, and sales intelligence.</p>
    </div>
  </section>

  <section class="content">
    <div class="container" style="max-width: 800px;">

      <div style="text-align: center; margin-bottom: var(--space-2xl); font-size: 1.125rem; letter-spacing: 0.15em;">
        {letter_nav}
      </div>

      <div class="glossary-list">
{entries_html}
      </div>

      <div class="text-center mt-xl">
        <a href="/#contact" class="btn btn--primary btn--lg">See What We'll Find</a>
        <p class="text-muted" style="margin-top: 1rem;"><a href="/resources/">Resources</a> | <a href="/services/">Our Services</a></p>
      </div>

    </div>
  </section>

  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''
    return html


if __name__ == "__main__":
    html = build_hub()
    with open(HUB_PATH, "w") as f:
        f.write(html)
    print(f"Updated glossary hub with {len(ALL_TERMS)} terms.")
