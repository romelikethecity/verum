# Verum Authority Building Plan

## Executive Summary

For a 1-month-old domain with 336 impressions and 3 clicks, authority building is critical. Google needs signals that Verum is a legitimate, trustworthy business. This plan outlines quick wins and ongoing strategies to establish domain authority and EEAT (Experience, Expertise, Authoritativeness, Trustworthiness).

---

## Current Authority Signals

### What's Working
- ✅ Google Analytics + Clarity tracking (legitimacy signal)
- ✅ Schema markup on key pages (Organization, FAQ, BreadcrumbList)
- ✅ /team page with founder Person schema
- ✅ LinkedIn company page linked
- ✅ Customer logos on homepage
- ✅ SSL certificate (HTTPS)
- ✅ Professional design and UX

### What's Missing
- ❌ No external backlinks (critical gap)
- ❌ No press mentions or "As Seen In"
- ❌ No third-party reviews (G2, Capterra, Clutch)
- ❌ No industry association memberships visible
- ❌ Limited outbound links to authoritative sources
- ❌ No testimonials with full attribution

---

## Quick Wins (Week 1-2)

### 1. Directory Submissions
Submit to business directories that provide backlinks and legitimacy signals.

**High-Priority (Free, Immediate)**
- [ ] Google Business Profile - veruminc.com
- [ ] LinkedIn Company Page (already exists, verify completeness)
- [ ] Crunchbase - create company profile
- [ ] AngelList/Wellfound - startup profile
- [ ] Clutch.co - B2B service provider directory
- [ ] G2 - software/services listing

**Data-Specific Directories**
- [ ] Data Services Directory
- [ ] B2B Marketing Tools directories
- [ ] RevOps tool directories
- [ ] Sales Tech Stack directories

**Action:** Create accounts and submit profiles within 1 week. Use consistent NAP (Name, Address, Phone) across all listings.

### 2. Add Outbound Authority Links

Add 2-3 contextual links to authoritative sources on key pages. This signals to Google that you're part of the broader industry conversation.

**Homepage**
```html
<!-- Add to content sections -->
According to <a href="https://www.gartner.com/..." rel="noopener">Gartner research</a>,
B2B data decays at approximately 30% annually...
```

**Industry Pages - Example Sources**
- Healthcare: CMS.gov, HIPAA Journal, AHLA
- Fintech: FINRA, SEC.gov, American Banker
- Legal: ABA Journal, Law.com, Above the Law
- SaaS: SaaStr, OpenView Partners research

**Target:** Add 2-3 outbound links per page to government, research, or industry authority sites.

### 3. Testimonials and Social Proof

**Immediate Actions**
- [ ] Request testimonials from any existing clients
- [ ] Add testimonials to homepage with full name + company + title
- [ ] Create case study snippets (even brief ones)

**Testimonial Format**
```html
<div class="testimonial">
  <blockquote>"Quote here"</blockquote>
  <cite>— Name, Title, Company</cite>
</div>
```

**Schema Markup for Testimonials**
```json
{
  "@type": "Review",
  "author": {"@type": "Person", "name": "Name"},
  "reviewBody": "Quote here",
  "itemReviewed": {"@type": "Organization", "name": "Verum"}
}
```

---

## Medium-Term Strategies (Month 1-3)

### 4. HARO and Journalist Outreach

HARO (Help A Reporter Out) connects journalists with sources. Perfect for building authority through press mentions.

**Setup**
- [ ] Sign up at helpareporter.com
- [ ] Set alerts for: "data quality", "CRM", "B2B data", "sales operations", "marketing data"
- [ ] Respond to relevant queries within 2-3 hours (speed matters)

**Response Framework**
1. Introduce yourself and Verum briefly
2. Answer their specific question with expertise
3. Provide a quotable statement
4. Include credentials (Rome's background)

**Expected Results:** 1-3 media mentions per month if actively responding.

### 5. Guest Posting Strategy

Write guest posts for industry publications that link back to Verum.

**Target Publications (by difficulty)**

**Lower Difficulty (Contributor Programs)**
- Medium.com (technology/data publications)
- Dev.to (for technical content)
- LinkedIn Articles (Rome's personal profile)
- Industry newsletters that accept contributors

**Medium Difficulty**
- RevGenius blog
- SaaStr (community content)
- Sales Hacker
- MarTech Today
- Demand Gen Report

**Higher Difficulty (Worth Pursuing)**
- Forbes (contributor network)
- Inc.com
- Entrepreneur
- TechCrunch (for news/funding announcements)

**Topic Ideas for Guest Posts**
1. "The Hidden Cost of Bad CRM Data" (data quality angle)
2. "Why Your ZoomInfo Subscription Isn't Solving Your Data Problem"
3. "What AI Can't Fix About Your Sales Data"
4. "Data Enrichment vs. Data Cleaning: Which Do You Need First?"
5. "The RevOps Leader's Guide to CRM Hygiene"

**Action:** Pitch 3-5 publications per week with unique angles.

### 6. Podcast Appearances

Getting on podcasts builds authority and creates backlinks (show notes link to guests).

**Target Podcasts**
- RevOps-focused: RevGenius, RevOps Podcast
- Sales-focused: Sales Hacker, The Brutal Truth About Sales
- Marketing-focused: Marketing Over Coffee, Demand Gen Chat
- B2B SaaS: SaaS Breakthrough, Scale or Die
- Data/Analytics: Data Skeptic, Partially Derivative

**Pitch Angle**
"I'm Rome Thorndike, founder of Verum. After leading sales at companies acquired by Databricks and working at Microsoft and Salesforce, I started Verum because I watched companies waste millions on bad data. I'd love to share what I've learned about..."

**Action:** Reach out to 5 podcasts per week.

---

## Ongoing Authority Building (Month 3+)

### 7. Industry Association Memberships

Join relevant associations and display membership badges.

**B2B Data/RevOps**
- Revenue Collective (membership)
- RevGenius (free community)
- Pavilion (formerly Revenue Collective)

**Industry-Specific**
- For healthcare focus: HIMSS, CHIME
- For fintech focus: FinTech Association
- For legal focus: ILTA (legal tech)

**Action:** Join at least 2 associations. Add membership badges to website footer.

### 8. Speaking Opportunities

Conference speaking builds authority and generates backlinks from event sites.

**Target Events**
- RevOps Summit
- SaaStr Annual
- LegalTech Conference
- HIMSS (healthcare IT)
- Dreamforce (Salesforce ecosystem)

**Speaking Topic Ideas**
1. "The True Cost of CRM Data Decay"
2. "Building a Data Quality Program Without a Data Team"
3. "AI-Powered Data Cleaning: What Actually Works"

**Action:** Apply to speak at 3-5 events per quarter.

### 9. Original Research and Data Reports

Publishing original research generates backlinks, citations, and authority.

**Research Ideas**
1. **"State of B2B Data Quality 2026"** - Survey 100+ companies on data hygiene practices
2. **"CRM Data Decay Benchmark Report"** - Analyze anonymized client data to publish decay rates by industry
3. **"The Cost of Bad Data Calculator"** - Interactive tool with supporting research

**Distribution**
- Publish on website
- Create press release
- Pitch to industry publications
- Offer as downloadable resource (lead magnet)

---

## Technical Authority Signals

### 10. Schema Markup Expansion

Already partially implemented. Ensure all pages have:
- [ ] BreadcrumbList on all pages (mostly done)
- [ ] FAQPage schema with 3+ questions per page
- [ ] Service schema on service pages
- [ ] Review/Testimonial schema when testimonials added
- [ ] Article schema on all blog/resource content

### 11. External Link Strategy

Add contextual outbound links to:
- Government sources (SBA, IRS, SEC, CMS)
- Industry associations
- Research institutions
- Major publications
- Industry statistics sources

**Target:** 2-3 relevant outbound links per content page.

---

## Backlink Acquisition Tracking

### Link Building KPIs

| Metric | Current | 30-Day Goal | 90-Day Goal |
|--------|---------|-------------|-------------|
| Referring Domains | ~0 | 10+ | 30+ |
| Directory Listings | ~2 | 15+ | 25+ |
| Guest Posts Published | 0 | 2-3 | 8-10 |
| Podcast Appearances | 0 | 1-2 | 5+ |
| Press Mentions | 0 | 1-2 | 5+ |

### Tools to Track Progress
- Ahrefs or Moz for backlink monitoring
- Google Search Console for new referring sites
- Brand mention monitoring (Google Alerts, Mention.com)

---

## Content Partnerships

### 12. Co-Marketing Opportunities

Partner with complementary tools for co-created content.

**Potential Partners**
- CRM platforms (HubSpot Partner Program, Salesforce AppExchange)
- Data orchestration tools (Census, Hightouch)
- Sales engagement platforms (Outreach, Salesloft)
- Intent data providers (Bombora, 6sense)

**Partnership Format**
- Co-authored blog posts
- Joint webinars
- Integration case studies
- Mutual backlinks

---

## Founder Thought Leadership

### 13. Rome Thorndike Personal Brand

Founder authority transfers to company authority.

**LinkedIn Strategy**
- [ ] Optimize Rome's LinkedIn profile with Verum positioning
- [ ] Post 3-5x per week on data quality topics
- [ ] Engage with RevOps and sales ops conversations
- [ ] Share insights from client work (anonymized)

**Content Ideas for LinkedIn**
- Hot takes on data quality
- Quick tips for CRM hygiene
- Industry observations
- Behind-the-scenes of data cleaning work
- Myths about data enrichment

**Twitter/X Strategy**
- Create @VerumData or use Rome's personal account
- Share industry news with commentary
- Engage with data/RevOps community
- Post threads on specific topics

---

## 30-Day Authority Building Sprint

### Week 1
- [ ] Submit to 10 business directories
- [ ] Create Crunchbase and G2 profiles
- [ ] Sign up for HARO
- [ ] Add outbound authority links to 10 key pages
- [ ] Request 3 testimonials from any existing clients

### Week 2
- [ ] Respond to 5+ HARO queries
- [ ] Pitch 5 podcasts
- [ ] Write and pitch 2 guest post ideas
- [ ] Join 2 industry communities (RevGenius, etc.)
- [ ] Add testimonials to website (if received)

### Week 3
- [ ] Follow up on podcast pitches
- [ ] Submit guest posts
- [ ] Expand directory submissions
- [ ] Start LinkedIn content cadence
- [ ] Apply to 1 speaking opportunity

### Week 4
- [ ] Assess results and adjust strategy
- [ ] Plan original research project
- [ ] Continue HARO responses
- [ ] Continue guest post pitching
- [ ] Document all new backlinks acquired

---

## Expected Impact

### Authority Metrics After 90 Days
- Domain Rating: 10-15 (from ~0)
- Referring Domains: 30+
- Branded search volume: Increasing
- Direct traffic: 5-10% of total

### SEO Metrics After 90 Days (with authority + content improvements)
- Organic impressions: 1,000+/month (from 336)
- Organic clicks: 30-50+/month (from 3)
- Average position: <15 (from 19.1)
- Keywords in top 10: 10+ (from ~0)

---

## Resources

### HARO Alternatives
- Qwoted
- SourceBottle
- JournoRequests
- #journorequest on Twitter

### Backlink Tracking Tools
- Ahrefs (paid, best)
- Moz (paid)
- Ubersuggest (freemium)
- Google Search Console (free, limited)

### Outreach Templates
See `/docs/outreach-templates.md` (to be created)

---

## Next Steps

1. **Immediate:** Submit to top 10 directories this week
2. **This Week:** Sign up for HARO and respond to first queries
3. **This Month:** Publish 2 guest posts and appear on 1 podcast
4. **Ongoing:** Build LinkedIn presence and continue outreach

The key insight: for a new domain, authority building matters as much as on-page optimization. Google needs to see external signals that Verum is a real, trusted business before it will rank the site competitively.
