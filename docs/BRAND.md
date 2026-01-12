# Verum Brand Guidelines

## Brand Identity

**Company:** Verum Inc.
**Domain:** veruminc.com
**Tagline:** "Enterprise data cleaning and enrichment you can trust."

## Color Palette

### Dark Theme (Primary)

| Color | Hex | Usage |
|-------|-----|-------|
| Background Primary | `#1a1d1e` | Main page background |
| Background Secondary | `#2d3436` | Section backgrounds, footer |
| Card Background | `#3d4446` | Cards, form inputs |
| Border | `#4d5456` | Borders, dividers |
| Teal (Accent) | `#00b894` | CTAs, links, highlights |
| Teal Light | `#00d9a7` | Hover states |
| Teal Dark | `#00a383` | Active states |
| Text Primary | `#ffffff` | Headings, primary text |
| Text Secondary | `#b2bec3` | Body text, descriptions |
| Text Muted | `#8a9499` | Placeholders, hints |

### CSS Variables

```css
:root {
  --color-bg-primary: #1a1d1e;
  --color-bg-secondary: #2d3436;
  --color-bg-card: #3d4446;
  --color-border: #4d5456;
  --color-teal: #00b894;
  --color-teal-light: #00d9a7;
  --color-teal-dark: #00a383;
  --color-text-primary: #ffffff;
  --color-text-secondary: #b2bec3;
  --color-text-muted: #8a9499;
}
```

## Typography

**Font Family:** Inter (Google Fonts)

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Type Scale

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| H1 | 3rem (48px) | 700 | 1.2 |
| H2 | 2.25rem (36px) | 600 | 1.2 |
| H3 | 1.5rem (24px) | 600 | 1.2 |
| H4 | 1.25rem (20px) | 600 | 1.2 |
| Body | 1rem (16px) | 400 | 1.6 |
| Small | 0.875rem (14px) | 400 | 1.5 |

## Logo

### Files

Located in `/assets/logos/logos-svg/`:

| File | Usage |
|------|-------|
| `verum-logo-horizontal-dark.svg` | Header & footer (white text for dark bg) |
| `verum-logo-horizontal-light.svg` | Light backgrounds (dark text) |
| `verum-favicon-32.svg` | Browser favicon |

### Logo Mark

The Verum logo is a network/triangle symbol with three connected nodes, representing data connections and relationships. The nodes are teal (#00b894) with connecting lines.

### Clear Space

Maintain padding equal to the height of the "V" in VERUM around the logo.

## Voice & Tone

### Principles (Harry Dry / Marketing Examples style)

**DO:**
- Problem-focused headlines ("Bad data costs you money")
- Specific statistics (23%, 30%, 50+)
- Concrete imagery ("chasing ghosts", "fighting fires")
- Value-focused CTAs ("Clean My Data")
- Direct, conversational language

**DON'T:**
- "Unlock", "Unleash", "Empower", "Supercharge"
- "Revolutionary", "Game-changing", "Best-in-class"
- Vague claims without specifics
- "Book a Demo", "Get Started", "Contact Us" (use value CTAs instead)
- Corporate jargon

### Example Headlines

Good:
- "Bad data costs you money"
- "Same person, 5 records"
- "30% of your contacts changed jobs"

Avoid:
- "Unlock the power of clean data"
- "Revolutionary data solutions"
- "Supercharge your sales pipeline"

## Buttons

### Primary (Teal)
```css
background: #00b894;
color: #ffffff;
```
Use for main CTAs: "Clean My Data", "Get Started"

### Secondary (Outline)
```css
background: transparent;
border: 1px solid #4d5456;
color: #ffffff;
```
Use for secondary actions: "Learn More", "See How It Works"

## Spacing Scale

```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
--space-4xl: 6rem;     /* 96px */
```

## Border Radius

```css
--radius-sm: 4px;
--radius-md: 6px;
--radius-lg: 12px;
--radius-full: 9999px;
```

## Shadows & Effects

### Glow Effect (Hover)
```css
box-shadow: 0 0 20px rgba(0, 184, 148, 0.3);
```

Used on buttons and cards on hover to create teal glow effect.
