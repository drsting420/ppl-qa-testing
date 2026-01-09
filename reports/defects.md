# Defects Report — PPL.cz Website

## DEF-001 — Map Zoom Controls Disappear on Mobile Screen Rotation

**ID:** DEF-001  
**Title:** Map zoom controls (+ / -) disappear after screen rotation on mobile devices  
**Severity:** Medium  
**Priority:** Medium  
**Status:** Open  
**Environment:** Mobile devices (emulated and real), Google Chrome  
**Component:** Pickup Points Map

### Description
When viewing the pickup points map on a mobile device, the zoom controls (+ / -) are visible in portrait orientation.  
After rotating the screen to landscape orientation, the zoom controls disappear and cannot be restored without reloading the page.

### Steps to Reproduce
1. Open the PPL.cz website on a mobile device
2. Navigate to the pickup points map
3. Ensure zoom controls (+ / -) are visible
4. Rotate the device from portrait to landscape orientation

### Expected Result
Zoom controls remain visible and functional after screen rotation.

### Actual Result
Zoom controls disappear after rotation and are no longer available.

### Impact
Users are unable to zoom the map after changing screen orientation, reducing usability on mobile devices.

---

## DEF-002 — Missing Structured Data (Schema.org) on Homepage

**ID:** DEF-002  
**Title:** Structured data (Schema.org) is missing on the homepage  
**Severity:** Low  
**Priority:** Low  
**Status:** Open  
**Environment:** Desktop and Mobile  
**Component:** SEO / Technical Markup

### Description
The homepage of the PPL.cz website does not contain structured data markup using Schema.org standards.

### Steps to Reproduce
1. Open the PPL.cz homepage
2. Inspect the page source or use a structured data testing tool
3. Check for Schema.org markup

### Expected Result
Homepage contains valid structured data markup according to Schema.org standards.

### Actual Result
No structured data markup is present on the homepage.

### Impact
Missing structured data may negatively affect search engine optimization (SEO) and rich search results.

---

## Summary

| Defect ID | Severity | Status |
|----------|----------|--------|
| DEF-001  | Medium   | Open   |
| DEF-002  | Low      | Open   |

The identified defects do not block core user functionality but should be addressed to improve usability and SEO quality.
