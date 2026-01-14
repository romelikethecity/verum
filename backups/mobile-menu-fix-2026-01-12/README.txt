Mobile Menu Background Fix - January 12, 2026
=============================================

PROBLEM:
Mobile hamburger menu had a transparent background, allowing page content
to show through behind the navigation links.

ROOT CAUSE:
The header element has `backdrop-filter: blur(8px)` which creates a new
containing block for `position: fixed` descendants. This caused .nav--mobile
to be positioned relative to the header, not the viewport.

SOLUTION:
Moved the mobile nav element outside the header (as a sibling, not a child)
to avoid the backdrop-filter containment issue.

FILES MODIFIED:
1. css/styles.css (lines 290-291)
   - Changed `background: #1a1d1e` to `background-color: #1a1d1e !important`
   - Added `opacity: 1`

2. js/components.js
   - Separated mobile nav HTML into its own template (mobileNavHTML)
   - Changed injection to use `insertAdjacentHTML('afterend', mobileNavHTML)`
     to place nav after header instead of inside it
   - Updated querySelector to find .nav--mobile from document instead of headerEl

COMMIT: 9321cee
