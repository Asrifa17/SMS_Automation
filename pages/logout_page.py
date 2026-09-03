import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogoutPage(BasePage):


    LOGOUT_BUTTON = (
        By.XPATH,
        "//span[normalize-space()='Logout']"
    )


    def logout(self):

        self.click(
            self.LOGOUT_BUTTON
        )


        time.sleep(3)


        print(
            "LOGOUT SUCCESSFULLY"
        )


    def verify_logout(self):

        assert "login" in self.driver.current_url.lower()

        print(
            "LOGIN PAGE DISPLAYED AFTER LOGOUT"
        )