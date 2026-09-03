import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class PaymentPage:

    # ==================================================
    # LOCATORS
    # ==================================================

    payment_menu = (
        By.XPATH,
        "//a[@href='/payments']"
    )

    payment_heading = (
        By.XPATH,
        "//h1[contains(@class,'hdr-title') "
        "and normalize-space()='Payment']"
    )

    search_field = (
        By.CSS_SELECTOR,
        "input.payment-search-bar"
    )

    add_payment_button = (
        By.CSS_SELECTOR,
        "button.payment-add-payment-btn"
    )

    add_payment_close = (
        By.CSS_SELECTOR,
        "button.payment-close-btn"
    )

    notification_icon = (
        By.CSS_SELECTOR,
        "img.hdr-notification-img"
    )


    # ==================================================
    # INIT
    # ==================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )


    # ==================================================
    # SAFE CLICK
    # ==================================================

    def _safe_click(self, element):

        try:

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                element
            )

        except Exception:

            pass

        time.sleep(0.1)

        try:

            element.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )


    # ==================================================
    # GET FRESH SEARCH FIELD
    # ==================================================

    def _fresh_search_field(self, driver):

        try:

            fields = driver.find_elements(
                *self.search_field
            )

            for field in fields:

                try:

                    if (
                        field.is_displayed()
                        and field.is_enabled()
                    ):
                        return field

                except StaleElementReferenceException:

                    continue

        except Exception:

            pass

        return False


    # ==================================================
    # OPEN PAYMENT MODULE
    # ==================================================

    def open_payment(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.payment_menu
            )
        )

        self._safe_click(
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.payment_heading
            )
        )

        print(
            "PAYMENT MODULE OPENED"
        )


    # ==================================================
    # VERIFY PAYMENT HEADING
    # ==================================================

    def verify_heading(self):

        heading = self.wait.until(
            EC.visibility_of_element_located(
                self.payment_heading
            )
        )

        assert (
            heading.text.strip()
            == "Payment"
        )

        print(
            "PAYMENT HEADING VERIFIED"
        )


    # ==================================================
    # VERIFY SEARCH FIELD
    # ==================================================

    def verify_search_field(self):

        field = self.wait.until(
            self._fresh_search_field
        )

        assert field.is_displayed()

        print(
            "SEARCH FIELD VERIFIED"
        )


    # ==================================================
    # SEARCH PAYMENT
    # ==================================================

    def search_payment(
        self,
        text
    ):

        target = text.strip()

        for attempt in range(
            1,
            6
        ):

            try:

                field = WebDriverWait(
                    self.driver,
                    10,
                    ignored_exceptions=(
                        StaleElementReferenceException,
                    )
                ).until(
                    self._fresh_search_field
                )

                field.click()

                field.send_keys(
                    Keys.CONTROL,
                    "a"
                )

                field.send_keys(
                    Keys.DELETE
                )

                field.send_keys(
                    target
                )


                def correct_value(driver):

                    fresh = (
                        self._fresh_search_field(
                            driver
                        )
                    )

                    if not fresh:

                        return False

                    try:

                        current_value = (
                            fresh.get_attribute(
                                "value"
                            )
                            or ""
                        ).strip()

                        return (
                            current_value.casefold()
                            == target.casefold()
                        )

                    except StaleElementReferenceException:

                        return False


                WebDriverWait(
                    self.driver,
                    5,
                    ignored_exceptions=(
                        StaleElementReferenceException,
                    )
                ).until(
                    correct_value
                )

                print(
                    f"SEARCH DONE : {target}"
                )

                time.sleep(1)

                return

            except (
                TimeoutException,
                StaleElementReferenceException
            ):

                print(
                    "PAYMENT SEARCH RETRY : "
                    f"{attempt}"
                )

                time.sleep(0.5)


        raise Exception(
            f"PAYMENT SEARCH FAILED : {target}"
        )


    # ==================================================
    # VERIFY ADD PAYMENT BUTTON
    # ==================================================

    def verify_add_payment_button(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_payment_button
            )
        )

        assert button.is_displayed()

        print(
            "ADD PAYMENT BUTTON VERIFIED"
        )


    # ==================================================
    # OPEN ADD PAYMENT
    # ==================================================

    def click_add_payment(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_payment_button
            )
        )

        self._safe_click(
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.add_payment_close
            )
        )

        print(
            "ADD PAYMENT POPUP OPENED"
        )


    # ==================================================
    # VERIFY NOTIFICATION ICON
    # ==================================================

    def verify_notification_icon(self):

        icon = self.wait.until(
            EC.visibility_of_element_located(
                self.notification_icon
            )
        )

        assert icon.is_displayed()

        print(
            "NOTIFICATION ICON VERIFIED"
        )


    # ==================================================
    # FIND LOGOUT CONTROL
    # ==================================================

    def _find_logout(self, driver):

        possible_locators = [

            (
                By.XPATH,
                "//*[normalize-space()='Logout']"
            ),

            (
                By.XPATH,
                "//*[normalize-space()='Log Out']"
            ),

            (
                By.CSS_SELECTOR,
                "[class*='logout']"
            ),
        ]


        for locator in possible_locators:

            try:

                elements = driver.find_elements(
                    *locator
                )

                for element in elements:

                    try:

                        if (
                            element.is_displayed()
                            and element.is_enabled()
                        ):
                            return element

                    except StaleElementReferenceException:

                        continue

            except Exception:

                continue


        return False


    # ==================================================
    # VERIFY LOGOUT
    # ==================================================

    def verify_logout(self):

        logout = WebDriverWait(
            self.driver,
            15,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        ).until(
            self._find_logout
        )

        assert logout.is_displayed()

        print(
            "LOGOUT VERIFIED"
        )

    # ==================================================
    # CLICK LOGOUT AND VERIFY LOGIN PAGE
    # ==================================================

    def click_logout_and_verify(self):

        logout = WebDriverWait(
            self.driver,
            20,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        ).until(
            self._find_logout
        )

        try:

            self.driver.execute_script(
                "arguments[0].click();",
                logout
            )


        except Exception:

            logout.click()

        print(
            "LOGOUT CLICKED"
        )

        # ==================================================
        # WAIT FOR LOGIN PAGE
        # ==================================================

        def login_page_open(driver):

            try:

                # ------------------------------------------
                # Check URL
                # ------------------------------------------

                current_url = (
                    driver.current_url
                    .casefold()
                )

                if "login" in current_url:
                    return True

                # ------------------------------------------
                # Check username/email field
                # ------------------------------------------

                username_fields = driver.find_elements(
                    By.XPATH,
                    "//input[@type='text' or @type='email']"
                )

                for field in username_fields:

                    try:

                        if field.is_displayed():
                            return True


                    except StaleElementReferenceException:

                        continue

                # ------------------------------------------
                # Check password field
                # ------------------------------------------

                password_fields = driver.find_elements(
                    By.CSS_SELECTOR,
                    "input[type='password']"
                )

                for field in password_fields:

                    try:

                        if field.is_displayed():
                            return True


                    except StaleElementReferenceException:

                        continue

                # ------------------------------------------
                # Check login button
                # ------------------------------------------

                login_buttons = driver.find_elements(
                    By.XPATH,
                    "//button[contains(text(),'Login')]"
                )

                for button in login_buttons:

                    try:

                        if button.is_displayed():
                            return True


                    except StaleElementReferenceException:

                        continue



            except Exception:

                pass

            return False

        try:

            WebDriverWait(
                self.driver,
                30,
                ignored_exceptions=(
                    StaleElementReferenceException,
                )
            ).until(
                login_page_open
            )


        except TimeoutException:

            raise Exception(
                "LOGOUT CLICKED BUT LOGIN PAGE "
                "WAS NOT VERIFIED"
            )

        print(
            "LOGOUT SUCCESSFUL"
        )

        print(
            "LOGIN PAGE VERIFIED"
        )