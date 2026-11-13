# E-commerce Automation Testing Project

A web automation testing project built using Python, Playwright, Pytest, and the Page Object Model (POM) design pattern.

## Application Under Test

SauceDemo: https://www.saucedemo.com/

## Technologies Used

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git and GitHub

## Features Automated

### Login Testing
- Successful login using valid credentials
- Invalid login scenarios using parameterization
- Validation of login error messages

### Product Testing
- Verification of product count after login
- Product sorting by price (low to high)

## Framework Features

- Reusable Page Object classes
- Pytest fixtures for browser setup and teardown
- Parameterized login testing
- Playwright assertions

## Project Structure

    Ecommerce_Automation_Project/
    ├── pages/
    │   ├── login_page.py
    │   └── inventory_page.py
    ├── tests/
    │   ├── test_login.py
    │   └── test_products.py
    ├── conftest.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Installation and Execution

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

       pip install -r requirements.txt

4. Install the Chromium browser:

       playwright install chromium

5. Run the tests:

       python -m pytest -v

## Current Test Coverage

- 6 automated test executions
- Login and inventory page scenarios

## Future Enhancements

- Shopping cart automation
- Checkout workflow automation
- Additional positive and negative test scenarios
- HTML test reports
- Screenshots on test failures
- GitHub Actions CI/CD integration

## Author

AneeshKumar M