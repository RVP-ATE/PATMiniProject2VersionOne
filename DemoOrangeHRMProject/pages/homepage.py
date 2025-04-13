import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # Locators for the login page input fields and login button
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def open_page(self, url):
        """
        Navigates to the given URL and waits for the login form elements to become visible.

        Args:
            url (str): The URL of the login page to open.
        """
        # Open the login page URL
        self.driver.get(url)

        # Wait until the username input is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )

        time.sleep(1)  # Optional pause; can be removed or replaced with explicit wait if needed

        # Wait until the password input is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )

        time.sleep(1)  # Optional pause

        # Wait until the login button is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_btn)
        )



