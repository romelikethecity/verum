#!/usr/bin/env python3
"""Add internal links from existing blog articles to glossary, case study, and alternatives pages.

Strategy:
- Add 2-4 inline glossary links per article (first mention of each term in blog-content)
- Skip text inside existing <a> tags, headings, title, meta tags
- Add relevant case study / alternatives links to the Related footer section
- Skip articles we just created (they already have good internal links)
"""
import os
import re
from collections import OrderedDict

SITE_ROOT = "/Users/rome/Documents/projects/verum-website"
RESOURCES_DIR = os.path.join(SITE_ROOT, "resources")

# Articles we created this session - skip them
SKIP_FILES = {
    "outsource-data-cleaning-vs-in-house.html",
    "self-serve-data-platforms-vs-managed-services.html",
    "evaluate-data-enrichment-vendors.html",
    "signs-crm-data-needs-cleaning.html",
    "data-enrichment-rfp-template.html",
    "index.html",
}

# ── Glossary term mapping ───────────────────────────────────────────────────
# Phrase → (glossary slug, display text for link)
# Ordered by specificity (longer phrases first to avoid partial matches)
GLOSSARY_LINKS = OrderedDict([
    ("account-based marketing", ("/glossary/abm/", "account-based marketing")),
    ("job title normalization", ("/glossary/job-title-normalization/", "job title normalization")),
    ("job title standardization", ("/glossary/job-title-normalization/", "job title standardization")),
    ("ideal customer profile", ("/glossary/ideal-customer-profile/", "ideal customer profile")),
    ("customer lifetime value", ("/glossary/customer-lifetime-value/", "customer lifetime value")),
    ("customer data platform", ("/glossary/customer-data-platform/", "customer data platform")),
    ("data quality management", ("/glossary/data-quality-management/", "data quality management")),
    ("revenue operations", ("/glossary/revenue-operations/", "revenue operations")),
    ("sales intelligence", ("/glossary/sales-intelligence/", "sales intelligence")),
    ("contact data waterfall", ("/glossary/contact-waterfall/", "contact data waterfall")),
    ("data waterfall", ("/glossary/contact-waterfall/", "data waterfall")),
    ("buyer intent data", ("/glossary/buyer-intent-data/", "buyer intent data")),
    ("sender reputation", ("/glossary/sender-reputation/", "sender reputation")),
    ("email deliverability", ("/glossary/email-deliverability/", "email deliverability")),
    ("email validation", ("/glossary/email-validation/", "email validation")),
    ("data deduplication", ("/glossary/data-deduplication/", "data deduplication")),
    ("data normalization", ("/glossary/data-normalization/", "data normalization")),
    ("data standardization", ("/glossary/data-standardization/", "data standardization")),
    ("technographic data", ("/glossary/technographic-data/", "technographic data")),
    ("firmographic data", ("/glossary/firmographic-data/", "firmographic data")),
    ("entity resolution", ("/glossary/entity-resolution/", "entity resolution")),
    ("data governance", ("/glossary/data-governance/", "data governance")),
    ("data validation", ("/glossary/data-validation/", "data validation")),
    ("lead scoring", ("/glossary/lead-scoring/", "lead scoring")),
    ("data profiling", ("/glossary/data-profiling/", "data profiling")),
    ("data migration", ("/glossary/data-migration/", "data migration")),
    ("golden record", ("/glossary/golden-record/", "golden record")),
    ("fuzzy matching", ("/glossary/fuzzy-matching/", "fuzzy matching")),
    ("suppression list", ("/glossary/suppression-list/", "suppression list")),
    ("data enrichment", ("/glossary/data-enrichment/", "data enrichment")),
    ("catch-all domain", ("/glossary/catch-all-domain/", "catch-all domain")),
    ("demand generation", ("/glossary/demand-generation/", "demand generation")),
    ("data append", ("/glossary/data-append/", "data append")),
    ("data hygiene", ("/glossary/data-hygiene/", "data hygiene")),
    ("CRM hygiene", ("/glossary/crm-hygiene/", "CRM hygiene")),
    ("data decay", ("/glossary/data-decay/", "data decay")),
    ("fill rate", ("/glossary/fill-rate/", "fill rate")),
    ("match rate", ("/glossary/match-rate/", "match rate")),
    ("bounce rate", ("/glossary/bounce-rate/", "bounce rate")),
    ("intent data", ("/glossary/buyer-intent-data/", "intent data")),
    ("deduplication", ("/glossary/data-deduplication/", "deduplication")),
    ("firmographic", ("/glossary/firmographic-data/", "firmographic")),
    ("technographic", ("/glossary/technographic-data/", "technographic")),
])

# ── Case study links (keyword → case study) ────────────────────────────────
CASE_STUDY_LINKS = {
    "crm-cleaning": ("/case-studies/crm-cleaning-staffing-agency/", "CRM Cleaning Case Study"),
    "data-enrichment": ("/case-studies/contact-enrichment-insurance-brokerage/", "Contact Enrichment Case Study"),
    "list-building": ("/case-studies/prospect-list-building-commercial-real-estate/", "Prospect List Building Case Study"),
    "crm-migration": ("/case-studies/crm-migration-data-prep-manufacturing/", "CRM Migration Case Study"),
    "maintenance": ("/case-studies/database-maintenance-marketing-agency/", "Database Maintenance Case Study"),
}

# Map article filenames to relevant case studies to add to their Related section
ARTICLE_CASE_STUDY_MAP = {
    # CRM cleaning related
    "how-to-clean-salesforce-data.html": ["crm-cleaning"],
    "hubspot-data-cleaning.html": ["crm-cleaning"],
    "hubspot-duplicate-contacts.html": ["crm-cleaning"],
    "salesforce-duplicate-contacts.html": ["crm-cleaning"],
    "cost-of-bad-crm-data.html": ["crm-cleaning", "maintenance"],
    "true-cost-bad-crm-data.html": ["crm-cleaning", "maintenance"],
    "crm-data-quality-checklist.html": ["crm-cleaning"],
    "data-cleaning-vs-data-enrichment.html": ["crm-cleaning", "data-enrichment"],
    "lead-cleansing-software.html": ["crm-cleaning"],
    "data-hygiene-for-marketing-ops.html": ["crm-cleaning", "maintenance"],
    "salesforce-company-name-normalization.html": ["crm-cleaning"],
    "salesforce-job-title-standardization.html": ["crm-cleaning"],
    # Data enrichment related
    "what-is-data-enrichment.html": ["data-enrichment"],
    "best-data-enrichment-tools.html": ["data-enrichment"],
    "how-to-choose-data-enrichment-provider.html": ["data-enrichment"],
    "data-enrichment-roi-calculator.html": ["data-enrichment"],
    "measuring-enrichment-roi.html": ["data-enrichment"],
    "contact-data-waterfall.html": ["data-enrichment"],
    "real-time-vs-batch-enrichment.html": ["data-enrichment"],
    "data-enrichment-for-saas.html": ["data-enrichment"],
    "data-enrichment-fintech.html": ["data-enrichment"],
    "data-enrichment-healthcare.html": ["data-enrichment"],
    "data-enrichment-for-healthcare.html": ["data-enrichment"],
    "data-enrichment-insurance.html": ["data-enrichment"],
    "data-enrichment-manufacturing.html": ["data-enrichment"],
    "data-enrichment-real-estate.html": ["data-enrichment"],
    "data-enrichment-recruiting.html": ["data-enrichment"],
    "data-enrichment-agencies.html": ["data-enrichment"],
    "missing-emails-crm.html": ["data-enrichment"],
    "data-enrichment-api-integration.html": ["data-enrichment"],
    "event-driven-enrichment.html": ["data-enrichment"],
    "data-enrichment-for-ecommerce.html": ["data-enrichment"],
    "data-enrichment-for-financial-services.html": ["data-enrichment"],
    "data-enrichment-legal.html": ["data-enrichment"],
    "data-enrichment-nonprofits.html": ["data-enrichment"],
    # CRM migration
    "crm-migration-data-cleanup.html": ["crm-migration"],
    "crm-backup-recovery.html": ["crm-migration"],
    "multi-crm-data-sync.html": ["crm-migration"],
    "salesforce-vs-hubspot-data-quality.html": ["crm-migration"],
    # Maintenance / decay
    "what-is-b2b-data-decay.html": ["maintenance"],
    "crm-data-decay-rate.html": ["maintenance"],
    "calculate-crm-data-decay-rate.html": ["maintenance"],
    "email-deliverability-data-quality.html": ["maintenance"],
    "data-quality-roadmap.html": ["maintenance"],
    "how-to-build-data-hygiene-strategy.html": ["maintenance"],
    # ICP analysis
    "how-to-build-data-driven-icp.html": [],  # Already links to the existing ICP case study
    "revops-team-size-customer-ltv.html": [],
    # Lead scoring / routing
    "lead-scoring-not-working.html": ["data-enrichment"],
    "lead-scoring-with-enriched-data.html": ["data-enrichment"],
    "lead-routing-broken-data.html": ["crm-cleaning"],
    # Data quality general
    "data-quality-metrics.html": ["crm-cleaning", "maintenance"],
    "data-quality-dashboards.html": ["crm-cleaning"],
    "data-quality-automation.html": ["maintenance"],
    "data-quality-for-sales-leaders.html": ["crm-cleaning", "data-enrichment"],
    "ceo-guide-crm-data-quality.html": ["crm-cleaning", "maintenance"],
    "building-data-quality-team.html": ["maintenance"],
    "data-quality-ai-ml.html": ["data-enrichment"],
    "data-quality-customer-success.html": ["data-enrichment"],
    "data-quality-for-ma-due-diligence.html": ["crm-migration", "crm-cleaning"],
    # Other
    "abm-account-data-quality.html": ["data-enrichment", "crm-cleaning"],
    "abm-data-strategy.html": ["data-enrichment"],
    "signal-based-selling.html": ["data-enrichment"],
    "first-party-data-strategy.html": ["data-enrichment"],
    "data-governance-without-team.html": ["maintenance"],
    "data-vendor-negotiation.html": ["data-enrichment"],
    "attribution-data-quality.html": ["crm-cleaning"],
    "gdpr-data-enrichment.html": ["data-enrichment"],
    "international-data-compliance.html": ["data-enrichment"],
    "people-data-labs-vs-zoominfo.html": ["data-enrichment"],
    "cognism-data-enrichment-salesforce.html": ["data-enrichment"],
    "intent-data-guide.html": ["data-enrichment"],
    "hubspot-email-validation.html": ["maintenance"],
    "hubspot-hard-bounce-filter.html": ["maintenance"],
    "hubspot-lifecycle-stage-cleanup.html": ["crm-cleaning"],
    "hubspot-marketing-contacts-cleanup.html": ["crm-cleaning"],
    "hubspot-contact-company-associations.html": ["crm-cleaning"],
    "hubspot-data-enrichment.html": ["data-enrichment"],
    "salesforce-data-enrichment.html": ["data-enrichment"],
    "salesforce-data-quality-audit.html": ["crm-cleaning"],
    "salesforce-email-validation.html": ["maintenance"],
}


def is_inside_tag(html, pos, tags=("a", "h1", "h2", "h3", "h4", "title", "meta", "strong")):
    """Check if position is inside any of the specified HTML tags."""
    # Look backwards for the nearest unclosed tag
    before = html[:pos]
    for tag in tags:
        # Find the last opening tag before this position
        open_pattern = re.compile(rf'<{tag}[\s>]', re.IGNORECASE)
        close_pattern = re.compile(rf'</{tag}>', re.IGNORECASE)

        opens = list(open_pattern.finditer(before))
        closes = list(close_pattern.finditer(before))

        if opens:
            last_open = opens[-1].start()
            last_close = max((m.end() for m in closes), default=0)
            if last_open > last_close:
                return True
    return False


def add_inline_glossary_links(html, max_links=3):
    """Add glossary links for first mentions of terms in blog content."""
    # Only work within the blog-content div
    content_match = re.search(r'(<div class="blog-content">)(.*?)(</div>\s*<div class="text-center)', html, re.DOTALL)
    if not content_match:
        return html, 0

    prefix = html[:content_match.start(2)]
    content = content_match.group(2)
    suffix = html[content_match.end(2):]

    links_added = 0
    linked_slugs = set()  # Track which glossary pages we've already linked to

    for phrase, (url, display) in GLOSSARY_LINKS.items():
        if links_added >= max_links:
            break

        # Skip if we already linked to this glossary page
        if url in linked_slugs:
            continue

        # Skip if this glossary page is already linked anywhere in the file
        if url in html:
            continue

        # Case-insensitive search for the phrase
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        match = pattern.search(content)

        if not match:
            continue

        # Check if this occurrence is inside a tag we shouldn't modify
        if is_inside_tag(content, match.start()):
            # Try to find next occurrence
            pos = match.end()
            found = False
            while pos < len(content):
                match = pattern.search(content, pos)
                if not match:
                    break
                if not is_inside_tag(content, match.start()):
                    found = True
                    break
                pos = match.end()
            if not found:
                continue

        # Build the replacement link
        original_text = match.group(0)
        link = f'<a href="{url}">{original_text}</a>'

        # Replace only this specific occurrence
        content = content[:match.start()] + link + content[match.end():]
        links_added += 1
        linked_slugs.add(url)

    return prefix + content + suffix, links_added


def add_related_links(html, filename):
    """Add case study links to the Related footer section of an article."""
    if filename not in ARTICLE_CASE_STUDY_MAP:
        return html, 0

    case_study_keys = ARTICLE_CASE_STUDY_MAP[filename]
    if not case_study_keys:
        return html, 0

    # Build links to add
    new_links = []
    for key in case_study_keys:
        url, text = CASE_STUDY_LINKS[key]
        # Don't add if already linked
        if url in html:
            continue
        new_links.append(f'<a href="{url}">{text}</a>')

    if not new_links:
        return html, 0

    # Find the Related: section (text-muted with Related:)
    related_pattern = re.compile(
        r'(<p class="text-muted"[^>]*>Related:\s*)(.*?)(</p>)',
        re.DOTALL
    )
    match = related_pattern.search(html)

    if match:
        existing = match.group(2).strip()
        separator = " | "
        addition = separator + separator.join(new_links)
        new_related = match.group(1) + existing + addition + match.group(3)
        html = html[:match.start()] + new_related + html[match.end():]
        return html, len(new_links)

    # If no Related: section exists, try to add one before the closing </div> in the content section
    # Look for the author bio or the last </div> in .content
    close_div = html.rfind('</div>\n  </section>\n\n  <footer')
    if close_div == -1:
        close_div = html.rfind('</div>\n  </section>')

    if close_div > 0:
        links_html = " | ".join(new_links)
        new_section = f'\n\n      <p class="text-muted" style="font-size: 0.875rem;">Related: {links_html}</p>\n'
        html = html[:close_div] + new_section + html[close_div:]
        return html, len(new_links)

    return html, 0


def process_file(filepath, filename):
    """Process a single article file."""
    with open(filepath, "r") as f:
        html = f.read()

    original = html

    # Add inline glossary links
    html, glossary_count = add_inline_glossary_links(html)

    # Add related case study links
    html, related_count = add_related_links(html, filename)

    if html != original:
        with open(filepath, "w") as f:
            f.write(html)
        return glossary_count, related_count

    return 0, 0


def main():
    total_glossary = 0
    total_related = 0
    files_modified = 0

    for filename in sorted(os.listdir(RESOURCES_DIR)):
        if not filename.endswith(".html"):
            continue
        if filename in SKIP_FILES:
            continue

        filepath = os.path.join(RESOURCES_DIR, filename)
        if not os.path.isfile(filepath):
            continue

        g, r = process_file(filepath, filename)
        if g > 0 or r > 0:
            files_modified += 1
            total_glossary += g
            total_related += r
            print(f"  {filename}: +{g} glossary links, +{r} case study links")

    print(f"\nTotal: {files_modified} files modified, {total_glossary} glossary links added, {total_related} case study links added")


if __name__ == "__main__":
    main()
