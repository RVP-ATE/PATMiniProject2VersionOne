from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for username input, password input, and login button
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        """
        Logs in to the application using the provided username and password.

        Args:
            username (str): The username to input.
            password (str): The password to input.
        """
        # Wait for the username field to be visible and enter the username
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

        # Enter the password
        self.driver.find_element(*self.password_input).send_keys(password)

        # Click the login button
        self.driver.find_element(*self.login_btn).click()


