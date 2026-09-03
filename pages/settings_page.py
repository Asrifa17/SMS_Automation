# settings_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SettingsPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= LOCATORS =================

    settings_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[10]'
    )

    notifications_option = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/div[1]/p[1]'
    )

    change_password_option = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/div[1]/p[2]'
    )

    # ================= METHODS =================

    def open_settings_page(self):

        settings = self.wait.until(
            EC.element_to_be_clickable(self.settings_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            settings
        )

        time.sleep(3)

    def open_notifications(self):

        notification = self.wait.until(
            EC.element_to_be_clickable(self.notifications_option)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            notification
        )

        time.sleep(3)

    def open_change_password(self):

        password = self.wait.until(
            EC.element_to_be_clickable(self.change_password_option)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            password
        )

        time.sleep(3)