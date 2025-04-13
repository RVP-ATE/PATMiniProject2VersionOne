import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoOrangeHRMProject.conftest import driver

def test_login_elements_visible(driver):
    # Wait for the username field to be visible
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # Locate the password field directly (assumes it's already rendered)
    password = driver.find_element(By.NAME, "password")

    # Short pause to ensure all elements have loaded (optional)
    time.sleep(2)

    # Assert that both username and password input fields are displayed
    assert username.is_displayed()
    assert password.is_displayed()
