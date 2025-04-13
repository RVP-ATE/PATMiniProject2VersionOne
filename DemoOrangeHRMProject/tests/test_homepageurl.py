import pytest
import time
from selenium import webdriver
from DemoOrangeHRMProject.pages.homepage import HomePage

# Pytest fixture to initialize and quit the WebDriver
@pytest.fixture()
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Implicit wait to handle dynamic elements
    driver.implicitly_wait(10)
    # Provide the driver to the test
    yield driver
    # Close and quit the driver after the test completes
    driver.close()
    driver.quit()

# Test to verify that the correct URL is opened
def test_home_url(driver):
    # Create an instance of the HomePage with the driver
    home_page = HomePage(driver)
    # Open the OrangeHRM login page
    home_page.open_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Wait briefly to ensure the page has fully loaded (can be replaced with an explicit wait)
    time.sleep(2)
    # Verify that the URL contains 'orangehrmlive'
    assert "orangehrmlive" in driver.current_url

