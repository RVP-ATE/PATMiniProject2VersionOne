import pickle
import os
from DemoOrangeHRMProject.pages.loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DemoOrangeHRMProject.conftest import driver


COOKIE_PATH = "cookies.pkl"

def test_login_and_save_cookie(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Wait for dashboard to load
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # Save cookies to file
    with open(COOKIE_PATH, "wb") as file:
        pickle.dump(driver.get_cookies(),file)

    assert os.path.exists(COOKIE_PATH)

def test_cookie_login(driver):
    driver.delete_all_cookies()

    # Load saved cookies
    if os.path.exists(COOKIE_PATH):
        with open(COOKIE_PATH, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.refresh()

        # Check if dashboard is still accessible
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url.lower()
    else:
        raise FileNotFoundError("cookies.pkl not found. Run test_login_and_save_cookie first.")