# PPL.cz QA Testing Project

This repository contains a manual and automated QA testing project for the **PPL.cz** delivery service website.
The project was created as part of a diploma work and demonstrates practical QA skills applicable to real commercial projects.

---

## Project Overview

The main goal of this project was to test the core user functionality of the PPL.cz website, focusing on critical user flows and business-important features.

Key areas covered:
- Shipment tracking
- Pickup points map
- Website navigation and content pages

---

## Scope of Testing

### Manual Testing

Manual testing was performed to validate:
- Shipment tracking functionality
- Pickup point search and map behavior
- Website navigation and menu structure
- Localization (CS / EN)
- Accessibility and keyboard navigation
- Adaptive layout (desktop / mobile)
- Negative and edge-case scenarios

All manual test cases and checklists are stored in the documentation section of the project.

---

### Automated Testing

Automated UI tests were implemented for the most important and stable user scenarios.

Technology stack:
- Python
- Selenium WebDriver
- Pytest
- Allure Reports

Automated test cases:
- TC-TRK-001 — Valid shipment tracking number
- TC-MAP-001 — Pickup point search by address
- TC-NAV-001 — Main menu structure and navigation

The automated tests are implemented using stable locators, explicit waits, and clear assertions to ensure reliability and readability.

---

## Project Structure

ppl-qa-testing/
├── tests/        Automated UI tests (Pytest + Selenium)
├── docs/         Manual test cases and checklists
├── reports/      Test reports (Allure)
├── requirements.txt
└── README.md

---

## How to Run Tests

1. Clone the repository:
git clone https://github.com/drsting420/ppl-qa-testing.git

2. Install dependencies:
pip install -r requirements.txt

3. Run automated tests:
pytest tests

Optional: generate Allure report:
allure serve reports

---

## Skills Demonstrated

- Test analysis and test design
- Manual functional testing
- UI test automation with Selenium
- Python and Pytest
- Bug detection and defect analysis
- Git and GitHub workflow
- Test documentation and reporting

---

## Author

Pavel Gribovskiy  
Junior QA Engineer (Manual + Automation)

This project reflects my practical experience in web application testing and can be used as a reference for freelance or entry-level QA work.
