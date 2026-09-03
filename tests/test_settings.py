# test_settings.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.settings_page import SettingsPage


def test_settings_module():

    # Launch Browser
    driver = webdriver.Chrome()

    # Maximize Browser
    driver.maximize_window()

    # Open Website
    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)

    login.login("admin", "admin123")

    # Wait Object
    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Create Settings Object
    settings = SettingsPage(driver)

    # Open Settings Page
    settings.open_settings_page()

    print("SETTINGS PAGE OPENED")

    time.sleep(3)

    # Open Notifications
    settings.open_notifications()

    print("NOTIFICATIONS OPENED")

    time.sleep(3)

    # Reopen Settings Page
    settings.open_settings_page()

    time.sleep(2)

    # Open Change Password
    settings.open_change_password()

    print("CHANGE PASSWORD OPENED")

    time.sleep(5)

    # Close Browser
    driver.quit()