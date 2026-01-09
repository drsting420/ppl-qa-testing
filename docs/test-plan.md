# Test Plan — PPL.cz Website

## 1. Introduction
This test plan describes the scope, objectives, approach, and resources for testing the PPL.cz delivery service website.  
The document covers both manual and automated testing activities performed as part of a diploma QA project.

---

## 2. Test Objectives
The main objectives of testing are:
- Verify correct functionality of core user features
- Identify functional and usability defects
- Ensure stable navigation and content availability
- Validate basic accessibility and responsive behavior
- Demonstrate manual and automated QA skills

---

## 3. Scope of Testing

### 3.1 In Scope
The following functionality was included in testing:
- Shipment tracking (Vyhledat zásilku)
- Pickup points map (Parcelshop / Parcelbox)
- Website navigation and main menu
- Content pages
- Localization (Czech / English)
- Responsive layout (desktop and mobile)
- Basic accessibility checks
- Input validation and negative scenarios

### 3.2 Out of Scope
The following areas were not tested:
- Backend services and databases
- Payment processing
- Performance and load testing
- Security testing
- API testing

---

## 4. Types of Testing
The following types of testing were applied:
- Functional testing
- Manual UI testing
- Automated UI testing
- Exploratory testing
- Regression testing (limited scope)
- Negative and edge case testing

---

## 5. Test Approach

### 5.1 Manual Testing
Manual testing was performed based on predefined test cases and checklists.  
Testing focused on user scenarios, UI behavior, validation messages, and navigation logic.

### 5.2 Automated Testing
Automated tests were implemented for selected critical scenarios using:
- Python
- Selenium WebDriver
- Pytest

Automation was applied to:
- Shipment tracking (valid input)
- Pickup point search by address
- Main menu navigation

---

## 6. Test Environment
- Operating System: Windows
- Browser: Google Chrome (latest version)
- Test Environment: Production website (https://www.ppl.cz)
- Screen resolutions: Desktop and mobile viewports

---

## 7. Test Data
Test data included:
- Valid shipment tracking numbers
- Invalid and non-existing tracking numbers
- Real addresses and partial address inputs for map search

---

## 8. Entry and Exit Criteria

### 8.1 Entry Criteria
- Website is accessible
- Test cases are prepared
- Test environment is available

### 8.2 Exit Criteria
- All planned test cases executed
- Critical defects identified and documented
- Test summary report prepared

---

## 9. Deliverables
The following deliverables were produced:
- Test plan
- Manual test cases
- Checklists
- Automated test scripts
- Defect descriptions
- Test summary report

---

## 10. Risks and Limitations
- Testing was limited to UI level
- Changes on the production website may affect test stability
- Automated tests depend on UI locators and page structure

---

## 11. Conclusion
This test plan provides a structured approach to validating the core functionality of the PPL.cz website and demonstrates practical QA testing skills in both manual and automated testing.
