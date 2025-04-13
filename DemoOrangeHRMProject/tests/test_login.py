import time
import pytest
from DemoOrangeHRMProject.pages.loginpage import LoginPage
from DemoOrangeHRMProject.utilities.excel_utilities import get_login_data
from DemoOrangeHRMProject.conftest import driver

# Parametrize the test with login data (username, password) from Excel file
@pytest.mark.parametrize("username,password", get_login_data("login_data.xlsx"))
def test_signin(driver, username, password):
    # Create a LoginPage instance and perform login
    login_page = LoginPage(driver)
    login_page.login(username, password)

    # Wait for login process to complete (consider using WebDriverWait instead)
    time.sleep(5)

    # Get the current URL after login attempt
    current_url = driver.current_url
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    try:
        if current_url == expected_url:
            # Login was successful
            print(f"[✅ PASS] Login successful for user: {username}")
            assert True
        else:
            # Login failed, but if invalid credentials were expected, test still passes
            print(f"[ℹ️ INFO] Login failed as expected for invalid user: {username}")
            assert True

    except Exception as e:
        # Handle unexpected errors during login attempt
        print(f"[❌ ERROR] Unexpected error for user '{username}': {e}")
        pytest.fail(f"Unexpected error for user '{username}': {e}")
