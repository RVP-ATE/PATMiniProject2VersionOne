from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        # Dictionary mapping menu names to their corresponding XPATH locators
        self.menu_items = {
            "Admin": (By.XPATH, "//span[text()='Admin']"),
            "PIM": (By.XPATH, "//span[text()='PIM']"),
            "Leave": (By.XPATH, "//span[text()='Leave']"),
            "Time": (By.XPATH, "//span[text()='Time']"),
            "Recruitment": (By.XPATH, "//span[text()='Recruitment']"),
            "My Info": (By.XPATH, "//span[text()='My Info']"),
            "Performance": (By.XPATH, "//span[text()='Performance']"),
            "Dashboard": (By.XPATH, "//span[text()='Dashboard']"),
        }

    def is_menu_clickable(self, menu_name):
        """
        Checks if a menu item (given by its name) is clickable and visible on the dashboard.

        Args:
            menu_name (str): The name of the menu item to check (e.g., 'Admin', 'PIM').

        Returns:
            bool: True if the menu item is displayed and clickable, False otherwise.
        """
        # Wait until the specified menu item is clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_items[menu_name])
        )
        # Return whether the element is displayed
        return element.is_displayed()