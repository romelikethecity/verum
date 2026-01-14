# Verum Website - Claude Code Guidelines

## Programmatic SEO Page Template

When creating or editing industry data enrichment pages, follow these guidelines:

### Pain Stats Formatting Rules

**CRITICAL: All stat numbers must fit on ONE LINE**

Before finalizing any page, verify each `.pain-stat__number` value:

1. **Keep stats short** - Use abbreviations and hyphenated forms:
   - Use `24-48hr` not `24-48 hours`
   - Use `84-day` not `84 days`
   - Use `$12.9M` not `$12.9 million`
   - Use `13 hrs` not `13 hours`

2. **Max character count** - Stat numbers should be ~8 characters or less

3. **Test multi-word stats** - If a stat has spaces (like "84 days"), use a hyphen instead ("84-day") or abbreviate

4. **Percentage stats are safe** - Single numbers with % always work (e.g., "70%", "25%", "90%")

### Pain Stats Checklist

Before committing any page with `.pain-stats`:
- [ ] Each stat number is 8 characters or fewer
- [ ] No multi-word stats that could wrap (use hyphens)
- [ ] Abbreviate units: hr, day, mo, yr, M, B, K

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

### CSS Classes Reference

- `.pain-stats` - Container for hero stats
- `.pain-stat` - Individual stat card
- `.pain-stat__number` - Large teal number (4.5rem desktop)
- `.pain-stat__label` - Small label below number
- `.solution-stats` - Mid-page stats with card background
- `.solution-stat__number` - 2.75rem with `white-space: nowrap`
- `.comparison-table` - Red/green styled comparison table
- `.hero-cta-group` - Button group below stats
