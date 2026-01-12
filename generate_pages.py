#!/usr/bin/env python3
"""
Verum Website - Programmatic Page Generator
Generates 265+ SEO pages from templates
"""

import os
from datetime import datetime

# Configuration
BASE_URL = "https://veruminc.com"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Data definitions
INDUSTRIES = [
    ("healthcare", "Healthcare", "healthcare companies", "HIPAA compliance and patient data security"),
    ("fintech", "Fintech", "financial technology companies", "regulatory compliance and financial accuracy"),
    ("saas", "SaaS", "SaaS companies", "subscription metrics and customer lifecycle"),
    ("ecommerce", "E-commerce", "e-commerce businesses", "customer purchase behavior and inventory data"),
    ("real-estate", "Real Estate", "real estate companies", "property data and agent networks"),
    ("insurance", "Insurance", "insurance companies", "policy holder data and risk assessment"),
    ("legal", "Legal", "law firms", "client confidentiality and case management"),
    ("manufacturing", "Manufacturing", "manufacturing companies", "supply chain and vendor relationships"),
    ("retail", "Retail", "retail businesses", "customer loyalty and store performance"),
    ("education", "Education", "educational institutions", "student records and enrollment data"),
    ("nonprofit", "Non-profit", "non-profit organizations", "donor management and grant tracking"),
    ("logistics", "Logistics", "logistics companies", "shipment tracking and carrier data"),
    ("professional-services", "Professional Services", "professional service firms", "client relationships and project data"),
    ("technology", "Technology", "technology companies", "product usage and developer ecosystems"),
    ("cybersecurity", "Cybersecurity", "cybersecurity companies", "threat intelligence and compliance"),
    ("ai-ml", "AI & ML", "AI and machine learning companies", "training data and model performance"),
    ("martech", "Martech", "marketing technology companies", "campaign performance and attribution"),
    ("hr-tech", "HR Tech", "HR technology companies", "employee data and talent pipelines"),
    ("adtech", "Adtech", "advertising technology companies", "audience targeting and campaign data"),
    ("telecommunications", "Telecommunications", "telecom companies", "subscriber data and network performance"),
    ("energy", "Energy", "energy companies", "utility data and sustainability metrics"),
    ("media", "Media & Entertainment", "media companies", "audience engagement and content performance"),
    ("travel", "Travel & Hospitality", "travel companies", "booking data and guest preferences"),
    ("construction", "Construction", "construction companies", "project data and contractor networks"),
    ("b2b-services", "B2B Services", "B2B service companies", "client retention and service delivery"),
]

ENRICHMENT_TYPES = [
    ("linkedin-profile-enrichment", "LinkedIn Profile Enrichment", "Append LinkedIn profile URLs and data to your contact records", "linkedin profiles"),
    ("facebook-profile-enrichment", "Facebook Profile Enrichment", "Find and match Facebook profiles for your B2B contacts", "facebook profiles"),
    ("instagram-profile-enrichment", "Instagram Profile Enrichment", "Discover Instagram profiles linked to business contacts", "instagram profiles"),
    ("twitter-profile-enrichment", "Twitter Profile Enrichment", "Match Twitter/X handles to your contact database", "twitter profiles"),
    ("social-media-enrichment", "Social Media Enrichment", "Comprehensive social profile matching across all platforms", "social media profiles"),
    ("email-enrichment", "Email Enrichment", "Find and verify email addresses for your contacts", "email addresses"),
    ("email-finder", "Email Finder", "Discover email addresses from names and company domains", "email addresses"),
    ("phone-number-enrichment", "Phone Number Enrichment", "Append direct phone numbers to your contact records", "phone numbers"),
    ("direct-dial-enrichment", "Direct Dial Enrichment", "Find direct dial numbers that bypass the front desk", "direct dials"),
    ("mobile-number-enrichment", "Mobile Number Enrichment", "Append mobile phone numbers for SMS and direct outreach", "mobile numbers"),
    ("contact-enrichment", "Contact Enrichment", "Complete contact record enrichment with all available data points", "contact data"),
    ("company-enrichment", "Company Enrichment", "Append firmographic data to your account records", "company data"),
    ("firmographic-enrichment", "Firmographic Enrichment", "Add company size, revenue, industry, and location data", "firmographics"),
    ("company-size-enrichment", "Company Size Enrichment", "Append employee count and company size ranges", "company size data"),
    ("employee-count-enrichment", "Employee Count Enrichment", "Get accurate employee counts for lead scoring", "employee counts"),
    ("company-revenue-enrichment", "Company Revenue Enrichment", "Append estimated annual revenue to accounts", "revenue data"),
    ("company-funding-enrichment", "Company Funding Enrichment", "Track funding rounds, amounts, and investors", "funding data"),
    ("funding-round-enrichment", "Funding Round Enrichment", "Identify recent funding rounds and investment activity", "funding rounds"),
    ("investor-enrichment", "Investor Enrichment", "Discover investors and board members for target accounts", "investor data"),
    ("company-location-enrichment", "Company Location Enrichment", "Append headquarters and office locations", "location data"),
    ("headquarters-enrichment", "Headquarters Enrichment", "Find company HQ addresses for territory mapping", "HQ addresses"),
    ("industry-classification-enrichment", "Industry Classification Enrichment", "Standardize industry codes across your database", "industry codes"),
    ("sic-code-enrichment", "SIC Code Enrichment", "Append SIC codes for accurate industry targeting", "SIC codes"),
    ("naics-code-enrichment", "NAICS Code Enrichment", "Add NAICS codes for precise industry classification", "NAICS codes"),
    ("technographic-enrichment", "Technographic Enrichment", "Discover the technology stack of target companies", "technographics"),
    ("tech-stack-enrichment", "Tech Stack Enrichment", "Identify software and tools companies use", "tech stack data"),
    ("technology-enrichment", "Technology Enrichment", "Append technology usage data for better targeting", "technology data"),
    ("crm-detection", "CRM Detection", "Identify which CRM systems companies are using", "CRM usage"),
    ("marketing-automation-detection", "Marketing Automation Detection", "Discover marketing automation platforms in use", "martech usage"),
    ("website-technology-enrichment", "Website Technology Enrichment", "Analyze websites to identify technologies used", "web technologies"),
    ("intent-data-enrichment", "Intent Data Enrichment", "Identify accounts showing buying intent signals", "intent signals"),
    ("buyer-intent-enrichment", "Buyer Intent Enrichment", "Track in-market buyers for timely outreach", "buyer intent"),
    ("buying-signals-enrichment", "Buying Signals Enrichment", "Detect signals indicating purchase readiness", "buying signals"),
    ("job-title-enrichment", "Job Title Enrichment", "Standardize and enrich job titles for targeting", "job titles"),
    ("seniority-enrichment", "Seniority Enrichment", "Classify contacts by seniority level", "seniority data"),
    ("department-enrichment", "Department Enrichment", "Identify departments for better routing", "department data"),
    ("decision-maker-enrichment", "Decision Maker Enrichment", "Identify decision makers within accounts", "decision makers"),
    ("c-suite-enrichment", "C-Suite Enrichment", "Find and enrich C-level executive contacts", "C-suite contacts"),
    ("domain-enrichment", "Domain Enrichment", "Append company data from domain lookups", "domain data"),
    ("website-enrichment", "Website Enrichment", "Extract and enrich data from company websites", "website data"),
    ("address-enrichment", "Address Enrichment", "Standardize and complete address information", "address data"),
    ("b2b-data-enrichment", "B2B Data Enrichment", "Comprehensive B2B data enrichment for all use cases", "B2B data"),
    ("lead-enrichment", "Lead Enrichment", "Enrich inbound leads with complete contact and company data", "lead data"),
]

CLEANING_TYPES = [
    ("data-deduplication", "Data Deduplication", "Remove duplicate records and merge the best data", "duplicate records"),
    ("duplicate-detection", "Duplicate Detection", "Identify and flag duplicate contacts and accounts", "duplicates"),
    ("record-matching", "Record Matching", "Match and merge records across multiple data sources", "record matching"),
    ("email-validation", "Email Validation", "Verify email addresses are real and deliverable", "email validation"),
    ("email-verification", "Email Verification", "Check email deliverability and remove invalid addresses", "email verification"),
    ("data-standardization", "Data Standardization", "Standardize formats across your entire database", "data formats"),
    ("data-normalization", "Data Normalization", "Normalize data fields for consistent reporting", "data normalization"),
    ("phone-formatting", "Phone Formatting", "Standardize phone number formats across regions", "phone formats"),
    ("address-normalization", "Address Normalization", "Standardize and validate address information", "address formats"),
    ("name-parsing", "Name Parsing", "Parse and structure name fields correctly", "name parsing"),
    ("company-name-standardization", "Company Name Standardization", "Standardize company names and legal entities", "company names"),
    ("job-title-normalization", "Job Title Normalization", "Normalize job titles to standard categories", "job titles"),
    ("crm-data-cleaning", "CRM Data Cleaning", "Complete CRM data cleanup and optimization", "CRM data"),
    ("database-cleanup", "Database Cleanup", "Full database cleanup and quality improvement", "database cleanup"),
    ("email-list-cleaning", "Email List Cleaning", "Clean email lists for better deliverability", "email lists"),
    ("contact-list-cleaning", "Contact List Cleaning", "Clean and validate your contact lists", "contact lists"),
    ("lead-data-cleaning", "Lead Data Cleaning", "Clean inbound leads for better conversion", "lead data"),
    ("data-quality-management", "Data Quality Management", "Ongoing data quality monitoring and improvement", "data quality"),
    ("data-hygiene", "Data Hygiene", "Maintain clean, accurate data over time", "data hygiene"),
    ("data-validation", "Data Validation", "Validate data accuracy and completeness", "data validation"),
]

USE_CASES = [
    ("crm-hygiene", "CRM Hygiene", "Keep your CRM clean and your data accurate", "CRM data quality"),
    ("sales-prospecting", "Sales Prospecting", "Give your sales team accurate data for outreach", "sales prospecting"),
    ("lead-routing", "Lead Routing", "Route leads accurately based on complete data", "lead routing"),
    ("territory-planning", "Territory Planning", "Plan territories with accurate company data", "territory planning"),
    ("pipeline-management", "Pipeline Management", "Manage pipeline with clean, enriched data", "pipeline management"),
    ("account-management", "Account Management", "Maintain complete account records", "account management"),
    ("abm-targeting", "ABM Targeting", "Target accounts with complete firmographic data", "ABM targeting"),
    ("marketing-segmentation", "Marketing Segmentation", "Segment audiences with rich data attributes", "marketing segmentation"),
    ("customer-segmentation", "Customer Segmentation", "Segment customers for targeted engagement", "customer segmentation"),
    ("email-marketing-cleanup", "Email Marketing Cleanup", "Clean email lists for better deliverability", "email marketing"),
    ("campaign-targeting", "Campaign Targeting", "Target campaigns with accurate data", "campaign targeting"),
    ("lead-scoring", "Lead Scoring", "Score leads accurately with complete data", "lead scoring"),
    ("lead-qualification", "Lead Qualification", "Qualify leads with enriched firmographics", "lead qualification"),
    ("revenue-intelligence", "Revenue Intelligence", "Power revenue insights with clean data", "revenue intelligence"),
    ("customer-data-platform", "Customer Data Platform", "Feed your CDP with clean, enriched data", "CDP data"),
    ("data-migration", "Data Migration", "Clean data before migrating to new systems", "data migration"),
    ("crm-migration", "CRM Migration", "Prepare data for CRM migrations", "CRM migration"),
    ("database-merge", "Database Merge", "Merge databases after acquisitions", "database merging"),
    ("data-integration", "Data Integration", "Integrate data across multiple systems", "data integration"),
    ("master-data-management", "Master Data Management", "Maintain a single source of truth", "master data"),
    ("icp-development", "ICP Development", "Develop your Ideal Customer Profile with data", "ICP development"),
    ("customer-profiling", "Customer Profiling", "Build detailed customer profiles", "customer profiling"),
    ("market-sizing", "Market Sizing", "Size your total addressable market", "market sizing"),
    ("tam-sam-som-analysis", "TAM SAM SOM Analysis", "Calculate your market opportunity", "market analysis"),
    ("lookalike-modeling", "Lookalike Modeling", "Find lookalike companies to your best customers", "lookalike modeling"),
    ("business-prospecting", "Business Prospecting", "Find and enrich business prospects", "business prospecting"),
    ("local-business-lists", "Local Business Lists", "Build targeted local business lists", "local businesses"),
    ("smb-targeting", "SMB Targeting", "Target small and medium businesses effectively", "SMB targeting"),
    ("franchise-prospecting", "Franchise Prospecting", "Find franchise owners and opportunities", "franchise prospecting"),
]

BUSINESS_FIND = [
    ("healthcare-businesses", "Healthcare Businesses", "Find and enrich healthcare company data", "healthcare businesses"),
    ("dental-practices", "Dental Practices", "Discover dental practices and their owners", "dental practices"),
    ("medical-practices", "Medical Practices", "Find medical practices and physician data", "medical practices"),
    ("mental-health-practices", "Mental Health Practices", "Locate mental health providers and practices", "mental health practices"),
    ("law-firms", "Law Firms", "Find law firms and attorney contact data", "law firms"),
    ("accounting-firms", "Accounting Firms", "Discover accounting firms and CPAs", "accounting firms"),
    ("real-estate-agencies", "Real Estate Agencies", "Find real estate agencies and agents", "real estate agencies"),
    ("insurance-agencies", "Insurance Agencies", "Locate insurance agencies and agents", "insurance agencies"),
    ("financial-advisors", "Financial Advisors", "Find financial advisors and wealth managers", "financial advisors"),
    ("marketing-agencies", "Marketing Agencies", "Discover marketing and advertising agencies", "marketing agencies"),
    ("construction-companies", "Construction Companies", "Find construction companies and contractors", "construction companies"),
    ("manufacturing-companies", "Manufacturing Companies", "Locate manufacturers and suppliers", "manufacturing companies"),
    ("restaurants", "Restaurants", "Find restaurants and food service businesses", "restaurants"),
    ("retail-stores", "Retail Stores", "Discover retail businesses and store owners", "retail stores"),
    ("auto-dealerships", "Auto Dealerships", "Find auto dealers and their leadership", "auto dealerships"),
    ("business-owner-contact-info", "Business Owner Contact Info", "Find contact information for business owners", "business owner contacts"),
    ("small-business-owners", "Small Business Owners", "Locate and contact small business owners", "small business owners"),
    ("healthcare-business-owners", "Healthcare Business Owners", "Find owners of healthcare businesses", "healthcare owners"),
    ("dental-practice-owners", "Dental Practice Owners", "Contact dental practice owners directly", "dental practice owners"),
    ("law-firm-partners", "Law Firm Partners", "Find and contact law firm partners", "law firm partners"),
    ("restaurant-owners", "Restaurant Owners", "Reach restaurant owners and operators", "restaurant owners"),
    ("retail-store-owners", "Retail Store Owners", "Find retail business owners", "retail store owners"),
    ("franchise-owners", "Franchise Owners", "Locate franchise owners across brands", "franchise owners"),
    ("agency-owners", "Agency Owners", "Find marketing and creative agency owners", "agency owners"),
    ("medical-practice-owners", "Medical Practice Owners", "Contact medical practice owners", "medical practice owners"),
]

ANALYSIS_TYPES = [
    ("icp-analysis", "ICP Analysis", "Build your Ideal Customer Profile with data", "ICP analysis"),
    ("ideal-customer-profile", "Ideal Customer Profile", "Define and refine your ideal customer", "ideal customer profile"),
    ("customer-segmentation", "Customer Segmentation Analysis", "Segment your customers for targeted strategies", "customer segmentation"),
    ("market-analysis", "Market Analysis", "Analyze your market opportunity", "market analysis"),
    ("competitor-analysis", "Competitor Analysis", "Understand your competitive landscape", "competitor analysis"),
    ("win-loss-analysis", "Win-Loss Analysis", "Learn from won and lost deals", "win-loss analysis"),
    ("churn-analysis", "Churn Analysis", "Identify churn patterns and prevention strategies", "churn analysis"),
    ("customer-lifetime-value", "Customer Lifetime Value", "Calculate and optimize CLV", "customer lifetime value"),
    ("lead-scoring-model", "Lead Scoring Model", "Build data-driven lead scoring", "lead scoring"),
    ("icp-analysis-for-startups", "ICP Analysis for Startups", "Define your ICP before scaling", "startup ICP"),
    ("icp-analysis-for-saas", "ICP Analysis for SaaS", "SaaS-specific ICP development", "SaaS ICP"),
    ("icp-analysis-for-series-a", "ICP Analysis for Series A", "Pre-Series A ICP development", "Series A ICP"),
    ("cmo-data-analysis", "CMO Data Analysis", "Marketing analytics for CMOs", "CMO analytics"),
    ("sales-data-analysis", "Sales Data Analysis", "Sales performance analytics", "sales analytics"),
    ("revenue-analysis", "Revenue Analysis", "Revenue trends and forecasting", "revenue analysis"),
    ("healthcare-market-analysis", "Healthcare Market Analysis", "Healthcare industry market insights", "healthcare market"),
    ("fintech-market-analysis", "Fintech Market Analysis", "Fintech industry market insights", "fintech market"),
    ("saas-market-analysis", "SaaS Market Analysis", "SaaS industry market insights", "SaaS market"),
    ("ecommerce-market-analysis", "E-commerce Market Analysis", "E-commerce market insights", "ecommerce market"),
]

COMPARISONS = [
    ("verum-vs-zoominfo", "Verum vs ZoomInfo", "How Verum compares to ZoomInfo for data enrichment"),
    ("verum-vs-clearbit", "Verum vs Clearbit", "How Verum compares to Clearbit for B2B data"),
    ("verum-vs-apollo", "Verum vs Apollo", "How Verum compares to Apollo.io for sales intelligence"),
    ("verum-vs-lusha", "Verum vs Lusha", "How Verum compares to Lusha for contact data"),
    ("verum-vs-cognism", "Verum vs Cognism", "How Verum compares to Cognism for B2B data"),
]

ALTERNATIVES = [
    ("zoominfo-alternative", "ZoomInfo Alternative", "Looking for a ZoomInfo alternative? Consider Verum."),
    ("clearbit-alternative", "Clearbit Alternative", "Looking for a Clearbit alternative? Consider Verum."),
    ("apollo-alternative", "Apollo Alternative", "Looking for an Apollo.io alternative? Consider Verum."),
    ("lusha-alternative", "Lusha Alternative", "Looking for a Lusha alternative? Consider Verum."),
]


def get_page_template(title, description, canonical_path, h1, content_html, keywords=""):
    """Generate a full HTML page from template"""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Verum</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">

  <link rel="canonical" href="{BASE_URL}{canonical_path}">
  <link rel="icon" href="/assets/logos/verum-favicon-32.svg" type="image/svg+xml">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css">

  <meta property="og:type" content="website">
  <meta property="og:url" content="{BASE_URL}{canonical_path}">
  <meta property="og:title" content="{title} | Verum">
  <meta property="og:description" content="{description}">
  <meta property="og:site_name" content="Verum">
  <meta property="og:image" content="{BASE_URL}/assets/social-preview.png">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | Verum">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{BASE_URL}/assets/social-preview.png">

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
</head>
<body>
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="header__logo">
        <img src="/assets/logos/logos-svg/verum-logo-horizontal-dark.svg" alt="Verum" width="120" height="32">
      </a>
      <nav class="nav nav--desktop">
        <ul class="nav__list">
          <li><a href="/services/" class="nav__link">Services</a></li>
          <li><a href="/solutions/" class="nav__link">Solutions</a></li>
          <li><a href="/pricing.html" class="nav__link">Pricing</a></li>
          <li><a href="/about.html" class="nav__link">About</a></li>
        </ul>
      </nav>
      <a href="/#contact" class="btn btn--primary btn--sm header__cta">Clean My Data</a>
      <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span class="menu-toggle__icon"></span>
      </button>
      <nav class="nav nav--mobile">
        <ul class="nav__list">
          <li><a href="/services/" class="nav__link">Services</a></li>
          <li><a href="/solutions/" class="nav__link">Solutions</a></li>
          <li><a href="/pricing.html" class="nav__link">Pricing</a></li>
          <li><a href="/about.html" class="nav__link">About</a></li>
        </ul>
        <a href="/#contact" class="btn btn--primary">Clean My Data</a>
      </nav>
    </div>
  </header>

  <section class="page-hero">
    <div class="container">
      <h1 class="page-hero__title">{h1}</h1>
    </div>
  </section>

  <section class="content">
    <div class="container" style="max-width: 800px;">
      {content_html}
      <div class="text-center mt-xl">
        <a href="/#contact" class="btn btn--primary btn--lg">Get Started</a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="/assets/logos/logos-svg/verum-logo-horizontal-dark.svg" alt="Verum" class="footer__logo" width="120" height="32">
          <p class="footer__tagline">Enterprise data cleaning and enrichment you can trust.</p>
        </div>
        <div>
          <h4 class="footer__heading">Services</h4>
          <ul class="footer__links">
            <li><a href="/services/data-cleaning.html">Data Cleaning</a></li>
            <li><a href="/services/data-enrichment.html">Data Enrichment</a></li>
            <li><a href="/services/data-analysis.html">Data Analysis</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer__heading">Company</h4>
          <ul class="footer__links">
            <li><a href="/about.html">About</a></li>
            <li><a href="/pricing.html">Pricing</a></li>
            <li><a href="/contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer__heading">Legal</h4>
          <ul class="footer__links">
            <li><a href="/privacy.html">Privacy Policy</a></li>
            <li><a href="/terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <p>&copy; 2025 Verum Inc. All rights reserved.</p>
        <div class="footer__social">
          <a href="https://www.linkedin.com/company/verumai/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>'''


def generate_industry_pages():
    """Generate industry + service pages"""
    pages = []
    for slug, name, plural, focus in INDUSTRIES:
        # Data Enrichment page
        path = f"/solutions/{slug}-data-enrichment/"
        title = f"{name} Data Enrichment"
        desc = f"Data enrichment services for {plural}. Append firmographic, technographic, and contact data focused on {focus}."
        content = f'''
<h2>{name} Data Enrichment</h2>
<p>Verum provides specialized data enrichment for {plural}. We understand the unique data needs of the {name.lower()} industry, including {focus}.</p>

<h2>What We Enrich</h2>
<ul>
  <li>Company firmographics (size, revenue, locations)</li>
  <li>Contact information (email, phone, LinkedIn)</li>
  <li>Technographic data (tech stack, tools in use)</li>
  <li>Industry-specific data points</li>
</ul>

<h2>Why {name} Companies Choose Verum</h2>
<p>We specialize in {focus}, ensuring your data meets industry standards and enables better targeting, personalization, and outreach.</p>
'''
        pages.append((path, title, desc, title, content, f"{name.lower()}, data enrichment, {focus}"))

        # Data Cleaning page
        path = f"/solutions/{slug}-data-cleaning/"
        title = f"{name} Data Cleaning"
        desc = f"Data cleaning services for {plural}. Remove duplicates, validate emails, and standardize records with focus on {focus}."
        content = f'''
<h2>{name} Data Cleaning</h2>
<p>Verum provides specialized data cleaning for {plural}. We understand the unique data challenges of the {name.lower()} industry, including {focus}.</p>

<h2>What We Clean</h2>
<ul>
  <li>Duplicate detection and merging</li>
  <li>Email validation and verification</li>
  <li>Data standardization and normalization</li>
  <li>Industry-specific field validation</li>
</ul>

<h2>Why {name} Companies Choose Verum</h2>
<p>We understand {focus}, ensuring your data is clean, accurate, and ready for your go-to-market efforts.</p>
'''
        pages.append((path, title, desc, title, content, f"{name.lower()}, data cleaning, {focus}"))

    return pages


def generate_enrichment_pages():
    """Generate enrichment type pages"""
    pages = []
    for slug, title, desc, data_type in ENRICHMENT_TYPES:
        path = f"/enrichment/{slug}/"
        content = f'''
<h2>{title}</h2>
<p>{desc}. Verum helps you append accurate {data_type} to your B2B database from 50+ trusted sources.</p>

<h2>How It Works</h2>
<ol>
  <li><strong>Send us your data</strong> - Share your contact or company records</li>
  <li><strong>We match and enrich</strong> - Our system finds and appends {data_type}</li>
  <li><strong>Get enriched data back</strong> - Receive complete records ready to use</li>
</ol>

<h2>Use Cases</h2>
<ul>
  <li>Sales prospecting and outreach</li>
  <li>Lead scoring and routing</li>
  <li>ABM targeting</li>
  <li>Marketing personalization</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{data_type}, enrichment, B2B data"))
    return pages


def generate_cleaning_pages():
    """Generate cleaning type pages"""
    pages = []
    for slug, title, desc, data_type in CLEANING_TYPES:
        path = f"/cleaning/{slug}/"
        content = f'''
<h2>{title}</h2>
<p>{desc}. Verum helps you maintain accurate, reliable {data_type} across your entire database.</p>

<h2>What We Do</h2>
<ul>
  <li>Identify and fix data quality issues</li>
  <li>Standardize formats and values</li>
  <li>Validate accuracy and completeness</li>
  <li>Merge and deduplicate records</li>
</ul>

<h2>Results</h2>
<ul>
  <li>Cleaner, more reliable data</li>
  <li>Better reporting and analytics</li>
  <li>Improved campaign performance</li>
  <li>Higher team productivity</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{data_type}, data cleaning, data quality"))
    return pages


def generate_use_case_pages():
    """Generate use case pages"""
    pages = []
    for slug, title, desc, keywords in USE_CASES:
        path = f"/use-cases/{slug}/"
        content = f'''
<h2>{title}</h2>
<p>{desc}. Verum provides the clean, enriched data you need for effective {keywords}.</p>

<h2>The Challenge</h2>
<p>Most teams struggle with {keywords} because their data is incomplete, outdated, or inconsistent. This leads to wasted effort and poor results.</p>

<h2>How Verum Helps</h2>
<ul>
  <li>Clean and deduplicate your existing data</li>
  <li>Enrich records with missing information</li>
  <li>Provide complete, accurate data for {keywords}</li>
  <li>Enable better targeting and personalization</li>
</ul>

<h2>Get Started</h2>
<p>Tell us about your {keywords} challenges and we'll show you how clean data can transform your results.</p>
'''
        pages.append((path, title, desc, title, content, f"{keywords}, use case, data quality"))
    return pages


def generate_find_pages():
    """Generate business discovery pages"""
    pages = []
    for slug, title, desc, data_type in BUSINESS_FIND:
        path = f"/find/{slug}/"
        content = f'''
<h2>{title}</h2>
<p>{desc}. Verum helps you build targeted lists of {data_type} with complete, accurate contact information.</p>

<h2>What You Get</h2>
<ul>
  <li>Verified business information</li>
  <li>Owner and decision-maker contacts</li>
  <li>Email addresses and phone numbers</li>
  <li>Company firmographics</li>
</ul>

<h2>Use Cases</h2>
<ul>
  <li>Sales prospecting</li>
  <li>Direct mail campaigns</li>
  <li>Local marketing</li>
  <li>Partnership development</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{data_type}, business lists, prospecting"))
    return pages


def generate_analysis_pages():
    """Generate analysis pages"""
    pages = []
    for slug, title, desc, keywords in ANALYSIS_TYPES:
        path = f"/analysis/{slug}/"
        content = f'''
<h2>{title}</h2>
<p>{desc}. Verum helps you understand your data and make better decisions with {keywords}.</p>

<h2>What We Analyze</h2>
<ul>
  <li>Customer patterns and segments</li>
  <li>Market opportunities</li>
  <li>Competitive positioning</li>
  <li>Growth potential</li>
</ul>

<h2>What You Get</h2>
<ul>
  <li>Data-driven insights</li>
  <li>Actionable recommendations</li>
  <li>Clear visualization of findings</li>
  <li>Strategic guidance</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{keywords}, data analysis, insights"))
    return pages


def generate_comparison_pages():
    """Generate comparison pages"""
    pages = []
    for slug, title, desc in COMPARISONS:
        path = f"/compare/{slug}/"
        competitor = title.split(" vs ")[1]
        content = f'''
<h2>{title}</h2>
<p>{desc}</p>

<h2>Why Consider Verum Over {competitor}?</h2>
<ul>
  <li><strong>Service-first approach</strong> - We handle the work so you don't have to</li>
  <li><strong>Quality over quantity</strong> - Accurate data, not just more data</li>
  <li><strong>Flexible engagement</strong> - Pay for what you need, when you need it</li>
  <li><strong>Human verification</strong> - Real people checking data quality</li>
</ul>

<h2>What We Offer</h2>
<ul>
  <li>Data cleaning (deduplication, validation, standardization)</li>
  <li>Data enrichment from 50+ sources</li>
  <li>ICP analysis and customer segmentation</li>
  <li>Custom data projects</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{competitor} alternative, data enrichment comparison"))
    return pages


def generate_alternative_pages():
    """Generate alternative pages"""
    pages = []
    for slug, title, desc in ALTERNATIVES:
        path = f"/alternatives/{slug}/"
        competitor = title.split(" ")[0]
        content = f'''
<h2>{title}</h2>
<p>{desc}</p>

<h2>Why Switch from {competitor}?</h2>
<ul>
  <li>Tired of self-serve tools that require your time?</li>
  <li>Frustrated with data quality issues?</li>
  <li>Looking for a more flexible engagement model?</li>
  <li>Need human expertise, not just automation?</li>
</ul>

<h2>What Makes Verum Different</h2>
<ul>
  <li><strong>We do the work</strong> - Not a self-serve platform</li>
  <li><strong>Quality focused</strong> - Human verification on every project</li>
  <li><strong>Full service</strong> - Cleaning, enrichment, and analysis</li>
  <li><strong>Fast turnaround</strong> - Results in 24-48 hours</li>
</ul>
'''
        pages.append((path, title, desc, title, content, f"{competitor} alternative, switch from {competitor}"))
    return pages


def generate_sitemap(all_pages):
    """Generate sitemap.xml"""
    today = datetime.now().strftime("%Y-%m-%d")

    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

    # Core pages
    core_pages = [
        ("/", "1.0", "weekly"),
        ("/about.html", "0.8", "monthly"),
        ("/contact.html", "0.8", "monthly"),
        ("/pricing.html", "0.8", "monthly"),
        ("/services/", "0.9", "weekly"),
        ("/services/data-cleaning.html", "0.9", "weekly"),
        ("/services/data-enrichment.html", "0.9", "weekly"),
        ("/services/data-analysis.html", "0.9", "weekly"),
    ]

    for path, priority, freq in core_pages:
        sitemap += f'''  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
'''

    # Programmatic pages
    for path, _, _, _, _, _ in all_pages:
        sitemap += f'''  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

    sitemap += '</urlset>'
    return sitemap


def write_page(path, content):
    """Write a page to disk"""
    # Convert path to file path
    if path.endswith('/'):
        file_path = os.path.join(OUTPUT_DIR, path.strip('/'), 'index.html')
    else:
        file_path = os.path.join(OUTPUT_DIR, path.strip('/'))

    # Create directory if needed
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        f.write(content)

    return file_path


def main():
    print("Generating Verum programmatic pages...")

    all_pages = []

    # Generate all page types
    print("  - Industry pages...")
    all_pages.extend(generate_industry_pages())

    print("  - Enrichment pages...")
    all_pages.extend(generate_enrichment_pages())

    print("  - Cleaning pages...")
    all_pages.extend(generate_cleaning_pages())

    print("  - Use case pages...")
    all_pages.extend(generate_use_case_pages())

    print("  - Business discovery pages...")
    all_pages.extend(generate_find_pages())

    print("  - Analysis pages...")
    all_pages.extend(generate_analysis_pages())

    print("  - Comparison pages...")
    all_pages.extend(generate_comparison_pages())

    print("  - Alternative pages...")
    all_pages.extend(generate_alternative_pages())

    print(f"\nTotal pages to generate: {len(all_pages)}")

    # Write all pages
    for path, title, desc, h1, content, keywords in all_pages:
        html = get_page_template(title, desc, path, h1, content, keywords)
        write_page(path, html)

    print(f"Generated {len(all_pages)} pages")

    # Generate sitemap
    print("\nGenerating sitemap.xml...")
    sitemap = generate_sitemap(all_pages)
    sitemap_path = os.path.join(OUTPUT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w') as f:
        f.write(sitemap)
    print(f"Sitemap generated with {len(all_pages) + 8} URLs")

    print("\nDone!")


if __name__ == "__main__":
    main()
