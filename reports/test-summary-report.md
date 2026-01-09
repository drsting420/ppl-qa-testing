# Test Summary Report — PPL.cz Website

## 1. Project Information

**Project:** PPL.cz Website QA Testing  
**Testing Type:** Manual and Automated Testing  
**Testing Period:** Diploma project timeframe  
**Tester:** Pavel Gribovskiy  
**Role:** Junior QA Engineer (Manual + Automation)

---

## 2. Testing Scope

The purpose of this testing was to verify the correct operation of core user functionality of the PPL.cz delivery service website.

The following functional areas were covered:

- Shipment tracking
- Pickup points map and search
- Website navigation and content pages
- Basic accessibility and UI behavior
- SEO-related technical checks

---

## 3. Types of Testing Performed

### Manual Testing
- Functional testing
- Negative testing
- UI and usability testing
- Localization testing (CS / EN)
- Responsive testing
- Accessibility checks (keyboard navigation)
- Basic SEO checks

### Automated Testing
Automated tests were implemented for selected critical scenarios using Selenium WebDriver and Pytest.

Automated test cases:
- **TC-TRK-001** — Valid shipment tracking number
- **TC-MAP-001** — Pickup point search by address
- **TC-NAV-001** — Main menu structure and navigation

---

## 4. Test Environment

- **Operating System:** Windows
- **Browser:** Google Chrome (latest stable version)
- **Automation Tools:** Selenium WebDriver, Pytest
- **Reporting Tool:** Allure Reports
- **Programming Language:** Python

---

## 5. Test Execution Results

| Area                     | Status  |
|--------------------------|---------|
| Shipment Tracking        | Passed  |
| Pickup Points Map        | Passed  |
| Navigation and Content   | Passed  |
| Automated Test Cases     | Passed  |

All automated test cases were executed successfully without critical failures.

---

## 6. Defects Summary

During testing, the following defects were identified:

1. **Map zoom controls issue**  
   On mobile devices, map zoom controls (+ / -) disappear when the screen orientation is changed.

2. **Missing structured data (Schema.org)**  
   Structured data markup is missing on the homepage, which may negatively impact SEO.

Both issues were documented and included in the defect analysis section of the diploma.

---

## 7. Risks and Limitations

- Only a limited number of test cases were automated.
- The majority of scenarios were tested manually.
- Performance and security testing were not included in scope.
- Testing was performed in a limited browser environment.

---

## 8. Conclusion

The core functionality of the PPL.cz website operates correctly and meets basic quality expectations.  
The implemented automated tests demonstrate the feasibility of further automation expansion.  
Identified defects do not block core user scenarios but should be addressed to improve usability and SEO quality.
This project demonstrates practical QA skills including test planning, manual testing, basic automation, and defect analysis.

