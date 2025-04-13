import time
from DemoOrangeHRMProject.pages.loginpage import LoginPage
from DemoOrangeHRMProject.pages.dashboardpage import DashboardPage
from DemoOrangeHRMProject.conftest import driver

def test_dashboard_menus(driver):
    # Perform login using valid credentials
    LoginPage(driver).login("Admin", "admin123")

    # Initialize the DashboardPage object
    dashboard = DashboardPage(driver)

    # Temporary wait to ensure the dashboard page loads (consider replacing with WebDriverWait)
    time.sleep(5)

    # List of menu items to check on the dashboard
    menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

    # Loop through each menu item and assert if it's clickable
    for menu in menus:
        # Assert that the menu is clickable; print status accordingly
        assert dashboard.is_menu_clickable(menu), f"[❌ ERROR] Menu '{menu}' is not clickable."
        print(f"[✅ CHECKED] Menu '{menu}' was checked and is clickable.")
