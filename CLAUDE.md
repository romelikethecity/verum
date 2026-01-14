# Verum Website - Claude Code Guidelines

## Programmatic SEO Page Template

When creating or editing industry data enrichment pages, follow these guidelines:

### Pain Stats Formatting Rules

**CRITICAL: Stat numbers must NEVER contain spaces**

Spaces in `.pain-stat__number` values cause line wrapping on mobile/tablet.

**THE RULE: No spaces inside stat values. Ever.**

✅ GOOD (no spaces):
- `30%` - percentages are always safe
- `$12.9M` - currency with abbreviation
- `24-48hr` - hyphenated, no spaces
- `84-day` - hyphenated, no spaces
- `13` - just the number, move "hours" to label
- `5+` - just the number with modifier
- `50+` - just the number with modifier

❌ BAD (contains spaces - WILL WRAP):
- `13 hrs` - HAS SPACE, will wrap to two lines
- `84 days` - HAS SPACE, will wrap
- `15+ hrs` - HAS SPACE, will wrap
- `5+ hrs` - HAS SPACE, will wrap

**Pattern for time-based stats:**
Instead of `13 hrs` in the number, use:
- Number: `13`
- Label: `Hours lost weekly to data hunting`

### MANDATORY: Run Verification Before Committing

**YOU MUST run this command before committing any page changes:**

```bash
grep -r "pain-stat__number" /Users/rome/Documents/projects/verum-website/solutions/*/index.html | grep -E ">[^<]+ [^<]+<"
```

If this returns ANY results, you have stats with spaces that will wrap. Fix them before committing.

### Pain Stats Checklist

Before committing any page with `.pain-stats`:
- [ ] Ran verification command above - returned no results
- [ ] Each stat number contains NO SPACES
- [ ] Stat numbers are 6 characters or fewer

### Page Template Structure

```html
<!-- Hero Section -->
<section class="page-hero">
  <div class="container">
    <h1 class="page-hero__title">[Industry] Data Enrichment That Actually Works</h1>
    <p class="page-hero__subtitle">[Pain-first subtitle]</p>

    <!-- Pain Stats - The Hook (VERIFY ALL STATS FIT ON ONE LINE) -->
    <div class="pain-stats">
      <div class="pain-stat">
        <span class="pain-stat__number">[SHORT STAT]</span>
        <span class="pain-stat__label">[Label]</span>
      </div>
      <!-- 2 more stats -->
    </div>

    <!-- CTAs Below Stats -->
    <div class="hero-cta-group">
      <a href="/#contact" class="btn btn--primary btn--lg">Clean My Data</a>
      <a href="/#contact" class="btn btn--secondary btn--lg">Get Free Data Assessment</a>
    </div>
  </div>
</section>
```

### Solution Stats (mid-page)

These also use large numbers. Same rules apply:
- `93%` - OK
- `24-48hr` - OK (hyphenated, no space)
- `50+` - OK

### Writing Style

See `/docs/WRITING-GUIDELINES.md` for anti-AI detection guidelines:
- Use contractions
- Vary sentence length
- Avoid em-dashes
- No performative interjections ("That's not a typo", "Let that sink in")
- Industry-specific details and stats with source links

### CSS Cache-Busting

**IMPORTANT: When modifying CSS, increment the version parameter**

GitHub Pages caches CSS for 4 hours. To ensure users see updated styles immediately:

1. All HTML files link to CSS with a version param: `styles.css?v=2`
2. When you modify `/css/styles.css`, increment the version: `?v=3`, `?v=4`, etc.
3. Update ALL HTML files with the new version (use find/sed)

```bash
# Example: Increment from v=2 to v=3 across all HTML files
find /Users/rome/Documents/projects/verum-website -name "*.html" \
  -exec sed -i '' 's|styles.css?v=2|styles.css?v=3|g' {} \;
```

This prevents the "design issues" where new pages show with old cached CSS.

### CSS Classes Reference

- `.pain-stats` - Container for hero stats
- `.pain-stat` - Individual stat card
- `.pain-stat__number` - Large teal number (4.5rem desktop)
- `.pain-stat__label` - Small label below number
- `.solution-stats` - Mid-page stats with card background
- `.solution-stat__number` - 2.75rem with `white-space: nowrap`
- `.comparison-table` - Red/green styled comparison table
- `.hero-cta-group` - Button group below stats
