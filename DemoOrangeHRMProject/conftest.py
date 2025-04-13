import sys
import os
import pytest
from selenium import webdriver

# ✅ Add root project path to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def driver():
    # Setup: initialize the driver
    driver = webdriver.Chrome()  # or Firefox, Edge, etc.

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver  # This is passed to the test

    # Teardown: quit the driver
    driver.quit()