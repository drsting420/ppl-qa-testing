# QA Checklist — PPL.cz Website

This checklist was used during manual testing of the PPL.cz website within a diploma QA project.  
It covers core user functionality, UI behavior, and basic quality attributes.

---

## 1. Shipment Tracking (Vyhledat zásilku)

- [ ] Tracking page is accessible from the homepage
- [ ] Input field for shipment number is visible and enabled
- [ ] Valid shipment number can be entered
- [ ] Invalid shipment number format is rejected
- [ ] Non-existing shipment number is handled correctly
- [ ] Error messages are displayed clearly and understandably
- [ ] Input mask works correctly
- [ ] Localization works correctly (CS / EN)
- [ ] Shipment details page opens for valid number
- [ ] Shipment status, date, and route information are displayed
- [ ] Page layout remains stable after form submission

---

## 2. Pickup Points Map (Parcelshop / Parcelbox)

- [ ] Pickup points map is accessible from the homepage
- [ ] Search field for address or postal code is visible
- [ ] Autocomplete suggestions appear while typing address
- [ ] Search by full address works correctly
- [ ] Search by partial address works correctly
- [ ] Search by postal code (PSČ) works correctly
- [ ] Map updates after search
- [ ] Pickup points list is displayed
- [ ] Parcelshop filter works correctly
- [ ] Parcelbox filter works correctly
- [ ] Pickup point card opens after selection
- [ ] Pickup point card contains address and opening hours
- [ ] Geolocation permission request is handled correctly
- [ ] Map zoom in/out works correctly
- [ ] Map navigation (dragging) works correctly
- [ ] Map adapts correctly to different screen sizes

---

## 3. Navigation and Content Pages

- [ ] Main menu is visible on all pages
- [ ] All main menu items are displayed
- [ ] Menu item text matches expected labels
- [ ] Internal links navigate to correct pages
- [ ] External links open in a new browser tab
- [ ] Language switch (CS / EN) works correctly
- [ ] Page redirects work as expected
- [ ] 404 error page is displayed for invalid URLs
- [ ] 404 page contains navigation options
- [ ] Website is usable with keyboard navigation
- [ ] Focus order is logical
- [ ] Content pages display correctly on mobile devices
- [ ] No critical layout issues on different resolutions

---

## 4. SEO and Technical Checks

- [ ] Page title is present
- [ ] Meta description is present
- [ ] Headings structure is logical
- [ ] Structured data (Schema.org) is reviewed
- [ ] Missing structured data is documented as a defect

---

## 5. General UI and Stability

- [ ] No critical JavaScript errors in browser console
- [ ] Page load time is acceptable
- [ ] Buttons and links are clickable
- [ ] No broken images detected
- [ ] No visible UI overlaps or broken elements
