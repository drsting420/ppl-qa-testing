# Test Cases — PPL.cz Website

This document contains manual test cases executed during testing of the PPL.cz website as part of a diploma QA project.

---

## 1. Shipment Tracking (Vyhledat zásilku)

### TC-TRK-001 — Valid shipment tracking number
**Description:** Verify correct behavior when a valid shipment number is entered.  
**Preconditions:** Website is accessible.  
**Steps:**
1. Open https://www.ppl.cz
2. Navigate to "Vyhledat zásilku"
3. Enter a valid shipment number
4. Submit the form  
**Expected Result:**  
- Shipment details page is displayed  
- Shipment status information is visible  
- No error messages are shown

---

### TC-TRK-002 — Valid format but non-existing shipment number
**Description:** Verify system behavior when a correctly formatted but non-existing number is entered.  
**Steps:**
1. Open shipment tracking page
2. Enter a non-existing shipment number
3. Submit the form  
**Expected Result:**  
- Informational or error message is displayed  
- Page does not break  
- User remains on tracking page

---

### TC-TRK-003 — Invalid shipment number format
**Description:** Verify input validation for incorrect shipment number format.  
**Steps:**
1. Open shipment tracking page
2. Enter invalid input (letters, special characters)
3. Submit the form  
**Expected Result:**  
- Validation error message is displayed  
- Form submission is blocked

---

### TC-TRK-004 — Navigation to shipment details
**Description:** Verify navigation and content on shipment details page.  
**Steps:**
1. Enter valid shipment number
2. Open shipment details page  
**Expected Result:**  
- Shipment status timeline is visible  
- Shipment number is displayed correctly  
- Page content is readable and structured

---

## 2. Pickup Points Map (Parcelshop / Parcelbox)

### TC-MAP-001 — Search pickup point by address
**Description:** Verify pickup point search using full and partial address.  
**Steps:**
1. Open pickup points map
2. Enter full address
3. Select suggestion from autocomplete  
**Expected Result:**  
- Map updates with results  
- Pickup points list is displayed

---

### TC-MAP-002 — Search pickup point by postal code
**Description:** Verify search functionality using postal code (PSČ).  
**Steps:**
1. Open pickup points map
2. Enter postal code
3. Submit search  
**Expected Result:**  
- Relevant pickup points are displayed

---

### TC-MAP-003 — Parcelshop / Parcelbox filters
**Description:** Verify filtering of pickup points by type.  
**Steps:**
1. Open pickup points map
2. Enable Parcelshop or Parcelbox filter  
**Expected Result:**  
- Only selected pickup point types are shown

---

### TC-MAP-004 — Pickup point details card
**Description:** Verify pickup point card information.  
**Steps:**
1. Select pickup point from list
2. Open pickup point details  
**Expected Result:**  
- Address, opening hours, and services are displayed

---

### TC-MAP-005 — Geolocation
**Description:** Verify geolocation-based search.  
**Steps:**
1. Allow browser location access
2. Open pickup points map  
**Expected Result:**  
- Nearest pickup points are displayed

---

### TC-MAP-006 — Map navigation
**Description:** Verify map zoom and movement.  
**Steps:**
1. Zoom in and out
2. Move map area  
**Expected Result:**  
- Map responds correctly to user actions

---

### TC-MAP-007 — Responsive behavior
**Description:** Verify map behavior on different screen sizes.  
**Steps:**
1. Open map on desktop and mobile view  
**Expected Result:**  
- Map and controls adapt correctly

---

## 3. Navigation and Content Pages

### TC-NAV-001 — Main menu structure and navigation
**Description:** Verify main menu items and navigation.  
**Steps:**
1. Open homepage
2. Check all main menu items
3. Click each menu item  
**Expected Result:**  
- Correct pages open  
- External links open in new tab where applicable

---

### TC-NAV-002 — Links and redirects (CS / EN)
**Description:** Verify correct language navigation and redirects.  
**Steps:**
1. Switch site language
2. Navigate between pages  
**Expected Result:**  
- Correct localized pages are displayed

---

### TC-NAV-003 — 404 error page
**Description:** Verify behavior for non-existing URLs.  
**Steps:**
1. Open invalid URL  
**Expected Result:**  
- Custom 404 page is displayed  
- Navigation options are available

---

### TC-NAV-004 — Keyboard accessibility
**Description:** Verify basic keyboard navigation.  
**Steps:**
1. Navigate site using keyboard only  
**Expected Result:**  
- Focus order is logical  
- Interactive elements are accessible

---

### TC-NAV-005 — Responsive layout
**Description:** Verify content display on different resolutions.  
**Steps:**
1. Resize browser window
2. Open content pages  
**Expected Result:**  
- Layout adapts correctly  
- No overlapping elements

---

### TC-NAV-006 — Meta tags and structured data
**Description:** Verify presence of meta tags and basic SEO elements.  
**Steps:**
1. Inspect page source of homepage  
**Expected Result:**  
- Meta title and description are present  
- Structured data issues are identified if missing
