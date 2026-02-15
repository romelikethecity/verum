#!/usr/bin/env python3
"""Generate glossary term pages - Batch 1 (17 terms)."""
import os

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"
GLOSSARY_DIR = os.path.join(SITE_ROOT, "glossary")

def generate_page(slug, term, meta_desc, definition, why_matters, how_heading, how_items, example, related_terms, related_resources, cta_headline, cta_text):
    """Generate a glossary term HTML page."""
    # Build related terms HTML
    rt_html = "\n".join(f'                <li><a href="/glossary/{s}/">{n}</a></li>' for n, s in related_terms)
    # Build related resources HTML
    rr_html = "\n".join(f'                <li><a href="{u}">{n}</a></li>' for n, u in related_resources)
    # Build how-it-works items
    how_html = "\n".join(f'                <li><strong>{title}:</strong> {desc}</li>' for title, desc in how_items)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="canonical" href="https://veruminc.com/glossary/{slug}/">
    <title>What Is {term}? | Verum</title>
    <meta name="description" content="{meta_desc}">

    <link rel="icon" type="image/svg+xml" href="/assets/favicons/favicon.svg">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicons/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicons/apple-touch-icon.png">
    <meta name="theme-color" content="#00b894">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/styles.css?v=6">

    <script async src="https://www.googletagmanager.com/gtag/js?id=G-R416JZ91B1"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-R416JZ91B1');</script>
    <script type="text/javascript">(function(c,l,a,r,i,t,y){{c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);}})(window,document,"clarity","script","uzzgoxxnof");</script>

    <meta property="og:type" content="article">
    <meta property="og:title" content="What Is {term}? | Verum">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://veruminc.com/glossary/{slug}/">
    <meta property="og:site_name" content="Verum">
    <meta property="og:image" content="https://veruminc.com/assets/social/og-image.png">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="What Is {term}? | Verum">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://veruminc.com/assets/social/twitter-card.png">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://veruminc.com/"
      }},{{
        "@type": "ListItem",
        "position": 2,
        "name": "Glossary",
        "item": "https://veruminc.com/glossary/"
      }},{{
        "@type": "ListItem",
        "position": 3,
        "name": "{term}"
      }}]
    }}
    </script>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "DefinedTerm",
      "name": "{term}",
      "description": "{meta_desc}",
      "inDefinedTermSet": "https://veruminc.com/glossary/"
    }}
    </script>
</head>
<body>
    <noscript>
        <nav style="padding: 1rem; background: #f5f5f5; text-align: center;">
            <a href="/" style="margin: 0 1rem;">Home</a>
            <a href="/services/" style="margin: 0 1rem;">Services</a>
            <a href="/resources/" style="margin: 0 1rem;">Resources</a>
            <a href="/#contact" style="margin: 0 1rem;">Contact</a>
        </nav>
    </noscript>

    <header id="site-header"></header>

    <section class="page-hero">
        <div class="container">
            <h1>{term}</h1>
        </div>
    </section>

    <section class="content">
        <div class="container" style="max-width: 800px;">
            {definition}

            <h2>Why It Matters</h2>
            {why_matters}

            <h2>{how_heading}</h2>
            <ul>
{how_html}
            </ul>

            <h3>Example</h3>
            {example}

            <h3>Related Terms</h3>
            <ul>
{rt_html}
            </ul>

            <h3>Related Resources</h3>
            <ul>
{rr_html}
            </ul>

            <div class="cta-box" style="margin-top: var(--space-2xl); padding: var(--space-xl); background: var(--color-bg-secondary); border-radius: var(--radius-lg);">
                <h3>{cta_headline}</h3>
                <p>{cta_text}</p>
                <a href="/#contact" class="btn btn-primary">See What We'll Find</a>
            </div>
        </div>
    </section>

    <footer id="site-footer"></footer>
    <script src="/js/components.js"></script>
</body>
</html>'''
    return html


TERMS = [
    {
        "slug": "abm",
        "term": "Account-Based Marketing (ABM)",
        "meta_desc": "Account-based marketing targets specific high-value accounts with personalized campaigns. Learn how ABM works and why data quality determines whether it succeeds or fails.",
        "definition": '<p><strong>Account-based marketing (ABM)</strong> is a B2B strategy that focuses sales and marketing resources on a defined set of target accounts rather than casting a wide net. Instead of generating thousands of leads and hoping some convert, ABM identifies the companies most likely to buy, then builds personalized campaigns for each one.</p>',
        "why_matters": "<p>ABM only works if you know who you're targeting. That means accurate firmographic data, verified contacts at each account, and enough intel on their tech stack and buying signals to personalize outreach. When your account data is wrong, you're personalizing messages to the wrong people at the wrong companies. The entire strategy collapses.</p>\n<p>Teams running ABM with dirty data waste 30-40% of their budget reaching accounts that don't fit their ICP or contacts who left the company months ago.</p>",
        "how_heading": "How ABM Uses Data",
        "how_items": [
            ("Account selection", "Use firmographic and technographic data to build a target account list that matches your ICP"),
            ("Contact mapping", "Identify the buying committee at each account: decision-makers, influencers, and budget holders"),
            ("Personalization", "Tailor messaging based on the account's industry, tech stack, growth stage, and recent activity"),
            ("Multi-channel orchestration", "Coordinate outreach across email, ads, direct mail, and sales touches for each account"),
            ("Measurement", "Track engagement and pipeline at the account level, not just the lead level"),
        ],
        "example": "<p>A sales enablement platform targets 200 mid-market SaaS companies. For each account, they identify the VP of Sales, CRO, and Head of Enablement. They reference each company's current CRM and sales methodology in outreach. One campaign costs 5x more per account than broad marketing but generates 3x the pipeline.</p>",
        "related_terms": [("Ideal Customer Profile (ICP)", "ideal-customer-profile"), ("Lead Scoring", "lead-scoring"), ("Buyer Intent Data", "buyer-intent-data")],
        "related_resources": [("ABM Data Strategy Guide", "/resources/abm-data-strategy.html"), ("ABM Targeting", "/use-cases/abm-targeting/"), ("Data Enrichment Services", "/services/data-enrichment.html")],
        "cta_headline": "Building an ABM target list?",
        "cta_text": "We'll enrich your accounts with verified contacts, tech stack data, and firmographics so your campaigns actually land.",
    },
    {
        "slug": "address-validation",
        "term": "Address Validation",
        "meta_desc": "Address validation confirms that a mailing address is real, deliverable, and formatted to postal standards. Learn how it works and why it matters for direct mail and territory planning.",
        "definition": '<p><strong>Address validation</strong> confirms that a physical address exists, is deliverable, and conforms to postal standards like USPS CASS certification. It goes beyond formatting: validation checks the address against official postal databases to verify that someone can actually receive mail there.</p>',
        "why_matters": "<p>Bad addresses cost money in two ways. Direct mail sent to invalid addresses is pure waste. And territory assignments based on incorrect locations put reps in the wrong geography. A database with 15% bad addresses means 15% of your direct mail budget goes in the trash and your territory maps have blind spots.</p>",
        "how_heading": "How Address Validation Works",
        "how_items": [
            ("Parsing", "Break the address into components: street number, street name, unit, city, state, ZIP"),
            ("Standardization", "Convert abbreviations and formats to USPS Publication 28 standards"),
            ("Database lookup", "Match against USPS, Royal Mail, or other national postal authority databases"),
            ("Deliverability check", "Confirm the address is a real delivery point, not just a valid format"),
            ("Geocoding", "Append latitude/longitude coordinates for mapping and territory assignment"),
        ],
        "example": "<p>A company runs a direct mail campaign to 10,000 addresses. Before mailing, validation catches 1,200 addresses that are incomplete, outdated, or non-existent. They save $6,000 in postage and printing, and their response rate jumps because every piece actually arrives.</p>",
        "related_terms": [("Data Normalization", "data-normalization"), ("Data Validation", "data-validation"), ("Data Hygiene", "data-hygiene")],
        "related_resources": [("Address Validation Service", "/validation/address-validation/"), ("Address Normalization", "/cleaning/address-normalization/"), ("Address Enrichment", "/enrichment/address-enrichment/")],
        "cta_headline": "Mailing to bad addresses?",
        "cta_text": "We'll validate your entire address database against postal records and fix what's broken.",
    },
    {
        "slug": "batch-enrichment",
        "term": "Batch Enrichment",
        "meta_desc": "Batch enrichment appends missing data to thousands of records at once. Learn how it differs from real-time enrichment and when to use each approach.",
        "definition": '<p><strong>Batch enrichment</strong> is the process of appending missing data fields to a large set of records all at once, rather than enriching them one at a time as they enter your system. You export a file, send it for enrichment, and get it back with new fields added: emails, phone numbers, company size, job titles, tech stack data.</p>',
        "why_matters": "<p>Most CRM databases accumulate gaps over time. Contacts are missing phone numbers, companies are missing revenue data, job titles are outdated. Fixing these one by one is impractical when you have 50,000 records. Batch enrichment lets you clean up an entire database in a single project, typically within 24-48 hours.</p>\n<p>It's also the only practical approach for preparing a database for a migration, a major campaign launch, or an annual data refresh.</p>",
        "how_heading": "How Batch Enrichment Works",
        "how_items": [
            ("Export", "Pull your records from your CRM or marketing platform in CSV or Excel format"),
            ("Field mapping", "Identify which fields need enrichment: emails, phones, titles, firmographics, technographics"),
            ("Multi-source matching", "Match each record against multiple data providers to maximize fill rates"),
            ("QA and verification", "Validate appended data for accuracy before returning the enriched file"),
            ("Import", "Load the enriched file back into your system with new fields mapped to the right columns"),
        ],
        "example": "<p>A marketing team exports 25,000 leads from HubSpot before a product launch. 60% are missing direct phone numbers and 40% have no company size data. Batch enrichment fills in 18,000 phone numbers and all 10,000 missing company records in two days. The launch campaign now has enough data to segment and prioritize properly.</p>",
        "related_terms": [("Data Enrichment", "data-enrichment"), ("Fill Rate", "fill-rate"), ("Contact Data Waterfall", "contact-waterfall")],
        "related_resources": [("Real-Time vs Batch Enrichment", "/resources/real-time-vs-batch-enrichment.html"), ("Data Enrichment Services", "/services/data-enrichment.html"), ("Batch Validation", "/validation/batch-validation/")],
        "cta_headline": "Need to enrich thousands of records?",
        "cta_text": "Send us your file. We'll fill the gaps and send it back ready to import.",
    },
    {
        "slug": "bounce-rate",
        "term": "Bounce Rate (Email)",
        "meta_desc": "Email bounce rate measures the percentage of emails that fail to deliver. Learn what causes bounces, what rate is acceptable, and how to fix a high bounce rate.",
        "definition": '<p><strong>Email bounce rate</strong> is the percentage of sent emails that fail to reach the recipient\'s inbox. A "hard bounce" means the address doesn\'t exist or the domain is invalid. A "soft bounce" means the mailbox is temporarily full, the server is down, or the message was too large. ISPs track your bounce rate and use it to decide whether to deliver your future emails or send them to spam.</p>',
        "why_matters": "<p>ISPs like Gmail and Outlook watch your bounce rate closely. Send to too many bad addresses and your sender reputation drops, which means even your emails to valid addresses start landing in spam. Most email platforms will suspend your account if your bounce rate exceeds 5%. A single bad campaign to an uncleaned list can damage your deliverability for weeks.</p>",
        "how_heading": "How to Reduce Bounce Rates",
        "how_items": [
            ("Verify before sending", "Run your list through email verification to catch invalid addresses before they bounce"),
            ("Remove hard bounces immediately", "Never send to an address that hard-bounced. It won't suddenly start working"),
            ("Monitor soft bounces", "Retry soft bounces once or twice, then remove them if they keep failing"),
            ("Clean on a schedule", "B2B email lists decay at 2-3% per month. Quarterly cleaning prevents accumulation"),
            ("Use double opt-in", "For inbound lists, confirm the email address works before adding it to your database"),
        ],
        "example": "<p>A sales team sends 5,000 cold emails and gets a 12% bounce rate. Their email provider flags the account. Deliverability drops from 95% to 60% across all campaigns for the next three weeks. They clean the list, remove 800 bad addresses, and slowly rebuild their sender score over the following month.</p>",
        "related_terms": [("Email Validation", "email-validation"), ("Sender Reputation", "sender-reputation"), ("Email Deliverability", "email-deliverability")],
        "related_resources": [("Email Deliverability & Data Quality", "/resources/email-deliverability-data-quality.html"), ("Email List Cleaning", "/cleaning/email-list-cleaning/"), ("Email Verification", "/cleaning/email-verification/")],
        "cta_headline": "Bounce rate too high?",
        "cta_text": "We'll verify every address in your database and remove the ones that will hurt your sender reputation.",
    },
    {
        "slug": "buyer-intent-data",
        "term": "Buyer Intent Data",
        "meta_desc": "Buyer intent data reveals which companies are actively researching solutions like yours. Learn how intent signals work and how to use them for sales prioritization.",
        "definition": '<p><strong>Buyer intent data</strong> tracks online research behavior to identify companies that are actively evaluating solutions in your category. When someone at a target account reads comparison articles, visits competitor websites, or searches for terms related to your product, intent data providers capture those signals and surface the account as "in-market."</p>',
        "why_matters": "<p>Without intent data, sales teams treat every prospect the same. They call 100 accounts hoping 5 are interested. With intent data, they can see which accounts are already researching and focus their energy there. Teams using intent signals report 2-3x higher conversion rates on outbound because they're reaching out when the prospect is already thinking about the problem.</p>",
        "how_heading": "Types of Intent Signals",
        "how_items": [
            ("Topic surge", "An account's research on a specific topic spikes above their baseline, indicating active evaluation"),
            ("Competitor research", "Visits to competitor websites, G2 reviews, or comparison pages signal they're shopping"),
            ("Content consumption", "Downloading whitepapers, attending webinars, or reading case studies on relevant topics"),
            ("Search behavior", "Searching for category keywords like 'CRM migration' or 'data enrichment tools'"),
            ("Job postings", "Hiring for roles that use your product type signals budget and organizational commitment"),
        ],
        "example": '<p>An enrichment vendor sees that Acme Corp\'s intent score for "data quality" spiked 300% this week. Three people at Acme read comparison articles and one visited the vendor\'s pricing page. The sales rep reaches out with a relevant case study and books a demo. Without intent data, Acme would have been call #47 on a cold list.</p>',
        "related_terms": [("Buying Signals", "buying-signals"), ("Lead Scoring", "lead-scoring"), ("Technographic Data", "technographic-data")],
        "related_resources": [("Intent Data Guide", "/resources/intent-data-guide.html"), ("Buyer Intent Enrichment", "/enrichment/buyer-intent-enrichment/"), ("Intent Data Enrichment", "/enrichment/intent-data-enrichment/")],
        "cta_headline": "Want to know who's in-market?",
        "cta_text": "We'll enrich your target accounts with intent signals so your reps call the right companies at the right time.",
    },
    {
        "slug": "buying-signals",
        "term": "Buying Signals",
        "meta_desc": "Buying signals are observable behaviors that indicate a company is ready to purchase. Learn the key signals to watch and how to act on them.",
        "definition": '<p><strong>Buying signals</strong> are observable actions or events that suggest a company is moving toward a purchase decision. They range from explicit signals like requesting a demo to implicit ones like a surge in website visits, a new executive hire, or a recent funding round. Sales teams use buying signals to prioritize outreach and time their conversations.</p>',
        "why_matters": "<p>Timing matters more than most sales teams realize. A prospect who just raised a Series B has budget. A company that just hired a VP of Sales needs tools. A business that's visiting your pricing page three times a week is comparing options. If you reach out during these windows, your response rate jumps. If you wait two months, someone else already closed the deal.</p>",
        "how_heading": "Common Buying Signals",
        "how_items": [
            ("Funding events", "A new funding round means fresh budget and pressure to grow. Series A and B companies are especially active buyers"),
            ("Executive hires", "A new CRO, VP of Sales, or Head of Marketing typically brings new tools and vendors within their first 90 days"),
            ("Tech stack changes", "Switching CRMs, adding a marketing automation platform, or dropping a competitor product"),
            ("Content engagement", "Repeated visits to your site, case study downloads, or webinar attendance from the same account"),
            ("Job postings", "Hiring for roles that would use your product. Ten new SDR postings means they need sales tools"),
        ],
        "example": "<p>A data provider monitors their target accounts and notices that a healthcare SaaS company just hired a new VP of Revenue Operations, raised $15M in Series B, and posted 8 SDR openings. All three signals hit within two weeks. The rep reaches out referencing the growth and books a call on the first try.</p>",
        "related_terms": [("Buyer Intent Data", "buyer-intent-data"), ("Lead Scoring", "lead-scoring"), ("Firmographic Data", "firmographic-data")],
        "related_resources": [("Signal-Based Selling", "/resources/signal-based-selling.html"), ("Buying Signals Enrichment", "/enrichment/buying-signals-enrichment/"), ("Lead Qualification", "/use-cases/lead-qualification/")],
        "cta_headline": "Missing buying signals in your data?",
        "cta_text": "We'll enrich your accounts with funding events, hiring trends, and tech stack changes so you never miss a buying window.",
    },
    {
        "slug": "catch-all-domain",
        "term": "Catch-All Domain",
        "meta_desc": "A catch-all domain accepts email sent to any address at that domain, making it impossible to verify individual mailboxes. Learn why this matters for email campaigns.",
        "definition": '<p>A <strong>catch-all domain</strong> (also called an "accept-all" domain) is configured to accept email sent to any address at that domain, whether the specific mailbox exists or not. If you email randomstring@catchall-company.com, the server accepts it. This makes it impossible for email verification tools to confirm whether a specific person\'s email is valid, because the server says "yes" to everything.</p>',
        "why_matters": "<p>Catch-all domains create a blind spot in your email verification process. Verification tools can confirm that the domain is active, but they can't confirm that john.smith@catchall-company.com actually reaches John Smith. You might be emailing an address that goes nowhere. About 10-15% of business domains are catch-all, and sending to unverified addresses at these domains can inflate your bounce rate if the company later changes their email configuration.</p>",
        "how_heading": "How to Handle Catch-All Domains",
        "how_items": [
            ("Flag, don't delete", "Mark catch-all addresses as 'unverifiable' rather than removing them. Many are still valid"),
            ("Cross-reference", "Check the contact against LinkedIn or company directories to confirm they actually work there"),
            ("Send cautiously", "Include catch-all addresses in campaigns but monitor bounce rates per domain"),
            ("Segment separately", "Keep catch-all addresses in a separate segment so you can measure their deliverability independently"),
            ("Verify over time", "Track which catch-all addresses engage (open, click) and promote those to your verified list"),
        ],
        "example": '<p>Your verification tool flags 2,000 emails as "catch-all." You cross-reference against LinkedIn and confirm 1,400 of the contacts actually work at those companies. You include them in your campaign with a separate tracking tag. Result: 92% deliverability on the catch-all segment, nearly as good as verified addresses.</p>',
        "related_terms": [("Email Validation", "email-validation"), ("Bounce Rate (Email)", "bounce-rate"), ("Email Deliverability", "email-deliverability")],
        "related_resources": [("Email Verification", "/cleaning/email-verification/"), ("Email Deliverability & Data Quality", "/resources/email-deliverability-data-quality.html"), ("Email List Cleaning", "/cleaning/email-list-cleaning/")],
        "cta_headline": "Stuck with unverifiable emails?",
        "cta_text": "We'll cross-reference catch-all addresses against multiple sources and tell you which ones are safe to send.",
    },
    {
        "slug": "customer-data-platform",
        "term": "Customer Data Platform (CDP)",
        "meta_desc": "A customer data platform unifies customer data from every touchpoint into a single profile. Learn how CDPs work and why clean data is the prerequisite.",
        "definition": '<p>A <strong>customer data platform (CDP)</strong> is software that collects customer data from every touchpoint, website visits, email engagement, product usage, support tickets, purchases, and unifies it into a single customer profile. Unlike a CRM, which stores data that reps manually enter, a CDP automatically ingests behavioral data and stitches it together across devices and channels.</p>',
        "why_matters": "<p>CDPs promise a \"single view of the customer,\" but they can only deliver it if the underlying data is clean. Duplicate records create duplicate profiles. Wrong email addresses prevent cross-channel matching. Missing firmographic data means segments are incomplete. Teams that implement a CDP without cleaning their data first just get a more expensive version of the same messy data, now unified into one place where everyone can see the problems.</p>",
        "how_heading": "What a CDP Does",
        "how_items": [
            ("Identity resolution", "Match anonymous website visitors to known contacts using cookies, email, and device IDs"),
            ("Data unification", "Combine data from CRM, marketing automation, product analytics, and support tools into one profile"),
            ("Segmentation", "Build audience segments based on behavior, firmographics, and engagement across all channels"),
            ("Activation", "Push segments to advertising platforms, email tools, and sales systems for coordinated campaigns"),
            ("Real-time updates", "Profiles update automatically as new interactions happen across any connected system"),
        ],
        "example": "<p>A SaaS company connects their CDP to Salesforce, HubSpot, Mixpanel, and Zendesk. It merges 120,000 contact records into 85,000 unique profiles, revealing 35,000 duplicates they didn't know existed. Now marketing can see that the person who submitted a support ticket yesterday also attended a webinar last week and visited the pricing page twice.</p>",
        "related_terms": [("CRM Hygiene", "crm-hygiene"), ("Data Integration", "data-integration"), ("Master Data Management", "master-data-management")],
        "related_resources": [("Customer Data Platform Use Case", "/use-cases/customer-data-platform/"), ("Data Integration", "/use-cases/data-integration/"), ("CRM Data Cleaning", "/cleaning/crm-data-cleaning/")],
        "cta_headline": "Implementing a CDP?",
        "cta_text": "Clean your data first. We'll deduplicate, standardize, and enrich your records so your CDP starts with accurate profiles.",
    },
    {
        "slug": "customer-lifetime-value",
        "term": "Customer Lifetime Value (CLV)",
        "meta_desc": "Customer lifetime value measures the total revenue a customer generates over their entire relationship. Learn how to calculate CLV and use it for acquisition decisions.",
        "definition": '<p><strong>Customer lifetime value (CLV)</strong> is the total revenue a customer is expected to generate over the entire duration of their relationship with your company. It accounts for recurring revenue, upsells, expansions, and churn probability. CLV tells you how much you can afford to spend acquiring a customer and still turn a profit.</p>',
        "why_matters": "<p>If you don't know your CLV by segment, you're guessing on acquisition spend. A customer segment with $8,000 CLV can justify $2,000 in acquisition cost. A segment with $800 CLV can't justify $200. Without this math, marketing spends the same amount acquiring every customer, overspending on low-value segments and underinvesting in high-value ones.</p>\n<p>CLV analysis also reveals which customer attributes predict long-term value, turning your ICP from a guess into a data-backed profile.</p>",
        "how_heading": "How CLV Is Calculated",
        "how_items": [
            ("Average revenue per period", "Monthly or annual revenue per customer, including base subscription and add-ons"),
            ("Customer lifespan", "Average number of months or years before churn, calculated from historical retention data"),
            ("Gross margin", "Revenue minus cost to serve, because not all revenue is profit"),
            ("Expansion revenue", "Upsells, cross-sells, and seat expansions that increase value over time"),
            ("Segmentation", "Break CLV by industry, company size, acquisition channel, or product tier to find your best segments"),
        ],
        "example": "<p>An ICP analysis of 315 closed deals reveals that companies with 2 RevOps professionals have an average CLV of $8,750, while companies with 0 RevOps average $1,400. Marketing reallocates 75% of budget to the high-CLV segment and CAC payback drops from 14 months to 5.</p>",
        "related_terms": [("Ideal Customer Profile (ICP)", "ideal-customer-profile"), ("Customer Segmentation", "customer-segmentation"), ("Lead Scoring", "lead-scoring")],
        "related_resources": [("Customer Lifetime Value Analysis", "/analysis/customer-lifetime-value/"), ("ICP Analysis Case Study", "/case-studies/icp-analysis-series-a-saas/"), ("ICP Analysis Service", "/services/icp-analysis.html")],
        "cta_headline": "Know which customers are worth the most?",
        "cta_text": "Our ICP analysis breaks down CLV by segment so you can focus acquisition spend where it actually pays off.",
    },
    {
        "slug": "customer-segmentation",
        "term": "Customer Segmentation",
        "meta_desc": "Customer segmentation divides your market into groups based on shared characteristics. Learn segmentation methods and how data quality determines accuracy.",
        "definition": '<p><strong>Customer segmentation</strong> divides your customer base or target market into groups that share common characteristics: industry, company size, buying behavior, product usage, or revenue potential. Each segment gets different messaging, pricing, sales motions, and success programs because what works for a 10-person startup doesn\'t work for a 5,000-person enterprise.</p>',
        "why_matters": "<p>Without segmentation, you treat every customer the same. Same emails, same sales pitch, same onboarding. The result: mediocre engagement across the board. With segmentation, you can tailor everything. Enterprise accounts get white-glove onboarding. SMBs get self-serve guides. High-growth startups get pitched on scalability. Each segment hears the message that resonates with their specific situation.</p>",
        "how_heading": "Common Segmentation Methods",
        "how_items": [
            ("Firmographic", "Segment by company size, industry, revenue, location, or growth stage"),
            ("Behavioral", "Group by product usage patterns, feature adoption, engagement frequency, or purchase history"),
            ("Needs-based", "Cluster by the problems they're trying to solve or the outcomes they care about"),
            ("Value-based", "Rank by customer lifetime value, deal size, or expansion potential"),
            ("Technographic", "Group by tech stack, which predicts both fit and competitive displacement opportunities"),
        ],
        "example": "<p>A B2B SaaS company segments 2,000 customers by company size and product usage. They discover that companies with 50-200 employees who use the reporting module have 3x the retention of those who don't. They redesign onboarding to push reporting adoption early and churn drops 18% across that segment.</p>",
        "related_terms": [("Customer Lifetime Value (CLV)", "customer-lifetime-value"), ("Ideal Customer Profile (ICP)", "ideal-customer-profile"), ("Firmographic Data", "firmographic-data")],
        "related_resources": [("Customer Segmentation Use Case", "/use-cases/customer-segmentation/"), ("Customer Segmentation Analysis", "/analysis/customer-segmentation/"), ("Marketing Segmentation", "/use-cases/marketing-segmentation/")],
        "cta_headline": "Need to segment your customers?",
        "cta_text": "We'll enrich your customer data with firmographics, technographics, and behavioral data so your segments are based on real attributes, not guesses.",
    },
    {
        "slug": "data-append",
        "term": "Data Append",
        "meta_desc": "Data append adds missing information to existing records by matching against external databases. Learn how appending works and what fields are typically added.",
        "definition": '<p><strong>Data append</strong> (also called data appending) is the process of adding missing fields to your existing records by matching them against external data sources. You have a name and company; we append the email, phone number, job title, LinkedIn URL, company size, and industry. The original record stays intact. New fields get added alongside it.</p>',
        "why_matters": "<p>Every database has gaps. Forms capture some fields but not others. Data decays as people change jobs. Imports from different systems have different fields populated. Data append fills these gaps without requiring your team to manually research each record. A database with 60% field completion becomes 90%+ after appending, which means your lead scoring, routing, and segmentation actually work.</p>",
        "how_heading": "What Gets Appended",
        "how_items": [
            ("Contact fields", "Email addresses, direct phone numbers, mobile numbers, LinkedIn profiles"),
            ("Job details", "Current job title, department, seniority level, start date"),
            ("Company firmographics", "Employee count, revenue range, industry, headquarters, year founded"),
            ("Technographics", "CRM, marketing automation, analytics tools, and other technology in use"),
            ("Social profiles", "LinkedIn, Twitter, and other professional social media URLs"),
        ],
        "example": "<p>A sales team has 8,000 contacts with names and company names but only 3,000 have email addresses and 1,500 have phone numbers. After appending, 7,200 have verified emails and 5,800 have direct dial phone numbers. The team triples its reachable contacts without buying a single new lead.</p>",
        "related_terms": [("Data Enrichment", "data-enrichment"), ("Batch Enrichment", "batch-enrichment"), ("Fill Rate", "fill-rate")],
        "related_resources": [("Data Enrichment Services", "/services/data-enrichment.html"), ("Contact Enrichment", "/enrichment/contact-enrichment/"), ("B2B Data Enrichment", "/enrichment/b2b-data-enrichment/")],
        "cta_headline": "Missing fields in your database?",
        "cta_text": "We'll append emails, phones, titles, and firmographics to your existing records. Send us a sample and see what we can fill.",
    },
    {
        "slug": "data-governance",
        "term": "Data Governance",
        "meta_desc": "Data governance is the framework of policies and processes that ensure data quality, security, and usability across an organization. Learn what it includes and how to start.",
        "definition": '<p><strong>Data governance</strong> is the set of policies, processes, roles, and standards that control how data is collected, stored, maintained, and used across an organization. It answers questions like: Who can edit this field? What format should phone numbers use? How often should records be verified? Who decides what gets deleted? Good governance prevents the data chaos that makes CRMs unreliable.</p>',
        "why_matters": "<p>Without governance, every team enters data differently. Marketing uses \"Software\" as an industry while sales uses \"SaaS\" and \"Tech.\" One rep enters phone numbers with dashes, another with dots, another with nothing. Fields get repurposed for things they weren't designed for. Within a year, the database is so inconsistent that reporting is unreliable and automation breaks. Governance prevents this by setting rules before the mess happens.</p>",
        "how_heading": "Core Components of Data Governance",
        "how_items": [
            ("Data standards", "Define formats, picklist values, required fields, and naming conventions for every object in your CRM"),
            ("Ownership", "Assign a data steward or team responsible for maintaining quality and enforcing standards"),
            ("Access controls", "Determine who can create, edit, and delete records. Restrict sensitive fields to authorized roles"),
            ("Quality monitoring", "Set up dashboards that track completeness, accuracy, and duplication rates over time"),
            ("Lifecycle policies", "Define when records should be reviewed, archived, or removed based on age and activity"),
        ],
        "example": "<p>A 200-person company implements basic governance: required fields on lead creation, picklist-only values for Industry and Title, quarterly duplicate scans, and a data steward who reviews imports. Within 6 months, their CRM completeness goes from 55% to 88% and their marketing automation stops breaking on malformed data.</p>",
        "related_terms": [("CRM Hygiene", "crm-hygiene"), ("Data Quality Management", "data-quality-management"), ("Data Standardization", "data-standardization")],
        "related_resources": [("Data Governance Without a Team", "/resources/data-governance-without-team.html"), ("Data Quality Management", "/cleaning/data-quality-management/"), ("CRM Data Cleaning", "/cleaning/crm-data-cleaning/")],
        "cta_headline": "No data governance yet?",
        "cta_text": "We'll audit your CRM, fix what's broken, and give you a framework to keep it clean going forward.",
    },
    {
        "slug": "data-hygiene",
        "term": "Data Hygiene",
        "meta_desc": "Data hygiene is the ongoing practice of keeping your database clean, accurate, and complete. Learn why it matters and what a hygiene routine includes.",
        "definition": '<p><strong>Data hygiene</strong> is the ongoing practice of maintaining clean, accurate, and usable data in your business systems. It includes regular deduplication, email verification, field standardization, and removal of outdated or incomplete records. Think of it as preventive maintenance for your database: if you don\'t do it regularly, small problems accumulate into systemic issues.</p>',
        "why_matters": "<p>B2B data decays at roughly 30% per year. People change jobs, companies get acquired, phone numbers disconnect, email addresses bounce. A database that was clean in January is 7-8% degraded by April. Without regular hygiene, your sales team spends more time chasing bad data than having conversations. Your marketing campaigns hit spam traps. Your reports show pipeline that doesn't actually exist.</p>",
        "how_heading": "What Data Hygiene Includes",
        "how_items": [
            ("Regular deduplication", "Run duplicate scans monthly or quarterly to catch records created through imports, form fills, and integrations"),
            ("Email verification", "Verify email deliverability quarterly. Remove hard bounces. Flag catch-all domains"),
            ("Field standardization", "Enforce consistent formats for phone numbers, addresses, titles, and company names"),
            ("Completeness audits", "Identify and fill records missing critical fields like email, phone, or industry"),
            ("Decay monitoring", "Track the rate at which your data degrades and schedule cleaning cycles accordingly"),
        ],
        "example": "<p>A company with 40,000 CRM records does quarterly hygiene. Each quarter they find and merge 800 duplicates, verify and remove 1,200 dead email addresses, and update 2,000 records where contacts changed jobs. Their deliverability stays above 95% and their sales team trusts the data enough to actually use it.</p>",
        "related_terms": [("CRM Hygiene", "crm-hygiene"), ("Data Decay", "data-decay"), ("Data Governance", "data-governance")],
        "related_resources": [("How to Build a Data Hygiene Strategy", "/resources/how-to-build-data-hygiene-strategy.html"), ("Data Hygiene for Marketing Ops", "/resources/data-hygiene-for-marketing-ops.html"), ("Data Hygiene Services", "/cleaning/data-hygiene/")],
        "cta_headline": "When's the last time your data got cleaned?",
        "cta_text": "We'll run a full hygiene pass on your database and set up a schedule to keep it from decaying again.",
    },
    {
        "slug": "data-integration",
        "term": "Data Integration",
        "meta_desc": "Data integration combines data from multiple systems into a unified view. Learn the common approaches and why data quality makes or breaks integration projects.",
        "definition": '<p><strong>Data integration</strong> is the process of combining data from multiple systems, CRM, marketing automation, support tools, product analytics, billing, into a unified and consistent view. It can be as simple as syncing two tools via an API or as complex as building a data warehouse that ingests from 15 sources. The goal is the same: get all your data in one place so teams can see the full picture.</p>',
        "why_matters": "<p>The average company uses 130+ SaaS tools. Customer data lives in all of them. Without integration, your sales team can't see support tickets. Marketing can't see product usage. Finance can't see pipeline. Everyone makes decisions with partial information. Integration fixes this, but only if the underlying data is clean. Integrating dirty data just spreads the mess across more systems faster.</p>",
        "how_heading": "Common Integration Approaches",
        "how_items": [
            ("Point-to-point sync", "Direct connections between two tools, like Salesforce-to-HubSpot sync. Simple but doesn't scale past a few integrations"),
            ("iPaaS platforms", "Middleware tools like Workato, Zapier, or Tray.io that connect multiple systems through a central hub"),
            ("Data warehouse", "Extract data from all sources into a central warehouse (Snowflake, BigQuery) for unified reporting"),
            ("Customer data platform", "CDPs unify customer-level data specifically, building profiles from behavioral and transactional data"),
            ("Custom ETL", "Extract, transform, load pipelines built for specific business needs when off-the-shelf tools don't fit"),
        ],
        "example": "<p>A company integrates Salesforce, HubSpot, Intercom, and Stripe into Snowflake. Before integration, the sales team couldn't see which leads had active support tickets. After integration, reps get a flag when a prospect's company already has 3 open tickets, and they adjust their pitch accordingly.</p>",
        "related_terms": [("Customer Data Platform (CDP)", "customer-data-platform"), ("Master Data Management", "master-data-management"), ("Data Migration", "data-migration")],
        "related_resources": [("Data Integration Use Case", "/use-cases/data-integration/"), ("Data Migration", "/use-cases/data-migration/"), ("CRM Migration Cleanup", "/resources/crm-migration-data-cleanup.html")],
        "cta_headline": "Integrating your systems?",
        "cta_text": "Clean your data before you connect it. We'll standardize, deduplicate, and enrich so your integrations start with accurate records.",
    },
    {
        "slug": "data-migration",
        "term": "Data Migration",
        "meta_desc": "Data migration moves data from one system to another. Learn why migrations fail, how to prepare your data, and what cleaning to do before and after the move.",
        "definition": '<p><strong>Data migration</strong> is the process of moving data from one system to another, typically during a CRM switch, platform upgrade, or system consolidation. It involves extracting data from the old system, transforming it to match the new system\'s schema, cleaning it, and loading it into the new environment. Migrations are high-stakes: if you bring dirty data into a new system, you\'ve just paid for a clean start and filled it with the same problems.</p>',
        "why_matters": "<p>CRM migrations are the single best opportunity to fix years of accumulated data problems. You're moving everything anyway. This is the time to deduplicate, standardize, verify emails, update job titles, and purge records that should have been deleted years ago. Teams that skip this step spend the first 6 months in their new CRM fighting the same data quality issues they had in the old one.</p>",
        "how_heading": "Migration Data Prep Steps",
        "how_items": [
            ("Audit before you move", "Profile your existing data to understand completeness, duplication rates, and decay. Know what you're working with"),
            ("Deduplicate first", "Merge duplicates before migration. It's much harder to deduplicate after records are in a new system with new IDs"),
            ("Standardize fields", "Map field names, picklist values, and formats between old and new systems. 'Industry' in system A needs to match 'Sector' in system B"),
            ("Verify contact data", "Run email verification and phone validation. Don't migrate bounced emails or disconnected numbers"),
            ("Test with a sample", "Migrate 1,000 records first. Check field mapping, data integrity, and automation triggers before doing the full load"),
        ],
        "example": "<p>A company migrates from Salesforce to HubSpot. Their Salesforce has 85,000 contacts. Pre-migration cleaning removes 12,000 duplicates, flags 8,000 bounced emails for removal, and standardizes 15,000 inconsistent job titles. They migrate 65,000 clean records. Their HubSpot starts with higher data quality than their Salesforce ever had.</p>",
        "related_terms": [("Data Integration", "data-integration"), ("Data Deduplication", "data-deduplication"), ("Data Normalization", "data-normalization")],
        "related_resources": [("CRM Migration Data Cleanup", "/resources/crm-migration-data-cleanup.html"), ("Data Migration Use Case", "/use-cases/data-migration/"), ("CRM Migration", "/use-cases/crm-migration/")],
        "cta_headline": "Migrating CRMs?",
        "cta_text": "Don't bring dirty data into a clean system. We'll prep your database before the move so you start fresh.",
    },
    {
        "slug": "data-profiling",
        "term": "Data Profiling",
        "meta_desc": "Data profiling analyzes your database to assess completeness, accuracy, consistency, and duplication rates. Learn what profiling reveals and when to do it.",
        "definition": '<p><strong>Data profiling</strong> is the process of examining your database to understand its quality, structure, and content. It answers fundamental questions: What percentage of records have email addresses? How many duplicates exist? Are phone numbers formatted consistently? Which fields have the most gaps? Profiling gives you the diagnostic picture before you start cleaning, like getting an X-ray before surgery.</p>',
        "why_matters": "<p>You can't fix what you haven't measured. Most teams assume their data is \"pretty good\" until profiling reveals that 40% of records are missing phone numbers, 18% of emails bounce, and 12% of accounts are duplicates. Profiling quantifies the problem and tells you where to focus cleaning efforts first. It also establishes a baseline so you can measure improvement after cleaning.</p>",
        "how_heading": "What Profiling Measures",
        "how_items": [
            ("Completeness", "What percentage of records have values in each field? Which fields have the most gaps?"),
            ("Accuracy", "Do email addresses actually deliver? Do phone numbers connect? Are job titles current?"),
            ("Consistency", "Are formats standardized? Does 'New York' appear as 'NY,' 'New York,' 'new york,' and 'NYC'?"),
            ("Duplication", "What's the duplicate rate? How many records share the same email, phone, or name+company combination?"),
            ("Freshness", "When were records last updated? What percentage haven't been touched in over a year?"),
        ],
        "example": "<p>A company profiles their 50,000-record CRM before a migration. Results: 72% have emails (but 15% of those bounce), 45% have phone numbers, 88% have company names, 12% are duplicates, and 8,000 records haven't been updated in two years. They now know exactly what needs fixing and can estimate the effort before starting.</p>",
        "related_terms": [("Data Quality Management", "data-quality-management"), ("Data Governance", "data-governance"), ("Fill Rate", "fill-rate")],
        "related_resources": [("Data Quality Metrics", "/resources/data-quality-metrics.html"), ("Data Quality Roadmap", "/resources/data-quality-roadmap.html"), ("Data Quality Assessment", "/assessment/")],
        "cta_headline": "Don't know the state of your data?",
        "cta_text": "We'll profile your database and show you exactly where the problems are before we fix them.",
    },
]

if __name__ == "__main__":
    created = 0
    for t in TERMS:
        slug_dir = os.path.join(GLOSSARY_DIR, t["slug"])
        os.makedirs(slug_dir, exist_ok=True)
        html = generate_page(
            t["slug"], t["term"], t["meta_desc"], t["definition"],
            t["why_matters"], t["how_heading"], t["how_items"], t["example"],
            t["related_terms"], t["related_resources"], t["cta_headline"], t["cta_text"]
        )
        with open(os.path.join(slug_dir, "index.html"), "w") as f:
            f.write(html)
        created += 1
        print(f"  Created: glossary/{t['slug']}/index.html")

    print(f"\nBatch 1 complete: {created} glossary pages created.")
