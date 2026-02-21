#!/usr/bin/env python3
"""Generate CRM integration landing pages for Verum website."""
import os

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"


def gen_integration_page(slug, crm_name, title, meta_desc, breadcrumb_name,
                         hero_subtitle, intro_html, services_html,
                         how_it_works, why_verum, faq_schema,
                         related_resources, cta_headline, cta_text):
    """Generate a CRM integration landing page."""
    og_title = title.split(" | ")[0] if " | " in title else title

    services_cards = "\n".join(f'''          <div style="background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-xl);">
            <h3 style="font-size: 1.125rem; margin-bottom: var(--space-sm);">{s[0]}</h3>
            <p style="color: var(--color-text-secondary); margin: 0;">{s[1]}</p>
          </div>''' for s in services_html)

    steps_html = "\n".join(f'''        <li><strong>{s[0]}.</strong> {s[1]}</li>''' for s in how_it_works)

    why_html = "\n".join(f'''          <li><strong>{w[0]}:</strong> {w[1]}</li>''' for w in why_verum)

    resource_html = " | ".join(f'<a href="{url}">{text}</a>' for text, url in related_resources)

    faq_body = "\n".join(f'''        <h3>{q}</h3>\n        <p>{a}</p>''' for q, a in faq_schema)

    faq_json = ",\n      ".join(
        f'''{{\n        "@type": "Question",\n        "name": "{q}",\n        "acceptedAnswer": {{\n          "@type": "Answer",\n          "text": "{a.replace('"', '&quot;')}"\n        }}\n      }}'''
        for q, a in faq_schema
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Verum</title>
  <meta name="description" content="{meta_desc}">

  <link rel="canonical" href="https://veruminc.com/integrations/{slug}/">
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
  <meta property="og:url" content="https://veruminc.com/integrations/{slug}/">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{meta_desc[:200]}">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{meta_desc[:200]}">
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
      {{"@type": "ListItem", "position": 2, "name": "Integrations", "item": "https://veruminc.com/integrations/"}},
      {{"@type": "ListItem", "position": 3, "name": "{breadcrumb_name}"}}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_json}
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

  <main>
    <section class="page-hero">
      <div class="container">
        <h1 class="page-hero__title">{og_title}</h1>
        <p class="page-hero__subtitle">{hero_subtitle}</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
{intro_html}
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <h2 class="text-center mb-xl">What We Do for {crm_name} Users</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; max-width: 900px; margin: 0 auto;">
{services_cards}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <h2>How It Works</h2>
        <ol class="feature-list">
{steps_html}
        </ol>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container" style="max-width: 800px;">
        <h2>Why {crm_name} Teams Choose Verum</h2>
        <ul class="feature-list">
{why_html}
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <h2>Frequently Asked Questions</h2>
{faq_body}
      </div>
    </section>

    <section class="section section--alt">
      <div class="container text-center">
        <h2>{cta_headline}</h2>
        <p class="mb-lg" style="max-width: 600px; margin-left: auto; margin-right: auto;">{cta_text}</p>
        <a href="/#contact" class="btn btn--primary btn--lg">See What We'll Find</a>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <p class="text-muted">Related: {resource_html}</p>
      </div>
    </section>
  </main>

  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


INTEGRATIONS = [
    {
        "slug": "salesforce",
        "crm_name": "Salesforce",
        "title": "Verum + Salesforce: Data Cleaning and Enrichment for Salesforce CRM",
        "meta_desc": "Clean, enrich, and maintain your Salesforce data. Deduplication, email validation, contact enrichment, and field standardization. Import-ready results in days.",
        "breadcrumb_name": "Verum + Salesforce",
        "hero_subtitle": "Clean data in your Salesforce, not another platform to manage. We export, clean, enrich, and deliver import-ready files.",
        "intro_html": """        <p>Salesforce is powerful. But it's only as good as the data inside it. After a few years of use, most Salesforce instances accumulate duplicates, outdated contacts, inconsistent job titles, and missing fields that break automation and reporting.</p>

        <p>You've probably looked at Salesforce-native tools like Duplicate Rules and Data.com (now retired). They help with prevention but don't fix the existing mess. Third-party enrichment tools like ZoomInfo require $15K+ annual contracts and another platform to manage.</p>

        <p>Verum takes a simpler approach: we export your Salesforce data, clean and enrich it, and deliver an import-ready file. No integration to maintain. No platform to learn. No annual contract.</p>""",
        "services_html": [
            ("Duplicate Contact Merging", "Fuzzy matching across name, email, phone, and account finds duplicates that Salesforce's native rules miss. Records merged into golden records preserving the most complete data."),
            ("Email Validation", "SMTP verification on every email address. Hard bounces, role-based addresses, and catch-all domains flagged. Deliverability typically jumps from 70% to 93%."),
            ("Contact Enrichment", "Missing phone numbers, job titles, and company data filled from 50+ sources. Direct dials prioritized over main lines. Titles verified for accuracy."),
            ("Company Name Standardization", "ABC Corp, A.B.C. Corporation, and abc corp all become one canonical format. Prevents duplicate accounts and fixes account-contact associations."),
            ("Job Title Normalization", "VP Sales, Vice President of Sales, and Sales VP standardized into a consistent taxonomy. Makes territory assignment, lead routing, and reporting reliable."),
            ("Field Standardization", "State abbreviations, phone formats, industry codes, and address fields cleaned to consistent formats. Your Salesforce reports return accurate results."),
        ],
        "how_it_works": [
            ("Export", "You export contacts, accounts, or leads from Salesforce (we can walk you through it or do it via API)."),
            ("Clean and enrich", "We run deduplication, validation, standardization, and enrichment. Typically takes 3-7 days."),
            ("Review", "You receive the cleaned file with a summary of changes. Review before importing."),
            ("Import", "Upload the cleaned file back into Salesforce using Data Loader or native import. We format for direct import with your field mapping."),
        ],
        "why_verum": [
            ("No integration required", "We work with CSV exports and imports. No connected app, no API credentials, no managed package to install or maintain."),
            ("Handles the full stack", "Most enrichment tools only add data. We also clean, deduplicate, and standardize. One vendor for the complete data quality lifecycle."),
            ("Per-project pricing", "Clean your Salesforce once for a flat fee. No annual contract tying you to a tool you use twice a year."),
            ("Import-ready delivery", "We match your Salesforce field structure and naming. The import file is ready to load without manual field mapping."),
        ],
        "faq_schema": [
            ("Do I need to install anything in Salesforce?",
             "No. We work with standard CSV exports. No managed package, connected app, or AppExchange installation required. You export your data, we clean it, and you import the cleaned file back using Data Loader or Salesforce native import."),
            ("How long does Salesforce data cleaning take?",
             "Most projects are delivered in 3-7 business days. A typical 50,000-record Salesforce cleaning (dedup, email validation, phone verification, title standardization) takes about 5 days. Enrichment-only projects are faster at 2-3 days."),
            ("Will cleaning affect our Salesforce automation?",
             "Cleaning improves automation by fixing the data it depends on. Lead routing works better with standardized fields. Lead scoring improves with complete firmographic data. Email sequences get higher deliverability with validated addresses."),
        ],
        "related_resources": [
            ("How to Clean Salesforce Data", "/resources/how-to-clean-salesforce-data.html"),
            ("Salesforce Duplicate Contacts", "/resources/salesforce-duplicate-contacts.html"),
            ("Salesforce Data Enrichment", "/resources/salesforce-data-enrichment.html"),
            ("CRM Cleaning Case Study", "/case-studies/crm-cleaning-staffing-agency/"),
        ],
        "cta_headline": "Clean Your Salesforce in Days, Not Months",
        "cta_text": "Tell us how many records you have and what problems you're seeing. We'll scope a project and give you a fixed price.",
    },
    {
        "slug": "hubspot",
        "crm_name": "HubSpot",
        "title": "Verum + HubSpot: Data Cleaning and Enrichment for HubSpot CRM",
        "meta_desc": "Clean and enrich your HubSpot data. Remove duplicates, validate emails, reduce marketing contacts, and fill missing fields. No Operations Hub required.",
        "breadcrumb_name": "Verum + HubSpot",
        "hero_subtitle": "Cut your marketing contact costs, fix your deliverability, and fill the fields that make automation work.",
        "intro_html": """        <p>HubSpot is great at marketing automation. It's not great at data quality. Duplicate contacts split your engagement history. Invalid emails tank your deliverability. Missing fields break your lead scoring and routing. And every bad contact in your marketing tier costs you money.</p>

        <p>HubSpot Operations Hub helps with some of these problems, but it requires a $800+/month upgrade and technical resources to configure. Breeze Intelligence (formerly Clearbit) adds enrichment but ties you to HubSpot's data sources and pricing.</p>

        <p>Verum cleans and enriches your HubSpot data without additional software. We export, clean, enrich, and deliver import-ready files that work with any HubSpot tier.</p>""",
        "services_html": [
            ("Marketing Contact Optimization", "Identify contacts you're paying for but shouldn't be: hard bounces, competitors, unsubscribes, and long-unengaged records. Most companies save 15-25% on their contact tier."),
            ("Duplicate Merging", "HubSpot's built-in dedup tool only catches exact matches. We use fuzzy matching to find near-duplicates that split your engagement data and inflate your database."),
            ("Email Validation", "SMTP verification on every email. Invalid addresses suppressed before your next send. Protect your sender reputation and keep bounce rates under 2%."),
            ("Contact Enrichment", "Fill missing job titles, phone numbers, company size, and industry from 50+ sources. Your lead scoring and lifecycle stages work with complete data."),
            ("Contact-Company Association Fix", "Contacts without company associations are invisible to account-based reporting. We match orphaned contacts to their companies and create the associations."),
            ("Lifecycle Stage Cleanup", "Contacts stuck in wrong lifecycle stages break your funnel metrics. We audit and correct stage assignments based on actual engagement and deal history."),
        ],
        "how_it_works": [
            ("Export", "Export your contacts and companies from HubSpot (we provide step-by-step instructions for your tier)."),
            ("Clean and enrich", "We run the full cleaning and enrichment process. Typically 3-7 days."),
            ("Review and approve", "You receive the cleaned file with a change summary showing what was modified and why."),
            ("Import", "Upload the cleaned file back into HubSpot using native import. We format to match your HubSpot properties exactly."),
        ],
        "why_verum": [
            ("No Operations Hub required", "Our cleaning and enrichment works with any HubSpot tier: Free, Starter, Professional, or Enterprise. No additional HubSpot product needed."),
            ("Save on marketing contacts", "By identifying and removing dead weight from your marketing contacts, we often save companies more than the cost of the cleaning project."),
            ("Works alongside Breeze Intelligence", "If you already use Breeze for real-time enrichment, we complement it with bulk cleaning, deduplication, and multi-source enrichment that Breeze doesn't do."),
            ("Per-project, not per-month", "No monthly subscription on top of your HubSpot costs. Use us once for a cleanup or quarterly for maintenance."),
        ],
        "faq_schema": [
            ("Do I need HubSpot Operations Hub for this?",
             "No. We work with CSV exports and imports, which are available on every HubSpot tier including Free. No Operations Hub, no additional HubSpot product, and no integration to install."),
            ("How much can I save on HubSpot marketing contacts?",
             "Most companies find 15-25% of their marketing contacts are dead weight. For a company paying for 50,000 marketing contacts, dropping to a lower tier can save $3,000-6,000/year. The cleaning project often pays for itself through contact tier savings."),
            ("Does this work with HubSpot Breeze Intelligence?",
             "Yes. Breeze handles real-time enrichment on inbound leads. We handle bulk operations: deduplication across your entire database, email validation, legacy data cleanup, and multi-source enrichment that covers contacts Breeze can't match."),
        ],
        "related_resources": [
            ("How to Clean HubSpot Data", "/resources/hubspot-data-cleaning.html"),
            ("HubSpot Duplicate Contacts", "/resources/hubspot-duplicate-contacts.html"),
            ("HubSpot Marketing Contacts Cleanup", "/resources/hubspot-marketing-contacts-cleanup.html"),
            ("HubSpot Email Validation", "/resources/hubspot-email-validation.html"),
        ],
        "cta_headline": "Clean Your HubSpot Without Upgrading",
        "cta_text": "Tell us about your HubSpot database and we'll tell you how much dead weight you're carrying.",
    },
    {
        "slug": "dynamics-365",
        "crm_name": "Dynamics 365",
        "title": "Verum + Dynamics 365: Data Cleaning and Enrichment for Microsoft CRM",
        "meta_desc": "Clean and enrich your Dynamics 365 data. Deduplication, email validation, contact enrichment, and field standardization for Microsoft CRM users.",
        "breadcrumb_name": "Verum + Dynamics 365",
        "hero_subtitle": "Dynamics 365 data quality doesn't require another Microsoft product. We clean and enrich your CRM data on a per-project basis.",
        "intro_html": """        <p>Dynamics 365 users have fewer third-party data quality options than Salesforce or HubSpot users. Most enrichment tools prioritize those two CRMs, leaving Dynamics teams to rely on manual processes or Microsoft's own ecosystem (which doesn't include a built-in enrichment solution).</p>

        <p>The result: Dynamics databases often accumulate data quality issues faster because there are fewer tools catching them. Duplicates grow unchecked. Email addresses go stale. Job titles drift into hundreds of unstandardized variations.</p>

        <p>Verum is CRM-agnostic. We clean and enrich data from any system, including Dynamics 365, using CSV exports and imports. No Dynamics marketplace app required, no Azure integration, and no Microsoft-specific tooling.</p>""",
        "services_html": [
            ("Deduplication", "Fuzzy matching across contacts, accounts, and leads finds duplicates that Dynamics' native detection rules miss. Merged into golden records preserving the most complete data."),
            ("Email Validation", "SMTP verification on every email address. Catch-all domains, role-based addresses, and invalid mailboxes identified. Bounce rates drop to under 3%."),
            ("Contact Enrichment", "Missing phone numbers, job titles, company size, and industry data filled from 50+ sources. Coverage matches what Salesforce and HubSpot users get from premium tools."),
            ("Field Standardization", "Company names, job titles, addresses, and industry codes standardized to consistent formats. Your Dynamics views and reports return accurate, filterable results."),
        ],
        "how_it_works": [
            ("Export", "Export your contacts, accounts, or leads from Dynamics 365 using Advanced Find or the Excel export feature."),
            ("Clean and enrich", "We process the full dataset: deduplication, validation, standardization, and enrichment. 3-7 business days."),
            ("Review", "You receive the cleaned file with a detailed change log. Review before importing."),
            ("Import", "Upload back into Dynamics using the Import Wizard or Data Management workspace. We format the file to match your entity fields."),
        ],
        "why_verum": [
            ("CRM-agnostic approach", "We don't require a Dynamics-specific integration. CSV in, cleaned CSV out. Works with any Dynamics deployment (online or on-premises)."),
            ("Same quality as premium CRM tools", "Dynamics users get the same multi-source enrichment, SMTP validation, and fuzzy deduplication that Salesforce and HubSpot users access through $15K+ annual platforms."),
            ("No Azure dependency", "No Azure Data Factory pipeline, no Power Automate flow, no Dataverse connector. Simple file exchange."),
            ("Per-project pricing", "Clean your Dynamics CRM once without an annual commitment. Pay for the project, not the platform."),
        ],
        "faq_schema": [
            ("Do you work with Dynamics 365 on-premises?",
             "Yes. Since we work with CSV exports rather than API integrations, it doesn't matter whether your Dynamics instance is cloud (online) or on-premises. Export your data, send it to us, and import the cleaned file back."),
            ("What fields can you enrich in Dynamics 365?",
             "We can fill any standard or custom field: email, phone, job title, company size, industry (NAICS/SIC), revenue range, technology stack, LinkedIn URL, and company address. We format the output to match your Dynamics entity structure."),
            ("How does pricing compare to Dynamics-specific tools?",
             "Most Dynamics data quality tools charge $500-2,000/month for ongoing subscriptions. A one-time Verum cleaning project for 50,000 records typically costs $2,500-5,000 with no recurring fees. For periodic needs, per-project pricing is significantly cheaper."),
        ],
        "related_resources": [
            ("Data Cleaning Services", "/services/data-cleaning.html"),
            ("Data Enrichment Services", "/services/data-enrichment.html"),
            ("CRM Migration Case Study", "/case-studies/crm-migration-data-prep-manufacturing/"),
            ("Multi-CRM Data Sync", "/resources/multi-crm-data-sync.html"),
        ],
        "cta_headline": "Get the Same Data Quality as Salesforce Teams",
        "cta_text": "Your CRM shouldn't determine your data quality. Tell us what you need and we'll deliver the same results regardless of platform.",
    },
]


def build_hub():
    """Build the integrations hub page."""
    cards = []
    for integ in INTEGRATIONS:
        cards.append(f'''          <a href="/integrations/{integ["slug"]}/" style="padding: var(--space-xl); background-color: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); transition: all 0.2s; display: block; text-decoration: none;">
            <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: var(--space-sm); color: var(--color-text-primary);">Verum + {integ["crm_name"]}</h3>
            <p style="color: var(--color-text-secondary); margin: 0; font-size: 0.9375rem; line-height: 1.6;">{integ["meta_desc"]}</p>
          </a>''')

    cards_html = "\n\n".join(cards)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRM Integrations: Salesforce, HubSpot, Dynamics 365 | Verum</title>
  <meta name="description" content="Verum works with any CRM. Clean and enrich data from Salesforce, HubSpot, Dynamics 365, and more. No integration to install. CSV in, clean data out.">

  <link rel="canonical" href="https://veruminc.com/integrations/">
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
  <meta property="og:url" content="https://veruminc.com/integrations/">
  <meta property="og:title" content="CRM Integrations | Verum">
  <meta property="og:description" content="Verum works with any CRM. Clean and enrich data from Salesforce, HubSpot, Dynamics 365, and more.">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="CRM Integrations | Verum">
  <meta name="twitter:description" content="Verum works with any CRM. Clean and enrich data from Salesforce, HubSpot, Dynamics 365, and more.">
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
      {{"@type": "ListItem", "position": 2, "name": "Integrations"}}
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

  <main>
    <section class="page-hero">
      <div class="container">
        <h1 class="page-hero__title">CRM Integrations</h1>
        <p class="page-hero__subtitle">Verum works with any CRM. No integration to install. Export your data, we clean and enrich it, you import the results.</p>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <p>Most data quality tools require installing a marketplace app, configuring API connections, and maintaining integrations. Verum skips all of that. We work with standard file exports from any CRM.</p>
        <p>Send us a CSV. We clean, enrich, and validate every record. You import the results. Done.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem; max-width: 800px; margin: 0 auto;">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <h2>Other CRMs We Work With</h2>
        <p>Our process works with any CRM that can export and import data. We've processed data from:</p>
        <ul>
          <li>Pipedrive</li>
          <li>Zoho CRM</li>
          <li>Monday.com CRM</li>
          <li>Freshsales</li>
          <li>Close</li>
          <li>Copper</li>
          <li>Insightly</li>
          <li>Custom databases and spreadsheets</li>
        </ul>
        <p>If your CRM can export a CSV, we can clean your data.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container text-center">
        <h2>Your CRM Shouldn't Limit Your Data Quality</h2>
        <p class="mb-lg" style="max-width: 600px; margin-left: auto; margin-right: auto;">Tell us what CRM you're using and what data problems you're seeing. We'll show you what clean data looks like.</p>
        <a href="/#contact" class="btn btn--primary btn--lg">See What We'll Find</a>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <p class="text-muted">Related: <a href="/services/">Our Services</a> | <a href="/solutions/">Industry Solutions</a> | <a href="/case-studies/">Case Studies</a></p>
      </div>
    </section>
  </main>

  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


if __name__ == "__main__":
    # Generate individual integration pages
    for integ in INTEGRATIONS:
        slug = integ["slug"]
        out_dir = os.path.join(SITE_ROOT, "integrations", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = gen_integration_page(**integ)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(html)
        print(f"Created: integrations/{slug}/index.html")

    # Generate hub page
    hub_html = build_hub()
    hub_dir = os.path.join(SITE_ROOT, "integrations")
    os.makedirs(hub_dir, exist_ok=True)
    with open(os.path.join(hub_dir, "index.html"), "w") as f:
        f.write(hub_html)
    print(f"Created: integrations/index.html (hub)")
    print(f"\nTotal: {len(INTEGRATIONS)} integration pages + 1 hub")
