import time

from DemoOrangeHRMProject.pages.loginpage import LoginPage
from DemoOrangeHRMProject.pages.adminpage import AdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoOrangeHRMProject.conftest import driver

def test_user_exists(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin()

    # Search for an existing user (e.g., "Admin")
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/../following-sibling::div//input"))
    )
    search_input.send_keys("Admin")

    time.sleep(5)

    search_button = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
    search_button.click()

    # Check if the result shows the user
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='table']//div[text()='Admin']"))
    )
    time.sleep(5)
    user_row = driver.find_element(By.XPATH, "//div[@role='table']//div[text()='Admin']")
    assert user_row.is_displayed()