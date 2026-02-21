#!/usr/bin/env python3
"""Generate persona/role-based landing pages for Verum website."""
import os

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"


def gen_persona_page(slug, title, meta_desc, breadcrumb_name, hero_subtitle,
                     intro_html, pain_points, how_we_help, use_cases_html,
                     related_resources, faq_schema, cta_headline, cta_text):
    """Generate a persona landing page."""
    og_title = title.split(" | ")[0] if " | " in title else title

    pain_html = "\n".join(f'''          <div style="background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-xl);">
            <h3 style="font-size: 1.125rem; margin-bottom: var(--space-sm);">{p[0]}</h3>
            <p style="color: var(--color-text-secondary); margin: 0;">{p[1]}</p>
          </div>''' for p in pain_points)

    help_html = "\n".join(f'''          <li><strong>{h[0]}:</strong> {h[1]}</li>''' for h in how_we_help)

    resource_html = " | ".join(f'<a href="{url}">{text}</a>' for text, url in related_resources)

    faq_body = "\n".join(f'''        <h3>{q}</h3>
        <p>{a}</p>''' for q, a in faq_schema)

    faq_schema_json = ",\n      ".join(
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

  <link rel="canonical" href="https://veruminc.com/solutions/{slug}/">
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
  <meta property="og:url" content="https://veruminc.com/solutions/{slug}/">
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
      {{"@type": "ListItem", "position": 2, "name": "Solutions", "item": "https://veruminc.com/solutions/"}},
      {{"@type": "ListItem", "position": 3, "name": "{breadcrumb_name}"}}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_schema_json}
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
        <h2 class="text-center mb-xl">The Data Problems You Deal With</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; max-width: 900px; margin: 0 auto;">
{pain_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width: 800px;">
        <h2>How Verum Helps</h2>
        <ul class="feature-list">
{help_html}
        </ul>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container" style="max-width: 800px;">
        <h2>Common Use Cases</h2>
{use_cases_html}
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


PERSONAS = [
    {
        "slug": "data-services-for-revops",
        "title": "Data Services for RevOps Teams",
        "meta_desc": "Managed data cleaning, enrichment, and maintenance for revenue operations teams. Stop spending ops cycles on data tasks. Per-project pricing, no annual contracts.",
        "breadcrumb_name": "Data Services for RevOps",
        "hero_subtitle": "You have a CRM to manage, processes to optimize, and reports to fix. Let someone else handle the data cleaning.",
        "intro_html": """        <p>RevOps teams sit at the intersection of sales, marketing, and customer success. You're responsible for clean data, working automation, accurate reporting, and the 47 other things that keep the revenue engine running.</p>

        <p>Data quality is part of the job, but it shouldn't be all of the job. When your best ops person is spending 15 hours a week deduplicating records and validating emails, that's 15 hours not spent on process optimization, territory planning, or the reporting project leadership has been asking about for two months.</p>

        <p>Verum handles the data work so your team can focus on the ops work.</p>""",
        "pain_points": [
            ("Deduplication never ends", "You clean up 5,000 duplicates and 2,000 new ones appear from the next trade show import. The cycle repeats every quarter."),
            ("Enrichment gaps break automation", "Lead scoring needs firmographics. Routing needs industry codes. Nurture sequences need job titles. If any field is missing, the automation fails silently."),
            ("Data decay outpaces your capacity", "Your database decays at 2-3% per month. That's 30% per year. Even with good processes, your team can't re-verify 50,000 records quarterly while doing everything else."),
            ("Every team blames the data", "Sales says leads are bad. Marketing says attribution is broken. CS says health scores are wrong. They're all correct, and you're expected to fix it."),
        ],
        "how_we_help": [
            ("Bulk cleaning projects", "Send us your full database. We deduplicate, validate emails, verify phones, standardize titles, and normalize company names. You get clean data back in 3-7 days."),
            ("Ongoing maintenance", "Monthly email re-verification, quarterly deep cleans, and new-record validation. Your database stays clean without your team touching it."),
            ("Enrichment for automation", "We fill missing fields (industry, company size, title, phone, email) so your lead scoring, routing, and nurture sequences work as designed."),
            ("CRM migration prep", "Switching from Salesforce to HubSpot (or vice versa)? We clean, deduplicate, and reformat every record before it touches the new system."),
            ("Per-project pricing", "No annual contract or platform subscription. Use us for a $2,000 project or $20,000/year of ongoing work. Pay for what you need."),
        ],
        "use_cases_html": """        <h3>Quarterly CRM hygiene</h3>
        <p>Every quarter, send us your full database. We run deduplication, email validation, phone verification, and field standardization. You import the cleaned file and move on.</p>

        <h3>Post-acquisition data merge</h3>
        <p>Acquiring a company means merging two CRMs with different data formats, duplicate records, and conflicting field values. We clean and merge them into a single, standardized dataset.</p>

        <h3>Enrichment for lead scoring rebuild</h3>
        <p>Rebuilding your lead scoring model? We enrich your contact and account records with the firmographic and technographic data your model needs: company size, industry, tech stack, and revenue range.</p>

        <h3>Territory realignment data prep</h3>
        <p>Realigning sales territories requires accurate geographic, industry, and company size data. We standardize and fill these fields so your territory model runs on real data instead of guesses.</p>""",
        "related_resources": [
            ("Data Cleaning Services", "/services/data-cleaning.html"),
            ("Data Enrichment Services", "/services/data-enrichment.html"),
            ("CRM Migration Case Study", "/case-studies/crm-migration-data-prep-manufacturing/"),
            ("Data Hygiene for Marketing Ops", "/resources/data-hygiene-for-marketing-ops.html"),
        ],
        "faq_schema": [
            ("How long does a typical RevOps data cleaning project take?",
             "Most projects are delivered in 3-7 business days. A 50,000-record CRM cleaning (dedup, email validation, phone verification, standardization) typically takes 5 days. Enrichment-only projects are faster, usually 2-3 days."),
            ("Can you work with our existing CRM workflows?",
             "Yes. We export from and import back to Salesforce, HubSpot, Dynamics, and other CRMs. We match your field structure and format so you can import directly without manual mapping."),
            ("How is this different from buying a data platform?",
             "Data platforms give you a login and credits. You still need someone on your team to build searches, manage exports, clean the data, and handle imports. We do all of that for you. Per-project pricing instead of annual contracts."),
        ],
        "cta_headline": "Free Up Your RevOps Team",
        "cta_text": "Tell us what data problems are eating your team's time. We'll show you how to get those hours back.",
    },
    {
        "slug": "data-services-for-sales-leaders",
        "title": "Data Services for Sales Leaders",
        "meta_desc": "Your reps spend 30% of their time on data tasks instead of selling. Verum provides managed data cleaning and enrichment so your team can focus on pipeline.",
        "breadcrumb_name": "Data Services for Sales Leaders",
        "hero_subtitle": "Your reps should be selling, not cleaning spreadsheets. We handle the data so they can handle the pipeline.",
        "intro_html": """        <p>Sales leaders have a visibility problem. Your CRM tells you pipeline is at $2.4M, but your gut says it's closer to $1.8M. The forecast is off because the data is off. Duplicates inflate deal counts. Missing fields break routing. Outdated contacts waste call time.</p>

        <p>The real cost isn't the data itself. It's the selling time your reps lose to data tasks. Salesforce research shows reps spend only 28% of their time actually selling. A big chunk of the other 72% is data entry, searching for contact info, and working around CRM problems.</p>

        <p>Verum gives your team clean, complete data so they can spend more time in conversations and less time in spreadsheets.</p>""",
        "pain_points": [
            ("Reps waste time finding contacts", "Your reps are Googling prospects, searching LinkedIn, and copying phone numbers into the CRM one at a time. That's $50-80/hour labor doing $5/hour work."),
            ("Pipeline reports don't match reality", "Duplicates inflate opportunity counts. Missing close dates create phantom deals. Inconsistent stage values make forecasting unreliable."),
            ("New reps ramp slowly on bad data", "A new hire's first week should be learning accounts, not discovering that half their territory records are outdated or duplicated."),
            ("Lead routing sends deals to wrong reps", "Inconsistent industry codes, missing geographic data, and unstandardized company sizes mean your routing rules misfire and delay follow-up."),
        ],
        "how_we_help": [
            ("Prospect list building", "Tell us your ICP. We find and verify the contacts: names, titles, direct dials, emails, and company firmographics. Your reps start calling on Day 1."),
            ("CRM cleanup for accurate forecasting", "We deduplicate deals, standardize stages, and clean pipeline data so your forecast reflects reality instead of artifacts."),
            ("Contact enrichment at scale", "We enrich your existing accounts and contacts with missing phone numbers, emails, and titles from 50+ data sources. Batch processing, not one-at-a-time lookups."),
            ("Territory data preparation", "Accurate company size, industry, and geographic data for territory alignment. Clean enough to feed directly into your territory planning model."),
            ("No platform for reps to manage", "We deliver data. Your reps never log into another tool, manage credits, or export CSVs. Data shows up in the CRM, ready to use."),
        ],
        "use_cases_html": """        <h3>New territory launch</h3>
        <p>Expanding into a new market? We build a prospect list of verified contacts matching your ICP, enriched with direct dials and emails. Your reps start outreach immediately instead of spending weeks researching.</p>

        <h3>Pre-QBR pipeline cleanup</h3>
        <p>Before your quarterly business review, we clean your pipeline: merge duplicate opportunities, flag stale deals, validate contact data on open opportunities, and standardize stage values. Your QBR runs on real numbers.</p>

        <h3>Annual database refresh</h3>
        <p>Once a year, send us your entire CRM. We re-verify every email, check every phone number, update job title changes, and remove contacts who've left their companies. Your database starts the year clean.</p>

        <h3>Event follow-up enrichment</h3>
        <p>After a trade show or conference, you have a list of badge scans with names and companies but little else. We enrich them with titles, phone numbers, and emails within 48 hours so your team can follow up while interest is hot.</p>""",
        "related_resources": [
            ("Data Quality for Sales Leaders", "/resources/data-quality-for-sales-leaders.html"),
            ("Prospect List Building Case Study", "/case-studies/prospect-list-building-commercial-real-estate/"),
            ("Cost of Bad CRM Data", "/resources/cost-of-bad-crm-data.html"),
            ("Lead Routing and Data", "/resources/lead-routing-broken-data.html"),
        ],
        "faq_schema": [
            ("How much does prospect list building cost?",
             "Per-record pricing typically runs $0.10-0.50 per contact depending on the depth of enrichment. A 2,000-contact list with verified emails, direct dials, and firmographics usually costs $400-1,000. No annual commitment required."),
            ("How accurate are the phone numbers?",
             "We verify phone numbers against carrier databases before delivery. Direct dial coverage typically runs 60-75% depending on the target market. Every number delivered is confirmed active, not a main office line or fax."),
            ("Can you enrich leads from trade shows?",
             "Yes. Send us your badge scan list (name + company is enough). We enrich with titles, verified emails, direct dials, company size, and industry. Typical turnaround is 48 hours for lists under 5,000 contacts."),
        ],
        "cta_headline": "Give Your Reps Better Data",
        "cta_text": "Tell us about your target market and we'll show you what verified contacts look like.",
    },
    {
        "slug": "data-services-for-marketing-ops",
        "title": "Data Services for Marketing Ops Teams",
        "meta_desc": "Managed data cleaning and enrichment for marketing operations. Fix deliverability, improve segmentation, and stop paying for bad contacts. No platform to manage.",
        "breadcrumb_name": "Data Services for Marketing Ops",
        "hero_subtitle": "Your campaigns are only as good as the data behind them. We make sure the data is right so your campaigns actually work.",
        "intro_html": """        <p>Marketing ops is where data quality problems become visible. Bounce rates climb. Segments return inconsistent counts. Personalization tokens render as blank fields. The nurture sequence that took two weeks to build sends to 40% fewer people than planned because email addresses are missing.</p>

        <p>You know the data needs fixing. You probably have a backlog of data quality tickets. The problem is capacity. Between campaign execution, automation maintenance, reporting, and the 12 other things on your plate, a systematic data cleanup keeps getting pushed to next quarter.</p>

        <p>Verum handles the cleanup so you can focus on the campaigns.</p>""",
        "pain_points": [
            ("Bounce rates threaten sender reputation", "Every email to an invalid address counts against your domain. Above 5% bounce rate, ISPs start throttling your sends. Above 10%, you risk blacklisting."),
            ("Segmentation is unreliable", "Job titles aren't standardized. Industry codes are missing. Company size fields are empty. Your segments include the wrong people and exclude the right ones."),
            ("Marketing contacts are bloated", "In HubSpot, you pay per marketing contact. Half of them bounced years ago or haven't opened an email since 2023. You're paying to store dead weight."),
            ("Enrichment is incomplete", "Form fills capture name and email. Everything else (title, company size, industry, phone) is missing. Without it, lead scoring and routing don't work."),
        ],
        "how_we_help": [
            ("Email list cleaning", "SMTP verification on your entire database. Invalid addresses flagged and suppressed. Catch-all domains identified. Deliverability restored before your next campaign."),
            ("Field standardization for segmentation", "Job titles normalized. Industry codes cleaned. Company sizes standardized. Your segments become reliable and repeatable."),
            ("Marketing contact optimization", "We identify contacts that should be removed from your billing (bounced, unengaged, invalid). Save on HubSpot or Marketo costs without losing real prospects."),
            ("Form submission enrichment", "New form fills arrive with name and email. We enrich them with title, company size, industry, and phone within hours. Your lead scoring fires with full data instead of guesses."),
            ("Suppression list management", "We maintain and validate your suppression lists: competitors, existing customers, do-not-contact records. Clean lists mean cleaner campaigns."),
        ],
        "use_cases_html": """        <h3>Pre-campaign email validation</h3>
        <p>Before a major campaign or product launch, we validate every email on your send list. Invalid addresses get suppressed. Your bounce rate stays under 2% and your sender reputation stays intact.</p>

        <h3>HubSpot marketing contact audit</h3>
        <p>We audit your marketing contacts to identify records you're paying for but shouldn't be: hard bounces, unsubscribes, competitors, and contacts who haven't engaged in 12+ months. Most companies save 15-25% on their contact tier.</p>

        <h3>ABM list building and enrichment</h3>
        <p>You've identified your target accounts. We find the right contacts at each one: verified emails and direct dials for the specific personas your ABM campaigns need to reach.</p>

        <h3>Post-webinar enrichment</h3>
        <p>Webinar registrations come in with incomplete data. We enrich registrants with company size, industry, and title so your follow-up sequences are properly segmented instead of one-size-fits-all.</p>""",
        "related_resources": [
            ("Data Hygiene for Marketing Ops", "/resources/data-hygiene-for-marketing-ops.html"),
            ("Email Deliverability Guide", "/resources/email-deliverability-data-quality.html"),
            ("Database Maintenance Case Study", "/case-studies/database-maintenance-marketing-agency/"),
            ("HubSpot Marketing Contacts Cleanup", "/resources/hubspot-marketing-contacts-cleanup.html"),
        ],
        "faq_schema": [
            ("How much can I save on HubSpot marketing contacts?",
             "Most companies find 15-25% of their marketing contacts are dead weight (bounced emails, unsubscribes not properly removed, competitors, and long-unengaged contacts). For a company on HubSpot's 50,000 contact tier, that could mean dropping to a lower tier and saving $3,000-6,000/year."),
            ("How does email validation protect sender reputation?",
             "Every hard bounce counts against your domain's sender score. ISPs track bounce rates per sending domain. Above 5%, some ISPs start routing your email to spam. SMTP validation catches invalid addresses before you send, keeping bounce rates under 2%."),
            ("Can you integrate with our marketing automation platform?",
             "We work with any platform that supports CSV import or has an API: HubSpot, Marketo, Pardot, Mailchimp, ActiveCampaign, and others. We deliver data in your platform's import format so there's no manual mapping needed."),
        ],
        "cta_headline": "Fix Your Marketing Data",
        "cta_text": "Tell us what's broken and we'll show you what clean data looks like for your campaigns.",
    },
    {
        "slug": "data-services-for-founders",
        "title": "Data Services for Founders and CEOs",
        "meta_desc": "You don't have a data team. You don't need one. Verum provides managed data services for startups and SMBs. Prospect lists, CRM cleaning, and enrichment on demand.",
        "breadcrumb_name": "Data Services for Founders",
        "hero_subtitle": "You need leads, not a data platform subscription. We find and verify the contacts so you can focus on closing.",
        "intro_html": """        <p>At an early-stage company, the founder is the sales team, the marketing team, and the data team. You don't have a RevOps person to manage a ZoomInfo subscription. You don't have time to manually research prospects on LinkedIn. And you definitely don't have $15,000/year for a data platform you'll use twice.</p>

        <p>What you need is simple: a list of verified people to talk to, delivered fast, at a price that makes sense for your stage.</p>

        <p>Verum works with startups and SMBs on a per-project basis. No annual contracts. No platform to learn. No credits to manage. You tell us who you're trying to reach, we deliver verified contacts.</p>""",
        "pain_points": [
            ("Data platforms are too expensive", "ZoomInfo starts at $15K/year. Apollo is $99/month for limited credits. Even budget tools cost $200-500/month for a startup that needs data twice a quarter."),
            ("Manual research doesn't scale", "You've been manually finding prospects on LinkedIn. It works for 20 contacts. It doesn't work for 200 or 2,000."),
            ("Your CRM is already a mess", "Six months of data entry by multiple people, imported lists from different sources, and no standardization. It's getting harder to find anything."),
            ("You don't know what you don't know", "Is your ICP right? Is your data accurate? Are you targeting the right companies? Without data expertise on staff, these questions go unanswered."),
        ],
        "how_we_help": [
            ("Prospect lists from scratch", "Describe your target market. We build a verified list of contacts with emails, phone numbers, titles, and company data. Start outreach the day you receive it."),
            ("One-time CRM cleanup", "Send us your messy CRM export. We deduplicate, validate emails, standardize fields, and return a clean file. No ongoing commitment needed."),
            ("ICP analysis", "We analyze your existing customers to find patterns: which segments have the highest LTV, lowest churn, and fastest sales cycles. Data-driven targeting instead of gut feel."),
            ("Affordable pricing", "Per-project pricing starting at a few hundred dollars. No annual contracts, no seat licenses, no minimum commitments. Pay for what you need, when you need it."),
            ("No technical setup", "Email us a CSV or share a Google Sheet. We send back clean, enriched data in the same format. No integrations, no API setup, no onboarding."),
        ],
        "use_cases_html": """        <h3>First outbound campaign</h3>
        <p>You've validated your product with inbound leads. Now you need to proactively reach your market. We build your first prospect list of 500-2,000 verified contacts matching your ICP, ready for email sequences or cold calls.</p>

        <h3>Investor-ready CRM cleanup</h3>
        <p>Heading into a fundraise? Investors will look at your pipeline. We clean your CRM so your deal data, contact counts, and pipeline metrics reflect reality instead of accumulated data debt.</p>

        <h3>Post-launch market sizing</h3>
        <p>How big is your addressable market? We build a comprehensive list of companies matching your criteria, enriched with company size, industry, and contact data. You get a real number instead of a TAM slide based on analyst estimates.</p>

        <h3>Conference prep</h3>
        <p>Attending a conference and want to book meetings in advance? Give us the attendee list or exhibitor list. We enrich contacts with emails and phone numbers for pre-show outreach.</p>""",
        "related_resources": [
            ("CEO Guide to CRM Data Quality", "/resources/ceo-guide-crm-data-quality.html"),
            ("ICP Analysis Case Study", "/case-studies/icp-analysis-series-a-saas/"),
            ("What Is Data Enrichment?", "/resources/what-is-data-enrichment.html"),
            ("Pricing", "/pricing.html"),
        ],
        "faq_schema": [
            ("How much does a startup prospect list cost?",
             "A 500-contact list with verified emails, phone numbers, and company data typically costs $250-500. A 2,000-contact list runs $600-1,500 depending on enrichment depth. No subscription or annual commitment."),
            ("Do I need a CRM to use Verum?",
             "No. We can deliver data in CSV, Excel, or Google Sheets format. If you have a CRM (Salesforce, HubSpot, Pipedrive, etc.), we can format data for direct import. We work with whatever tools you're using."),
            ("How is this different from buying a list?",
             "Purchased lists are generic and unverified. We build custom lists matching your specific criteria, verify every email via SMTP, check phone numbers against carrier databases, and confirm job titles are current. Typical deliverability is 90%+ compared to 60-70% for purchased lists."),
        ],
        "cta_headline": "Get the Data Without the Platform",
        "cta_text": "Tell us who you're trying to reach. We'll build the list and verify every contact before delivery.",
    },
    {
        "slug": "data-services-for-data-teams",
        "title": "Data Services for Data and Analytics Teams",
        "meta_desc": "Outsource the grunt work of data cleaning and enrichment. Your data team should build models, not deduplicate records. Managed data quality services from Verum.",
        "breadcrumb_name": "Data Services for Data Teams",
        "hero_subtitle": "Your team was hired to build models and generate insights. Not to spend 60% of their time cleaning datasets.",
        "intro_html": """        <p>Data scientists and analysts spend an estimated 60% of their time on data preparation and cleaning, according to surveys from Kaggle and Anaconda. That's $60,000+ per year in salary going to work that doesn't require their expertise.</p>

        <p>The irony is that companies hire data teams to extract insights, but the teams get buried in the prerequisite work: standardizing formats, resolving entities, deduplicating records, filling missing values, and validating data quality. The analysis that leadership actually wants keeps getting pushed back.</p>

        <p>Verum handles the data preparation so your team can focus on the analysis.</p>""",
        "pain_points": [
            ("60% of time on prep, not analysis", "Your team spends more time cleaning data than analyzing it. Every project starts with the same tedious prep work before the real work begins."),
            ("Entity resolution is a recurring headache", "Matching records across systems with different identifiers, name formats, and data structures is critical and time-consuming. Getting it wrong invalidates downstream analysis."),
            ("Data quality degrades between projects", "You clean a dataset for one analysis. Six months later, someone needs the same data and it's decayed again. There's no maintenance layer."),
            ("Enrichment gaps limit your models", "Your predictive models need firmographic, technographic, and contact data that doesn't exist in your internal systems. Filling those gaps manually is slow."),
        ],
        "how_we_help": [
            ("Dataset preparation", "Send us raw data from any source. We clean, standardize, deduplicate, and deliver analysis-ready datasets. Your team starts with clean data instead of spending weeks on prep."),
            ("Entity resolution at scale", "We match records across systems using fuzzy matching, probabilistic linkage, and multi-field comparison. Company names, contact names, addresses, and identifiers resolved into unified entities."),
            ("Enrichment for model features", "We add external data fields your models need: company size, industry classification, technology usage, geographic data, and contact attributes. From 50+ data sources."),
            ("Ongoing data quality monitoring", "Monthly validation and re-enrichment keeps your datasets current. Data quality doesn't degrade between projects because we maintain it continuously."),
            ("Custom data pipelines", "Recurring data needs (quarterly customer analysis, monthly market sizing, weekly lead scoring inputs) can be automated on a schedule. We deliver updated, clean datasets at whatever cadence you need."),
        ],
        "use_cases_html": """        <h3>Customer analysis dataset prep</h3>
        <p>Your customer success team wants a churn analysis. You need to merge CRM data, billing data, and product usage data into a single clean dataset. We handle the merge, deduplication, and entity resolution so you can go straight to modeling.</p>

        <h3>Market research enrichment</h3>
        <p>Building a market map or competitive analysis? We enrich company lists with firmographic data, technology usage, employee counts, revenue estimates, and contact information. Clean, structured data ready for analysis.</p>

        <h3>Training data preparation</h3>
        <p>ML models are only as good as their training data. We clean, standardize, and validate the datasets your models train on. Consistent labeling, resolved entities, and validated records improve model accuracy.</p>

        <h3>Board reporting data cleanup</h3>
        <p>Before board meetings, the data team scrambles to reconcile numbers across systems. We maintain clean, deduplicated datasets so your reporting always pulls from a single source of truth.</p>""",
        "related_resources": [
            ("Data Quality for AI & ML", "/resources/data-quality-ai-ml.html"),
            ("Data Quality Metrics", "/resources/data-quality-metrics.html"),
            ("Entity Resolution", "/glossary/entity-resolution/"),
            ("Data Profiling", "/glossary/data-profiling/"),
        ],
        "faq_schema": [
            ("What data formats do you work with?",
             "We accept CSV, Excel, JSON, Parquet, database exports, and API connections. We deliver in whatever format your team prefers. For recurring projects, we can push directly to your data warehouse or cloud storage."),
            ("Can you handle datasets larger than 1 million records?",
             "Yes. Our infrastructure handles datasets of any size. For very large datasets (10M+ records), we scope the project upfront to set turnaround expectations. Most datasets under 1M records are delivered in 3-7 days."),
            ("How do you handle entity resolution across multiple systems?",
             "We use a combination of deterministic matching (exact email, phone, ID matches) and probabilistic matching (fuzzy name comparison, address normalization, company name standardization). Match confidence scores are included so your team can set their own thresholds."),
        ],
        "cta_headline": "Stop Wasting Data Team Hours on Cleaning",
        "cta_text": "Tell us what datasets need preparation and we'll show you how much time your team can get back.",
    },
]


if __name__ == "__main__":
    for persona in PERSONAS:
        slug = persona["slug"]
        out_dir = os.path.join(SITE_ROOT, "solutions", slug)
        os.makedirs(out_dir, exist_ok=True)
        html = gen_persona_page(**persona)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Created: solutions/{slug}/index.html")

    print(f"\nTotal: {len(PERSONAS)} persona landing pages")
