# 🚀 Playwright MCP Automation Framework

## 📋 Project Overview
The Playwright MCP Automation Framework is a comprehensive end-to-end testing solution for web applications using Playwright with Python, Pytest, and MCP (Model Context Protocol) for AI-assisted test generation. It supports cross-browser testing, modular code structure, and detailed reporting for efficient automation.

## 🛠️ Tech Stack
- **Language:** Python
- **Testing Framework:** Pytest, Playwright
- **Reporting:** Allure, HTML Reports
- **Browsers:** Chromium, Firefox, WebKit
- **Version Control:** Git
- **Code Quality:** Pytest plugins, modular structure

## 🏗️ Architecture
The framework follows a modular Page Object Model (POM) architecture:
- **Test Layer:** Contains test cases using Pytest fixtures.
- **Page Objects:** Reusable classes for UI interactions.
- **Utilities:** Helpers for data management and common functions.
- **Configuration:** Pytest and Playwright configs for setup.

### Framework Structure
```
playright-mcp-automation-framework/
├── pages/                          # Page Object classes
│   ├── LoginPage.py
│   ├── InventoryPage.py
│   ├── CartPage.py
│   └── CheckoutPage.py
├── tests/                          # Test files
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/                          # Utilities and helpers
│   ├── helpers.py
│   └── test-data.json
├── allure-results/                 # Allure report data
├── allure-report/                 # Generated Allure HTML report
├── test-results/                   # HTML reports
├── pytest.ini                      # Pytest configuration
├── requirements.txt                # Python dependencies
├── package.json                    # Node.js dependencies (MCP)
├── server.py                       # MCP server for AI integration
└── README.md
```

### Dataflow Diagram
```
[User/Test Runner] --> [Pytest] --> [Test Files] --> [Page Objects] --> [Playwright Browser]
                              |           |              |
                              |           |              --> [Utils/Helpers]
                              |           |
                              --> [Allure Reporting] --> [allure-results/]
                              --> [HTML Reporting] --> [test-results/]
```

## 🧰 Test Coverage

The framework includes **39 comprehensive test cases** covering the full SauceDemo e-commerce flow:

### Login Functionality (9 tests)
| Test Case | Description |
|-----------|-------------|
| `test_valid_login_standard_user` | Verify standard user can log in successfully |
| `test_invalid_username` | Verify error for invalid username |
| `test_invalid_password` | Verify error for invalid password |
| `test_locked_out_user` | Verify locked out user receives error message |
| `test_empty_username_and_password` | Verify validation for empty credentials |
| `test_logout_flow` | Verify logout redirects to login page |
| `test_direct_url_access` | Verify protection against unauthorized access |
| `test_session_handling` | Verify session invalidation after cookie clear |
| `test_performance_user` | Verify performance glitch user login |

### Inventory Functionality (12 tests)
| Test Case | Description |
|-----------|-------------|
| `test_add_single_item_to_cart` | Verify single item can be added to cart |
| `test_add_multiple_items_to_cart` | Verify multiple items can be added |
| `test_remove_item_from_cart_on_inventory_page` | Verify item removal from inventory |
| `test_sort_products_by_name_a_to_z` | Verify A-Z alphabetical sorting |
| `test_sort_products_by_name_z_to_a` | Verify Z-A alphabetical sorting |
| `test_sort_products_by_price_low_to_high` | Verify low-to-high price sorting |
| `test_sort_products_by_price_high_to_low` | Verify high-to-low price sorting |
| `test_navigate_to_cart_from_inventory` | Verify cart navigation from inventory |
| `test_view_product_details` | Verify product details page access |
| `test_add_item_from_product_details_page` | Verify adding item from details page |
| `test_ui_state_consistency` | Verify UI consistency during operations |
| `test_multi_tab_behavior` | Verify multi-tab functionality |

### Cart Functionality (5 tests)
| Test Case | Description |
|-----------|-------------|
| `test_view_cart_with_items` | Verify cart displays items correctly |
| `test_remove_item_from_cart` | Verify item removal from cart |
| `test_continue_shopping_from_cart` | Verify navigation back to inventory |
| `test_checkout_from_cart` | Verify checkout navigation from cart |
| `test_cart_persists_after_page_refresh` | Verify cart persists after refresh |

### Checkout Functionality (13 tests)
| Test Case | Description |
|-----------|-------------|
| `test_valid_checkout` | Verify complete checkout with valid info |
| `test_missing_first_name` | Verify validation for missing first name |
| `test_missing_last_name` | Verify validation for missing last name |
| `test_missing_postal_code` | Verify validation for missing postal code |
| `test_cancel_checkout` | Verify cancel checkout returns to cart |
| `test_checkout_with_multiple_items` | Verify checkout with multiple items |
| `test_checkout_overview_page` | Verify overview page displays items |
| `test_cancel_from_checkout_overview` | Verify cancel from overview page |
| `test_complete_order_and_return_to_inventory` | Verify post-checkout navigation |
| `test_checkout_with_empty_cart` | Verify checkout button with empty cart |
| `test_price_validation` | Verify total price calculation accuracy |
| `test_tax_validation` | Verify tax calculation |
| `test_remove_item_from_overview` | Verify item removal from overview |

## 📸 Screenshots

The framework automatically captures screenshots during test execution for visual verification. Screenshots are attached to Allure reports:

- **Login Tests**: Login success, error messages, logout confirmation
- **Inventory Tests**: Product listings, sorting, cart badge updates
- **Cart Tests**: Cart items, empty cart, checkout button
- **Checkout Tests**: Checkout form, order completion, error states

Screenshot attachments are stored in `allure-report/data/attachments/` and displayed in the Allure HTML report.

## 📸 Evidences

The following table shows the passed test evidence screenshots captured during test execution:

| # | Screenshot | Test Case | Description |
|---|------------|-----------|-------------|
| 1 | ![Login Successful](attachments_passed/8d393226dc2b988f.png) | test_valid_login_standard_user | Standard user login successful - redirected to inventory page |
| 2 | ![Invalid Username](attachments_passed/8f1f4bba2c282617.png) | test_invalid_username | Error message for invalid username |
| 3 | ![Locked Out User](attachments_passed/69a327da212120d6.png) | test_locked_out_user | Locked out user error message displayed |
| 4 | ![Empty Credentials](attachments_passed/515bebc54dd573e0.png) | test_empty_username_and_password | Validation error for empty credentials |
| 5 | ![Logout Successful](attachments_passed/1361d99ad8db9786.png) | test_logout_flow | Logout successful - redirected to login page |
| 6 | ![Cart with Items](attachments_passed/7681a0a453effa3e.png) | test_view_cart_with_items | Cart displays item count correctly |
| 7 | ![Checkout Complete](attachments_passed/7876b4090366bfea.png) | test_valid_checkout | Order completed successfully with confirmation message |
| 8 | ![Inventory Page](attachments_passed/846930f296721ace.png) | test_add_single_item_to_cart | Inventory page with add to cart functionality |
| 9 | ![Multiple Items Cart](attachments_passed/9914165bb148fc46.png) | test_checkout_with_multiple_items | Cart showing multiple items |
| 10 | ![Cart Badge Update](attachments_passed/8287147735a70420.png) | test_add_multiple_items_to_cart | Cart badge shows correct count |
| 11 | ![Product Sorting](attachments_passed/a3afca59a43f9abb.png) | test_sort_products_by_name_a_to_z | Products sorted alphabetically A-Z |
| 12 | ![Checkout Overview](attachments_passed/c1fc9fa12085df8b.png) | test_checkout_overview_page | Checkout overview with item details |
| 13 | ![Price Validation](attachments_passed/d1ccb38553f3171d.png) | test_price_validation | Price breakdown with tax calculation |
| 14 | ![Cart Empty State](attachments_passed/d68b13f8bba996b7.png) | test_checkout_with_empty_cart | Empty cart checkout button state |
| 15 | ![UI Consistency](attachments_passed/d842a3cd4886acca.png) | test_ui_state_consistency | UI state consistent during operations |
| 16 | ![Remove from Cart](attachments_passed/e2eb78434e6d2f85.png) | test_remove_item_from_cart | Item removed - cart shows zero items |
| 17 | ![Tax Calculation](attachments_passed/e7c0b342c8f3929b.png) | test_tax_validation | Tax calculated and displayed correctly |
| 18 | ![Order Complete](attachments_passed/fc854cf885f2446c.png) | test_complete_order_and_return_to_inventory | Order complete message displayed |

> **Note:** All 18 screenshots represent passed test executions demonstrating the functionality of the SauceDemo e-commerce flow.

## 🎯 Features
- Cross-browser testing (Chromium, Firefox, WebKit) in headed mode
- Parallel test execution with Pytest
- Modular Page Object Model for reusable code
- AI-assisted test generation via MCP server
- Comprehensive reporting (Allure and HTML)
- Headed execution for visual verification
- Test data management with JSON fixtures

## ⚙️ Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbhishekKandari/playright-mcp-automation-framework.git
   cd playright-mcp-automation-framework
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install  # Install browser binaries
   ```

4. **Set up environment variables** (if needed) in a `.env` file.

## 🧪 Test Execution
Run all tests:
```bash
pytest
```

Run specific test files:
```bash
pytest tests/test_login.py
```

Run with specific browser:
```bash
pytest --browser chromium
```

Run in parallel (default):
```bash
pytest  # Uses fullyParallel: true in config
```

Run with headed mode (default):
```bash
pytest  # headless: false in playwright.config.js
```

## 📊 Reporting

The framework provides comprehensive reporting capabilities through multiple channels:

### HTML Reports
Generated automatically in `test-results/report.html`:
```bash
pytest --html=test-results/report.html
```

### Allure Reports
Generate Allure results:
```bash
pytest --alluredir=allure-results
```

Generate and open Allure report:
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

Alternatively, serve Allure report directly (requires Allure CLI):
```bash
allure serve allure-results
```

### 📈 Report Dashboard Preview

![Allure Report Dashboard](reporting_screenshots/img.png)

> **Note:** The Allure report provides a comprehensive view of test execution with:
> - **Test Categories**: Epic → Feature → Story hierarchy
> - **Visual Trends**: Pass/Fail trends over time
> - **Attachment Support**: Screenshots, logs, and videos
> - **Retries**: Retry analysis and history

### Report Contents

| Report Type | Location | Description |
|-------------|----------|-------------|
| **HTML Report** | `test-results/report.html` | Pytest HTML report with test results |
| **Allure Results** | `allure-results/` | Raw JSON test result data |
| **Allure HTML** | `allure-report/` | Interactive HTML report with charts |
| **Screenshots** | `allure-report/data/attachments/` | Visual evidence of test execution |

---

> 📁 **Note:** The `attachments_passed/` and `reporting_screenshots/` folders contain screenshots used exclusively for README documentation purposes. These are not part of the automated test execution output.

## 💡 Best Practices
- **Modular Code:** Use Page Objects for UI interactions to ensure reusability.
- **Test Data:** Store test data in `utils/test-data.json` and load via helpers.
- **Assertions:** Use `assert` for simple checks; `expect` from Playwright for complex validations.
- **Fixtures:** Leverage Pytest fixtures for setup/teardown (e.g., autouse for login).
- **Parallel Execution:** Run tests in parallel for faster execution.
- **Headed Mode:** Use headed execution for debugging and visual verification.
- **Reporting:** Always generate reports for test analysis.
- **Version Control:** Commit changes regularly and use branches for features.
- **Code Quality:** Follow PEP8 for Python code; keep functions small and focused.
- **Error Handling:** Use try-except in page objects for robust interactions.
- **Documentation:** Update README and add docstrings to classes/functions.

## 🔧 Commands Summary
- **Install dependencies:** `pip install -r requirements.txt`
- **Install browsers:** `playwright install`
- **Run all tests:** `pytest`
- **Run specific tests:** `pytest tests/<file>.py`
- **Generate HTML report:** `pytest --html=test-results/report.html`
- **Generate Allure results:** `pytest --alluredir=allure-results`
- **Generate Allure report:** `allure generate allure-results --clean -o allure-report`
- **Open Allure report:** `allure open allure-report`
- **Serve Allure report:** `allure serve allure-results`
- **Run MCP server:** `python server.py`

## 🚀 Future Enhancements

The framework is designed to be extensible. The following enhancements are planned for future implementation:

### 1. API Integration

- **REST API Testing**: Add support for API endpoint testing using Python's `requests` library or Playwright's API route handling
- **API Test Layer**: Create dedicated API test files (`tests/api/`)
- **API Utilities**: Implement `utils/api_client.py` for reusable API calls
- **Response Validation**: Compare API responses against expected schemas

```python
# Planned API test structure
def test_api_create_user():
    response = api_client.post('/api/users', data=user_payload)
    assert response.status_code == 201
    assert response.json()['id'] is not None
```

### 2. Database Integration

- **Database Connectivity**: Add SQLAlchemy or direct database connections (PostgreSQL, MySQL)
- **Data Fixtures**: Load test data from database instead of JSON files
- **State Verification**: Verify application state by querying the database
- **Test Data Management**: Create utilities for seeding and cleaning test data

```python
# Planned database fixture
@pytest.fixture
def db_connection():
    return create_engine('postgresql://user:pass@localhost/testdb')

def test_verify_user_in_database(db_connection):
    result = db_connection.execute("SELECT * FROM users WHERE username = 'test'")
    assert result.fetchone() is not None
```

### 3. CI/CD Implementation

- **GitHub Actions**: Add `.github/workflows/` with automated test pipelines
- **Jenkins Pipeline**: Add `Jenkinsfile` for enterprise CI/CD integration
- **Docker Support**: Add `Dockerfile` and `docker-compose.yml` for containerized execution
- **Cloud Execution**: Support for Sauce Labs, BrowserStack, or LambdaTest execution

#### CI/CD Block Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CI/CD Pipeline Architecture                           │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │   CODE   │     │  BUILD   │     │   TEST   │     │  DEPLOY  │
    │  PUSH    │────▶│  STAGE   │────▶│  STAGE   │────▶│  STAGE   │
    └──────────┘     └──────────┘     └──────────┘     └──────────┘
         │                │                │                │
         ▼                ▼                ▼                ▼
    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  GitHub  │     │  Install │     │  Run     │     │  Publish │
    │  Trigger │     │  Deps    │     │  Tests   │     │  Reports │
    └──────────┘     └──────────┘     └──────────┘     └──────────┘
                              │                │                │
                              ▼                ▼                ▼
                         ┌──────────┐     ┌──────────┐     ┌──────────┐
                         │ Playwright│    │ Allure   │     │  Slack/  │
                         │ Install   │    │ Report   │     │  Email   │
                         │ Browsers  │    │ HTML     │     │  Notify  │
                         └──────────┘     └──────────┘     └──────────┘
```

#### Enhanced Architecture Block Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Enhanced Framework Architecture                          │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────┐
                              │   CI/CD Server   │
                              │ (GitHub Actions) │
                              └────────┬────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
              ┌─────▼─────┐    ┌──────▼──────┐    ┌─────▼─────┐
              │   Docker  │    │   Pytest    │    │  MCP AI   │
              │  Container│───▶│   Runner    │───▶│  Server   │
              └───────────┘    └──────┬──────┘    └───────────┘
                                       │
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
   ┌─────▼─────┐              ┌──────▼──────┐              ┌─────▼─────┐
   │   UI/API  │              │  Database   │              │  Reports  │
   │   Tests   │              │   Tests     │              │  (Allure) │
   └─────┬─────┘              └──────┬──────┘              └───────────┘
         │                            │
    ┌────▼────┐                 ┌────▼────┐
    │Playwright│                │ SQLAlchemy│
    │Browser  │                │Database  │
    └─────────┘                 └──────────┘
```

### Implementation Roadmap

| Phase | Feature | Description | Priority |
|-------|---------|-------------|----------|
| Phase 1 | API Testing | Add REST API test support | High |
| Phase 2 | DB Integration | Connect to PostgreSQL/MySQL | Medium |
| Phase 3 | CI/CD Pipeline | GitHub Actions workflow | High |
| Phase 4 | Docker Support | Containerized test execution | Medium |
| Phase 5 | Cloud Integration | Sauce Labs / BrowserStack | Low |

### GitHub Actions Workflow Example

```yaml
name: Playwright Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps
      - name: Run tests
        run: pytest --alluredir=allure-results
      - name: Upload Allure results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: allure-results
          path: allure-results/
```

## 🔄 CI/CD Setup (GitHub Actions)

This project includes automated test execution via GitHub Actions. The workflow runs tests every 6 hours and on every push/PR.

### Setup Instructions

#### 1. Enable GitHub Actions
1. Go to your repository on GitHub
2. Navigate to the **Actions** tab
3. The workflow will be automatically detected from `.github/workflows/`

#### 2. Configure GitHub Pages (Optional)
To host Allure reports automatically:
1. Go to **Settings** → **Pages**
2. Under "Build and deployment", select **GitHub Actions** as the source
3. The workflow will deploy reports after each run

#### 3. Run Workflow Manually
1. Go to **Actions** → **Playwright Scheduled Tests**
2. Click **Run workflow** → **Run workflow**

### Workflow Features

| Feature | Description |
|---------|-------------|
| **Scheduled Runs** | Every 6 hours (00:00, 06:00, 12:00, 18:00 UTC) |
| **Multi-browser** | Chromium, Firefox, WebKit |
| **Artifacts** | Allure results, HTML reports, screenshots |
| **Auto-deploy** | Reports deployed to GitHub Pages on main branch |

### Viewing Results

- **Allure Reports**: Download from Actions artifacts or view on GitHub Pages
- **Test Results**: Check the **Actions** tab for run history
- **Artifacts**: Each run produces downloadable test artifacts

### Customization

Modify `.github/workflows/playwright-tests.yml` to change:
- Schedule timing: Edit the `cron` expression
- Browser matrix: Add/remove browsers
- Environment variables: Add secrets for API keys, URLs, etc.

---

## 🤝 Contributing
Follow the best practices above. Ensure tests pass before committing. Use descriptive commit messages.
