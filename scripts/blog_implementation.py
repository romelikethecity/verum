#!/usr/bin/env python3
"""Generate implementation-stage blog articles for Verum website."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from blog_articles import generate_article

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"

ARTICLES = [
    {
        "filename": "what-to-expect-data-cleaning-project.html",
        "title": "What to Expect from a Data Cleaning Project: Timeline, Process & Deliverables",
        "meta_desc": "What happens when you hire someone to clean your CRM data? A step-by-step walkthrough of the process, typical timelines, and what you should receive at the end.",
        "og_title": "What to Expect from a Data Cleaning Project",
        "canonical_slug": "what-to-expect-data-cleaning-project.html",
        "date": "2026-02-15",
        "category_label": "Implementation Guide",
        "hero_title": "What to Expect from a Data Cleaning Project",
        "hero_subtitle": "You've decided to clean your CRM. Here's what the process actually looks like from start to finish.",
        "read_time": "8",
        "faq_schema": [
            ("How long does a data cleaning project take?",
             "Most managed data cleaning projects take 3-7 business days for databases under 100,000 records. The timeline depends on scope: deduplication alone is fastest (2-3 days), while a full clean (dedup + email validation + phone verification + standardization) takes 5-7 days. Enrichment adds 1-2 days."),
            ("What should a data cleaning deliverable include?",
             "At minimum, you should receive: the cleaned data file in your CRM's import format, a change log showing what was modified, summary statistics (duplicates found, emails validated, fields standardized), and recommendations for preventing future data quality issues."),
            ("How do I prepare my CRM for a data cleaning project?",
             "Export your contacts, accounts, and leads as CSV files. Include all fields you want cleaned or standardized. Note any custom fields or picklist values. Identify which records are most critical (active deals, recent leads) so the provider can prioritize."),
        ],
        "content_html": """        <p>You've decided your CRM needs professional cleaning. Maybe the bounce rates forced the issue. Maybe a CRM migration is coming. Maybe your sales leader finally asked why the pipeline report doesn't add up.</p>

        <p>Whatever the trigger, you're about to hand your data to someone else. Here's what the process looks like so you know what to expect at each stage.</p>

        <h2>Stage 1: Scoping (Day 1)</h2>

        <p>Before any work starts, the provider needs to understand your database. A good scoping conversation covers:</p>

        <ul>
          <li><strong>Database size:</strong> How many contact, account, and lead records?</li>
          <li><strong>Known issues:</strong> Duplicates? Bouncing emails? Inconsistent job titles? Missing fields?</li>
          <li><strong>Services needed:</strong> Deduplication only? Full cleaning? Cleaning plus enrichment?</li>
          <li><strong>CRM platform:</strong> Salesforce, HubSpot, Dynamics, or other?</li>
          <li><strong>Custom requirements:</strong> Specific fields to standardize? Particular merge rules? Records to exclude?</li>
        </ul>

        <p>From this conversation, the provider should give you a fixed price and timeline. If they can't give you a number after understanding your scope, that's a red flag.</p>

        <h2>Stage 2: Data Export (Day 1-2)</h2>

        <p>You'll export your data from your CRM and send it to the provider. Most providers accept CSV or Excel files. A few can connect directly via API.</p>

        <p>What to export:</p>
        <ul>
          <li><strong>Contacts/Leads:</strong> All fields including name, email, phone, title, company, address</li>
          <li><strong>Accounts/Companies:</strong> Company name, industry, size, address, website</li>
          <li><strong>Include record IDs:</strong> So cleaned records can be matched back to your CRM on import</li>
        </ul>

        <div class="callout-box">
          <p><strong>Tip:</strong> Export more fields than you think you need. It's easier to ignore extra columns than to re-export because a needed field was missing.</p>
        </div>

        <h2>Stage 3: Processing (Days 2-6)</h2>

        <p>This is where the actual cleaning happens. A typical full-scope project runs through these steps in order:</p>

        <h3>Deduplication</h3>
        <p>Fuzzy matching identifies records that represent the same person or company despite differences in spelling, formatting, or completeness. Duplicate clusters are merged into golden records that keep the most complete and recent data from each duplicate.</p>

        <h3>Email Validation</h3>
        <p>Every email address is checked via SMTP verification. Results are categorized: valid, invalid (hard bounce), risky (catch-all domain), or role-based (info@, admin@). Invalid emails are flagged for removal.</p>

        <h3>Phone Verification</h3>
        <p>Phone numbers are checked against carrier databases. Disconnected numbers, landlines, and fax numbers are flagged separately from active direct dials and mobile numbers.</p>

        <h3>Field Standardization</h3>
        <p>Job titles, company names, addresses, and industry codes are normalized to consistent formats. "VP of Sales" and "Vice President, Sales" become the same value. State names and abbreviations become consistent.</p>

        <h3>Enrichment (if included)</h3>
        <p>Missing fields are filled from external data sources: phone numbers, email addresses, job titles, company size, industry, and other firmographic data.</p>

        <h2>Stage 4: Review (Day 6-7)</h2>

        <p>Before you import anything, the provider should deliver:</p>

        <ol>
          <li><strong>The cleaned data file</strong> formatted for your CRM's import tool</li>
          <li><strong>A change log</strong> showing what was modified, added, or flagged on each record</li>
          <li><strong>Summary statistics:</strong>
            <ul>
              <li>How many duplicates were found and merged</li>
              <li>How many emails were validated vs. flagged as invalid</li>
              <li>How many phone numbers were verified vs. disconnected</li>
              <li>How many fields were standardized</li>
              <li>Fill rate improvements from enrichment (if applicable)</li>
            </ul>
          </li>
          <li><strong>Recommendations</strong> for preventing the same issues from recurring</li>
        </ol>

        <p>Take time to spot-check 20-30 records against your CRM. Verify that merges were done correctly, that standardization makes sense for your use case, and that no critical data was lost.</p>

        <h2>Stage 5: Import (Day 7-8)</h2>

        <p>Import the cleaned data back into your CRM. Most providers deliver files formatted for your specific CRM's import tool (Salesforce Data Loader, HubSpot native import, etc.).</p>

        <p>Best practices for import:</p>
        <ul>
          <li><strong>Back up your CRM first.</strong> Always have a rollback point.</li>
          <li><strong>Import in batches</strong> if your database is large (50,000+ records). Start with a small batch to verify everything looks right.</li>
          <li><strong>Use record IDs for matching.</strong> Update existing records rather than creating new ones.</li>
          <li><strong>Test your automation</strong> after import. Make sure lead scoring, routing, and sequences still work with the standardized data.</li>
        </ul>

        <h2>What Good Looks Like After</h2>

        <p>Within a week of importing cleaned data, you should notice:</p>
        <ul>
          <li>Email bounce rates drop to under 3%</li>
          <li>List segmentation returns consistent counts</li>
          <li>Lead routing sends records to the right reps</li>
          <li>Reps stop complaining about finding the same prospect under three different records</li>
          <li>Pipeline reports start matching what your sales manager expects</li>
        </ul>

        <h2>Frequently Asked Questions</h2>

        <h3>How long does a data cleaning project take?</h3>
        <p>3-7 business days for databases under 100,000 records. Dedup only is 2-3 days. Full cleaning (dedup + email + phone + standardization) is 5-7 days.</p>

        <h3>What should a data cleaning deliverable include?</h3>
        <p>The cleaned file, a change log, summary statistics, and recommendations for preventing future issues. If a provider doesn't include a change log, ask for one.</p>

        <h3>How do I prepare my CRM for a data cleaning project?</h3>
        <p>Export contacts, accounts, and leads as CSV files with all fields. Include record IDs. Note any custom fields or special requirements.</p>""",
        "related_links": [
            ("Data Cleaning Services", "/services/data-cleaning.html"),
            ("CRM Cleaning Case Study", "/case-studies/crm-cleaning-staffing-agency/"),
            ("CRM Data Quality Checklist", "/resources/crm-data-quality-checklist.html"),
            ("Outsource vs. In-House", "/resources/outsource-data-cleaning-vs-in-house.html"),
        ],
    },
    {
        "filename": "prepare-crm-for-enrichment.html",
        "title": "How to Prepare Your CRM for Data Enrichment: A Pre-Project Checklist",
        "meta_desc": "Before enriching your CRM, clean it first. A pre-enrichment checklist covering deduplication, field mapping, record selection, and quality thresholds.",
        "og_title": "How to Prepare Your CRM for Data Enrichment",
        "canonical_slug": "prepare-crm-for-enrichment.html",
        "date": "2026-02-15",
        "category_label": "Implementation Guide",
        "hero_title": "How to Prepare Your CRM for Data Enrichment",
        "hero_subtitle": "Enriching dirty data makes it dirtier. Here's what to do before you start filling in missing fields.",
        "read_time": "7",
        "faq_schema": [
            ("Should I clean my CRM before enrichment?",
             "Yes. Enriching before cleaning means appending data to duplicate records (making deduplication harder), filling fields on records that should have been deleted, and standardizing the new data differently from the old. Clean first, then enrich."),
            ("What fields should I prioritize for enrichment?",
             "Prioritize fields that drive revenue operations: email (for outreach), phone (for calls), job title (for routing and scoring), company size (for territory assignment), and industry (for segmentation). These fields have the highest impact on sales and marketing effectiveness."),
            ("How many records should I enrich at once?",
             "Start with a batch of 1,000-5,000 records to validate quality before committing to a full database enrichment. Check match rates, accuracy, and fill rates on the test batch. If results meet your thresholds, proceed with the full dataset."),
        ],
        "content_html": """        <p>You've decided to enrich your CRM data. You want to fill in missing phone numbers, add company firmographics, and get verified emails for contacts that only have a name and company.</p>

        <p>Before you submit your database to an enrichment provider, there's prep work that will dramatically improve your results. Enriching a messy database is like painting over rust. It looks better briefly but the underlying problems will surface quickly.</p>

        <h2>Step 1: Deduplicate First</h2>

        <p>This is the most important step and the one most companies skip.</p>

        <p>If you have 3 records for John Smith at ABC Corp and you enrich all three, you now have 3 enriched duplicates. You've paid three times for the same data and made deduplication harder because each record now has more fields to reconcile during merging.</p>

        <p><strong>Action:</strong> Run deduplication before enrichment. Merge duplicates into golden records. Then enrich the deduplicated dataset.</p>

        <h2>Step 2: Remove Records That Shouldn't Be Enriched</h2>

        <p>Not every record in your CRM needs enrichment. Remove or exclude:</p>

        <ul>
          <li><strong>Competitors</strong> you're tracking for intelligence (enrich separately if needed)</li>
          <li><strong>Do-not-contact records</strong> that should never receive outreach</li>
          <li><strong>Test records</strong> created by admins or during onboarding</li>
          <li><strong>Completely stale records</strong> from years-old imports that are no longer in your target market</li>
          <li><strong>Records with no identifiable information</strong> (no name, no email, no company) that can't be matched by an enrichment provider</li>
        </ul>

        <p>Every record you exclude saves money and keeps your enriched dataset focused on contacts that matter.</p>

        <h2>Step 3: Standardize Key Matching Fields</h2>

        <p>Enrichment providers match your records against their database using fields like company name, email domain, and person name. If these fields are inconsistent, match rates suffer.</p>

        <p>Before submission, standardize:</p>
        <ul>
          <li><strong>Company names:</strong> Remove Inc., LLC, Corp. variations. Pick one format.</li>
          <li><strong>Email domains:</strong> Lowercase everything. Remove trailing spaces.</li>
          <li><strong>Names:</strong> Fix obvious issues (ALL CAPS, name in wrong field, initials instead of names)</li>
        </ul>

        <div class="callout-box">
          <p><strong>Why this matters:</strong> A provider might fail to match "ABC MANUFACTURING INC." but successfully match "ABC Manufacturing." Clean inputs produce better match rates.</p>
        </div>

        <h2>Step 4: Define Which Fields You Need</h2>

        <p>Don't enrich everything. Focus on the fields that drive your revenue operations:</p>

        <ul>
          <li><strong>For outbound sales:</strong> Email, direct dial phone, job title</li>
          <li><strong>For lead scoring:</strong> Company size, industry, revenue range</li>
          <li><strong>For territory assignment:</strong> Company HQ location, employee count</li>
          <li><strong>For ABM:</strong> Technology stack, funding stage, growth signals</li>
        </ul>

        <p>More fields cost more. Prioritize the ones your team will actually use in the next 90 days.</p>

        <h2>Step 5: Set Quality Thresholds</h2>

        <p>Before the project starts, decide what "good enough" looks like:</p>

        <ul>
          <li><strong>Email match rate:</strong> What percentage of records need verified emails? (80%+ is typical)</li>
          <li><strong>Phone match rate:</strong> What direct dial coverage do you expect? (60-70% is realistic for most markets)</li>
          <li><strong>Accuracy standard:</strong> How will you spot-check results?</li>
        </ul>

        <p>Setting thresholds before the project prevents disagreements about quality after delivery.</p>

        <h2>Step 6: Run a Test Batch</h2>

        <p>Don't enrich your entire database on the first try. Start with 1,000-5,000 records:</p>

        <ol>
          <li>Submit the test batch to your enrichment provider</li>
          <li>Review match rates per field</li>
          <li>Spot-check 50 records for accuracy (verify titles, phone numbers, company data manually)</li>
          <li>Check email deliverability on a sample (send a small campaign)</li>
          <li>If quality meets your thresholds, proceed with the full dataset</li>
        </ol>

        <h2>Step 7: Plan the Import</h2>

        <p>Before you get the enriched data back, plan how you'll import it:</p>

        <ul>
          <li><strong>Field mapping:</strong> Which enriched fields map to which CRM properties?</li>
          <li><strong>Overwrite rules:</strong> Should enriched data overwrite existing values or only fill empty fields?</li>
          <li><strong>Backup:</strong> Back up your CRM before importing. Always have a rollback point.</li>
          <li><strong>Automation check:</strong> After import, test lead scoring, routing, and any automation that uses the enriched fields.</li>
        </ul>

        <h2>The Checklist</h2>

        <ol>
          <li>Deduplicate your database</li>
          <li>Remove records that shouldn't be enriched</li>
          <li>Standardize company names, emails, and contact names</li>
          <li>Define which fields you need enriched</li>
          <li>Set match rate and accuracy thresholds</li>
          <li>Run a test batch of 1,000-5,000 records</li>
          <li>Plan your import (field mapping, overwrite rules, backup)</li>
        </ol>

        <p>Spending 2-3 hours on this prep work will improve your match rates, reduce your costs, and give you cleaner results when the enriched data comes back.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>Should I clean my CRM before enrichment?</h3>
        <p>Yes. Enriching before cleaning means appending data to duplicate records and filling fields on records that should have been deleted. Clean first, then enrich.</p>

        <h3>What fields should I prioritize for enrichment?</h3>
        <p>Email, phone, job title, company size, and industry. These fields have the highest impact on sales and marketing operations.</p>

        <h3>How many records should I enrich at once?</h3>
        <p>Start with 1,000-5,000 records to validate quality. Check match rates and accuracy before committing to a full database enrichment.</p>""",
        "related_links": [
            ("Data Enrichment Services", "/services/data-enrichment.html"),
            ("Data Cleaning vs. Data Enrichment", "/resources/data-cleaning-vs-data-enrichment.html"),
            ("Contact Enrichment Case Study", "/case-studies/contact-enrichment-insurance-brokerage/"),
            ("How to Choose an Enrichment Provider", "/resources/how-to-choose-data-enrichment-provider.html"),
        ],
    },
    {
        "filename": "data-quality-sla-template.html",
        "title": "Data Quality SLAs: What to Include in Your Vendor Agreement",
        "meta_desc": "A practical guide to data quality SLAs for enrichment and cleaning vendors. Covers match rates, accuracy thresholds, turnaround times, and remediation terms.",
        "og_title": "Data Quality SLAs: What to Include in Your Vendor Agreement",
        "canonical_slug": "data-quality-sla-template.html",
        "date": "2026-02-15",
        "category_label": "Implementation Guide",
        "hero_title": "Data Quality SLAs for Vendor Agreements",
        "hero_subtitle": "What to put in writing before your data vendor starts work. Protect your investment with measurable quality commitments.",
        "read_time": "9",
        "faq_schema": [
            ("What SLAs should I include in a data enrichment contract?",
             "Key SLAs include: minimum match rate (percentage of records enriched), email deliverability guarantee (typically 90%+), phone accuracy threshold (percentage connecting to the named contact), turnaround time commitment, and remediation process for data that falls below thresholds."),
            ("What is a reasonable email deliverability SLA?",
             "For SMTP-verified emails, expect a deliverability SLA of 90-95%. Anything below 90% suggests the vendor is pattern-guessing rather than verifying. The SLA should specify how deliverability is measured and what happens if the threshold is missed."),
            ("How do you enforce data quality SLAs?",
             "Build measurement and remediation into the contract. Specify how quality is measured (sample audit, full validation), who measures it (you or a third party), the measurement timeline (within 30 days of delivery), and the remedy (re-enrichment, credit, or refund for records below threshold)."),
        ],
        "content_html": """        <p>Most data enrichment and cleaning contracts don't include meaningful quality commitments. The vendor promises "high quality data" and you discover what that means after you've paid.</p>

        <p>A good SLA turns vague promises into measurable obligations. It protects both sides: the vendor knows exactly what's expected, and you have recourse if the data doesn't perform.</p>

        <p>Here's what to include.</p>

        <h2>Match Rate SLAs</h2>

        <p>The match rate is the percentage of your submitted records that the vendor can successfully enrich. This should be defined per field, not as an overall average.</p>

        <h3>Typical thresholds:</h3>
        <ul>
          <li><strong>Email addresses:</strong> 75-85% match rate (US mid-market)</li>
          <li><strong>Direct dial phone:</strong> 55-70% match rate</li>
          <li><strong>Job title:</strong> 80-90% match rate</li>
          <li><strong>Company firmographics:</strong> 85-95% match rate</li>
        </ul>

        <p>Match rates vary by market. SMB and niche industries will be lower. Enterprise and well-known companies will be higher. Set thresholds based on your test batch results, not the vendor's general claims.</p>

        <div class="callout-box">
          <p><strong>Important:</strong> Specify whether the match rate is measured against all submitted records or only records where the vendor had enough information to attempt a match. These produce very different numbers.</p>
        </div>

        <h2>Accuracy SLAs</h2>

        <p>A match isn't useful if it's wrong. Accuracy measures whether enriched data is correct, not just present.</p>

        <h3>How to define accuracy:</h3>
        <ul>
          <li><strong>Email accuracy:</strong> % of delivered emails that are deliverable (measured via SMTP verification or test campaign). Target: 90-95%.</li>
          <li><strong>Phone accuracy:</strong> % of delivered phone numbers that connect to the named contact. Target: 80-85%.</li>
          <li><strong>Title accuracy:</strong> % of delivered titles that match the contact's current role. Target: 85-90%.</li>
        </ul>

        <h3>Measurement method:</h3>
        <p>Specify how accuracy is measured. Options include:</p>
        <ul>
          <li><strong>Random sample audit:</strong> You manually verify 50-100 records within 30 days of delivery</li>
          <li><strong>Full email validation:</strong> Run all delivered emails through a third-party verification tool</li>
          <li><strong>Call test:</strong> Attempt to reach 25-50 delivered phone contacts</li>
        </ul>

        <h2>Turnaround Time SLAs</h2>

        <p>Define when the clock starts and what the delivery commitment is:</p>

        <ul>
          <li><strong>Start trigger:</strong> When the vendor receives your complete data file (not when the contract is signed)</li>
          <li><strong>Delivery commitment:</strong> X business days for Y records (e.g., 5 business days for up to 50,000 records)</li>
          <li><strong>Rush options:</strong> If you need faster delivery, define the premium and timeline</li>
          <li><strong>Delay notification:</strong> Vendor must notify you within 24 hours if delivery will be delayed</li>
        </ul>

        <h2>Remediation Terms</h2>

        <p>What happens when data doesn't meet the SLA? Define this upfront:</p>

        <h3>Tiered remediation:</h3>
        <ul>
          <li><strong>Minor miss (within 5% of threshold):</strong> Vendor re-enriches or re-cleans the shortfall at no cost</li>
          <li><strong>Significant miss (5-15% below threshold):</strong> Vendor re-processes affected records and provides credit toward future work</li>
          <li><strong>Major miss (15%+ below threshold):</strong> Partial or full refund for the affected portion of the project</li>
        </ul>

        <h3>Measurement timeline:</h3>
        <p>You should have 30 days from delivery to identify quality issues and invoke the SLA. This gives you time to import, test, and audit without feeling rushed.</p>

        <h2>Data Freshness SLAs</h2>

        <p>For ongoing enrichment or maintenance contracts, define freshness requirements:</p>

        <ul>
          <li><strong>Re-verification frequency:</strong> How often are records re-checked? (Monthly, quarterly)</li>
          <li><strong>Staleness threshold:</strong> What's the maximum age of a delivered record? (e.g., verified within the last 90 days)</li>
          <li><strong>Change detection:</strong> Does the vendor proactively flag records where the contact has changed jobs?</li>
        </ul>

        <h2>What Not to Include</h2>

        <p>Avoid SLAs that are unmeasurable or create perverse incentives:</p>

        <ul>
          <li><strong>Don't SLA on database size.</strong> "Access to 200M contacts" doesn't mean 200M contacts in your market.</li>
          <li><strong>Don't SLA on response rates.</strong> The vendor controls data quality, not your messaging or timing.</li>
          <li><strong>Don't SLA on revenue impact.</strong> Too many variables between data quality and closed deals.</li>
        </ul>

        <p>Focus SLAs on what the vendor can directly control: match rates, accuracy, deliverability, turnaround time, and freshness.</p>

        <h2>Frequently Asked Questions</h2>

        <h3>What SLAs should I include in a data enrichment contract?</h3>
        <p>Minimum match rate per field, email deliverability guarantee (90%+), phone accuracy threshold, turnaround time, and remediation terms for data below thresholds.</p>

        <h3>What is a reasonable email deliverability SLA?</h3>
        <p>90-95% for SMTP-verified emails. Below 90% suggests pattern-guessing. Specify how deliverability is measured and what happens if the threshold is missed.</p>

        <h3>How do you enforce data quality SLAs?</h3>
        <p>Build measurement into the contract: who measures quality, how, within what timeline, and what remedy applies. A 30-day measurement window after delivery is standard.</p>""",
        "related_links": [
            ("Data Enrichment RFP Template", "/resources/data-enrichment-rfp-template.html"),
            ("How to Evaluate Vendors", "/resources/evaluate-data-enrichment-vendors.html"),
            ("Data Vendor Negotiation", "/resources/data-vendor-negotiation.html"),
            ("Data Quality Metrics", "/resources/data-quality-metrics.html"),
        ],
    },
]

if __name__ == "__main__":
    for article in ARTICLES:
        filename = article["filename"]
        html = generate_article(**article)
        out_path = os.path.join(SITE_ROOT, "resources", filename)
        with open(out_path, "w") as f:
            f.write(html)
        print(f"Created: resources/{filename}")

    print(f"\nTotal: {len(ARTICLES)} implementation-stage articles")
