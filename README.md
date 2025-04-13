# OrangeHRM Automation Testing Project

This is a Selenium-based automation testing project built to test the OrangeHRM demo application. The project follows the **Page Object Model (POM)** and utilizes **Pytest** and **Data-Driven Testing Framework (DDTF)** principles to ensure scalability and maintainability.

## 🚀 Features

- Automated UI testing for OrangeHRM demo site
- Page Object Model (POM) structure
- Data-driven testing using external files
- HTML reports for test runs
- Reusable methods and organized page classes
- Includes cookies handling and Git versioning

  ## 🛠 Technologies Used

- Python
- Selenium WebDriver
- Pytest
- HTMLTestRunner or Allure for reporting (if used)
- Page Object Model
- Data-driven testing (with Python data structures or files)

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/RVP-ATE/OrangeHRM-Automation.git
   cd OrangeHRM-Automation

Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\\Scripts\\activate

Install dependencies:
  pip install -r requirements.txt

Run all test cases:
  pytest

Run specific test file:
  pytest testcases/test_login.py

📊 Test Report
  After execution, the test report is generated as an HTML file (report.html) and saved in the root directory.

👤 Author
-PAVAN KUMAR RV

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

   
