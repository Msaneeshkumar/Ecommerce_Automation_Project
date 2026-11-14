# E-Commerce Web Automation Testing Framework

A Python-based end-to-end test automation framework for the [SauceDemo](https://www.saucedemo.com/) e-commerce application, developed using **Playwright, Pytest, and the Page Object Model (POM)**.

## Tech Stack

- **Programming Language:** Python 3.12
- **Automation Tool:** Playwright
- **Testing Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** pytest-html
- **CI:** GitHub Actions
- **Version Control:** Git and GitHub

## Features

- Automated login validation with positive and negative scenarios
- Inventory product validation and price sorting
- Shopping cart functionality testing
- End-to-end checkout automation
- Data-driven testing using Pytest parameterization
- Reusable Pytest fixtures
- Automatic screenshot capture on test failures
- HTML test execution reports
- GitHub Actions workflow for automated test execution

## Test Coverage

| Module | Test Cases |
|---|---:|
| Login and Inventory | 6 |
| Shopping Cart | 4 |
| Checkout | 5 |
| **Total** | **15** |

## Project Structure

```text
Ecommerce_Automation_Project/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Msaneeshkumar/Ecommerce_Automation_Project.git
cd Ecommerce_Automation_Project
```

**2. Create and activate a virtual environment**

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Install Playwright Chromium**

```bash
python -m playwright install chromium
```

## Running Tests

Run all tests:

```bash
python -m pytest -v
```

Run checkout tests:

```bash
python -m pytest tests/test_checkout.py -v
```

Generate an HTML report:

```bash
python -m pytest -v --html=reports/test_report.html --self-contained-html
```

## Test Reports and Screenshots

The framework generates HTML reports using `pytest-html`.

When a test fails during execution, a screenshot is automatically captured and saved in the `screenshots/` directory to support debugging.

## Continuous Integration

The project includes a GitHub Actions workflow configured to run automated tests on pushes and pull requests targeting the `main` branch.

The workflow installs Python dependencies, sets up Playwright Chromium, executes Pytest tests, and uploads the HTML test report as an artifact.

## Latest Local Test Results

**15 tests passed** during local execution.

## Learning Outcomes

This project demonstrates practical knowledge of:

- Python automation programming
- Playwright browser automation
- Pytest fixtures and parameterization
- Page Object Model architecture
- Functional and end-to-end testing
- Test execution reporting and debugging
- GitHub Actions CI configuration

## Author

Aneesh Kumar

**GitHub:** [Msaneeshkumar](https://github.com/Msaneeshkumar)

*This project was developed as part of hands-on QA automation learning and portfolio development.*