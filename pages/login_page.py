from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )


    # -------------------------------
    # Locators
    # -------------------------------

    username_input = (
        By.NAME,
        "username"
    )


    password_input = (
        By.NAME,
        "password"
    )


    login_button = (
        By.XPATH,
        '//*[@id="root"]/div/div/div/form/button'
    )


    # -------------------------------
    # Actions
    # -------------------------------


    def enter_username(self, username):

        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.username_input
            )
        )

        username_field.clear()

        username_field.send_keys(
            username
        )


    def enter_password(self, password):

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.password_input
            )
        )

        password_field.clear()

        password_field.send_keys(
            password
        )


    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()



    def login(self, username, password):

        self.enter_username(
            username
        )

        self.enter_password(
            password
        )

        self.click_login()