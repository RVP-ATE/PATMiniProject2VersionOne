import time

from DemoOrangeHRMProject.pages.loginpage import LoginPage
from DemoOrangeHRMProject.pages.adminpage import AdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoOrangeHRMProject.conftest import driver

def test_create_and_login_with_new_user(driver):
    # Step 1: Admin logs in
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(5)

    # Step 2: Navigate to Admin section and create user
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin()
    time.sleep(5)
    name = "R"
    new_username = "Pavan"
    new_password = "Pavan@223"
    admin_page.create_user(new_username, new_password, name)
    time.sleep(5)

    # Step 3: Log out
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    ).click()
    time.sleep(5)

    # Step 4: Login with new user
    login_page = LoginPage(driver)  # Re-initiate after logout
    login_page.login(new_username, new_password)
    time.sleep(5)

    # Step 5: Assert dashboard reached
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()