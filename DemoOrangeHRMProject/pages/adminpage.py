import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for Admin Page elements
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.add_user_button = (By.XPATH, "//button[normalize-space()='Add']")

        # Locators for User Role selection dropdown
        self.user_role = (By.XPATH, "(//*[@class='oxd-select-text--after'])[1]")
        self.user_select = (By.XPATH, "//*[@class = 'oxd-select-text-input' and text() = '-- Select --']")
        self.user_admin = (By.XPATH, "//*[@class = 'oxd-select-text-input' and text() = 'Admin']")

        # Locators for Status dropdown
        self.status = (By.XPATH, "(//*[@class='oxd-select-text--after'])[2]")
        self.status_select = (By.XPATH, "//*[@class = 'oxd-select-text-input' and text() = '-- Select --']")
        self.status_enabled = (By.XPATH, "//*[@class = 'oxd-select-text-input' and text() = 'Enabled']")

        # Locators for input fields
        self.employee_name = (By.XPATH, '//input[@placeholder="Type for hints..."]')
        self.username_field = (By.XPATH, "(//*[@class='oxd-input oxd-input--active'])[2]")
        self.password_field = (By.XPATH, "(//*[@type='password'])[1]")
        self.confirm_password_field = (By.XPATH, "(//*[@type='password'])[2]")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")

    def navigate_to_admin(self):
        """
        Navigates to the Admin page by clicking the Admin menu item.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()

    def create_user(self, username, password, employee):
        """
        Creates a new user in the Admin section using provided username, password, and employee name.
        """

        # Click on the 'Add' button to add a new user
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_user_button)
        ).click()

        time.sleep(5)  # Static wait for UI stability (can be replaced with better waits)

        # Select 'Admin' from the User Role dropdown
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.user_role)
        ).click()
        time.sleep(2)
        self.driver.find_element(*self.user_select).send_keys(Keys.DOWN)
        time.sleep(2)
        self.driver.find_element(*self.user_admin).send_keys(Keys.ENTER)
        time.sleep(2)

        # Select 'Enabled' from the Status dropdown
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.status)
        ).click()
        time.sleep(2)
        self.driver.find_element(*self.status_select).send_keys(Keys.DOWN)
        time.sleep(2)
        self.driver.find_element(*self.status_enabled).send_keys(Keys.ENTER)
        time.sleep(2)

        # Enter employee name and select from auto-suggestion
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.employee_name)
        ).send_keys(employee)
        time.sleep(2)
        self.driver.find_element(*self.employee_name).send_keys(Keys.DOWN)
        time.sleep(2)
        self.driver.find_element(*self.employee_name).send_keys(Keys.ENTER)
        time.sleep(2)

        # Fill in username and password fields
        self.driver.find_element(*self.username_field).send_keys(username)
        time.sleep(2)
        self.driver.find_element(*self.password_field).send_keys(password)
        time.sleep(2)
        self.driver.find_element(*self.confirm_password_field).send_keys(password)
        time.sleep(2)

        # Click the Save button to create the user
        self.driver.find_element(*self.save_button).click()