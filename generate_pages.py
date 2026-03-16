#!/usr/bin/env python3
"""
Verum Website - Full-Quality SEO Page Generator
Generates 200+ rich SEO pages (~300 lines, 1200-1500 words each)
Skips manually enhanced pages. Skips solutions/ entirely.
"""

import os
import json
from datetime import datetime

BASE_URL = "https://veruminc.com"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.now().strftime("%Y-%m-%d")

SKIP_PAGES = {
    "/enrichment/linkedin-profile-enrichment/",
    "/enrichment/domain-enrichment/",
    "/enrichment/marketing-automation-detection/",
    "/cleaning/lead-data-cleaning/",
    "/use-cases/crm-hygiene/",
    "/use-cases/customer-data-platform/",
}

def esc(t):
    return t.replace('"', '&quot;').replace("'", "&#39;")

def faq_schema_json(faqs):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs
    ]}, indent=4)

def breadcrumb_json(crumbs):
    items = []
    for i,(n,u) in enumerate(crumbs,1):
        it = {"@type":"ListItem","position":i,"name":n}
        if u: it["item"] = u
        items.append(it)
    return json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}, indent=4)

def service_json(name, desc, stype, url):
    return json.dumps({"@context":"https://schema.org","@type":"Service","name":name,
        "provider":{"@id":"https://veruminc.com/#organization"},"description":desc,
        "serviceType":stype,"areaServed":"Worldwide","url":url}, indent=4)

def write_page(path, html):
    if path.endswith('/'):
        fp = os.path.join(OUTPUT_DIR, path.strip('/'), 'index.html')
    else:
        fp = os.path.join(OUTPUT_DIR, path.strip('/'))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'w') as f:
        f.write(html)
    return fp

def full_page(title, meta_desc, canonical, breadcrumbs, svc_schema, faq_schema,
              h1, subtitle, pain_stats, body_html, related_links):
    """Build complete ~300-line HTML page."""
    bc = breadcrumb_json(breadcrumbs)
    url = f"{BASE_URL}{canonical}"
    stats_h = ""
    for num, label in pain_stats:
        stats_h += f'          <div class="pain-stat">\n            <span class="pain-stat__number">{num}</span>\n            <span class="pain-stat__label">{label}</span>\n          </div>\n'
    svc_block = f'  <script type="application/ld+json">\n{svc_schema}\n  </script>\n' if svc_schema else ""
    rel_h = " | ".join(f'<a href="{u}">{t}</a>' for t,u in related_links)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <link rel="canonical" href="{url}">
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
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(meta_desc)}">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="{BASE_URL}/assets/social/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(meta_desc)}">
  <meta name="twitter:image" content="{BASE_URL}/assets/social/twitter-card.png">
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
{bc}
  </script>
{svc_block}  <script type="application/ld+json">
{faq_schema}
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
        <h1 class="page-hero__title">{h1}</h1>
        <p class="page-hero__subtitle">{subtitle}</p>
        <div class="pain-stats">
{stats_h}        </div>
        <div class="hero-cta-group">
          <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>
          <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Assessment</a>
        </div>
      </div>
    </section>
    <section class="content">
      <div class="container" style="max-width: 800px;">
{body_html}
        <p class="mt-lg text-muted">Related: {rel_h}</p>
      </div>
    </section>
  </main>
  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


def build_body(pain_title, pain_paras, solution_title, solution_paras,
               use_cases_title, use_cases, process_context,
               why_title, why_items, comp_rows, faq_title, faqs,
               final_h2, final_p1, final_p2):
    """Build the body HTML between hero and footer with all required sections."""
    h = ""
    # PAIN SECTION
    h += f"        <h2>{pain_title}</h2>\n"
    for p in pain_paras:
        if p.startswith("<h3>"):
            h += f"        {p}\n"
        else:
            h += f"        <p>{p}</p>\n"
    h += '\n        <div class="text-center mt-xl">\n          <a href="/#contact" class="btn btn--secondary">See How Clean Data Transforms Operations</a>\n        </div>\n\n'
    # SOLUTION SECTION
    h += f"        <h2>{solution_title}</h2>\n"
    for p in solution_paras:
        if p.startswith("<h3>") or p.startswith("<p><strong>"):
            h += f"        {p}\n"
        else:
            h += f"        <p>{p}</p>\n"
    # SOLUTION STATS BAR
    h += """
        <div class="solution-stats">
          <div class="solution-stat">
            <span class="solution-stat__number">93%</span>
            <span class="solution-stat__label">Deliverability guarantee</span>
          </div>
          <div class="solution-stat">
            <span class="solution-stat__number">24&#8209;48hr</span>
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

"""
    # USE CASES
    h += f'        <h2>{use_cases_title}</h2>\n        <ul class="feature-list">\n'
    for strong, detail in use_cases:
        h += f"          <li><strong>{strong}</strong> {detail}</li>\n"
    h += "        </ul>\n\n"
    # PROCESS
    h += "        <h2>Getting Started Takes Less Time Than Your Average Meeting</h2>\n"
    h += f"        <p><strong>Step 1: Free Assessment (5 minutes)</strong><br>Upload a sample file or tell us what you need. We'll review your data and tell you exactly what we can do, with expected match rates and timelines{process_context}.</p>\n"
    h += "        <p><strong>Step 2: Discovery Call (30 minutes)</strong><br>We'll walk through your current stack, data sources, and goals. No sales pitch. Just a technical conversation about your data.</p>\n"
    h += "        <p><strong>Step 3: Data Analysis (on us)</strong><br>We run a free analysis on a sample of your records so you can see results before committing to anything.</p>\n"
    h += "        <p><strong>Step 4: Full Engagement</strong><br>Once you approve the sample results, we process your full dataset. Most projects complete in 24&#8209;48 hours.</p>\n"
    h += "        <p><strong>Step 5: Ongoing (if you want it)</strong><br>Data decays at 30% per year. We offer quarterly or monthly re&#8209;enrichment to keep your records current. No long&#8209;term contracts required.</p>\n\n"
    # WHY VERUM
    h += f'        <h2>{why_title}</h2>\n        <ul class="feature-list">\n'
    for strong, detail in why_items:
        h += f"          <li><strong>{strong}</strong> {detail}</li>\n"
    h += "        </ul>\n\n"
    # COMPARISON TABLE
    h += '        <h2>The Old Way vs. With Verum</h2>\n        <table class="comparison-table">\n          <thead>\n            <tr>\n              <th>The Old Way</th>\n              <th>With Verum</th>\n            </tr>\n          </thead>\n          <tbody>\n'
    for old, new in comp_rows:
        h += f"            <tr><td>{old}</td><td>{new}</td></tr>\n"
    h += "          </tbody>\n        </table>\n\n"
    # FAQ
    h += f'        <h2>{faq_title}</h2>\n        <div class="faq-section">\n'
    for q, a in faqs:
        h += f'          <div class="faq-item" style="margin-bottom: 1.5rem;">\n            <h3 style="font-size: 1rem; margin-bottom: 0.5rem;">{q}</h3>\n            <p style="color: var(--color-text-secondary);">{a}</p>\n          </div>\n'
    h += "        </div>\n\n"
    # FINAL CTA
    h += f"        <h2>{final_h2}</h2>\n"
    h += f"        <p>{final_p1}</p>\n"
    h += f"        <p>{final_p2}</p>\n"
    h += '\n        <div class="cta-group mt-xl">\n          <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Assessment</a>\n          <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>\n        </div>\n\n'
    return h

ZOOMINFO_FAQ = ("How is this different from buying a ZoomInfo license?",
    "Three differences. First, different problem: ZoomInfo sells net-new contacts, Verum enriches your existing records. Second, different pricing: ZoomInfo runs $15K-$50K+ per year, Verum charges per project. Third, different ownership: ZoomInfo requires data deletion when you cancel. Verum data is yours forever.")


# ============================================================
# ENRICHMENT PAGES - Compact data + category template
# ============================================================
# Each tuple: (slug, display_name, short_desc, sub_group)
# sub_group determines which pain/solution template variant to use

ENRICHMENT_TYPES = [
    # Social profiles
    ("facebook-profile-enrichment", "Facebook Profile Enrichment", "Match Facebook profiles and business pages to your CRM contacts", "social"),
    ("instagram-profile-enrichment", "Instagram Profile Enrichment", "Discover Instagram business accounts linked to your B2B contacts", "social"),
    ("twitter-profile-enrichment", "Twitter/X Profile Enrichment", "Match Twitter handles to contacts for social selling signals", "social"),
    ("social-media-enrichment", "Social Media Enrichment", "Comprehensive social profile matching across all platforms in one pass", "social"),
    # Email & phone
    ("email-enrichment", "Email Enrichment", "Find and verify business email addresses for your contacts", "contact"),
    ("email-finder", "Email Finder", "Discover email addresses from names and company domains", "contact"),
    ("phone-number-enrichment", "Phone Number Enrichment", "Append direct phone numbers to your contact records", "contact"),
    ("direct-dial-enrichment", "Direct Dial Enrichment", "Find direct dial numbers that bypass the front desk", "contact"),
    ("mobile-number-enrichment", "Mobile Number Enrichment", "Append mobile phone numbers for SMS and direct outreach", "contact"),
    ("contact-enrichment", "Contact Enrichment", "Complete contact record enrichment with all available data points", "contact"),
    # Company / firmographic
    ("company-enrichment", "Company Enrichment", "Append firmographic data including size, revenue, and industry", "company"),
    ("firmographic-enrichment", "Firmographic Enrichment", "Add company size, revenue, industry, and location data to accounts", "company"),
    ("company-size-enrichment", "Company Size Enrichment", "Append accurate employee counts and company size ranges", "company"),
    ("employee-count-enrichment", "Employee Count Enrichment", "Get accurate employee counts for lead scoring and segmentation", "company"),
    ("company-revenue-enrichment", "Company Revenue Enrichment", "Append estimated annual revenue to your account records", "company"),
    ("company-funding-enrichment", "Company Funding Enrichment", "Track funding rounds, amounts, and investors for target accounts", "company"),
    ("funding-round-enrichment", "Funding Round Enrichment", "Identify recent funding rounds and investment activity", "company"),
    ("investor-enrichment", "Investor Enrichment", "Discover investors and board members for target accounts", "company"),
    ("company-location-enrichment", "Company Location Enrichment", "Append headquarters and office locations for territory mapping", "company"),
    ("headquarters-enrichment", "Headquarters Enrichment", "Find company HQ addresses for territory and routing logic", "company"),
    # Industry classification
    ("industry-classification-enrichment", "Industry Classification Enrichment", "Standardize industry codes across your entire database", "classification"),
    ("sic-code-enrichment", "SIC Code Enrichment", "Append SIC codes for accurate industry targeting and segmentation", "classification"),
    ("naics-code-enrichment", "NAICS Code Enrichment", "Add NAICS codes for precise industry classification", "classification"),
    # Technographic
    ("technographic-enrichment", "Technographic Enrichment", "Discover the technology stack of your target companies", "tech"),
    ("tech-stack-enrichment", "Tech Stack Enrichment", "Identify software and tools companies use for better targeting", "tech"),
    ("technology-enrichment", "Technology Enrichment", "Append technology usage data across 10,000+ products", "tech"),
    ("crm-detection", "CRM Detection", "Identify which CRM systems your target companies use", "tech"),
    ("website-technology-enrichment", "Website Technology Enrichment", "Analyze websites to identify technologies and platforms in use", "tech"),
    # Intent
    ("intent-data-enrichment", "Intent Data Enrichment", "Identify accounts showing active buying intent signals", "intent"),
    ("buyer-intent-enrichment", "Buyer Intent Enrichment", "Track in-market buyers for timely outreach at the right moment", "intent"),
    ("buying-signals-enrichment", "Buying Signals Enrichment", "Detect signals indicating purchase readiness across your accounts", "intent"),
    # Role / title
    ("job-title-enrichment", "Job Title Enrichment", "Standardize and enrich job titles for accurate targeting", "role"),
    ("seniority-enrichment", "Seniority Enrichment", "Classify contacts by seniority level for lead routing", "role"),
    ("department-enrichment", "Department Enrichment", "Identify functional departments for better routing and targeting", "role"),
    ("decision-maker-enrichment", "Decision Maker Enrichment", "Identify decision makers within your target accounts", "role"),
    ("c-suite-enrichment", "C-Suite Enrichment", "Find and enrich C-level executive contacts at target companies", "role"),
    # Web / domain
    ("website-enrichment", "Website Enrichment", "Extract and enrich company data from website analysis", "web"),
    ("address-enrichment", "Address Enrichment", "Standardize and complete mailing address information", "web"),
    # Broad
    ("b2b-data-enrichment", "B2B Data Enrichment", "Comprehensive B2B data enrichment across all data types", "broad"),
    ("lead-enrichment", "Lead Enrichment", "Enrich inbound leads with complete contact and company data instantly", "broad"),
]

# Sub-group specific content templates
_ENRICH_PAIN = {
    "social": {
        "title": "The {name} Problem Nobody Talks About",
        "paras": [
            "Your CRM has names and emails. Maybe phone numbers. But the social profiles connected to those contacts tell a completely different story. Activity levels, content interests, professional networks, brand affiliations. All of it invisible to your sales team because {lname} data isn't in your system.",
            "<h3>Reps Research Manually (and Inconsistently)</h3>",
            "Some reps check social profiles before calls. Most don't. The ones who do spend 3-5 minutes per contact searching, scanning, and noting details that never make it into the CRM. Multiply that by a pipeline of 300 accounts and you've lost days of selling time to research that should've been automated.",
            "<h3>Social Data Decays Faster Than You Think</h3>",
            "People change handles, deactivate accounts, switch platforms. The social profile you saved six months ago might point to the wrong person or a dead link. B2B contact data decays at 30% annually, and social handles decay even faster because there's no formal change notification.",
            "<h3>Single&#8209;Platform Blindness</h3>",
            "Most enrichment tools only cover LinkedIn. That misses the SMB owners active on Facebook, the marketers living on Twitter, and the agencies whose primary presence is Instagram. If you're only enriching one platform, your social data has gaps.",
            "<h3>Disconnected Intelligence</h3>",
            "Even when someone does find a social profile, that data lives in their head, a browser tab, or a Slack message. It never becomes a structured field in your CRM that the whole team can filter, score, and act on. That's wasted intelligence.",
        ],
    },
    "contact": {
        "title": "The {name} Challenge",
        "paras": [
            "You've got contacts in your CRM. Some have email addresses. Some have phone numbers. Very few have both, and the ones that do are aging by the day. Reaching a B2B buyer requires accurate contact data, and most databases are missing the basics.",
            "<h3>Incomplete Records Kill Outreach</h3>",
            "A contact without an email can't enter your sequences. A contact without a phone can't get a cold call. Salesforce reports that 91% of CRM data is incomplete. That means your reps are working with one hand tied behind their back on almost every record.",
            "<h3>Data Decays at 30% Per Year</h3>",
            "People change jobs, companies switch email formats, phone numbers get reassigned. HubSpot found that email lists decay at 22.5% per year. If you enriched your database 12 months ago and haven't touched it since, nearly a quarter of those email addresses may bounce.",
            "<h3>Guessing Email Formats Costs You</h3>",
            "The first.last@company.com approach works sometimes. But when it doesn't, you're sending to invalid addresses, hurting your sender reputation, and potentially getting your domain blacklisted. A 15-25% bounce rate from guessed formats is typical. Verified enrichment drops that below 3%.",
            "<h3>Manual Research Doesn't Scale</h3>",
            "Your SDRs shouldn't be spending their selling hours hunting for email addresses and phone numbers. At an average of $75K/year fully loaded, every hour they spend on data research costs you $36. That adds up fast across a team of 10.",
        ],
    },
    "company": {
        "title": "The {name} Gap in Your Database",
        "paras": [
            "Your CRM has company names. Maybe websites. But the firmographic details that drive lead scoring, territory assignment, and account prioritization? Most records are missing them. 62% of organizations rely on data that's up to 40% inaccurate according to Experian.",
            "<h3>Lead Scoring Without Firmographics Is Guesswork</h3>",
            "If you can't score leads by company size, revenue, or industry, you're treating a 10-person startup the same as a 5,000-employee enterprise. Your reps waste time on accounts that will never close, and qualified accounts sit in the queue untouched.",
            "<h3>Territory Planning With Bad Data Creates Conflict</h3>",
            "When company locations are missing or wrong, deals get routed to the wrong reps. Territory overlap causes internal conflict. Gartner estimates that 40% of business objectives fail due to bad data, and territory planning is one of the first things that breaks.",
            "<h3>Account&#8209;Based Marketing Needs Complete Records</h3>",
            "ABM campaigns target accounts by firmographic attributes. If your account records don't have accurate employee counts, revenue ranges, or industry classifications, your targeting is as broad as the spray&#8209;and&#8209;pray approach you were trying to replace.",
            "<h3>Stale Firmographics Mislead Your Strategy</h3>",
            "Companies grow, shrink, get acquired, and relocate. The firmographic data you imported two years ago doesn't reflect the company as it exists today. A startup that was 50 people when you last enriched might be 500 now, completely changing its qualification.",
        ],
    },
    "classification": {
        "title": "The {name} Problem",
        "paras": [
            "You've got accounts spread across a dozen industry labels. Some say 'Technology.' Others say 'Tech' or 'IT' or 'Software.' Your CRM can't distinguish a healthcare company from a health tech company because nobody standardized the industry fields. This creates chaos in reporting, routing, and targeting.",
            "<h3>Inconsistent Labels Break Reporting</h3>",
            "When your industry fields aren't standardized, a simple question like 'how many healthcare accounts do we have?' becomes a 30-minute data exercise. You'll find them scattered across Healthcare, Health Care, Medical, Pharma, Life Sciences, and a dozen other variations.",
            "<h3>Lead Routing Goes Wrong</h3>",
            "If your routing rules depend on industry classification, inconsistent labels send leads to the wrong teams. A fintech company labeled 'Financial Services' might get routed to your banking team instead of your technology team. These misroutes cost you response time and first impressions.",
            "<h3>Segmentation Becomes Unreliable</h3>",
            "Marketing campaigns targeting specific industries underperform when 20-30% of accounts have missing or incorrect classifications. You end up either over-mailing people in the wrong segment or missing qualified accounts entirely.",
            "<h3>Compliance and Reporting Requirements</h3>",
            "Many organizations need to report on customers and prospects by SIC or NAICS code. Without standardized industry codes, producing these reports requires manual classification that takes weeks and introduces errors.",
        ],
    },
    "tech": {
        "title": "The {name} Advantage You're Missing",
        "paras": [
            "Knowing what software your prospects use changes how you sell to them. A company running Salesforce has different needs than one on HubSpot. A company using AWS is a different conversation than one on Azure. But most CRMs have zero technographic data.",
            "<h3>Selling Blind Without Tech Stack Data</h3>",
            "Your reps are pitching integration stories to companies using tools you don't integrate with. They're positioning against competitors that aren't in the deal. Without knowing what's already in the stack, every call starts from zero instead of building on what you know.",
            "<h3>Competitive Displacement Requires Intelligence</h3>",
            "If you're trying to replace a competitor's product, you need to know who's using it. Manually researching tech stacks through job postings, G2 reviews, and website source code is possible but takes 15-20 minutes per account. That doesn't scale to 5,000 target accounts.",
            "<h3>Integration Compatibility Drives Adoption</h3>",
            "Companies buy tools that work with what they already have. Knowing a prospect's tech stack lets you lead with relevant integration stories, which is the fastest path to a technical win. Without this data, your demo is generic and your value prop is abstract.",
            "<h3>Technology Signals Buying Intent</h3>",
            "When a company adopts a new CRM, they'll need data migration and enrichment. When they add a marketing automation platform, they need clean email lists. Technology changes create buying moments. Without technographic monitoring, you'll miss them.",
        ],
    },
    "intent": {
        "title": "The {name} Edge Your Competitors Already Have",
        "paras": [
            "Somewhere in your TAM, accounts are actively researching solutions like yours right now. They're reading comparison articles, attending webinars, and searching for alternatives. Intent data tells you which accounts those are so you can reach them while they're in-market, not six months late.",
            "<h3>Cold Outreach Wastes Most of Your Budget</h3>",
            "When you spray outreach across your entire TAM, 95% of those accounts aren't in a buying cycle. That means 95% of your SDR time, email sends, and ad spend hits accounts that won't convert regardless of how good your messaging is. Intent data focuses your resources on the 5% that matter now.",
            "<h3>Timing Is the Biggest Variable in B2B Sales</h3>",
            "The same prospect who ignores your email in March might be actively evaluating vendors in June. Without intent signals, you have no way to know when the window opens. By the time they fill out a form, they've already shortlisted vendors and you might not be on the list.",
            "<h3>Competitors With Intent Data Move Faster</h3>",
            "If your competitor is using intent data and you're not, they're reaching your shared prospects while those prospects are actively researching. They get the first meeting, set the evaluation criteria, and shape the deal before you even know it exists.",
            "<h3>Content Consumption Reveals Pain Points</h3>",
            "When an account consumes content about CRM migration, they have a CRM problem. When they research data cleaning, they have a data quality problem. Intent data doesn't just tell you who's in-market. It tells you what they're struggling with so you can tailor your outreach to their specific pain.",
        ],
    },
    "role": {
        "title": "The {name} Mess in Your CRM",
        "paras": [
            "Job titles in CRMs are unreliable. 'Manager' could mean anything from a team lead managing two people to a senior leader running a department. 'VP' at a startup is different from 'VP' at a Fortune 500. Without normalized titles and seniority data, your routing, scoring, and targeting are all working with garbage inputs.",
            "<h3>Lead Routing Fails on Unstandardized Titles</h3>",
            "When your routing rules look for 'Director' and above, they miss the 'Head of' and 'Principal' titles that carry the same authority. They also over-route 'Director of First Impressions' (a receptionist title). Inconsistent title data sends qualified leads to the wrong team and wastes time on unqualified ones.",
            "<h3>Lead Scoring Can't Score What It Can't Classify</h3>",
            "If your lead scoring model weights seniority, it needs clean seniority data. A free-text title field with 10,000 variations doesn't give your scoring model anything to work with. You end up treating a C-level executive the same as an individual contributor.",
            "<h3>ABM Campaigns Need Decision-Maker Accuracy</h3>",
            "ABM targeting depends on reaching the right people within target accounts. When you can't reliably identify decision-makers, budget holders, and influencers from your existing data, your multi-threaded outreach hits the wrong layers of the org chart.",
            "<h3>50% of Rep Time on Non&#8209;Selling Activities</h3>",
            "Salesforce research shows reps spend half their time on tasks other than selling. A meaningful chunk of that is figuring out whether a contact is worth pursuing based on their title, role, and seniority. Enriched role data eliminates that guesswork.",
        ],
    },
    "web": {
        "title": "The {name} Gap",
        "paras": [
            "Company websites and physical addresses contain intelligence that most CRMs don't capture. What technologies power the site, where the company actually operates, how many locations they have, what their recent news says about growth or contraction. Without this data, your account records are incomplete.",
            "<h3>Websites Tell You More Than LinkedIn</h3>",
            "A company's website reveals their tech stack (through source code analysis), their growth trajectory (through job postings), their market positioning (through messaging), and their investment in digital (through site quality). All of this is public data that most teams never systematically capture.",
            "<h3>Address Data Is a Mess</h3>",
            "Inconsistent address formats, missing suite numbers, outdated locations after office moves, and PO boxes listed as headquarters. Bad address data breaks territory mapping, direct mail campaigns, and field sales routing. USPS estimates that undeliverable mail costs U.S. businesses $20 billion annually.",
            "<h3>No Systematic Website Monitoring</h3>",
            "Companies redesign their websites, add new product pages, change their leadership team bios, and update their footer addresses. These changes signal business events that matter to your sales team. But nobody's checking 5,000 websites manually for changes.",
            "<h3>Data Integration Problems</h3>",
            "When website data does exist in your CRM, it's often in a free-text notes field or an outdated URL column. It's not structured, not current, and not usable for automation, scoring, or segmentation.",
        ],
    },
    "broad": {
        "title": "The {name} Problem That's Costing You Revenue",
        "paras": [
            "Your database is the foundation of every go-to-market motion. Outbound sequences, inbound routing, ABM targeting, email campaigns, pipeline forecasting. All of it runs on data. And if that data is incomplete, outdated, or wrong, everything downstream breaks.",
            "<h3>91% of CRM Data Is Incomplete</h3>",
            "Salesforce's own research found that 91% of CRM data is incomplete. Missing emails, wrong phone numbers, outdated titles, no firmographics. Your team is building their strategy on a database full of holes, and they've gotten so used to it they've stopped noticing.",
            "<h3>Data Decays at 30% Per Year</h3>",
            "People change jobs, companies get acquired, phone numbers get reassigned, offices relocate. The database you cleaned six months ago is already losing value. Gartner estimates that the average cost of poor data quality is $15 million per year for large organizations.",
            "<h3>Multiple Tools, Same Problems</h3>",
            "Most teams have tried ZoomInfo, Clearbit, Apollo, or some combination. They paid $15K-$50K per year for access to databases that still require manual cleanup. The data comes in with duplicates, inconsistencies, and gaps. You traded one data problem for another.",
            "<h3>Revenue Impact Is Real</h3>",
            "D&amp;B research shows that 27% of revenue is impacted by bad data. Deals lost because reps called the wrong person. Campaigns that bounced because emails were invalid. Territories assigned incorrectly because company data was stale. The cost is real even if it doesn't show up on a line item.",
        ],
    },
}

_ENRICH_SOLUTION = {
    "social": [
        "We match your contacts to their social profiles using multi-signal identity resolution. Name, company, email, and cross-platform links all factor into the match. You get back verified profile URLs and structured social data appended to your CRM records.",
        "<h3>Multi&#8209;Signal Identity Matching</h3>",
        "Social usernames rarely match CRM records exactly. We use company affiliation, email domain, bio text, and cross-platform links to disambiguate common names and find the right profile.",
        "<p><strong>For your team:</strong> Every enriched record includes a confidence score so reps know which matches are solid and which need a second look.</p>",
        "<h3>Structured Data, Not Just URLs</h3>",
        "We don't just hand you a profile link. Each match comes with account type, activity status, follower metrics, and bio text in structured fields your CRM can actually use for scoring and segmentation.",
        "<h3>Human QA on Everything</h3>",
        "Social matching is noisy. Common names produce multiple candidates. Our team reviews ambiguous matches to make sure your records connect to the right person, not a name-match at a different company.",
    ],
    "contact": [
        "We find, verify, and append contact data from 50+ sources. Every email is SMTP-verified. Every phone number is checked against carrier databases. You get back complete contact records with deliverability scores on every data point.",
        "<h3>Multi&#8209;Source Discovery</h3>",
        "We don't rely on a single database. We cross-reference professional networks, business registrations, corporate directories, and public records to find the most current contact information for each person.",
        "<p><strong>For your team:</strong> Higher match rates than any single vendor because we're pulling from 50+ sources and picking the best result, not just the first result.</p>",
        "<h3>Verification Before Delivery</h3>",
        "Every email address is SMTP-verified to confirm it exists and can receive mail. Every phone number is checked against carrier data to confirm it's active and correctly formatted. You don't pay for data that bounces.",
        "<h3>Human QA on Everything</h3>",
        "Automated enrichment catches most records. But the edge cases, contacts with common names at large companies, people who recently changed roles, records with conflicting data across sources, get human review to ensure accuracy.",
    ],
    "company": [
        "We append complete firmographic profiles to your account records. Employee count, revenue range, industry, founding year, HQ location, office count, and more. All sourced from business registrations, financial filings, and verified databases.",
        "<h3>Multi&#8209;Source Firmographic Matching</h3>",
        "Single-source firmographics are unreliable. Employee counts vary wildly between LinkedIn, Crunchbase, and SEC filings. We cross-reference multiple sources to deliver the most accurate number, not just the most recent one.",
        "<p><strong>For your team:</strong> Accurate firmographics mean your lead scoring, territory assignment, and ICP filtering actually work instead of routing on garbage data.</p>",
        "<h3>Company Hierarchy Resolution</h3>",
        "Is it the parent company or a subsidiary? A regional office or the HQ? We resolve company hierarchies so your account records reflect the entity your reps actually sell to, not a holding company they'll never reach.",
        "<h3>Human QA on Everything</h3>",
        "Automated firmographic matching works well for well-known companies. For SMBs, startups, and recently acquired companies, our team manually verifies the data to ensure accuracy.",
    ],
    "classification": [
        "We standardize your industry fields to recognized classification systems (SIC, NAICS, or custom taxonomies) and resolve the inconsistencies that break your reporting, routing, and segmentation.",
        "<h3>Automated Reclassification</h3>",
        "We analyze company descriptions, websites, and existing classifications to assign accurate industry codes. A company labeled 'Technology' gets reclassified to the specific NAICS code that matches their actual business (e.g., 511210 for Software Publishers).",
        "<p><strong>For your team:</strong> Clean industry codes mean your routing rules, reporting dashboards, and marketing segments actually reflect reality instead of whatever someone typed in three years ago.</p>",
        "<h3>Custom Taxonomy Support</h3>",
        "Not every team uses SIC or NAICS. If you have an internal industry taxonomy, we'll map your records to your categories. We've built custom mappings for dozens of companies with unique classification needs.",
        "<h3>Human QA on Everything</h3>",
        "Automated classification handles clear-cut cases. But companies that span multiple industries (a healthcare SaaS company, a financial services consulting firm) need human judgment. Our team reviews edge cases to ensure accurate classification.",
    ],
    "tech": [
        "We identify and append technology stack data for your target accounts using website analysis, job posting signals, partnership directories, and verified technographic databases. You get structured fields showing exactly what tools each company uses.",
        "<h3>Website Technology Detection</h3>",
        "We analyze company websites to identify CRMs, marketing automation platforms, analytics tools, CDPs, and hundreds of other technologies. This gives you current, verified tech stack data without relying on self-reported surveys.",
        "<p><strong>For your team:</strong> Know exactly which CRM, MAP, and key tools each prospect uses before the first call. Lead with relevant integration stories instead of generic feature pitches.</p>",
        "<h3>Job Posting Signal Analysis</h3>",
        "When a company posts a job requiring Salesforce experience, they use Salesforce. When they list Snowflake as a requirement, they run Snowflake. We analyze job postings as a secondary technographic signal to validate and expand website-based detection.",
        "<h3>Human QA on Everything</h3>",
        "Technology detection from websites produces some false positives (a company may have legacy JavaScript on their site from a tool they no longer use). Our team validates detected technologies against multiple signals before appending.",
    ],
    "intent": [
        "We layer intent signals on top of your existing account data so your team can prioritize outreach to accounts that are actively in-market. You'll know who's researching, what they're researching, and how intensely.",
        "<h3>Topic&#8209;Level Intent Matching</h3>",
        "We don't just tell you an account is 'showing intent.' We tell you what topics they're researching, whether it's CRM migration, data enrichment, sales automation, or any of hundreds of B2B buying topics relevant to your business.",
        "<p><strong>For your team:</strong> Reps can tailor their outreach to the specific pain the prospect is researching instead of sending generic messaging to every intent-flagged account.</p>",
        "<h3>Surge Detection</h3>",
        "A single page visit isn't meaningful. But when an account's research activity spikes 3-5x above their baseline, that's a surge signal. We flag accounts showing unusual research intensity so your team can act on real buying behavior, not noise.",
        "<h3>Human QA on Everything</h3>",
        "Intent data has a noise problem. Researchers, students, and job seekers trigger false positives. Our team reviews flagged accounts to filter out non-buyer activity and ensure your pipeline prioritization is based on real purchase intent.",
    ],
    "role": [
        "We normalize job titles, classify seniority levels, identify departments, and flag decision-makers across your database. The result is structured role data your scoring, routing, and targeting can actually rely on.",
        "<h3>Title Normalization</h3>",
        "We map thousands of title variations to a standardized taxonomy. 'VP of Sales,' 'Vice President, Revenue,' 'Head of Sales,' and 'Chief Revenue Officer' all get classified correctly so your routing rules and reports work.",
        "<p><strong>For your team:</strong> Scoring models that use seniority and department data finally have clean inputs. Lead routing based on role actually sends leads to the right team.</p>",
        "<h3>Decision&#8209;Maker Identification</h3>",
        "We identify budget holders, technical evaluators, and executive sponsors within each account. Not every VP is a decision-maker, and not every Manager is junior. We use title, department, and company context to classify buying roles accurately.",
        "<h3>Human QA on Everything</h3>",
        "Title normalization is harder than it looks. 'Partner' means something different at a law firm versus a VC firm versus a consulting company. Our team handles the edge cases that automated classification gets wrong.",
    ],
    "web": [
        "We analyze company websites and standardize address data to give you accurate digital and physical location intelligence on every account in your CRM.",
        "<h3>Website Intelligence Extraction</h3>",
        "We scan company websites for technology indicators, employee count clues, location data, and business signals that aren't available in standard firmographic databases. Pricing pages, career pages, and leadership pages all contain intelligence we capture.",
        "<p><strong>For your team:</strong> Structured website intelligence fields in your CRM that update when companies make significant website changes.</p>",
        "<h3>Address Standardization and Verification</h3>",
        "We normalize addresses to USPS standards, verify deliverability, append missing components (ZIP+4, county, metro area), and flag addresses that don't match the expected company location. Clean addresses mean your direct mail actually arrives and your territory mapping is accurate.",
        "<h3>Human QA on Everything</h3>",
        "Website data extraction and address verification both have edge cases. Shell companies with minimal websites, co-working space addresses listed as HQ, subsidiary addresses confused with parent company. Our team catches what automation misses.",
    ],
    "broad": [
        "We enrich your entire database in a single engagement. Contact data, company firmographics, technographics, social profiles, and role classification. Instead of buying five separate tools, you get one clean, comprehensive enrichment pass with human QA.",
        "<h3>Full&#8209;Spectrum Enrichment</h3>",
        "We don't specialize in just one data type. A single enrichment pass fills in emails, phone numbers, titles, seniority, company size, revenue, industry, technology stack, and social profiles. One project, one vendor, one delivery.",
        "<p><strong>For your team:</strong> Instead of managing subscriptions to ZoomInfo for contacts, Clearbit for firmographics, and BuiltWith for technographics, you get complete enrichment from one source.</p>",
        "<h3>Database&#8209;Wide Quality Assessment</h3>",
        "Before we enrich anything, we analyze your entire database to identify completeness gaps, decay patterns, and quality issues. This assessment (which is free) shows you exactly where your data needs work and what results to expect.",
        "<h3>Human QA on Everything</h3>",
        "Every enrichment project gets human review. We don't just run your data through an API and hand it back. Our team reviews match rates, flags questionable records, and validates edge cases before delivery.",
    ],
}

# Per-page unique elements: (slug -> custom_subtitle, custom_stats, custom_faqs, custom_use_cases, custom_comparison, custom_related)
# These override defaults from sub-group
_ENRICH_CUSTOM = {
    "email-enrichment": {
        "subtitle": "You've got contacts without email addresses. We find the right ones and verify they won't bounce. Every address SMTP-checked before delivery.",
        "stats": [("22.5%", "Email lists decay per year"), ("91%", "Of CRM data is incomplete"), ("3%", "Bounce rate after verification")],
    },
    "email-finder": {
        "subtitle": "Give us names and companies. We'll find their business email addresses, verify every one at the server level, and deliver them ready for outreach.",
        "stats": [("60&#8209;75%", "Typical email discovery rate"), ("15%", "Bounce rate from guessed formats"), ("50+", "Sources cross&#8209;referenced")],
    },
    "phone-number-enrichment": {
        "subtitle": "Your reps need phone numbers. Not main switchboard lines that go to a receptionist. Direct numbers that reach the actual person they're trying to sell to.",
        "stats": [("91%", "Of CRM data is incomplete"), ("50%", "Of rep time on non&#8209;selling tasks"), ("50+", "Sources cross&#8209;referenced")],
    },
    "direct-dial-enrichment": {
        "subtitle": "Switchboard numbers waste time. Gatekeepers block calls. Direct dials connect your reps to the actual decision-maker without the runaround.",
        "stats": [("7x", "More connects with direct dials"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "mobile-number-enrichment": {
        "subtitle": "Mobile numbers cut through. No gatekeepers, no switchboards, no voicemail jail. Your reps reach the person directly, whether they're at their desk or not.",
        "stats": [("45%", "Higher connect rate on mobile"), ("30%", "Contact data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "contact-enrichment": {
        "subtitle": "Complete contact records drive everything. Email, phone, title, LinkedIn, social. We fill in every field from 50+ sources so your team stops working with partial data.",
        "stats": [("91%", "Of CRM data is incomplete"), ("$15M", "Avg annual cost of poor data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "company-enrichment": {
        "subtitle": "Your account records have company names. We add the firmographic detail that actually drives targeting: size, revenue, industry, location, funding, and tech stack.",
        "stats": [("62%", "Rely on 40%+ inaccurate data"), ("40%", "Of goals fail from bad data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "firmographic-enrichment": {
        "subtitle": "Employee count, revenue, industry, HQ location, founding year. The firmographic fields your lead scoring model depends on are probably missing or wrong.",
        "stats": [("62%", "Rely on 40%+ inaccurate data"), ("27%", "Revenue impacted by bad data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "company-size-enrichment": {
        "subtitle": "A 10-person startup is a different sale than a 5,000-employee enterprise. Without accurate company size data, your reps can't prioritize and your scoring model is broken.",
        "stats": [("40%", "Of goals fail from bad data"), ("25%", "Of accounts have wrong size data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "employee-count-enrichment": {
        "subtitle": "Employee count drives lead scoring, territory assignment, and pricing tier logic. If your CRM says 'Unknown' or shows a number from 2022, every downstream decision is compromised.",
        "stats": [("62%", "Rely on 40%+ inaccurate data"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "company-revenue-enrichment": {
        "subtitle": "Revenue data separates your best-fit accounts from the rest. Without it, your team treats a $2M company and a $200M company with the same playbook.",
        "stats": [("27%", "Revenue impacted by bad data"), ("$15M", "Avg cost of poor data quality"), ("50+", "Sources cross&#8209;referenced")],
    },
    "company-funding-enrichment": {
        "subtitle": "Freshly funded companies are buying. New capital means new tools, new hires, and new infrastructure. Your CRM should know who just raised and how much.",
        "stats": [("3x", "More likely to buy post&#8209;funding"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "funding-round-enrichment": {
        "subtitle": "Series A through IPO, each funding event creates buying windows. We track rounds, amounts, investors, and dates so your team reaches companies at the right moment.",
        "stats": [("3x", "Higher conversion post&#8209;funding"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "investor-enrichment": {
        "subtitle": "Knowing who invested and who sits on the board gives your team warm-path introductions and strategic context that cold outreach can't match.",
        "stats": [("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced"), ("24&#8209;48hr", "Typical turnaround")],
    },
    "company-location-enrichment": {
        "subtitle": "HQ versus field office versus co-working space. Your territory mapping and field sales routing only work when location data is accurate and current.",
        "stats": [("30%", "B2B data decays annually"), ("40%", "Of goals fail from bad data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "headquarters-enrichment": {
        "subtitle": "Territory assignment, field sales routing, and event targeting all depend on knowing where the HQ actually is. Not where it was three years ago.",
        "stats": [("30%", "B2B data decays annually"), ("$20B", "Lost to undeliverable mail yearly"), ("50+", "Sources cross&#8209;referenced")],
    },
    "industry-classification-enrichment": {
        "subtitle": "Your CRM has 47 variations of 'Technology' in the industry field. We standardize every account to SIC, NAICS, or your custom taxonomy so reporting and routing actually work.",
        "stats": [("62%", "Rely on 40%+ inaccurate data"), ("30%", "Of accounts misclassified"), ("50+", "Sources cross&#8209;referenced")],
    },
    "sic-code-enrichment": {
        "subtitle": "SIC codes are the standard for industry targeting, compliance reporting, and market analysis. Most CRMs have them on fewer than half of account records.",
        "stats": [("40%", "Of goals fail from bad data"), ("62%", "Rely on inaccurate data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "naics-code-enrichment": {
        "subtitle": "NAICS codes power federal contracting, compliance reporting, and precise industry segmentation. We append 6-digit codes to every account in your database.",
        "stats": [("1,057", "Active NAICS codes"), ("62%", "Rely on inaccurate data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "technographic-enrichment": {
        "subtitle": "What software do your prospects use? Their tech stack tells you how to position, what to demo, and which competitors you're displacing. We give you that data.",
        "stats": [("10K+", "Technologies we detect"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "tech-stack-enrichment": {
        "subtitle": "CRM, marketing automation, analytics, cloud infrastructure. We detect the tools your target accounts use so your reps can lead with relevant integration stories.",
        "stats": [("10K+", "Technologies tracked"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "technology-enrichment": {
        "subtitle": "Technology adoption data across 10,000+ products. Know what your prospects use, what they've recently adopted, and what they're likely to buy next.",
        "stats": [("10K+", "Products in our database"), ("30%", "Tech stack data decays yearly"), ("50+", "Sources cross&#8209;referenced")],
    },
    "crm-detection": {
        "subtitle": "Salesforce, HubSpot, Dynamics, Pipedrive, or something else entirely. Knowing your prospect's CRM changes your pitch, your demo, and your competitive positioning.",
        "stats": [("85%", "Detection accuracy"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "website-technology-enrichment": {
        "subtitle": "Every company website leaks technology signals. Analytics scripts, CMS platforms, CDN providers, chatbots. We capture all of it and structure it for your CRM.",
        "stats": [("10K+", "Technologies detected"), ("30%", "Tech data decays yearly"), ("50+", "Sources cross&#8209;referenced")],
    },
    "intent-data-enrichment": {
        "subtitle": "Your TAM is 50,000 accounts. Only 5% are in-market right now. Intent data tells you which ones are actively researching so your team focuses on accounts ready to buy.",
        "stats": [("5%", "Of TAM in&#8209;market at any time"), ("3x", "Higher conversion on intent leads"), ("50+", "Sources cross&#8209;referenced")],
    },
    "buyer-intent-enrichment": {
        "subtitle": "In-market buyers leave digital footprints. Content downloads, comparison searches, review site visits. We match those signals to your accounts so you reach them first.",
        "stats": [("3x", "Higher win rate on intent leads"), ("67%", "Of buyer journey is digital"), ("50+", "Sources cross&#8209;referenced")],
    },
    "buying-signals-enrichment": {
        "subtitle": "Job postings, tech adoptions, leadership changes, funding rounds. Buying signals come from dozens of sources. We consolidate them into your CRM so your team acts on real triggers.",
        "stats": [("27%", "Revenue impacted by bad data"), ("3x", "More pipeline from signal&#8209;based outreach"), ("50+", "Sources cross&#8209;referenced")],
    },
    "job-title-enrichment": {
        "subtitle": "Your CRM has 'Manager' in 4,000 records. Some are Directors. Some are individual contributors. Until you normalize titles, your scoring and routing are broken.",
        "stats": [("91%", "Of CRM data is incomplete"), ("40%", "Of leads misrouted from bad titles"), ("50+", "Sources cross&#8209;referenced")],
    },
    "seniority-enrichment": {
        "subtitle": "C-level, VP, Director, Manager, IC. Clean seniority classification drives lead scoring, routing, and outreach personalization. Without it, you're guessing.",
        "stats": [("50%", "Of rep time on non&#8209;selling tasks"), ("91%", "Of CRM data is incomplete"), ("50+", "Sources cross&#8209;referenced")],
    },
    "department-enrichment": {
        "subtitle": "Sales, marketing, engineering, finance, operations. Knowing which department a contact sits in determines who should reach out and what message to send.",
        "stats": [("91%", "Of CRM data is incomplete"), ("40%", "Of leads misrouted"), ("50+", "Sources cross&#8209;referenced")],
    },
    "decision-maker-enrichment": {
        "subtitle": "Not every VP controls a budget. Not every Director makes purchasing decisions. We identify the actual decision-makers in your target accounts based on title, role, and organizational context.",
        "stats": [("6.8", "Average B2B buying committee size"), ("91%", "Of CRM data is incomplete"), ("50+", "Sources cross&#8209;referenced")],
    },
    "c-suite-enrichment": {
        "subtitle": "C-level executives change roles frequently and are hard to reach. We keep your executive contact records current with verified emails, direct numbers, and career data.",
        "stats": [("18mo", "Average C&#8209;suite tenure"), ("30%", "Executive data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "website-enrichment": {
        "subtitle": "Company websites contain intelligence your CRM never captures. Technologies, team size signals, location data, growth indicators. We extract it all.",
        "stats": [("10K+", "Technologies detected"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "address-enrichment": {
        "subtitle": "Standardize addresses to USPS format, verify deliverability, and fill in missing ZIP+4 codes. Clean addresses mean direct mail that arrives and territories that work.",
        "stats": [("$20B", "Lost to bad address data yearly"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "b2b-data-enrichment": {
        "subtitle": "Contact data, firmographics, technographics, social profiles, and intent signals. Comprehensive B2B enrichment from one vendor, not five separate subscriptions.",
        "stats": [("91%", "Of CRM data is incomplete"), ("$15M", "Avg annual cost of poor data"), ("50+", "Sources cross&#8209;referenced")],
    },
    "lead-enrichment": {
        "subtitle": "A new lead hits your CRM with a name and email. Within seconds, it should have title, company, size, industry, tech stack, and social profiles. That's what real-time lead enrichment does.",
        "stats": [("91%", "Of CRM data is incomplete"), ("5min", "Median lead response time goal"), ("50+", "Sources cross&#8209;referenced")],
    },
    "facebook-profile-enrichment": {
        "subtitle": "Facebook business pages reveal company activity, ad spending, and local business data that LinkedIn misses. We match them to your CRM records.",
        "stats": [("2.9B", "Monthly active Facebook users"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "instagram-profile-enrichment": {
        "subtitle": "200M+ businesses have Instagram accounts. We match business profiles to your contacts for brand activity, content signals, and follower intelligence.",
        "stats": [("200M+", "Business accounts on Instagram"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "twitter-profile-enrichment": {
        "subtitle": "Twitter/X is where B2B buyers share opinions, engage with vendors, and signal purchase intent in public. We match handles to your CRM records.",
        "stats": [("500M+", "Tweets posted daily"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
    "social-media-enrichment": {
        "subtitle": "LinkedIn, Twitter, Facebook, Instagram. Your contacts are active across all of them. We match all four platforms in a single pass and deliver structured social data to your CRM.",
        "stats": [("4+", "Social platforms matched"), ("30%", "B2B data decays annually"), ("50+", "Sources cross&#8209;referenced")],
    },
}

def _enrich_default_faqs(name, group):
    """Generate default FAQs for an enrichment page."""
    base = [
        (f"How long does {name.lower()} take?", f"Most projects complete in 24-48 hours. For databases over 100,000 records, turnaround may extend to 3-5 business days. We'll give you an exact timeline during the free assessment."),
        (f"What's the typical match rate for {name.lower()}?", f"Match rates depend on the completeness of your input data and the specific enrichment type. For well-structured B2B records with company names and domains, expect 60-80% match rates. We run a free sample analysis to show you expected rates before you commit."),
        ZOOMINFO_FAQ,
    ]
    if group == "social":
        base.insert(1, ("Do you scrape private social data?", "No. We match your contacts to public profiles and return publicly accessible data like profile URLs, bios, and account type. We don't access private posts, messages, friend lists, or any data behind privacy settings."))
    elif group == "contact":
        base.insert(1, ("Do you verify every email and phone number?", "Every email address is SMTP-verified to confirm it exists and accepts mail. Phone numbers are validated against carrier databases to confirm they're active. You don't pay for data that bounces or disconnects."))
    elif group == "company":
        base.insert(1, ("How do you handle subsidiaries vs. parent companies?", "We resolve company hierarchies and can match to either the parent or subsidiary level depending on your needs. During the discovery call, we'll agree on which entity level matters for your use case."))
    elif group == "tech":
        base.insert(1, ("How often does technographic data change?", "Tech stacks change frequently. Companies adopt new tools, sunset old ones, and switch vendors regularly. We recommend quarterly re-enrichment for technographic data to keep your records current."))
    elif group == "intent":
        base.insert(1, ("How is intent data different from demographic data?", "Demographic/firmographic data tells you who a company is. Intent data tells you what they're actively researching right now. The combination lets you focus on accounts that fit your ICP and are in-market simultaneously."))
    elif group == "role":
        base.insert(1, ("How do you handle non-standard titles?", "We've built a title normalization taxonomy that maps thousands of variations to standardized categories. 'VP Sales,' 'VP of Sales,' 'Vice President - Sales,' and 'SVP Revenue' all resolve correctly. Edge cases get human review."))
    return base

def _enrich_default_use_cases(name, group):
    """Generate default use cases for an enrichment page."""
    if group == "social":
        return [
            ("Social selling at scale.", f"Pre-load social profiles into your CRM so reps can engage on the right platforms without manual searching. {name} turns every record into a multi-channel outreach opportunity."),
            ("Lead scoring with social signals.", "Add social presence and activity as scoring dimensions. Contacts active across multiple platforms are more reachable and more likely to engage."),
            ("Audience segmentation.", "Segment your database by social platform activity for targeted campaigns. Twitter-active contacts get different messaging than LinkedIn-only contacts."),
            ("Influencer identification.", "Flag contacts with high follower counts or engagement rates for partnership, advocacy, or co-marketing programs."),
            ("Complete contact profiles.", "Give reps a full picture of each contact's social presence before every interaction. Social context makes outreach feel personal."),
        ]
    elif group == "contact":
        return [
            ("Sales prospecting.", f"Give your SDRs complete contact records with verified emails and phone numbers. {name} means every rep works with data they can trust."),
            ("Outbound sequences.", "Populate email and phone sequences with verified contact data. Reduce bounce rates below 3% and connect rates above industry average."),
            ("Lead routing.", "Route inbound leads accurately using enriched contact fields. Complete records get assigned to the right rep instantly."),
            ("Re-engagement campaigns.", "Reach out to dormant contacts with freshly verified data. Re-enrichment recovers contacts you thought were lost."),
            ("Event follow-up.", "Enrich event attendee lists with complete contact data within 24 hours so your team follows up while the conversation is fresh."),
        ]
    elif group == "company":
        return [
            ("Lead scoring accuracy.", f"Score leads by company size, revenue, and industry using verified firmographic data. {name} means your scoring model works on facts, not empty fields."),
            ("Territory planning.", "Assign accounts to territories using accurate HQ locations and company size data. Eliminate overlap and coverage gaps."),
            ("ABM targeting.", "Build target account lists filtered by firmographic attributes that actually match reality. No more campaigns hitting the wrong company profile."),
            ("ICP validation.", "Compare your customer base to your ICP definition using real firmographic data. Find where your ICP matches reality and where it needs updating."),
            ("Pipeline forecasting.", "Weight pipeline by deal size using verified revenue data. Stop forecasting based on rep-entered estimates."),
        ]
    elif group == "classification":
        return [
            ("Reporting accuracy.", f"Generate industry reports that are actually reliable. {name} eliminates the 47 variations of 'Technology' in your database."),
            ("Lead routing by vertical.", "Route leads to industry-specialized reps using standardized codes. A fintech lead goes to your financial services team, not your general tech team."),
            ("Compliance reporting.", "Produce SIC/NAICS reports for regulatory compliance, government contracting, or investor reporting without weeks of manual classification."),
            ("Market sizing.", "Calculate your TAM by industry using standardized codes. Accurate classification means accurate market size estimates."),
            ("Campaign segmentation.", "Build industry-specific campaigns with confidence that your segments actually contain the right accounts."),
        ]
    elif group == "tech":
        return [
            ("Competitive displacement.", f"Identify accounts using competitor products for targeted displacement campaigns. {name} shows you exactly who to go after."),
            ("Integration-led selling.", "Lead with relevant integration stories by knowing what's already in the prospect's stack before the first call."),
            ("Upsell and cross-sell.", "Identify customers who've adopted complementary tools, signaling readiness for additional products from your portfolio."),
            ("Market analysis.", "Map technology adoption across your TAM to identify trends, whitespace, and emerging platforms."),
            ("Product roadmap input.", "Use technology adoption data to prioritize integrations and features based on what your best customers and prospects actually use."),
        ]
    elif group == "intent":
        return [
            ("Pipeline prioritization.", f"Focus your team's time on accounts showing active buying signals. {name} tells you who's in-market right now."),
            ("Timed outreach.", "Reach accounts while they're actively researching. First-mover advantage in B2B is real and measurable."),
            ("Content personalization.", "Tailor outreach to the specific topics a prospect is researching. Intent data tells you their pain before they tell you."),
            ("Ad spend optimization.", "Target your paid campaigns at accounts showing intent signals. Stop wasting ad budget on the 95% of your TAM that isn't buying today."),
            ("Competitive intelligence.", "Know when target accounts are researching your competitors so you can insert yourself into the evaluation early."),
        ]
    elif group == "role":
        return [
            ("Lead routing accuracy.", f"Route leads to the right team based on seniority and department, not free-text title fields. {name} makes your routing rules reliable."),
            ("Lead scoring precision.", "Score leads by verified seniority level instead of keyword matching on messy title fields. C-level contacts score differently than managers."),
            ("ABM committee mapping.", "Identify the full buying committee within target accounts: decision-makers, budget holders, influencers, and technical evaluators."),
            ("Personalized outreach.", "Tailor messaging by seniority and role. An email to a VP of Sales reads differently than one to a Sales Operations Manager."),
            ("Org chart building.", "Construct account org charts from enriched role data to plan multi-threaded engagement strategies."),
        ]
    elif group == "web":
        return [
            ("Direct mail campaigns.", f"Send direct mail that actually arrives. {name} ensures your addresses are current, standardized, and deliverable."),
            ("Territory accuracy.", "Map territories using verified HQ and office locations. Eliminate the routing errors caused by outdated address data."),
            ("Website intelligence.", "Understand each prospect's digital maturity, tech stack, and growth trajectory from their web presence."),
            ("Field sales planning.", "Give field reps accurate office locations for in-person visits. No more showing up at addresses where the company moved out two years ago."),
            ("Event targeting.", "Identify companies within driving distance of your events using verified location data for targeted event promotion."),
        ]
    else:  # broad
        return [
            ("Complete database overhaul.", f"Clean and enrich your entire CRM in one engagement. {name} fills every gap: contacts, firmographics, technographics, social, and role data."),
            ("New CRM setup.", "Starting fresh in a new CRM? We'll clean and enrich your migrated data so you launch with a database your team can trust from day one."),
            ("Quarterly data refresh.", "Data decays at 30% per year. Quarterly re-enrichment keeps your records current and your outreach effective."),
            ("Post-acquisition database merge.", "Combine databases from acquired companies with clean, enriched, deduplicated records. No data loss, no duplicates."),
            ("Go-to-market launch.", "Entering a new market or launching a new product? We'll build and enrich your target account database from scratch."),
        ]

def _enrich_default_comparison(group):
    """Generate default comparison rows for enrichment pages."""
    if group == "social":
        return [
            ("Manual social searching, 3&#8209;5 min per contact", "Batch matching across thousands in 24&#8209;48 hours"),
            ("Data lives in browser tabs and rep notes", "Structured fields in your CRM, filterable and scoreable"),
            ("No confidence indicator on matches", "Confidence scores on every profile match"),
            ("Snapshot goes stale in weeks", "Quarterly re&#8209;enrichment keeps data current"),
            ("Inconsistent coverage across your team", "Every contact enriched to the same standard"),
        ]
    elif group == "contact":
        return [
            ("Reps hunt for contact info manually", "Verified emails and phones pre&#8209;loaded in CRM"),
            ("15&#8209;25% email bounce rate from guessed formats", "Under 3% bounce rate with SMTP verification"),
            ("Incomplete records block sequence enrollment", "Complete records flow into outreach automatically"),
            ("One-time import, stale in months", "Periodic re&#8209;enrichment catches job changes"),
            ("Multiple tools for email, phone, and social", "All contact data from one vendor, one pass"),
        ]
    elif group == "company":
        return [
            ("Empty firmographic fields in your CRM", "Complete company profiles on every account"),
            ("Lead scoring without company context", "Scoring models built on verified firmographics"),
            ("Territory mapping on outdated locations", "Current HQ and office data for accurate routing"),
            ("Manual research on key accounts", "Automated enrichment across your entire database"),
            ("Annual data refresh (maybe)", "Quarterly re&#8209;enrichment keeps data current"),
        ]
    elif group == "classification":
        return [
            ("47 variations of 'Technology' in your CRM", "Standardized SIC/NAICS codes on every account"),
            ("Reporting requires manual cleanup first", "Reports run on clean, consistent industry data"),
            ("Lead routing mismatches on vague labels", "Precise routing based on verified industry codes"),
            ("Segmentation gaps and overlaps", "Clean segments with complete, accurate coverage"),
            ("Weeks of manual classification", "Automated classification with human QA in days"),
        ]
    elif group == "tech":
        return [
            ("Reps ask 'what CRM do you use?' on cold calls", "Tech stack data pre&#8209;loaded before first contact"),
            ("Generic demos with no integration context", "Tailored demos that show relevant integrations"),
            ("No competitive intelligence on install base", "Clear picture of which prospects use competitors"),
            ("Manual website research for tech clues", "Automated detection across 10K+ technologies"),
            ("Point&#8209;in&#8209;time snapshots", "Quarterly refresh catches technology changes"),
        ]
    elif group == "intent":
        return [
            ("Spray outreach across entire TAM", "Focus on the 5% showing active buying signals"),
            ("Same messaging to all prospects", "Outreach tailored to specific research topics"),
            ("Competitors reach in&#8209;market buyers first", "First&#8209;mover advantage on intent&#8209;flagged accounts"),
            ("Cold outreach with no timing signal", "Reach accounts during active research windows"),
            ("Ad budget spread thin across TAM", "Paid campaigns concentrated on in&#8209;market accounts"),
        ]
    elif group == "role":
        return [
            ("Free&#8209;text title field with 10K variations", "Normalized titles mapped to standard taxonomy"),
            ("Routing guesses based on keywords", "Routing rules on verified seniority and department"),
            ("Scoring treats all 'Managers' equally", "Scoring distinguishes Director from IC accurately"),
            ("Manual org chart research per account", "Buying committee mapped automatically"),
            ("Outreach with wrong seniority assumptions", "Messaging matched to actual decision level"),
        ]
    elif group == "web":
        return [
            ("Addresses with typos, missing ZIPs, wrong states", "USPS&#8209;standardized addresses verified for delivery"),
            ("No systematic website intelligence", "Structured web data in your CRM fields"),
            ("Direct mail returned as undeliverable", "Verified addresses that reach the right office"),
            ("Territories drawn on stale location data", "Current addresses for accurate territory mapping"),
            ("Website changes go unnoticed", "Periodic monitoring catches significant changes"),
        ]
    else:  # broad
        return [
            ("5 vendor subscriptions at $15K&#8209;$50K each", "One vendor, one engagement, complete enrichment"),
            ("Data still requires manual cleanup", "Human QA on every project before delivery"),
            ("Each tool covers one data type", "Full&#8209;spectrum: contacts, firms, tech, social, roles"),
            ("Annual contracts with data deletion clauses", "Per&#8209;project pricing, data is yours forever"),
            ("Self&#8209;serve tools that require your team's time", "We do the work, you get the results"),
        ]


def generate_enrichment_pages():
    """Generate all enrichment pages."""
    pages = []
    for slug, display_name, short_desc, group in ENRICHMENT_TYPES:
        path = f"/enrichment/{slug}/"
        if path in SKIP_PAGES:
            print(f"  SKIP (manually enhanced): {path}")
            continue

        custom = _ENRICH_CUSTOM.get(slug, {})
        pain_tmpl = _ENRICH_PAIN[group]
        solution_paras = _ENRICH_SOLUTION[group]

        title = f"{display_name}: {short_desc}"
        if len(title) > 65:
            title = display_name
        meta_desc = short_desc + ". Verum enriches from 50+ sources with human QA. 24-48hr turnaround, no contracts."
        if len(meta_desc) > 155:
            meta_desc = short_desc[:120] + ". 50+ sources, human QA, no contracts."

        subtitle = custom.get("subtitle", f"{short_desc}. Your team needs accurate {display_name.lower().replace(' enrichment','')} data to target, score, and sell effectively. We deliver it in 24-48 hours.")
        stats = custom.get("stats", [("30%", "B2B data decays annually"), ("91%", "Of CRM data is incomplete"), ("50+", "Sources cross&#8209;referenced")])

        lname = display_name.lower()
        pain_paras = [p.replace("{name}", display_name).replace("{lname}", lname) for p in pain_tmpl["paras"]]
        pain_title = pain_tmpl["title"].replace("{name}", display_name)
        sol_paras = [p.replace("{name}", display_name).replace("{lname}", lname) for p in solution_paras]

        faqs = custom.get("faqs", _enrich_default_faqs(display_name, group))
        use_cases = _enrich_default_use_cases(display_name, group)
        comparison = _enrich_default_comparison(group)

        related = [("All Enrichment", "/enrichment/"), ("Enrichment Services", "/services/data-enrichment.html")]
        # Add contextual related links based on group
        if group == "social":
            related.extend([("Contact Enrichment", "/enrichment/contact-enrichment/"), ("LinkedIn Enrichment", "/enrichment/linkedin-profile-enrichment/")])
        elif group == "contact":
            related.extend([("Social Media Enrichment", "/enrichment/social-media-enrichment/"), ("Lead Enrichment", "/enrichment/lead-enrichment/")])
        elif group == "company":
            related.extend([("Technographic Enrichment", "/enrichment/technographic-enrichment/"), ("Industry Classification", "/enrichment/industry-classification-enrichment/")])
        elif group == "classification":
            related.extend([("Company Enrichment", "/enrichment/company-enrichment/"), ("Firmographic Enrichment", "/enrichment/firmographic-enrichment/")])
        elif group == "tech":
            related.extend([("Company Enrichment", "/enrichment/company-enrichment/"), ("Intent Data", "/enrichment/intent-data-enrichment/")])
        elif group == "intent":
            related.extend([("Technographic Enrichment", "/enrichment/technographic-enrichment/"), ("ABM Targeting", "/use-cases/abm-targeting/")])
        elif group == "role":
            related.extend([("Contact Enrichment", "/enrichment/contact-enrichment/"), ("Decision Maker Enrichment", "/enrichment/decision-maker-enrichment/")])
        elif group == "web":
            related.extend([("Company Location", "/enrichment/company-location-enrichment/"), ("Address Enrichment", "/enrichment/address-enrichment/")])
        else:
            related.extend([("Contact Enrichment", "/enrichment/contact-enrichment/"), ("Company Enrichment", "/enrichment/company-enrichment/")])

        breadcrumbs = [("Home", BASE_URL + "/"), ("Data Enrichment", BASE_URL + "/enrichment/"), (display_name, None)]
        svc = service_json(display_name, short_desc + ". 50+ sources, human QA, 24-48hr turnaround.", "Data Enrichment", BASE_URL + path)
        faq_s = faq_schema_json(faqs)

        body = build_body(
            pain_title, pain_paras,
            f"How Verum Handles {display_name}", sol_paras,
            f"What Teams Do With {display_name}", use_cases,
            f" for {lname}",
            f"Why Teams Choose Verum for {display_name}", [
                ("We do the work.", "You don't log into a self-serve platform. Send us your data, we send back enriched records."),
                ("Fast turnaround.", "Most enrichment projects complete in 24-48 hours. Larger datasets may take 3-5 business days."),
                ("Human verification.", "Every project gets human QA. We don't just run your data through an API and hand it back."),
                ("No long-term contracts.", "Per-project pricing. Use us once or set up a recurring schedule. No annual commitments."),
                (f"We understand {lname}.", f"We've enriched millions of records across every data type. Our team knows the edge cases and pitfalls specific to {lname}."),
            ],
            comparison,
            f"Common Questions About {display_name}", faqs,
            "Ready to Enrich Your Data?",
            "<strong>Not sure yet?</strong> Send us a sample file. We'll run a free analysis showing match rates, data gaps, and what enrichment can add. No commitment required.",
            "<strong>Ready to go?</strong> Tell us what you need and we'll have enriched data back to you in 24-48 hours.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, svc, faq_s,
                         display_name, subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")

    return pages


# ============================================================
# CLEANING PAGES
# ============================================================

CLEANING_TYPES = [
    ("data-deduplication", "Data Deduplication", "Remove duplicate records and merge the best data from each", "dedup"),
    ("duplicate-detection", "Duplicate Detection", "Identify and flag duplicate contacts and accounts in your CRM", "dedup"),
    ("record-matching", "Record Matching", "Match and merge records across multiple data sources", "dedup"),
    ("email-validation", "Email Validation", "Verify email addresses are real, deliverable, and safe to send", "email"),
    ("email-verification", "Email Verification", "Check email deliverability and remove invalid addresses", "email"),
    ("data-standardization", "Data Standardization", "Standardize formats across your entire database", "standard"),
    ("data-normalization", "Data Normalization", "Normalize data fields for consistent reporting", "standard"),
    ("phone-formatting", "Phone Formatting", "Standardize phone number formats across regions", "standard"),
    ("address-normalization", "Address Normalization", "Standardize and validate physical address information", "standard"),
    ("name-parsing", "Name Parsing", "Parse and structure name fields correctly", "standard"),
    ("company-name-standardization", "Company Name Standardization", "Standardize company names and legal entities", "standard"),
    ("job-title-normalization", "Job Title Normalization", "Normalize job titles to standard categories for routing and scoring", "standard"),
    ("crm-data-cleaning", "CRM Data Cleaning", "Complete CRM data cleanup and optimization", "database"),
    ("database-cleanup", "Database Cleanup", "Full database cleanup and quality improvement", "database"),
    ("email-list-cleaning", "Email List Cleaning", "Clean email lists for better deliverability and sender reputation", "email"),
    ("contact-list-cleaning", "Contact List Cleaning", "Clean and validate your contact lists end to end", "database"),
    ("data-quality-management", "Data Quality Management", "Ongoing data quality monitoring and improvement", "quality"),
    ("data-hygiene", "Data Hygiene", "Maintain clean, accurate data over time with periodic refresh", "quality"),
    ("data-validation", "Data Validation", "Validate data accuracy and completeness across your CRM", "quality"),
]

_CLEAN_PAIN = {
    "dedup": {
        "title": "The Duplicate Records Problem",
        "paras": [
            "B2B databases have 25% duplicate records on average. That means a quarter of your CRM is noise. Reps call the same prospect twice. Marketing sends the same person three emails. Reports inflate pipeline by counting the same deal under different spellings of the company name.",
            "<h3>Duplicates Erode Trust in Your Data</h3>",
            "When reps encounter duplicate records, they stop trusting the CRM. They build their own spreadsheets. They stop logging activities. The CRM becomes a reporting tool nobody believes in, and your investment in it drops in value every quarter.",
            "<h3>Lead Routing Breaks Down</h3>",
            "Duplicate leads get assigned to different reps. Two people on your team call the same prospect the same week. The prospect is confused, your reps are annoyed, and you look disorganized. D&B found that 27% of revenue is impacted by data quality issues like this.",
            "<h3>Marketing Metrics Become Unreliable</h3>",
            "Duplicates inflate list sizes, skew engagement rates, and make segmentation unreliable. If 20% of your email list is duplicates, your open rate is actually 20% higher than reported because the denominator is wrong. Every metric downstream is distorted.",
            "<h3>Merging Is Harder Than It Looks</h3>",
            "Finding duplicates is only half the problem. Merging them requires deciding which record has the best email, the most recent title, the correct phone number. Manual merge projects take weeks and introduce new errors. Automated dedup without rules loses data.",
        ],
    },
    "email": {
        "title": "The Email Quality Crisis",
        "paras": [
            "Email lists decay at 22.5% per year according to HubSpot. That means nearly a quarter of your email database is invalid right now. You're sending to addresses that bounce, damaging your sender reputation, and wasting every dollar you spend on email marketing.",
            "<h3>Bounce Rates Destroy Sender Reputation</h3>",
            "ISPs watch your bounce rate. Above 2%, you start getting flagged. Above 5%, you're getting throttled. Above 10%, your entire domain may be blacklisted. Once your sender reputation tanks, even your valid emails start landing in spam. Recovery takes months.",
            "<h3>Invalid Emails Waste Campaign Budget</h3>",
            "Every email sent to an invalid address costs you money in platform fees and opportunity cost. If you're running 50,000-record campaigns with a 15% invalid rate, that's 7,500 wasted sends per campaign. Over a year of weekly campaigns, that's hundreds of thousands of wasted sends.",
            "<h3>Catch&#8209;All Domains Hide Problems</h3>",
            "Some domains accept all incoming email regardless of whether the address exists. Your ESP shows them as 'delivered' but nobody reads them. Without catch-all detection, you think your list is clean when 10-15% of your 'delivered' emails hit dead ends.",
            "<h3>Role Addresses and Spam Traps</h3>",
            "info@, sales@, admin@ addresses don't belong in B2B outreach sequences. Neither do recycled spam traps set up by ISPs to catch senders with bad list hygiene. Both lower your deliverability and can get you blacklisted.",
        ],
    },
    "standard": {
        "title": "The Data Standardization Mess",
        "paras": [
            "Your CRM has 'NYC,' 'New York,' 'New York City,' and 'new york' in the same field. Phone numbers appear as (555) 123-4567, 555-123-4567, 5551234567, and +1 555 123 4567. Job titles have thousands of variations for the same role. This inconsistency breaks everything downstream.",
            "<h3>Reporting Requires Manual Cleanup First</h3>",
            "Before you can run a report on 'all contacts in New York,' someone has to identify every variation of New York in your data. This turns a 5-minute report into a 2-hour data project. And next quarter, new variations will have crept in.",
            "<h3>Automation Rules Fail on Inconsistent Data</h3>",
            "Your routing rule says 'if state equals California, assign to West Coast team.' But the field contains 'CA,' 'California,' 'Calif,' and 'Cali.' A quarter of your California leads go to the wrong team because the automation can only match what it's told to look for.",
            "<h3>Integrations Break Silently</h3>",
            "When data flows between your CRM, marketing automation, and BI tools, format inconsistencies cause silent failures. Records that don't match merge rules get skipped. Fields that exceed character limits get truncated. You don't find out until someone notices a gap in a report weeks later.",
            "<h3>Manual Cleanup Is a Recurring Tax</h3>",
            "Every quarter, someone on your team spends days cleaning up data formats. It's tedious, error-prone, and gets undone the moment new records enter the system. Without systematic standardization, you're paying the cleanup tax forever.",
        ],
    },
    "database": {
        "title": "The Database Cleanup You've Been Avoiding",
        "paras": [
            "You know the data is bad. Everyone knows. But the cleanup project keeps getting pushed because it's big, messy, and nobody wants to own it. Meanwhile, every team that touches the CRM is working with data that's 30% decayed, 25% duplicated, and 91% incomplete.",
            "<h3>Ops Teams Spend More Time Fixing Data Than Using It</h3>",
            "Gartner estimates that data quality issues cost organizations an average of $15 million per year. Much of that cost is hidden in the hours your RevOps, Sales Ops, and Marketing Ops teams spend cleaning, reconciling, and patching data instead of driving strategy.",
            "<h3>New Records Inherit Old Problems</h3>",
            "Every new lead that enters your CRM picks up the same problems. Duplicates of existing contacts, inconsistent formats, missing fields. Without a systematic cleanup and ongoing standards, your database gets worse every day.",
            "<h3>CRM Migrations Amplify the Mess</h3>",
            "Moving from one CRM to another without cleaning first just moves the mess to a new system. Duplicate records, inconsistent fields, and incomplete data follow you to the new platform. The migration is an opportunity to clean, but only if you actually do it.",
            "<h3>Nobody Trusts the Data</h3>",
            "When reps and managers don't trust CRM data, they stop using it. Pipeline reviews become arguments about data accuracy instead of strategy discussions. Forecasting becomes fiction. The CRM becomes an expensive spreadsheet nobody believes in.",
        ],
    },
    "quality": {
        "title": "The Data Quality Problem That Gets Worse Every Month",
        "paras": [
            "Data quality isn't a project. It's a condition. Your database is decaying at 30% per year whether you're watching or not. People change jobs. Companies get acquired. Email addresses expire. Phone numbers get reassigned. Without ongoing quality management, today's clean database is next quarter's mess.",
            "<h3>One&#8209;Time Cleanups Don't Last</h3>",
            "You cleaned your database six months ago. Great. Since then, 15% of those records have already decayed. New records entered with missing fields, wrong formats, and duplicate matches. The cleanup bought you a few months of clean data, but the decay never stopped.",
            "<h3>Quality Problems Compound</h3>",
            "A missing email becomes a bounced campaign. A wrong title becomes a misrouted lead. A duplicate becomes a confused prospect. Each individual data error is small. But across 50,000 records, they compound into millions of dollars in lost efficiency and missed revenue.",
            "<h3>You Can't Improve What You Don't Measure</h3>",
            "Most teams can't answer basic questions about their data quality. What percentage of records have valid emails? How many duplicates exist? When was the last time firmographic data was refreshed? Without a quality baseline, you can't set targets or track improvement.",
            "<h3>Reactive Fixes Cost More Than Proactive Maintenance</h3>",
            "Fixing a data problem after it causes a bad customer experience costs 10x more than preventing it. A bounced email to a key prospect is embarrassing. A misrouted enterprise lead that sits for three days is revenue lost. Ongoing quality management prevents these incidents.",
        ],
    },
}

_CLEAN_SOLUTION = {
    "dedup": [
        "We find, flag, and merge duplicate records across your entire database. Our matching algorithm handles spelling variations, abbreviations, and format differences that simple exact-match dedup misses. You choose the merge rules. We execute them at scale.",
        "<h3>Fuzzy Matching That Actually Works</h3>",
        "Exact-match dedup catches 'John Smith' duplicated twice. Fuzzy matching catches 'John Smith' and 'Jon Smith' and 'J. Smith' at the same company. Our algorithms use name, company, email, phone, and address data to identify duplicates that simpler tools miss.",
        "<p><strong>For your team:</strong> We present a dedup report showing every match pair with confidence scores before merging anything. You approve the rules. We execute at scale.</p>",
        "<h3>Smart Merge Logic</h3>",
        "When two duplicate records have conflicting data, which email do you keep? Which phone number? Which title? We use recency, source reliability, and completeness scores to pick the best value for every field. No data loss. No guesswork.",
        "<h3>Human QA on Everything</h3>",
        "Automated dedup catches most duplicates. But edge cases (parent company vs. subsidiary, same person at two companies, shared office addresses) need human judgment. Our team reviews flagged pairs before any merge is executed.",
    ],
    "email": [
        "We validate every email address in your database using SMTP-level verification, syntax checks, domain analysis, and spam trap detection. You get back a clean list with status codes on every address.",
        "<h3>SMTP&#8209;Level Verification</h3>",
        "We connect to the recipient mail server to verify each address exists and can receive mail, without actually sending a message. This catches invalid addresses that syntax checks alone would miss.",
        "<p><strong>For your team:</strong> Every email comes back with a status: valid, invalid, catch-all, disposable, or role-based. You decide which statuses to keep in your campaigns.</p>",
        "<h3>Catch&#8209;All and Disposable Detection</h3>",
        "We flag domains that accept all incoming email (catch-all) and addresses from temporary email services (disposable). These require different handling than verified or clearly invalid addresses.",
        "<h3>Human QA on Everything</h3>",
        "Bulk verification tools produce false negatives on some legitimate enterprise domains. Our team reviews anomalous results, especially for high-value accounts, to prevent incorrectly removing valid addresses.",
    ],
    "standard": [
        "We standardize every field in your database to consistent formats. Phone numbers get normalized. Addresses get USPS-standardized. Titles get mapped to a taxonomy. States, countries, and industries get unified. The result is a database where automation, reporting, and integrations work.",
        "<h3>Field&#8209;by&#8209;Field Standardization</h3>",
        "We don't just run a global find-and-replace. Each field type has specific normalization rules. Phone numbers follow E.164 format. Addresses follow USPS standards. Titles map to a role taxonomy. Every field gets the treatment it needs.",
        "<p><strong>For your team:</strong> After standardization, your routing rules, reporting queries, and integration mappings work correctly without the manual workarounds you've been maintaining.</p>",
        "<h3>Custom Rules for Your Data</h3>",
        "Every database has unique conventions. If your team uses specific title categories, industry labels, or regional conventions, we build custom standardization rules that match your internal standards.",
        "<h3>Human QA on Everything</h3>",
        "Automated standardization handles 90% of cases. The remaining 10% (ambiguous abbreviations, international formats, compound names) get human review to ensure accuracy.",
    ],
    "database": [
        "We handle the entire cleanup: deduplication, email validation, format standardization, missing field enrichment, and quality scoring. One engagement, one vendor, one clean database.",
        "<h3>Full&#8209;Database Assessment</h3>",
        "Before we touch anything, we run a comprehensive quality assessment. Duplicate rate, email validity rate, field completeness, format consistency. You get a clear picture of what needs fixing and what it will cost before committing.",
        "<p><strong>For your team:</strong> The assessment is free and typically completed in 24 hours. It shows you the exact scope of your data quality problems with no obligation.</p>",
        "<h3>Phased Cleanup Approach</h3>",
        "We clean in stages: dedup first (so we're not cleaning duplicates), then validation (so we're working with unique records), then standardization (so formats are consistent), then enrichment (so gaps are filled). Each phase builds on the last.",
        "<h3>Human QA on Everything</h3>",
        "At every stage, our team reviews the results before proceeding. Dedup merge pairs get approval. Validation edge cases get manual checks. Standardization anomalies get human review. Nothing ships without quality verification.",
    ],
    "quality": [
        "We set up ongoing data quality monitoring and periodic cleanup so your database stays clean after the initial project. Monthly or quarterly refresh cycles catch decay before it compounds into bigger problems.",
        "<h3>Quality Scorecards</h3>",
        "We establish baseline quality metrics (completeness, accuracy, consistency, validity) and track them over time. Your team gets a monthly scorecard showing where quality improved and where decay is happening.",
        "<p><strong>For your team:</strong> Quality scorecards turn data quality from an invisible problem into a measurable metric that leadership can track and resource appropriately.</p>",
        "<h3>Automated Decay Detection</h3>",
        "We monitor for signals that records have decayed: email bounces, phone disconnects, title changes, company acquisitions. Records flagged for decay get re-enriched or removed before they cause downstream problems.",
        "<h3>Human QA on Everything</h3>",
        "Automated monitoring catches the obvious decay. But some data problems (a company rebranding, a merger completing, an address changing due to office consolidation) need human judgment. Our team handles the cases algorithms can't.",
    ],
}

def _clean_default_faqs(name, group):
    base = [
        (f"How long does {name.lower()} take?", f"Most projects complete in 24-48 hours for databases under 100,000 records. Larger databases may take 3-5 business days. We'll give you an exact timeline after reviewing your data."),
    ]
    if group == "dedup":
        base.append(("Will merging duplicates lose any data?", "No. Our merge logic preserves the most complete and most recent value for every field. Before any merges execute, you review and approve the merge rules and see a preview of the results."))
        base.append(("Can I review duplicates before they're merged?", "Absolutely. We provide a dedup report showing every match pair with confidence scores. You approve which pairs to merge and which to keep separate. Nothing merges without your approval."))
    elif group == "email":
        base.append(("What's the difference between validation and verification?", "Validation checks the format and syntax of an email address. Verification goes further by connecting to the mail server to confirm the address exists and can receive mail. We do both."))
        base.append(("Will this affect my sender reputation?", "No. Our verification process doesn't send actual emails. We check at the server level whether addresses exist without triggering bounce or complaint signals."))
    elif group == "standard":
        base.append(("Can you standardize to our custom format?", "Yes. If your team has specific conventions for titles, industries, regions, or other fields, we'll build custom standardization rules that match your internal standards."))
        base.append(("Will standardization change the actual data?", "Standardization changes the format, not the meaning. 'NYC' becomes 'New York' and '(555) 123-4567' becomes '+15551234567,' but the underlying data stays the same. We preserve original values in a separate column if you want them."))
    elif group == "database":
        base.append(("Do we need to export our CRM data?", "For most CRMs, yes. You export a CSV or provide API access, and we work with the data file. For Salesforce and HubSpot, we can connect directly if you prefer. We'll discuss the best approach during the discovery call."))
        base.append(("How do we re-import the cleaned data?", "We provide the cleaned data in the same format you gave us (CSV, XLSX, etc.) with clear field mappings. We can also provide import guidance specific to your CRM. Some clients ask us to handle the import directly."))
    else:  # quality
        base.append(("How often should we run quality maintenance?", "Quarterly is the minimum for most teams. Monthly is better if you have high-volume lead inflows or your industry has rapid personnel changes. We'll recommend a cadence based on your decay rate and data volume."))
        base.append(("What metrics do you track?", "Completeness (% of fields populated), accuracy (% of records verified current), consistency (% conforming to format standards), validity (% of emails/phones deliverable), and duplication (% of database that's duplicated). We establish baselines and track trends."))
    base.append(ZOOMINFO_FAQ)
    return base

def _clean_default_use_cases(name, group):
    if group == "dedup":
        return [
            ("CRM accuracy.", f"Remove duplicates before they confuse reps, distort reports, or cause embarrassing double-outreach to prospects."),
            ("Pre-migration cleanup.", "Deduplicate before migrating to a new CRM so you start fresh instead of moving the mess."),
            ("Post-import dedup.", "After importing a purchased list or event leads, deduplicate against your existing database to avoid duplicates."),
            ("Accurate pipeline reporting.", "Eliminate duplicated opportunities and contacts that inflate pipeline numbers and distort forecasting."),
            ("Marketing list hygiene.", "Remove duplicates from email lists so contacts don't receive the same campaign multiple times."),
        ]
    elif group == "email":
        return [
            ("Pre-campaign cleaning.", f"Validate your email list before every campaign to maintain sender reputation and maximize deliverability."),
            ("Sender reputation protection.", "Remove invalid, disposable, and role-based addresses that drag down your deliverability scores."),
            ("Re-engagement campaign prep.", "Validate dormant contact emails before re-engagement campaigns. No point nurturing bounced addresses."),
            ("CRM hygiene.", "Flag invalid emails across your entire CRM so your data team can prioritize re-enrichment for high-value contacts."),
            ("Compliance.", "Verify email consent records against valid addresses. Invalid emails with opt-in records indicate potential data quality issues."),
        ]
    elif group == "standard":
        return [
            ("Reporting accuracy.", f"Run reports on clean, consistent data without spending hours normalizing fields first."),
            ("Automation reliability.", "Make your routing rules, workflows, and integrations work correctly by feeding them standardized data."),
            ("Integration compatibility.", "Ensure data flows cleanly between CRM, marketing automation, BI tools, and other platforms."),
            ("Lead routing precision.", "Route leads correctly by standardizing the fields your routing rules depend on."),
            ("Data migration prep.", "Standardize data before migrating to a new system so you don't import formatting problems."),
        ]
    elif group == "database":
        return [
            ("Full CRM overhaul.", f"Clean everything at once: duplicates, invalid emails, inconsistent formats, and missing data. One project, one vendor."),
            ("Pre-migration prep.", "Clean your database before migrating to a new CRM. Don't pay migration costs to move bad data."),
            ("Quarterly maintenance.", "Schedule regular cleanups to prevent data decay from compounding into a bigger problem."),
            ("Post-acquisition merge.", "Merge databases from acquired companies with proper deduplication, standardization, and enrichment."),
            ("Compliance readiness.", "Clean and organize data to meet audit requirements, GDPR obligations, or SOC 2 expectations."),
        ]
    else:  # quality
        return [
            ("Ongoing data health.", f"Maintain data quality as a continuous process, not a one-time project. Regular monitoring catches problems early."),
            ("Executive reporting.", "Provide leadership with data quality metrics they can track and act on, not just complaints about bad data."),
            ("Revenue operations.", "Give RevOps teams confidence that the data powering their models, forecasts, and automations is accurate."),
            ("Customer experience.", "Prevent bad data from reaching customer-facing interactions. Clean data means fewer embarrassing mistakes."),
            ("Cost reduction.", "Reduce the hidden costs of bad data: wasted campaigns, lost productivity, missed leads, and incorrect forecasting."),
        ]

def _clean_default_comparison(group):
    if group == "dedup":
        return [
            ("Manual dedup, record by record", "Automated fuzzy matching across your entire database"),
            ("Merge logic based on whoever gets there first", "Smart merge rules that preserve the best data"),
            ("Duplicates reappear after every import", "Ongoing dedup catches new duplicates as they enter"),
            ("25% of your database is noise", "Clean, unique records you can trust"),
            ("Reporting inflated by duplicate counts", "Accurate metrics based on deduplicated data"),
        ]
    elif group == "email":
        return [
            ("Send and hope for the best", "Every address SMTP&#8209;verified before send"),
            ("15&#8209;25% bounce rates on cold lists", "Under 3% bounce rate after validation"),
            ("Sender reputation slowly degrading", "Reputation protected by clean list hygiene"),
            ("Catch&#8209;all domains showing false 'delivered'", "Catch&#8209;all detection flags unreliable deliveries"),
            ("Annual email cleanup (maybe)", "Continuous validation on new records, quarterly refresh"),
        ]
    elif group == "standard":
        return [
            ("47 variations of the same state name", "One standardized format across all records"),
            ("Phone numbers in 8 different formats", "E.164 standard format on every number"),
            ("Hours of manual cleanup before reporting", "Reports run instantly on clean, consistent data"),
            ("Integration errors from format mismatches", "Clean data flows between systems without errors"),
            ("New records break existing standards", "Validation rules catch format issues at entry"),
        ]
    elif group == "database":
        return [
            ("One person manually cleaning records", "Full team cleaning your entire database in days"),
            ("Fixing symptoms, not root causes", "Systematic cleanup that addresses every quality dimension"),
            ("Clean data decays within months", "Ongoing maintenance options to prevent re&#8209;decay"),
            ("Multiple tools for different cleanup tasks", "One vendor handles dedup, validation, standardization, and enrichment"),
            ("Nobody trusts the CRM", "A database your team actually believes in"),
        ]
    else:  # quality
        return [
            ("One&#8209;time cleanup, back to messy in 6 months", "Ongoing monitoring catches decay as it happens"),
            ("No visibility into data quality trends", "Monthly scorecards track every quality dimension"),
            ("Reactive: fix problems after they cause damage", "Proactive: prevent problems before they reach your team"),
            ("Quality is ops team's problem alone", "Quality metrics visible to leadership with clear ROI"),
            ("Data hygiene is a project", "Data hygiene is an ongoing program"),
        ]

def generate_cleaning_pages():
    pages = []
    for slug, display_name, short_desc, group in CLEANING_TYPES:
        path = f"/cleaning/{slug}/"
        if path in SKIP_PAGES:
            print(f"  SKIP (manually enhanced): {path}")
            continue

        pain_tmpl = _CLEAN_PAIN[group]
        sol_paras = _CLEAN_SOLUTION[group]
        faqs = _clean_default_faqs(display_name, group)
        use_cases = _clean_default_use_cases(display_name, group)
        comparison = _clean_default_comparison(group)

        title = display_name
        meta_desc = short_desc + ". Human-verified quality. 24-48hr turnaround, no contracts."
        if len(meta_desc) > 155:
            meta_desc = short_desc[:110] + ". Human QA, no contracts."
        subtitle = f"{short_desc}. Bad data costs the average company $15M per year. We fix it in 24-48 hours."
        stats = [("30%", "B2B data decays annually"), ("$15M", "Avg cost of poor data yearly"), ("24&#8209;48hr", "Typical turnaround")]
        if group == "dedup":
            stats = [("25%", "Avg duplicate rate in B2B databases"), ("27%", "Revenue impacted by bad data"), ("24&#8209;48hr", "Typical turnaround")]
        elif group == "email":
            stats = [("22.5%", "Email lists decay per year"), ("2%", "Max bounce rate before ISP flags"), ("24&#8209;48hr", "Typical turnaround")]
        elif group == "quality":
            stats = [("30%", "Data decays annually"), ("$100", "Avg cost per bad CRM record"), ("24&#8209;48hr", "Typical turnaround")]

        related = [("All Cleaning", "/cleaning/"), ("Data Cleaning Services", "/services/data-cleaning.html")]
        if group == "dedup":
            related.extend([("Email Validation", "/cleaning/email-validation/"), ("CRM Cleaning", "/cleaning/crm-data-cleaning/")])
        elif group == "email":
            related.extend([("Data Deduplication", "/cleaning/data-deduplication/"), ("Email Enrichment", "/enrichment/email-enrichment/")])
        elif group == "standard":
            related.extend([("Data Deduplication", "/cleaning/data-deduplication/"), ("Database Cleanup", "/cleaning/database-cleanup/")])
        elif group == "database":
            related.extend([("Data Deduplication", "/cleaning/data-deduplication/"), ("Email Validation", "/cleaning/email-validation/")])
        else:
            related.extend([("CRM Cleaning", "/cleaning/crm-data-cleaning/"), ("Data Validation", "/cleaning/data-validation/")])

        breadcrumbs = [("Home", BASE_URL + "/"), ("Data Cleaning", BASE_URL + "/cleaning/"), (display_name, None)]
        svc = service_json(display_name, short_desc, "Data Cleaning", BASE_URL + path)
        faq_s = faq_schema_json(faqs)

        pain_paras = [p.replace("{name}", display_name) for p in pain_tmpl["paras"]]
        sol_list = [p.replace("{name}", display_name) for p in sol_paras]

        body = build_body(
            pain_tmpl["title"], pain_paras,
            f"How Verum Handles {display_name}", sol_list,
            f"What Teams Do With {display_name}", use_cases,
            f" for {display_name.lower()}",
            f"Why Teams Choose Verum for {display_name}", [
                ("We do the work.", "You don't log into a self-serve tool. Send us your data, we send it back clean."),
                ("Fast turnaround.", "Most cleaning projects complete in 24-48 hours."),
                ("Human verification.", "Every project gets human QA before delivery."),
                ("No long-term contracts.", "Per-project pricing. No annual commitments required."),
                (f"We know {display_name.lower()}.", f"We've cleaned millions of records. Our team handles the edge cases that automated tools get wrong."),
            ],
            comparison,
            f"Common Questions About {display_name}", faqs,
            "Ready to Clean Your Data?",
            "<strong>Not sure yet?</strong> Send us a sample. We'll run a free quality assessment showing duplicates, invalid emails, and format issues. No commitment.",
            "<strong>Ready to go?</strong> We'll have clean data back to you in 24-48 hours.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, svc, faq_s,
                         display_name, subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# USE CASE PAGES
# ============================================================

USE_CASES = [
    ("sales-prospecting", "Sales Prospecting", "Give your sales team accurate data for effective outreach", "sales"),
    ("lead-routing", "Lead Routing", "Route leads accurately based on complete, standardized data", "ops"),
    ("territory-planning", "Territory Planning", "Plan territories with accurate company location and size data", "ops"),
    ("pipeline-management", "Pipeline Management", "Manage pipeline with clean, enriched data you can trust", "sales"),
    ("account-management", "Account Management", "Maintain complete, current account records for retention and growth", "sales"),
    ("abm-targeting", "ABM Targeting", "Target accounts with complete firmographic and technographic data", "marketing"),
    ("marketing-segmentation", "Marketing Segmentation", "Segment audiences with rich, accurate data attributes", "marketing"),
    ("customer-segmentation", "Customer Segmentation", "Segment customers for targeted engagement and retention", "marketing"),
    ("email-marketing-cleanup", "Email Marketing Cleanup", "Clean email lists for better deliverability and engagement", "marketing"),
    ("campaign-targeting", "Campaign Targeting", "Target campaigns with accurate, enriched audience data", "marketing"),
    ("lead-scoring", "Lead Scoring", "Score leads accurately with complete firmographic and behavioral data", "ops"),
    ("lead-qualification", "Lead Qualification", "Qualify leads faster with enriched firmographic context", "ops"),
    ("revenue-intelligence", "Revenue Intelligence", "Power revenue insights with clean, complete data", "analytics"),
    ("data-migration", "Data Migration", "Clean data before migrating to new systems", "ops"),
    ("crm-migration", "CRM Migration", "Prepare data for CRM migrations with proper cleanup", "ops"),
    ("database-merge", "Database Merge", "Merge databases after acquisitions without losing data", "ops"),
    ("data-integration", "Data Integration", "Integrate data across multiple systems cleanly", "ops"),
    ("master-data-management", "Master Data Management", "Maintain a single source of truth across all systems", "ops"),
    ("icp-development", "ICP Development", "Develop your Ideal Customer Profile with real data analysis", "analytics"),
    ("customer-profiling", "Customer Profiling", "Build detailed customer profiles from enriched data", "analytics"),
    ("market-sizing", "Market Sizing", "Size your total addressable market with accurate data", "analytics"),
    ("tam-sam-som-analysis", "TAM SAM SOM Analysis", "Calculate your market opportunity with verified data", "analytics"),
    ("lookalike-modeling", "Lookalike Modeling", "Find lookalike companies matching your best customers", "analytics"),
    ("business-prospecting", "Business Prospecting", "Find and enrich business prospect lists", "sales"),
    ("local-business-lists", "Local Business Lists", "Build targeted local business lists with verified data", "sales"),
    ("smb-targeting", "SMB Targeting", "Target small and medium businesses with accurate contact data", "sales"),
    ("franchise-prospecting", "Franchise Prospecting", "Find franchise owners and franchise business contacts", "sales"),
]

_UC_PAIN = {
    "sales": {
        "title": "The Data Problem Behind Weak {name}",
        "paras": [
            "Your sales team isn't slow because they lack motivation. They're slow because they're working with incomplete, outdated data. Every hour a rep spends hunting for contact info, verifying company details, or cleaning their pipeline is an hour they're not selling.",
            "<h3>Reps Spend 50% of Time on Non&#8209;Selling Activities</h3>",
            "Salesforce research confirms it: the average salesperson spends half their time on tasks other than selling. Data research, record cleanup, manual enrichment. All preventable with clean, enriched CRM data.",
            "<h3>Incomplete Records Block Outreach</h3>",
            "A contact without an email can't enter a sequence. A prospect without a phone can't get called. An account without firmographics can't be scored. Your team isn't ignoring good prospects. They literally can't reach them because the data is missing.",
            "<h3>Stale Data Wastes Everyone's Time</h3>",
            "Your rep calls a number that's been disconnected. Sends an email to someone who left the company last quarter. Shows up to a meeting based on outdated company information. These aren't edge cases. With 30% annual data decay, they're everyday occurrences.",
            "<h3>The Cost Compounds Quickly</h3>",
            "Gartner estimates that poor data costs the average organization $15 million per year. For a sales team of 20, that breaks down to wasted pipeline, lost deals from bad routing, and hours of productivity burned on data problems.",
        ],
    },
    "ops": {
        "title": "The Data Quality Issue Breaking Your {name}",
        "paras": [
            "Operations processes depend on data quality. When the underlying data is wrong, every automated workflow, routing rule, and scoring model built on top of it produces wrong results. You're not fixing an ops problem. You're fixing a data problem.",
            "<h3>Automation Amplifies Bad Data</h3>",
            "When you automate lead routing on dirty data, you route leads to the wrong team faster. When you automate scoring on incomplete data, you prioritize the wrong accounts faster. Automation doesn't fix bad data. It scales the damage.",
            "<h3>Every System Gets Its Own Version of the Truth</h3>",
            "Your CRM says one thing. Your marketing automation says another. Your BI tool shows a third number. Data inconsistency across systems means nobody agrees on pipeline, conversion rates, or customer counts. Meetings become arguments about data instead of strategy discussions.",
            "<h3>Migration and Integration Projects Fail on Bad Data</h3>",
            "40% of business objectives fail due to bad data according to Gartner. CRM migrations, system integrations, and database merges amplify existing quality problems. Dirty data in the source becomes dirty data in the destination, plus new errors from the migration process itself.",
            "<h3>Manual Workarounds Become Permanent</h3>",
            "Your team has spreadsheets that correct CRM data. Manual routing overrides. Escalation processes for misscored leads. These workarounds started as temporary fixes and became permanent infrastructure. They're expensive, error-prone, and invisible to leadership.",
        ],
    },
    "marketing": {
        "title": "Why Your {name} Underperforms",
        "paras": [
            "Marketing campaigns run on data. List quality determines deliverability. Segmentation accuracy determines relevance. Contact completeness determines reach. When the data is bad, campaign performance suffers and nobody can explain why because they're looking at creative and messaging, not the data underneath.",
            "<h3>Deliverability Is a Data Problem</h3>",
            "Email lists decay at 22.5% per year. If your list hasn't been validated recently, 15-20% of your sends are bouncing. That drags down your sender reputation, which puts even your valid emails at risk of landing in spam. The fix isn't a new ESP. It's clean data.",
            "<h3>Segmentation Accuracy Depends on Data Quality</h3>",
            "When 62% of organizations rely on data that's up to 40% inaccurate (Experian), every segmentation decision is compromised. Your 'enterprise segment' includes mid-market companies with wrong employee counts. Your 'healthcare segment' includes health tech companies misclassified in your CRM.",
            "<h3>Personalization Without Data Is Just Mail Merge</h3>",
            "Dynamic content powered by incomplete CRM fields produces 'Hi {FirstName}' emails where the first name is missing, company names are wrong, and industry references don't match. Bad personalization is worse than no personalization because it signals to the recipient that you don't actually know them.",
            "<h3>Attribution Models Break on Dirty Data</h3>",
            "When duplicate records inflate your contact counts, when lead sources are inconsistent, when campaign memberships are misassigned, your attribution model produces numbers nobody trusts. Marketing can't prove ROI because the data behind the model is broken.",
        ],
    },
    "analytics": {
        "title": "Why Your {name} Produces Wrong Answers",
        "paras": [
            "Analysis is only as good as the data feeding it. When your CRM data is 91% incomplete (Salesforce) and 40% inaccurate (Experian), every model, report, and recommendation built on that data is unreliable. You're not making data-driven decisions. You're making bad-data-driven decisions.",
            "<h3>Garbage In, Strategy Out</h3>",
            "Your ICP analysis says your best customers are mid-market SaaS companies. But the employee count data is wrong on 30% of accounts, the industry classification is inconsistent, and 25% of accounts are duplicated. That ICP might be right. Or it might be an artifact of dirty data. You can't tell.",
            "<h3>Market Sizing on Incomplete Data</h3>",
            "Calculating TAM requires accurate firmographic data across your target market. When company revenue estimates vary by 50% between sources, employee counts are missing for a third of accounts, and industry codes are unstandardized, your market size calculation has such wide error bars that it's barely useful.",
            "<h3>Customer Insights Require Customer Data</h3>",
            "Segmentation, CLV analysis, churn prediction, and lookalike modeling all require complete customer records. When your customer database has gaps in firmographics, missing contact data, and inconsistent classifications, every analytical output is compromised.",
            "<h3>Leadership Loses Confidence</h3>",
            "When your analysis consistently conflicts with operational reality, leadership stops trusting the numbers. The board sees a TAM that doesn't match revenue trajectory. The VP of Sales sees lead scores that don't predict close rates. Trust in data-driven decision-making erodes.",
        ],
    },
}

def _uc_use_cases(name, group):
    if group == "sales":
        return [
            ("Complete contact records.", f"Give every rep a database with verified emails, direct dials, and current titles. No more hunting for basic contact information."),
            ("Enriched account context.", "Pre-load company size, revenue, industry, tech stack, and funding data so reps walk into every conversation prepared."),
            ("Real-time lead enrichment.", "Enrich inbound leads within minutes of form submission so your team responds with full context, not just a name and email."),
            ("Pipeline cleanup.", "Remove duplicates, validate contacts, and update stale records across your active pipeline so forecasting reflects reality."),
            ("Ongoing data maintenance.", "Quarterly re-enrichment prevents data decay from degrading your team's effectiveness over time."),
        ]
    elif group == "ops":
        return [
            ("Accurate lead routing.", f"Route leads to the right team based on verified firmographic fields, not free-text entries that match inconsistently."),
            ("Reliable scoring models.", "Build scoring models on clean, complete data so high-score leads actually convert at higher rates."),
            ("Clean system migrations.", "Deduplicate, standardize, and enrich before migrating to ensure you start clean in the new system."),
            ("Integration reliability.", "Standardized data flows between systems without the mapping errors and silent failures caused by inconsistent formats."),
            ("Single source of truth.", "Unified records across CRM, MAP, and BI tools so every team works from the same data."),
        ]
    elif group == "marketing":
        return [
            ("Clean email campaigns.", f"Validate and clean email lists before every send to maintain deliverability above 97%."),
            ("Accurate segmentation.", "Segment on verified firmographic and technographic data instead of incomplete, outdated CRM fields."),
            ("Effective personalization.", "Personalize with data you can trust. Complete records mean dynamic content that actually resonates."),
            ("Attribution accuracy.", "Clean, deduplicated data produces attribution models that marketing can stand behind in board meetings."),
            ("ABM precision.", "Target the right accounts with the right message by building ABM lists on verified data."),
        ]
    else:  # analytics
        return [
            ("Reliable ICP analysis.", f"Build your Ideal Customer Profile on clean, complete data so the analysis reflects reality, not data artifacts."),
            ("Accurate market sizing.", "Calculate TAM, SAM, and SOM with verified firmographic data that produces trustworthy estimates."),
            ("Customer segmentation.", "Segment customers by verified attributes to identify your most valuable cohorts and their shared characteristics."),
            ("Churn prediction.", "Model churn on complete customer records so your predictions are actionable, not noise."),
            ("Board-ready analytics.", "Produce analyses that leadership trusts because the underlying data has been cleaned and verified."),
        ]

def generate_use_case_pages():
    pages = []
    for slug, display_name, short_desc, group in USE_CASES:
        path = f"/use-cases/{slug}/"
        if path in SKIP_PAGES:
            print(f"  SKIP (manually enhanced): {path}")
            continue

        pain_tmpl = _UC_PAIN[group]
        title = display_name
        meta_desc = short_desc + ". Clean, enriched data from 50+ sources. 24-48hr turnaround, no contracts."
        if len(meta_desc) > 155:
            meta_desc = short_desc[:110] + ". 50+ sources, no contracts."
        subtitle = f"{short_desc}. The difference between good and bad {display_name.lower()} is almost always the data underneath it."
        stats = [("30%", "B2B data decays annually"), ("91%", "Of CRM data is incomplete"), ("$15M", "Avg cost of poor data yearly")]
        if group == "sales":
            stats = [("50%", "Of rep time on non&#8209;selling tasks"), ("30%", "B2B data decays annually"), ("27%", "Revenue impacted by bad data")]
        elif group == "marketing":
            stats = [("22.5%", "Email lists decay per year"), ("62%", "Rely on 40%+ inaccurate data"), ("27%", "Revenue impacted by bad data")]
        elif group == "analytics":
            stats = [("91%", "Of CRM data is incomplete"), ("40%", "Of goals fail from bad data"), ("$15M", "Avg cost of poor data yearly")]

        faqs = [
            (f"How does clean data improve {display_name.lower()}?", f"Clean data eliminates the errors, gaps, and inconsistencies that cause {display_name.lower()} to underperform. When your CRM data is accurate and complete, every process built on it works better: routing, scoring, segmentation, outreach, and reporting."),
            (f"How long does it take to see results?", f"Most data projects complete in 24-48 hours. You'll see the impact on your {display_name.lower()} immediately because the underlying data quality improves overnight, not over months."),
            ("Do we need to change our existing tools or processes?", f"No. We clean and enrich the data inside your existing CRM. Your current tools and processes stay the same. They just work better because the data feeding them is better."),
            ZOOMINFO_FAQ,
        ]

        use_cases = _uc_use_cases(display_name, group)
        comparison_rows = [
            ("Working with 91% incomplete CRM data", "Every record enriched from 50+ verified sources"),
            ("30% of data decayed and outdated", "Quarterly refresh keeps records current"),
            ("Manual data research eats selling time", "Pre&#8209;enriched records ready for immediate use"),
            ("Reports nobody trusts", "Analytics built on verified, complete data"),
            ("Multiple tools, same data problems", "One vendor for cleaning, enrichment, and maintenance"),
        ]

        related = [("All Use Cases", "/use-cases/"), ("Data Cleaning", "/services/data-cleaning.html"),
                   ("Data Enrichment", "/services/data-enrichment.html")]
        if group == "sales":
            related.append(("Lead Enrichment", "/enrichment/lead-enrichment/"))
        elif group == "marketing":
            related.append(("Email List Cleaning", "/cleaning/email-list-cleaning/"))
        elif group == "ops":
            related.append(("CRM Data Cleaning", "/cleaning/crm-data-cleaning/"))
        else:
            related.append(("ICP Analysis", "/analysis/icp-analysis/"))

        breadcrumbs = [("Home", BASE_URL + "/"), ("Use Cases", BASE_URL + "/use-cases/"), (display_name, None)]
        svc = service_json(display_name, short_desc, "Data Quality", BASE_URL + path)
        faq_s = faq_schema_json(faqs)

        pain_title = pain_tmpl["title"].replace("{name}", display_name)
        pain_paras = [p.replace("{name}", display_name) for p in pain_tmpl["paras"]]

        sol_paras = [
            f"Clean, enriched data transforms {display_name.lower()} from a struggle into a strength. We handle the cleanup and enrichment so your team focuses on execution, not data problems.",
            "<h3>Complete Records From 50+ Sources</h3>",
            f"We fill in the missing fields that {display_name.lower()} depends on. Emails, phones, titles, company size, industry, tech stack, and social profiles. All verified from 50+ sources and cross-referenced for accuracy.",
            f"<p><strong>For your team:</strong> Instead of working around data gaps, your team works with complete records that make every {display_name.lower()} decision more confident.</p>",
            "<h3>Ongoing Quality Maintenance</h3>",
            "Data decays at 30% per year. We offer quarterly re-enrichment and validation to keep your records current so your processes don't degrade over time.",
            "<h3>Human QA on Everything</h3>",
            "Every project gets human review before delivery. We don't just run your data through APIs. Our team validates edge cases, reviews match quality, and ensures accuracy.",
        ]

        body = build_body(
            pain_title, pain_paras,
            f"How Clean Data Transforms {display_name}", sol_paras,
            f"What You Can Do With Clean Data for {display_name}", use_cases,
            f" for {display_name.lower()}",
            f"Why Teams Choose Verum for {display_name}", [
                ("We do the work.", "Send us your data. We clean, enrich, and return it. You don't manage another tool."),
                ("Fast turnaround.", "24-48 hours for most projects."),
                ("Human verification.", "Every project reviewed by our data team before delivery."),
                ("No long-term contracts.", "Per-project pricing. No annual lock-in."),
                (f"We understand {display_name.lower()}.", f"We've helped dozens of teams improve their {display_name.lower()} through better data. We know what matters."),
            ],
            comparison_rows,
            f"Common Questions About {display_name}", faqs,
            f"Ready to Improve Your {display_name}?",
            "<strong>Not sure yet?</strong> Upload a sample file and we'll run a free data quality assessment. See exactly what we can improve before committing.",
            "<strong>Ready to fix this?</strong> Tell us what you need. Clean data in your CRM within 24-48 hours.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, svc, faq_s,
                         display_name, subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# FIND PAGES - Business discovery
# ============================================================

BUSINESS_FIND = [
    ("healthcare-businesses", "Healthcare Businesses", "healthcare businesses", "Healthcare companies have complex org structures with clinical and administrative decision-makers."),
    ("dental-practices", "Dental Practices", "dental practices", "Dental practices often have owner-operators who handle both clinical and business decisions."),
    ("medical-practices", "Medical Practices", "medical practices", "Medical practices range from solo practitioners to multi-location groups with dedicated management teams."),
    ("mental-health-practices", "Mental Health Practices", "mental health practices", "Mental health providers operate across private practice, group practice, and institutional settings."),
    ("law-firms", "Law Firms", "law firms", "Law firms have partnership structures where decision-making authority varies by practice area and seniority."),
    ("accounting-firms", "Accounting Firms", "accounting firms", "Accounting firms operate on busy season cycles that affect purchasing decisions and available bandwidth."),
    ("real-estate-agencies", "Real Estate Agencies", "real estate agencies", "Real estate agencies have high agent turnover and complex brokerage-agent relationships."),
    ("insurance-agencies", "Insurance Agencies", "insurance agencies", "Insurance agencies range from captive single-carrier shops to independent multi-carrier brokerages."),
    ("financial-advisors", "Financial Advisors", "financial advisors", "Financial advisors operate under RIA, broker-dealer, or hybrid structures that affect their tech and vendor choices."),
    ("marketing-agencies", "Marketing Agencies", "marketing agencies", "Marketing agencies have fast-moving rosters of clients and high staff turnover that makes contact data decay quickly."),
    ("construction-companies", "Construction Companies", "construction companies", "Construction companies operate across GC, specialty, and trade contractor categories with different decision-makers."),
    ("manufacturing-companies", "Manufacturing Companies", "manufacturing companies", "Manufacturing companies have long sales cycles and decisions that involve plant managers, engineers, and procurement."),
    ("restaurants", "Restaurants", "restaurants", "Restaurants have high ownership turnover and often operate under management companies or franchise groups."),
    ("retail-stores", "Retail Stores", "retail stores", "Retail businesses range from single-location independents to multi-location chains with corporate buyers."),
    ("auto-dealerships", "Auto Dealerships", "auto dealerships", "Auto dealerships have dealer principals, GMs, and department heads with distinct purchasing authority."),
    ("business-owner-contact-info", "Business Owner Contact Info", "business owner contacts", "Business owners are the hardest contacts to reach because their data changes when businesses are sold, relocated, or restructured."),
    ("small-business-owners", "Small Business Owners", "small business owners", "Small business owners wear multiple hats and are harder to find in traditional B2B databases that focus on enterprises."),
    ("healthcare-business-owners", "Healthcare Business Owners", "healthcare business owners", "Healthcare practice owners are physicians or allied health professionals who also run businesses."),
    ("dental-practice-owners", "Dental Practice Owners", "dental practice owners", "Dental practice owners are both clinicians and business operators, making them a unique B2B contact type."),
    ("law-firm-partners", "Law Firm Partners", "law firm partners", "Law firm partners control purchasing decisions but are notoriously difficult to reach through standard outreach."),
    ("restaurant-owners", "Restaurant Owners", "restaurant owners", "Restaurant owners turn over frequently and often operate under LLCs that make entity matching difficult."),
    ("retail-store-owners", "Retail Store Owners", "retail store owners", "Retail store owners range from single-location independents to multi-unit operators with management layers."),
    ("franchise-owners", "Franchise Owners", "franchise owners", "Franchise owners operate under brand constraints but make independent decisions about services, supplies, and local vendors."),
    ("agency-owners", "Agency Owners", "agency owners", "Agency owners run lean operations where the founder is often the primary decision-maker and hardest to reach."),
    ("medical-practice-owners", "Medical Practice Owners", "medical practice owners", "Medical practice owners juggle clinical work and business management, making timing and relevance critical for outreach."),
]

def generate_find_pages():
    pages = []
    for slug, display_name, plural, context in BUSINESS_FIND:
        path = f"/find/{slug}/"
        title = f"Find {display_name}"
        meta_desc = f"Build targeted lists of {plural} with verified contact data. Owner names, emails, phone numbers, and company details. 24-48hr turnaround."
        if len(meta_desc) > 155:
            meta_desc = f"Find {plural} with verified contact data. Emails, phones, company details. 24-48hr delivery."
        subtitle = f"{context} We build accurate, verified lists of {plural} with the contact data your team needs to reach the right people."
        stats = [("30%", "B2B data decays annually"), ("91%", "Of CRM data is incomplete"), ("50+", "Sources cross&#8209;referenced")]

        faqs = [
            (f"How do you build {plural} lists?", f"We compile data from business registrations, professional directories, verified databases, and public records. Every record is cross-referenced across 50+ sources and validated before delivery. You get accurate, current data, not a scraped list from 2023."),
            (f"What data do I get for each {plural.rstrip('s') if plural.endswith('s') else plural} record?", f"Business name, address, phone, owner/operator name, owner email, owner phone, website, and available firmographic data (employee count, revenue range, years in business). Exact fields depend on data availability for each record."),
            ("Can you filter by geography, size, or specialty?", "Yes. We can build lists filtered by state, city, metro area, employee count, revenue range, specialty, and other criteria. Tell us your targeting requirements during the discovery call."),
            ZOOMINFO_FAQ,
        ]

        use_cases = [
            ("Sales prospecting.", f"Build targeted lists of {plural} for outbound sales campaigns with verified contact data that reaches the right decision-makers."),
            ("Direct mail campaigns.", f"Reach {plural} through direct mail with verified physical addresses. Clean address data means higher delivery rates."),
            ("Local market expansion.", f"Enter new markets with a complete list of {plural} in your target geography. Know the landscape before you deploy resources."),
            ("Partnership development.", f"Identify potential partners among {plural} with complete contact data for outreach to owners and operators."),
            ("Market research.", f"Understand the {plural} landscape in any market with firmographic data on every business in the segment."),
        ]

        comparison_rows = [
            ("Buy a stale list from a list broker", "Custom&#8209;built list verified from 50+ current sources"),
            ("20&#8209;30% of contacts are outdated", "Every record validated before delivery"),
            ("Generic business data, no owner contacts", "Owner names, direct emails, and phone numbers"),
            ("One&#8209;time purchase, no updates", "Re&#8209;enrichment available as data decays"),
            ("Same list your competitors already bought", "Custom list built to your specific targeting criteria"),
        ]

        related = [("All Find", "/find/"), ("Contact Enrichment", "/enrichment/contact-enrichment/"),
                   ("Sales Prospecting", "/use-cases/sales-prospecting/"), ("Local Business Lists", "/use-cases/local-business-lists/")]

        breadcrumbs = [("Home", BASE_URL + "/"), ("Find", BASE_URL + "/find/"), (display_name, None)]
        svc = service_json(f"Find {display_name}", f"Build targeted lists of {plural} with verified contact data", "List Building", BASE_URL + path)
        faq_s = faq_schema_json(faqs)

        pain_paras = [
            f"Building a targeted list of {plural} sounds simple until you try it. Business directories are outdated. Purchased lists are stale. LinkedIn shows you names but not emails or direct phone numbers. Your team spends hours on manual research and still ends up with incomplete, unreliable data.",
            "<h3>Purchased Lists Are Already Stale</h3>",
            f"List brokers sell the same {plural} data to everyone. By the time you get it, 20-30% of the records have already decayed. Owners have changed, businesses have closed, phone numbers have been reassigned. You're paying for data your competitors already have, and it's already going bad.",
            "<h3>Online Directories Miss the Details That Matter</h3>",
            f"Google, Yelp, and industry directories give you business names and addresses. They don't give you owner names, direct email addresses, or mobile numbers. The data that actually gets you a meeting, the owner's direct contact info, requires deeper sourcing.",
            "<h3>Manual Research Doesn't Scale</h3>",
            f"Your reps can research 10-15 {plural} per hour manually. At that rate, building a list of 500 takes a full work week. That's a week of selling time burned on data work that should've been handled in 24 hours.",
            "<h3>Data Decays Before You Use It</h3>",
            f"{context} Contact data for {plural} decays at 30% per year. The list you built in January is already losing value by March. Without periodic refresh, your prospecting data gets worse every quarter.",
        ]

        sol_paras = [
            f"We build custom lists of {plural} from 50+ verified sources. Every record includes the contact data your team needs: owner names, business emails, direct phone numbers, and company details. All verified before delivery.",
            "<h3>Multi&#8209;Source List Building</h3>",
            f"We don't scrape one directory and call it done. We cross-reference business registrations, professional licensing databases, verified directories, and public records to build the most complete and accurate list of {plural} available.",
            f"<p><strong>For your team:</strong> You get a list built to your exact targeting criteria with data quality that exceeds any off-the-shelf purchased list.</p>",
            "<h3>Owner and Decision&#8209;Maker Focus</h3>",
            f"We don't just find {plural}. We find the people who make decisions at those businesses. Owner names, direct emails, and phone numbers that reach the actual decision-maker, not a receptionist.",
            "<h3>Human QA on Everything</h3>",
            f"Every list goes through human review before delivery. We verify business operating status, validate contact data accuracy, and flag records that need attention.",
        ]

        body = build_body(
            f"The Challenge of Finding {display_name} Data", pain_paras,
            f"How Verum Builds {display_name} Lists", sol_paras,
            f"What Teams Do With {display_name} Data", use_cases,
            f" for {plural}",
            f"Why Teams Choose Verum for {display_name} Lists", [
                ("We do the work.", "Tell us your targeting criteria. We build and verify the list. You focus on selling."),
                ("Fast turnaround.", "Most lists delivered in 24-48 hours. Larger projects may take 3-5 business days."),
                ("Human verification.", "Every record validated by our team before delivery."),
                ("No long-term contracts.", "Per-project pricing. Order one list or set up recurring builds."),
                (f"We know {plural}.", f"{context} Our team understands the data landscape and knows where to find accurate information."),
            ],
            comparison_rows,
            f"Common Questions About Finding {display_name}", faqs,
            f"Ready to Build Your {display_name} List?",
            "<strong>Not sure yet?</strong> Tell us your target market and we'll estimate list size and data coverage. Free, no commitment.",
            "<strong>Ready to go?</strong> We'll have your verified list ready in 24-48 hours.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, svc, faq_s,
                         f"Find {display_name}", subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# ANALYSIS PAGES
# ============================================================

ANALYSIS_TYPES = [
    ("icp-analysis", "ICP Analysis", "Build your Ideal Customer Profile from real customer data", "icp"),
    ("ideal-customer-profile", "Ideal Customer Profile", "Define and refine your ideal customer with data analysis", "icp"),
    ("customer-segmentation", "Customer Segmentation Analysis", "Segment your customers by verified attributes for targeted strategy", "segment"),
    ("market-analysis", "Market Analysis", "Analyze your market opportunity with accurate firmographic data", "market"),
    ("competitor-analysis", "Competitor Analysis", "Understand your competitive landscape through data intelligence", "market"),
    ("win-loss-analysis", "Win-Loss Analysis", "Analyze won and lost deals to find patterns in your data", "performance"),
    ("churn-analysis", "Churn Analysis", "Identify churn patterns and prevention opportunities from your data", "performance"),
    ("customer-lifetime-value", "Customer Lifetime Value", "Calculate and optimize CLV with complete customer data", "performance"),
    ("lead-scoring-model", "Lead Scoring Model", "Build data-driven lead scoring on clean, enriched data", "scoring"),
    ("icp-analysis-for-startups", "ICP Analysis for Startups", "Define your ICP before you scale with data, not assumptions", "icp"),
    ("icp-analysis-for-saas", "ICP Analysis for SaaS", "SaaS-specific ICP development using product and revenue data", "icp"),
    ("icp-analysis-for-series-a", "ICP Analysis for Series A", "Pre-Series A ICP definition to focus your go-to-market", "icp"),
    ("cmo-data-analysis", "CMO Data Analysis", "Marketing analytics for CMOs built on clean, trustworthy data", "executive"),
    ("sales-data-analysis", "Sales Data Analysis", "Sales performance analytics on verified pipeline data", "executive"),
    ("revenue-analysis", "Revenue Analysis", "Revenue trends and forecasting on accurate financial data", "executive"),
    ("healthcare-market-analysis", "Healthcare Market Analysis", "Healthcare industry market sizing and opportunity analysis", "market"),
    ("fintech-market-analysis", "Fintech Market Analysis", "Fintech industry market sizing and competitive landscape", "market"),
    ("saas-market-analysis", "SaaS Market Analysis", "SaaS market sizing, benchmarking, and opportunity analysis", "market"),
    ("ecommerce-market-analysis", "E-commerce Market Analysis", "E-commerce market sizing and competitive analysis", "market"),
]

def generate_analysis_pages():
    pages = []
    for slug, display_name, short_desc, group in ANALYSIS_TYPES:
        path = f"/analysis/{slug}/"
        title = display_name
        meta_desc = short_desc + ". Clean data in, accurate insights out. 24-48hr turnaround."
        if len(meta_desc) > 155:
            meta_desc = short_desc[:120] + ". Accurate data, real insights."
        subtitle = f"{short_desc}. Analysis built on dirty data produces conclusions you can't trust. We clean the data first, then deliver insights you can act on."
        stats = [("91%", "Of CRM data is incomplete"), ("40%", "Of goals fail from bad data"), ("$15M", "Avg cost of poor data yearly")]

        faqs = [
            (f"What data do I need to provide for {display_name.lower()}?", f"Typically your CRM export (contacts and accounts), closed-won and closed-lost deal data, and any product usage data you have. We'll tell you exactly what we need during the discovery call. More data means better analysis, but we can work with what you have."),
            (f"How is this different from hiring an analyst?", f"We combine data cleaning with analysis. Most analysts spend 80% of their time cleaning data before they can analyze it. We handle the cleaning and enrichment automatically, then focus our analysis time on insights and recommendations."),
            ("How long does the analysis take?", f"Data cleaning takes 24-48 hours. Analysis depends on scope, but most {display_name.lower()} projects complete within 1-2 weeks including data preparation, analysis, and delivery of recommendations."),
            ZOOMINFO_FAQ,
        ]

        use_cases_items = [
            ("Data-driven strategy.", f"Replace assumptions with evidence. {display_name} on clean data gives you confidence that your strategy targets the right market."),
            ("Board-ready deliverables.", "Analysis that leadership trusts because the underlying data has been verified and cleaned."),
            ("Go-to-market focus.", "Know exactly which segments, verticals, and company profiles to prioritize based on actual performance data."),
            ("Resource allocation.", "Allocate sales, marketing, and product resources to the segments with the highest demonstrated ROI."),
            ("Competitive positioning.", "Understand where you win, where you lose, and why, based on data patterns rather than anecdotes."),
        ]

        comparison_rows = [
            ("Analysis on dirty CRM data", "Analysis on cleaned, enriched data"),
            ("80% of analyst time spent cleaning", "Data arrives pre&#8209;cleaned, analyst focuses on insights"),
            ("Conclusions nobody trusts", "Results backed by verified, complete data"),
            ("Static report, outdated in months", "Refreshable analysis with updated data"),
            ("DIY with spreadsheets", "Professional analysis with clear methodology"),
        ]

        related = [("All Analysis", "/analysis/"), ("ICP Development", "/use-cases/icp-development/"),
                   ("Data Enrichment", "/services/data-enrichment.html"), ("Data Cleaning", "/services/data-cleaning.html")]

        breadcrumbs = [("Home", BASE_URL + "/"), ("Analysis", BASE_URL + "/analysis/"), (display_name, None)]
        svc = service_json(display_name, short_desc, "Data Analysis", BASE_URL + path)
        faq_s = faq_schema_json(faqs)

        pain_paras = [
            f"Most {display_name.lower()} fails before it starts. Not because the methodology is wrong, but because the data is bad. 91% of CRM data is incomplete. 62% of organizations rely on data that's up to 40% inaccurate. Every model and conclusion built on that foundation is compromised.",
            "<h3>Dirty Data Produces Wrong Answers</h3>",
            f"Your {display_name.lower()} says mid-market SaaS is your best segment. But the employee counts driving that conclusion are wrong on 30% of accounts. The industry classifications are inconsistent. 25% of your customer records are duplicates inflating the pattern. Is the conclusion right? Maybe. Can you bet your strategy on it? Not confidently.",
            "<h3>Analysts Spend 80% of Time Cleaning</h3>",
            "Data scientists report spending 80% of their time on data preparation and cleaning. That means your expensive analysis project is mostly janitorial work. The actual analysis, the part that generates insight, gets compressed into the remaining 20% of effort.",
            "<h3>Incomplete Records Create Blind Spots</h3>",
            f"If 40% of your customer records are missing firmographic data, your {display_name.lower()} has a 40% blind spot. Patterns that appear significant may just reflect which records happened to have complete data. Real patterns get masked by data gaps.",
            "<h3>Stale Data Reflects Yesterday's Market</h3>",
            "Analysis based on data that's 12-18 months old reflects a market that no longer exists. Companies have grown, been acquired, pivoted, or closed. Your analysis needs current data to produce current insights.",
        ]

        sol_paras = [
            f"We clean and enrich your data first, then perform the analysis. This means your {display_name.lower()} runs on complete, accurate, current data, not the 91% incomplete CRM export you started with.",
            "<h3>Data Preparation Included</h3>",
            "We deduplicate records, validate emails, standardize industry codes, enrich missing firmographics, and normalize titles before any analysis begins. The data cleaning is included, not an extra charge.",
            f"<p><strong>For your team:</strong> You get analysis results you can trust because the foundation was verified first. No asterisks about data quality caveats.</p>",
            "<h3>Actionable Recommendations</h3>",
            f"Our {display_name.lower()} doesn't end with a data dump. You get specific, actionable recommendations for targeting, messaging, resource allocation, and strategy that your team can execute immediately.",
            "<h3>Human QA on Everything</h3>",
            "Both the data cleaning and the analysis get human review. Our team validates data quality before analysis begins and reviews analytical conclusions for accuracy before delivery.",
        ]

        body = build_body(
            f"Why Most {display_name} Produces Wrong Answers", pain_paras,
            f"How Verum Delivers Reliable {display_name}", sol_paras,
            f"What You Get From {display_name}", use_cases_items,
            f" for {display_name.lower()}",
            f"Why Teams Choose Verum for {display_name}", [
                ("We clean the data first.", "Most analysts skip this. We don't. Your analysis runs on verified, enriched data."),
                ("Actionable output.", "Not just charts and tables. Specific recommendations your team can execute."),
                ("Fast delivery.", "Data cleaning in 24-48 hours. Analysis complete within 1-2 weeks."),
                ("No long-term contracts.", "Per-project pricing. Get the analysis you need without annual commitments."),
                ("Domain expertise.", f"We've done hundreds of {display_name.lower()} projects across industries. We know what works and what doesn't."),
            ],
            comparison_rows,
            f"Common Questions About {display_name}", faqs,
            f"Ready to Get Reliable {display_name}?",
            "<strong>Not sure yet?</strong> Send us a sample of your data. We'll run a free quality assessment so you can see what needs cleaning before analysis.",
            f"<strong>Ready to go?</strong> Tell us your {display_name.lower()} goals and we'll scope the project within 24 hours.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, svc, faq_s,
                         display_name, subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# ALTERNATIVES PAGES
# ============================================================

ALTERNATIVES = [
    ("zoominfo-alternative", "ZoomInfo", "$15K-$50K+/year for a database you have to clean yourself. Verum cleans your existing data for a fraction of the cost.", "15K&#8209;$50K+", "database access with usage caps"),
    ("clearbit-alternative", "Clearbit", "Clearbit enriches in real-time but leaves the cleanup to you. Verum handles both enrichment and quality.", "$12K&#8209;$36K+", "API-based enrichment with rate limits"),
    ("apollo-alternative", "Apollo", "Apollo gives you a big database. Verum gives you a clean one. Different problems, different approaches.", "$5K&#8209;$24K+", "prospecting platform with email sequences"),
    ("lusha-alternative", "Lusha", "Lusha finds contact data one record at a time. Verum enriches your entire database in batch with human QA.", "$3K&#8209;$12K+", "browser extension with credit-based pricing"),
    ("cognism-alternative", "Cognism", "Cognism sells European B2B data. Verum cleans and enriches data globally with 50+ sources and human verification.", "$20K&#8209;$60K+", "European-focused B2B data with GDPR compliance"),
    ("seamless-ai-alternative", "Seamless.AI", "Seamless.AI searches for contacts in real-time. Verum enriches and cleans your existing database in batch.", "$5K&#8209;$15K+", "real-time contact search with AI matching"),
    ("rocketreach-alternative", "RocketReach", "RocketReach is self-serve contact lookup. Verum is done-for-you enrichment and cleaning at scale.", "$3K&#8209;$12K+", "contact lookup with email and phone"),
    ("uplead-alternative", "UpLead", "UpLead offers pay-per-contact data. Verum cleans and enriches your entire CRM without per-record limitations.", "$1K&#8209;$6K+", "pay-per-contact B2B database"),
    ("lead411-alternative", "Lead411", "Lead411 provides trigger-based leads. Verum cleans your existing data and enriches it for better outreach.", "$5K&#8209;$12K+", "trigger-based sales intelligence"),
    ("salesintel-alternative", "SalesIntel", "SalesIntel offers human-verified contacts. Verum goes further by cleaning, enriching, and deduplicating your entire database.", "$10K&#8209;$30K+", "human-verified B2B contact data"),
    ("6sense-alternative", "6sense", "6sense focuses on intent data and ABM orchestration. Verum focuses on making your underlying data clean and complete.", "$30K&#8209;$100K+", "intent data and ABM platform"),
    ("demandbase-alternative", "Demandbase", "Demandbase is an ABM platform. Verum is data quality. They're complementary, but if your data is bad, the ABM won't work.", "$25K&#8209;$80K+", "ABM platform with intent and advertising"),
    ("hunter-alternative", "Hunter", "Hunter finds emails by domain. Verum enriches complete contact records from 50+ sources with human QA.", "$600&#8209;$6K+", "email finder with domain search"),
    ("kaspr-alternative", "Kaspr", "Kaspr pulls LinkedIn data via browser extension. Verum enriches your entire CRM in batch without manual clicking.", "$600&#8209;$3K+", "LinkedIn data extraction tool"),
    ("adapt-alternative", "Adapt", "Adapt provides industry-specific B2B data. Verum cleans and enriches data across all industries from 50+ sources.", "$3K&#8209;$12K+", "industry-focused B2B data"),
]

def generate_alternative_pages():
    pages = []
    for slug, competitor, tagline, price_range, product_desc in ALTERNATIVES:
        path = f"/alternatives/{slug}/"
        title = f"Best {competitor} Alternative for B2B Data"
        meta_desc = f"Looking for a {competitor} alternative? Verum enriches from 50+ sources with human QA. Per-project pricing, no annual contracts."
        if len(meta_desc) > 155:
            meta_desc = f"{competitor} alternative: Verum enriches from 50+ sources with human QA. No contracts."
        subtitle = tagline
        stats = [("50+", "Data sources"), ("93%", "Deliverability guarantee"), ("24&#8209;48hr", "Typical turnaround")]

        faqs = [
            (f"Why switch from {competitor}?", f"If you're tired of self-serve tools that still require your team's time to clean and validate data, Verum is a different approach. We do the work. You send us data, we send it back clean and enriched. No platform to manage, no credits to monitor."),
            (f"How does Verum's pricing compare to {competitor}?", f"{competitor} typically costs {price_range}/year for {product_desc}. Verum charges per project with no annual commitment. You pay for what you need, when you need it. Most projects cost a fraction of an annual {competitor} subscription."),
            (f"Can I use Verum alongside {competitor}?", f"Yes. Many teams use Verum to clean and enrich data they've sourced from {competitor} or other tools. We're complementary to prospecting platforms. We make the data better regardless of where it came from."),
            ZOOMINFO_FAQ,
        ]

        use_cases = [
            ("Data you already have.", f"{competitor} helps you find new contacts. Verum makes your existing data accurate and complete. Different problems."),
            ("Human QA included.", f"With {competitor}, data quality is your problem. With Verum, every record gets human verification before delivery."),
            ("No annual contracts.", f"{competitor} locks you into annual contracts at {price_range}. Verum is per-project. Use us once or set up recurring work."),
            ("Full-service, not self-serve.", f"{competitor} gives you a platform and expects your team to do the work. Verum does the work for you."),
            ("You own the data.", f"Cancel {competitor} and you lose access to data you've been paying for. Verum data is yours forever."),
        ]

        comparison_rows = [
            (f"{competitor}: {price_range}/year subscription", "Verum: per&#8209;project pricing, no minimums"),
            (f"{competitor}: self-serve platform", "Verum: done&#8209;for&#8209;you service"),
            (f"{competitor}: data quality is your problem", "Verum: human QA on every project"),
            (f"{competitor}: annual contract required", "Verum: no contracts, no commitments"),
            (f"{competitor}: lose access when you cancel", "Verum: data is yours forever"),
        ]

        related = [("All Alternatives", "/alternatives/"), ("Data Enrichment", "/services/data-enrichment.html"),
                   ("Data Cleaning", "/services/data-cleaning.html"), ("Compare", "/compare/")]

        breadcrumbs = [("Home", BASE_URL + "/"), ("Alternatives", BASE_URL + "/alternatives/"), (f"{competitor} Alternative", None)]
        svc = ""
        faq_s = faq_schema_json(faqs)

        pain_paras = [
            f"You've been paying {price_range}/year for {competitor}. The database is big. The interface is fine. But your CRM data is still a mess. Duplicates, outdated titles, bouncing emails, missing firmographics. {competitor} gives you access to data. It doesn't clean the data you already have.",
            f"<h3>{competitor} Solves a Different Problem</h3>",
            f"{competitor} is {product_desc}. That's useful for prospecting. But it doesn't deduplicate your CRM, validate your existing emails, standardize your fields, or fill in missing firmographic data on your current accounts. Those are the problems that actually drive data quality, and they're the problems Verum solves.",
            "<h3>Self&#8209;Serve Tools Still Require Your Time</h3>",
            f"With {competitor}, your team logs in, searches, exports, imports, deduplicates, and validates. You're paying for a platform but still doing the work. If your ops team is already stretched thin, adding another self-serve tool doesn't help. It adds another workflow to manage.",
            "<h3>Annual Contracts Lock You In</h3>",
            f"{competitor} typically requires annual contracts at {price_range}. If your needs change, your budget shifts, or the tool isn't delivering expected value, you're still on the hook. Verum charges per project. Use us when you need us. Stop when you don't.",
            "<h3>Data Deletion on Cancellation</h3>",
            f"Most data platforms, including {competitor}, require you to delete sourced data when your subscription ends. That means the contacts and accounts you've been enriching your CRM with may need to be removed. With Verum, enriched data is yours permanently. No deletion clauses.",
        ]

        sol_paras = [
            f"Verum is a fundamentally different approach to B2B data. Instead of giving you a platform to search and self-serve, we handle the entire data quality process. You send us your CRM data. We clean, enrich, validate, and return it. Done.",
            "<h3>Done&#8209;For&#8209;You Service</h3>",
            f"You don't need another login, another dashboard, or another tool to manage. Send us a file (or give us API access to your CRM) and we handle everything: deduplication, email validation, firmographic enrichment, title normalization, and quality scoring.",
            "<p><strong>The difference:</strong> Your team spends zero hours on data cleanup. Zero hours on platform management. Zero hours on export/import cycles.</p>",
            "<h3>50+ Sources, Not One Database</h3>",
            f"{competitor} has one database. Verum cross-references 50+ sources for every record. More sources means higher match rates, more accurate data, and fewer gaps.",
            "<h3>Human QA on Everything</h3>",
            f"With {competitor}, data quality is your team's responsibility. With Verum, every project gets human review before delivery. Our team catches the edge cases, false matches, and data anomalies that automation misses.",
        ]

        body = build_body(
            f"Why Teams Look for {competitor} Alternatives", pain_paras,
            f"How Verum Compares to {competitor}", sol_paras,
            f"What Makes Verum Different from {competitor}", use_cases,
            "",
            f"Why Teams Switch from {competitor} to Verum", [
                ("We do the work.", "No self-serve platform to manage. Send data, get results."),
                ("Per-project pricing.", f"No {price_range}/year commitment. Pay for what you need."),
                ("Human verification.", "Every record reviewed before delivery."),
                ("Data ownership.", "Enriched data is yours forever. No deletion on cancellation."),
                ("50+ sources.", f"More sources than {competitor}'s single database for higher match rates."),
            ],
            comparison_rows,
            f"Common Questions About Switching from {competitor}", faqs,
            f"Ready to Try a {competitor} Alternative?",
            "<strong>Not sure yet?</strong> Send us a sample of your CRM data. We'll run a free assessment showing what we can clean and enrich. Compare the results to what you're getting now.",
            f"<strong>Ready to switch?</strong> First project completes in 24-48 hours. No contracts, no commitment.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, "", faq_s,
                         f"{competitor} Alternative", subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# COMPARISON PAGES
# ============================================================

COMPARISONS = [
    ("verum-vs-zoominfo", "ZoomInfo", "$15K-$50K+/year", "the largest B2B contact database", "150M+ contacts"),
    ("verum-vs-clearbit", "Clearbit", "$12K-$36K+/year", "real-time API enrichment", "real-time enrichment via API"),
    ("verum-vs-apollo", "Apollo", "$5K-$24K+/year", "prospecting and engagement platform", "email sequences plus contact data"),
    ("verum-vs-lusha", "Lusha", "$3K-$12K+/year", "browser extension for contact lookup", "credit-based contact lookup"),
    ("verum-vs-cognism", "Cognism", "$20K-$60K+/year", "European-focused B2B data", "GDPR-compliant European data"),
]

def generate_comparison_pages():
    pages = []
    for slug, competitor, price, desc, feature in COMPARISONS:
        path = f"/compare/{slug}/"
        title = f"Verum vs {competitor}: Which Is Right for You?"
        meta_desc = f"Compare Verum vs {competitor} for B2B data. Different approaches, different pricing, different ownership. See which fits your needs."
        if len(meta_desc) > 155:
            meta_desc = f"Verum vs {competitor}: compare pricing, data quality, ownership. Find the right fit."
        subtitle = f"{competitor} is {desc}. Verum is done-for-you data cleaning and enrichment. They solve different problems, and understanding the difference saves you from buying the wrong solution."
        stats = [("50+", "Verum data sources"), ("93%", "Deliverability guarantee"), ("24&#8209;48hr", "Typical turnaround")]

        faqs = [
            (f"Is Verum better than {competitor}?", f"They solve different problems. {competitor} provides {feature}. Verum cleans, enriches, and maintains your existing CRM data. If your CRM data is already clean and you need net-new contacts, {competitor} might be the right choice. If your existing data is messy and incomplete, Verum solves that."),
            (f"Can I use Verum and {competitor} together?", f"Yes. Many teams use {competitor} for prospecting and Verum for data quality. {competitor} helps you find new contacts. Verum makes sure all your data, including {competitor}-sourced records, is clean, accurate, and enriched."),
            (f"How does pricing compare?", f"{competitor} costs {price} with annual contracts. Verum charges per project with no annual commitment. A typical Verum project costs a fraction of a {competitor} annual subscription."),
            ZOOMINFO_FAQ,
        ]

        use_cases = [
            (f"{competitor} for net-new prospecting.", f"{competitor} excels at finding new contacts you don't have. If you need to build lists from scratch, {competitor} does that well."),
            ("Verum for existing data quality.", "Verum excels at cleaning, enriching, and maintaining the data you already have. If your CRM is messy, Verum fixes it."),
            ("Use both together.", f"Many teams source contacts from {competitor} and then clean and enrich them with Verum. The tools are complementary."),
            ("Verum for cost-conscious teams.", f"If {price}/year is too much for your current stage, Verum's per-project pricing lets you get data quality work done without a large annual commitment."),
            ("Verum for data ownership.", f"{competitor} requires data deletion on cancellation. Verum data is yours forever. If ownership matters, Verum is the better choice."),
        ]

        comparison_rows = [
            (f"{competitor}: {price}/year subscription", "Verum: per&#8209;project, no annual commitment"),
            (f"{competitor}: self-serve platform", "Verum: done&#8209;for&#8209;you service"),
            (f"{competitor}: {feature}", "Verum: cleaning + enrichment + validation"),
            (f"{competitor}: data deletion on cancel", "Verum: data is yours forever"),
            (f"{competitor}: one database", "Verum: 50+ sources cross&#8209;referenced"),
        ]

        related = [("All Comparisons", "/compare/"), (f"{competitor} Alternative", f"/alternatives/{competitor.lower().replace('.','').replace(' ','-')}-alternative/"),
                   ("Data Enrichment", "/services/data-enrichment.html"), ("Data Cleaning", "/services/data-cleaning.html")]

        breadcrumbs = [("Home", BASE_URL + "/"), ("Compare", BASE_URL + "/compare/"), (f"Verum vs {competitor}", None)]
        faq_s = faq_schema_json(faqs)

        pain_paras = [
            f"You're comparing Verum and {competitor}. That makes sense on the surface because both companies work with B2B data. But they solve fundamentally different problems, and picking the wrong one means paying for a solution that doesn't address your actual issue.",
            f"<h3>What {competitor} Does Well</h3>",
            f"{competitor} is {desc}. It provides {feature}. If you need to build prospecting lists from scratch with net-new contacts you don't currently have, {competitor} is designed for that. It's a large database with good coverage.",
            "<h3>What {competitor} Doesn't Do</h3>",
            f"{competitor} doesn't clean your existing CRM data. It doesn't deduplicate your records, validate your emails, standardize your fields, or fill in missing firmographic data on accounts you already have. You can import {competitor} data, but it enters your CRM alongside your existing mess. Duplicates multiply. Formats conflict.",
            "<h3>The Real Question</h3>",
            f"Is your primary problem finding new contacts (that's {competitor}'s strength) or fixing the data you already have (that's Verum's strength)? Most teams need both, but if you had to pick one, the answer depends on whether your CRM is empty or dirty.",
            "<h3>Price vs. Value</h3>",
            f"{competitor} costs {price} for platform access. Verum charges per project. If you need ongoing, daily access to a prospecting database, {competitor}'s subscription model makes sense. If you need periodic data cleanup and enrichment, Verum's per-project model is more cost-effective.",
        ]

        sol_paras = [
            f"Verum takes a different approach than {competitor}. Instead of giving you a database to search, we take your existing data and make it better. Cleaner. More complete. More accurate. The result is a CRM your team actually trusts.",
            "<h3>Data Quality, Not Data Volume</h3>",
            f"{competitor} has {feature}. Verum has 50+ sources we cross-reference to verify and enrich your existing records. We're not trying to give you more data. We're trying to make your data right.",
            f"<p><strong>The difference:</strong> {competitor} adds records to your CRM. Verum makes every record in your CRM accurate and complete.</p>",
            "<h3>Service, Not Software</h3>",
            f"With {competitor}, your team does the work: searching, filtering, exporting, importing, deduplicating. With Verum, we do the work. You send us data. We send it back clean. Your team focuses on selling, not data management.",
            "<h3>Human QA on Everything</h3>",
            f"{competitor} relies on algorithms for data quality. Verum adds human review on every project. Edge cases, ambiguous matches, and data anomalies get human judgment before delivery.",
        ]

        body = build_body(
            f"Verum vs {competitor}: Understanding the Difference", pain_paras,
            f"How Verum's Approach Differs from {competitor}", sol_paras,
            f"When to Choose {competitor} vs. Verum", use_cases,
            "",
            "Why Teams Choose Verum", [
                ("Data quality focus.", f"Verum cleans what you have. {competitor} adds what you don't."),
                ("Done-for-you.", "No platform to manage. No exports to run. We do the work."),
                ("Per-project pricing.", f"No {price}/year commitment."),
                ("Data ownership.", "Enriched data is yours permanently."),
                ("Human verification.", "Every project reviewed by our team."),
            ],
            comparison_rows,
            f"Common Questions: Verum vs {competitor}", faqs,
            "Ready to Try a Different Approach?",
            "<strong>Not sure yet?</strong> Send us a sample of your CRM data. We'll show you what Verum can clean and enrich, free. Compare the results to your current setup.",
            "<strong>Ready to go?</strong> First project in 24-48 hours. No contracts.",
        )

        html = full_page(title, meta_desc, path, breadcrumbs, "", faq_s,
                         f"Verum vs {competitor}", subtitle, stats, body, related)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# GLOSSARY PAGES - Educational pages with definitions, examples, FAQ
# ============================================================

GLOSSARY_TERMS = [
    ("abm", "Account-Based Marketing (ABM)", "A B2B strategy that targets specific high-value accounts with personalized campaigns instead of casting a wide net.", "marketing", ["ideal-customer-profile", "lead-scoring", "customer-segmentation"]),
    ("address-validation", "Address Validation", "The process of verifying that a physical address is real, correctly formatted, and deliverable.", "data-quality", ["data-validation", "data-standardization", "data-hygiene"]),
    ("batch-enrichment", "Batch Enrichment", "Processing a large dataset through enrichment in bulk rather than one record at a time.", "enrichment", ["data-enrichment", "data-append", "fill-rate"]),
    ("bounce-rate", "Bounce Rate", "The percentage of emails that fail to deliver to the recipient's inbox, either due to invalid addresses or server issues.", "email", ["email-deliverability", "email-validation", "sender-reputation"]),
    ("buyer-intent-data", "Buyer Intent Data", "Behavioral signals that indicate a company or contact is actively researching a purchase decision.", "intent", ["buying-signals", "demand-generation", "lead-scoring"]),
    ("buying-signals", "Buying Signals", "Actions or events that suggest a prospect is moving closer to a purchase decision, such as job postings, funding rounds, or technology adoptions.", "intent", ["buyer-intent-data", "demand-generation", "sales-intelligence"]),
    ("catch-all-domain", "Catch-All Domain", "An email domain configured to accept all incoming messages regardless of whether the specific address exists.", "email", ["email-validation", "email-deliverability", "bounce-rate"]),
    ("contact-waterfall", "Contact Waterfall", "A sequential enrichment process that queries multiple data providers in order, using the first successful match for each record.", "enrichment", ["data-enrichment", "batch-enrichment", "fill-rate"]),
    ("crm-hygiene", "CRM Hygiene", "The ongoing practice of maintaining clean, accurate, and complete data within a Customer Relationship Management system.", "data-quality", ["data-hygiene", "data-deduplication", "data-validation"]),
    ("customer-data-platform", "Customer Data Platform (CDP)", "A system that unifies customer data from multiple sources into a single, persistent customer profile accessible by other systems.", "systems", ["data-integration", "master-data-management", "first-party-data"]),
    ("customer-lifetime-value", "Customer Lifetime Value (CLV)", "The total revenue a business expects from a single customer account over the entire duration of their relationship.", "analytics", ["customer-segmentation", "revenue-intelligence", "lead-scoring"]),
    ("customer-segmentation", "Customer Segmentation", "The practice of dividing customers into groups based on shared characteristics like industry, company size, behavior, or value.", "analytics", ["ideal-customer-profile", "lookalike-modeling", "firmographic-data"]),
    ("data-append", "Data Append", "Adding new data fields to existing records, such as appending phone numbers to contacts that only have email addresses.", "enrichment", ["data-enrichment", "batch-enrichment", "fill-rate"]),
    ("data-decay", "Data Decay", "The gradual degradation of database accuracy over time as contacts change jobs, companies relocate, and information becomes outdated.", "data-quality", ["data-hygiene", "crm-hygiene", "data-validation"]),
    ("data-deduplication", "Data Deduplication", "The process of identifying and removing or merging duplicate records within a database.", "data-quality", ["duplicate-detection", "fuzzy-matching", "golden-record"]),
    ("data-enrichment", "Data Enrichment", "The process of adding missing information to existing records by pulling data from external sources.", "enrichment", ["data-append", "batch-enrichment", "firmographic-data"]),
    ("data-governance", "Data Governance", "The framework of policies, processes, and standards that manage how data is collected, stored, used, and maintained across an organization.", "data-quality", ["data-quality-management", "master-data-management", "data-validation"]),
    ("data-hygiene", "Data Hygiene", "The ongoing process of maintaining clean, accurate, and properly formatted data across all systems.", "data-quality", ["crm-hygiene", "data-decay", "data-validation"]),
    ("data-integration", "Data Integration", "Combining data from multiple sources into a unified view, typically across CRM, marketing automation, and analytics platforms.", "systems", ["master-data-management", "customer-data-platform", "data-normalization"]),
    ("data-migration", "Data Migration", "The process of moving data from one system to another, such as switching CRM platforms.", "systems", ["data-integration", "data-standardization", "data-deduplication"]),
    ("data-normalization", "Data Normalization", "Converting data to consistent formats and structures so that equivalent values are stored the same way across all records.", "data-quality", ["data-standardization", "job-title-normalization", "data-validation"]),
    ("data-profiling", "Data Profiling", "Analyzing a dataset to understand its structure, content, quality, and relationships before cleaning or migrating.", "analytics", ["data-quality-management", "data-validation", "fill-rate"]),
    ("data-quality-management", "Data Quality Management", "The systematic process of monitoring, measuring, and improving data quality across an organization.", "data-quality", ["data-governance", "data-hygiene", "data-validation"]),
    ("data-standardization", "Data Standardization", "Converting data to consistent formats, such as standardizing phone numbers, addresses, and company names.", "data-quality", ["data-normalization", "address-validation", "job-title-normalization"]),
    ("data-validation", "Data Validation", "Checking data against rules or reference sources to confirm it is accurate, complete, and properly formatted.", "data-quality", ["email-validation", "address-validation", "data-quality-management"]),
    ("demand-generation", "Demand Generation", "Marketing activities designed to create awareness and interest in a product or service, driving qualified leads into the sales pipeline.", "marketing", ["lead-scoring", "lead-qualification", "abm"]),
    ("duplicate-detection", "Duplicate Detection", "Identifying records in a database that represent the same entity, even when fields don't match exactly.", "data-quality", ["data-deduplication", "fuzzy-matching", "record-matching"]),
    ("email-deliverability", "Email Deliverability", "The ability of an email to reach the recipient's inbox rather than being blocked, bounced, or filtered to spam.", "email", ["bounce-rate", "sender-reputation", "email-validation"]),
    ("email-validation", "Email Validation", "Verifying that an email address is properly formatted, associated with a real domain, and capable of receiving messages.", "email", ["email-deliverability", "bounce-rate", "catch-all-domain"]),
    ("entity-resolution", "Entity Resolution", "Determining when two or more records in a dataset refer to the same real-world entity, even with variations in how the entity is represented.", "data-quality", ["fuzzy-matching", "record-matching", "golden-record"]),
    ("fill-rate", "Fill Rate", "The percentage of records in a dataset that have a value in a specific field, measuring data completeness.", "analytics", ["data-enrichment", "data-profiling", "data-quality-management"]),
    ("firmographic-data", "Firmographic Data", "Company-level attributes like industry, employee count, revenue, location, and founding year used for B2B targeting and segmentation.", "enrichment", ["data-enrichment", "industry-classification", "customer-segmentation"]),
    ("first-party-data", "First-Party Data", "Data collected directly from your own customers and prospects through your owned channels and systems.", "systems", ["customer-data-platform", "data-governance", "data-integration"]),
    ("fuzzy-matching", "Fuzzy Matching", "An algorithm-based technique that identifies records as potential matches even when field values aren't exactly identical.", "data-quality", ["duplicate-detection", "entity-resolution", "record-matching"]),
    ("golden-record", "Golden Record", "The single, most complete and accurate version of a record created by merging data from multiple duplicate or related records.", "data-quality", ["data-deduplication", "entity-resolution", "master-data-management"]),
    ("ideal-customer-profile", "Ideal Customer Profile (ICP)", "A detailed description of the company characteristics that define your best-fit customers, including industry, size, technology, and behavior patterns.", "analytics", ["customer-segmentation", "lookalike-modeling", "firmographic-data"]),
    ("industry-classification", "Industry Classification", "Categorizing companies by their primary business activity using standardized code systems like SIC or NAICS.", "enrichment", ["firmographic-data", "data-standardization", "data-enrichment"]),
    ("job-title-normalization", "Job Title Normalization", "Mapping the many variations of job titles to standardized categories for consistent routing, scoring, and reporting.", "data-quality", ["data-normalization", "data-standardization", "lead-routing"]),
    ("lead-qualification", "Lead Qualification", "Evaluating whether a lead meets your criteria for a potential customer based on firmographic, behavioral, and engagement data.", "marketing", ["lead-scoring", "ideal-customer-profile", "demand-generation"]),
    ("lead-routing", "Lead Routing", "Automatically assigning inbound leads to the appropriate sales rep or team based on data attributes like territory, company size, or industry.", "marketing", ["lead-scoring", "lead-qualification", "data-standardization"]),
    ("lead-scoring", "Lead Scoring", "Assigning numerical values to leads based on their attributes and behaviors to prioritize sales follow-up.", "marketing", ["lead-qualification", "lead-routing", "ideal-customer-profile"]),
    ("lookalike-modeling", "Lookalike Modeling", "Using characteristics of your best customers to identify new prospects with similar attributes.", "analytics", ["ideal-customer-profile", "customer-segmentation", "firmographic-data"]),
    ("market-sizing", "Market Sizing", "Calculating the total addressable market (TAM), serviceable addressable market (SAM), and serviceable obtainable market (SOM) for a product or service.", "analytics", ["ideal-customer-profile", "firmographic-data", "customer-segmentation"]),
    ("master-data-management", "Master Data Management (MDM)", "Creating and maintaining a single, authoritative source of truth for critical business data across all systems.", "systems", ["golden-record", "data-governance", "data-integration"]),
    ("match-rate", "Match Rate", "The percentage of records in your dataset that successfully match against an external data source during enrichment.", "enrichment", ["fill-rate", "data-enrichment", "batch-enrichment"]),
    ("mql", "Marketing Qualified Lead (MQL)", "A lead that has engaged with marketing content or campaigns enough to be considered likely to become a customer.", "marketing", ["lead-scoring", "lead-qualification", "demand-generation"]),
    ("net-new-contact", "Net-New Contact", "A contact record that doesn't already exist in your database, added through prospecting, events, or data purchases.", "enrichment", ["data-deduplication", "data-enrichment", "lead-qualification"]),
    ("pipeline-management", "Pipeline Management", "The process of tracking and managing sales opportunities from initial contact through close.", "marketing", ["revenue-intelligence", "lead-scoring", "lead-qualification"]),
    ("prospect-list-building", "Prospect List Building", "Creating targeted lists of potential customers based on firmographic, technographic, and behavioral criteria.", "enrichment", ["firmographic-data", "ideal-customer-profile", "data-enrichment"]),
    ("record-matching", "Record Matching", "The process of identifying records across different datasets that represent the same entity.", "data-quality", ["fuzzy-matching", "entity-resolution", "duplicate-detection"]),
    ("revenue-intelligence", "Revenue Intelligence", "Using data analytics to provide insights into revenue performance, pipeline health, and forecasting accuracy.", "analytics", ["customer-lifetime-value", "pipeline-management", "lead-scoring"]),
    ("revenue-operations", "Revenue Operations (RevOps)", "A business function that aligns sales, marketing, and customer success operations to drive predictable revenue growth.", "systems", ["revenue-intelligence", "pipeline-management", "data-governance"]),
    ("sales-intelligence", "Sales Intelligence", "Data and insights that help sales teams identify, target, and engage potential buyers more effectively.", "enrichment", ["buyer-intent-data", "firmographic-data", "technographic-data"]),
    ("sender-reputation", "Sender Reputation", "A score assigned to your email sending domain by ISPs, based on bounce rates, spam complaints, and engagement metrics.", "email", ["email-deliverability", "bounce-rate", "email-validation"]),
    ("suppression-list", "Suppression List", "A list of contacts who should be excluded from outreach, including opt-outs, competitors, existing customers, or bounced addresses.", "email", ["email-deliverability", "data-hygiene", "email-validation"]),
    ("tech-stack-data", "Tech Stack Data", "Information about the software and technology tools a company uses, identified through website analysis, job postings, and verified databases.", "enrichment", ["technographic-data", "data-enrichment", "sales-intelligence"]),
    ("technographic-data", "Technographic Data", "Data about the technology products and platforms a company uses, enabling tech-stack-based targeting and positioning.", "enrichment", ["tech-stack-data", "firmographic-data", "data-enrichment"]),
    ("territory-planning", "Territory Planning", "Dividing your market into geographic or account-based territories for sales team assignment, requiring accurate location and firmographic data.", "marketing", ["lead-routing", "firmographic-data", "data-standardization"]),
]

def _glossary_page_html(slug, term, definition, category, related_slugs):
    """Generate a full glossary page."""
    path = f"/glossary/{slug}/"
    url = f"{BASE_URL}{path}"
    title = f"What Is {term}?"
    meta_desc = f"{definition[:130]}..." if len(definition) > 130 else definition
    if not meta_desc.endswith('.'):
        meta_desc = meta_desc.rstrip('.') + '.'

    # Build related terms links
    related_html = ""
    for rs in related_slugs[:5]:
        rname = rs.replace("-", " ").title()
        for s, n, d, c, r in GLOSSARY_TERMS:
            if s == rs:
                rname = n
                break
        related_html += f'                <li><a href="/glossary/{rs}/">{rname}</a></li>\n'

    # Example paragraph based on category
    examples = {
        "enrichment": f"You have 10,000 contacts in your CRM but only 6,000 have email addresses. {term} can fill in those missing 4,000 emails from external sources, turning incomplete records into reachable contacts.",
        "data-quality": f"Your CRM has 50,000 records. After applying {term.lower()}, you discover that 15% need attention. Fixing those 7,500 records before your next campaign prevents bounces, misroutes, and wasted spend.",
        "email": f"Before sending your quarterly newsletter to 25,000 contacts, you run {term.lower()}. It flags 3,200 addresses as invalid. Removing them protects your sender reputation and improves deliverability for the remaining 21,800.",
        "marketing": f"Your marketing team wants to target VP-level contacts at SaaS companies with 200-1,000 employees. {term} ensures those filters work on accurate data, not the incomplete fields currently in your CRM.",
        "analytics": f"You're trying to calculate your Ideal Customer Profile. {term} on clean data reveals that your best customers share three firmographic traits you hadn't identified before, because previous analyses ran on incomplete records.",
        "intent": f"Your TAM is 40,000 accounts but only 2,000 are in-market at any given time. {term} identifies those 2,000 so your team focuses outreach on accounts that are actively researching solutions.",
        "systems": f"After implementing {term.lower()}, your CRM, marketing automation, and BI tools all show the same numbers. Pipeline reviews focus on strategy instead of arguing about which system is right.",
    }
    example = examples.get(category, f"Applying {term.lower()} to your database improves the accuracy and completeness of your records, enabling better targeting, personalization, and reporting across your go-to-market operations.")

    # FAQs
    faqs = [
        (f"What is {term.lower()}?", definition),
        (f"Why does {term.lower()} matter for B2B teams?", f"B2B data decays at 30% per year. Without {term.lower()}, your database loses accuracy every month. Clean, complete data drives better targeting, higher conversion rates, and more accurate reporting. The average cost of poor data quality is $15M per year for large organizations."),
        (f"How does Verum help with {term.lower()}?", f"We handle {term.lower()} as part of our data cleaning and enrichment services. Send us your data, and we'll apply {term.lower()} best practices using 50+ sources with human QA. Most projects complete in 24-48 hours."),
    ]
    faq_s = faq_schema_json(faqs)

    bc = breadcrumb_json([("Home", BASE_URL + "/"), ("Glossary", BASE_URL + "/glossary/"), (term, None)])

    dt_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": term,
        "description": definition,
        "inDefinedTermSet": f"{BASE_URL}/glossary/"
    }, indent=4)

    return path, f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <link rel="canonical" href="{url}">
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
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(meta_desc)}">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="{BASE_URL}/assets/social/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(meta_desc)}">
  <meta name="twitter:image" content="{BASE_URL}/assets/social/twitter-card.png">
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
{bc}
  </script>
  <script type="application/ld+json">
{dt_schema}
  </script>
  <script type="application/ld+json">
{faq_s}
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
        <h1 class="page-hero__title">{term}</h1>
        <p class="page-hero__subtitle">{definition}</p>
      </div>
    </section>
    <section class="content">
      <div class="container" style="max-width: 800px;">
        <h2>Definition</h2>
        <p><strong>{term}</strong> is {definition[0].lower()}{definition[1:]}</p>

        <h2>Why It Matters</h2>
        <p>B2B databases decay at 30% per year. Without proper attention to {term.lower()}, your CRM loses accuracy every quarter. Gartner estimates the average cost of poor data quality at $15 million per year for large organizations. Even for smaller teams, the impact shows up in bounced emails, misrouted leads, and wasted selling time.</p>
        <p>{term} directly affects your team's ability to target the right accounts, personalize outreach, and report accurately. When this area of your data strategy breaks down, everything downstream, from lead scoring to pipeline forecasting, produces unreliable results.</p>

        <h2>How It Works</h2>
        <p>{term} involves several steps depending on your specific data challenges. At a high level:</p>
        <ul>
            <li><strong>Assessment:</strong> Analyze your current data to identify gaps, inconsistencies, and quality issues related to {term.lower()}.</li>
            <li><strong>Processing:</strong> Apply the relevant techniques, whether that's enrichment from external sources, validation against reference data, or normalization to standard formats.</li>
            <li><strong>Verification:</strong> Cross-reference results against multiple sources and apply human QA to catch edge cases that automated processes miss.</li>
            <li><strong>Delivery:</strong> Return cleaned, enriched data to your CRM in a format ready for immediate use.</li>
            <li><strong>Maintenance:</strong> Schedule periodic refreshes to prevent data decay from undoing the improvements.</li>
        </ul>

        <h2>Example</h2>
        <p>{example}</p>

        <h2>Common Mistakes</h2>
        <ul>
            <li><strong>Treating it as a one-time project.</strong> Data decays continuously. A one-time effort buys you a few months of clean data, then quality degrades right back to where it started.</li>
            <li><strong>Relying on a single data source.</strong> No single vendor has complete or perfectly accurate data. Cross-referencing 50+ sources produces significantly better results than relying on one.</li>
            <li><strong>Skipping human QA.</strong> Automated processes handle 90% of cases well. The remaining 10%, the edge cases and ambiguous matches, need human review to prevent errors from entering your database.</li>
        </ul>

        <h2>Frequently Asked Questions</h2>
        <div class="faq-section">
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem;">What is {term.lower()}?</h3>
            <p style="color: var(--color-text-secondary);">{definition}</p>
          </div>
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem;">Why does {term.lower()} matter for B2B teams?</h3>
            <p style="color: var(--color-text-secondary);">B2B data decays at 30% per year. Without {term.lower()}, your database loses accuracy every month. Clean, complete data drives better targeting, higher conversion rates, and more accurate reporting.</p>
          </div>
          <div class="faq-item" style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1rem; margin-bottom: 0.5rem;">How does Verum help with {term.lower()}?</h3>
            <p style="color: var(--color-text-secondary);">We handle {term.lower()} as part of our data cleaning and enrichment services. Send us your data, and we'll apply best practices using 50+ sources with human QA. Most projects complete in 24-48 hours.</p>
          </div>
        </div>

        <h2>Related Terms</h2>
        <ul>
{related_html}        </ul>

        <div class="cta-group mt-xl">
          <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Assessment</a>
          <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>
        </div>

        <p class="mt-lg text-muted">Related: <a href="/glossary/">All Glossary Terms</a> | <a href="/services/data-enrichment.html">Enrichment Services</a> | <a href="/services/data-cleaning.html">Cleaning Services</a></p>
      </div>
    </section>
  </main>
  <footer id="site-footer"></footer>
  <script src="/js/components.js"></script>
  <script src="/js/main.js"></script>
</body>
</html>'''


def generate_glossary_pages():
    pages = []
    for slug, term, definition, category, related_slugs in GLOSSARY_TERMS:
        path, html = _glossary_page_html(slug, term, definition, category, related_slugs)
        pages.append((path, html))
        print(f"  Generated: {path}")
    return pages


# ============================================================
# SITEMAP GENERATION
# ============================================================

def generate_sitemap(all_paths):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    core_pages = [
        ("/", "1.0", "weekly"),
        ("/about.html", "0.8", "monthly"),
        ("/contact.html", "0.8", "monthly"),
        ("/pricing.html", "0.8", "monthly"),
        ("/services/", "0.9", "weekly"),
        ("/services/data-cleaning.html", "0.9", "weekly"),
        ("/services/data-enrichment.html", "0.9", "weekly"),
        ("/services/data-analysis.html", "0.9", "weekly"),
        ("/services/icp-analysis.html", "0.8", "monthly"),
        ("/team/", "0.7", "monthly"),
        ("/resources/", "0.8", "weekly"),
        ("/enrichment/", "0.8", "monthly"),
        ("/cleaning/", "0.8", "monthly"),
        ("/find/", "0.8", "monthly"),
        ("/use-cases/", "0.8", "monthly"),
        ("/analysis/", "0.8", "monthly"),
        ("/alternatives/", "0.8", "monthly"),
        ("/compare/", "0.8", "monthly"),
        ("/glossary/", "0.8", "monthly"),
        ("/solutions/", "0.9", "weekly"),
    ]

    for p, pri, freq in core_pages:
        sitemap += f'  <url>\n    <loc>{BASE_URL}{p}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>\n'

    # Add solutions pages (already exist, not regenerated)
    solutions_dir = os.path.join(OUTPUT_DIR, 'solutions')
    if os.path.isdir(solutions_dir):
        for d in sorted(os.listdir(solutions_dir)):
            dp = os.path.join(solutions_dir, d, 'index.html')
            if os.path.isfile(dp) and d != 'index.html':
                sitemap += f'  <url>\n    <loc>{BASE_URL}/solutions/{d}/</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'

    for path in all_paths:
        sitemap += f'  <url>\n    <loc>{BASE_URL}{path}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'

    sitemap += '</urlset>'
    return sitemap


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("Verum Website - Full-Quality SEO Page Generator")
    print("=" * 60)

    all_paths = []

    print("\n--- Enrichment Pages ---")
    for path, html in generate_enrichment_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Cleaning Pages ---")
    for path, html in generate_cleaning_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Use Case Pages ---")
    for path, html in generate_use_case_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Find Pages ---")
    for path, html in generate_find_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Analysis Pages ---")
    for path, html in generate_analysis_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Alternatives Pages ---")
    for path, html in generate_alternative_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Comparison Pages ---")
    for path, html in generate_comparison_pages():
        write_page(path, html)
        all_paths.append(path)

    print("\n--- Glossary Pages ---")
    for path, html in generate_glossary_pages():
        write_page(path, html)
        all_paths.append(path)

    print(f"\n{'=' * 60}")
    print(f"Generated {len(all_paths)} pages")
    print(f"Skipped {len(SKIP_PAGES)} manually enhanced pages")
    print(f"Solutions pages NOT regenerated (manually managed)")

    # Sitemap
    print(f"\nGenerating sitemap.xml...")
    sitemap = generate_sitemap(all_paths)
    sitemap_path = os.path.join(OUTPUT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w') as f:
        f.write(sitemap)
    print(f"Sitemap written with {sitemap.count('<url>')} URLs")

    print(f"\nDone!")


if __name__ == "__main__":
    main()
