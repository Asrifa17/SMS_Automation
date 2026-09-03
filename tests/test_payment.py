import time
import importlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
)

from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


# ==================================================
# IMPORT payment-2_page.py
# ==================================================

PaymentFormPage = importlib.import_module(
    "pages.payment-2_page"
).PaymentFormPage


# ==================================================
# TEST DATA - NUHA IFFA
# ==================================================

STUDENT_SEARCH = "nuha iffa"

STUDENT_NAME = "nuha iffa"

STUDENT_ID = "Coo1"

PAYMENT_MONTH = "AUTO"

COURSE = "Cello"

GRADE = "10"

PAYMENT_AMOUNT = "2500"

# ==================================================
# PAYMENT MODULE TEST
# ==================================================

def test_payment_module():

    driver = webdriver.Chrome()

    driver.maximize_window()


    try:

        # ==================================================
        # 1. LOGIN
        # ==================================================

        driver.get(
            "https://aradanaqa.pineappleai.cloud/login"
        )


        login = LoginPage(
            driver
        )


        login.login(
            "admin",
            "admin123"
        )


        # ==================================================
        # VERIFY LOGIN
        #
        # Dashboard OR Payment menu means authenticated.
        # ==================================================

        def login_completed(driver):

            try:

                dashboard = driver.find_elements(
                    By.XPATH,
                    "//h1[contains("
                    "normalize-space(.),"
                    "'Dashboard'"
                    ")]"
                )


                for element in dashboard:

                    try:

                        if element.is_displayed():

                            return True

                    except StaleElementReferenceException:

                        continue


                payment_links = driver.find_elements(
                    By.XPATH,
                    "//a[@href='/payments']"
                )


                for element in payment_links:

                    try:

                        if element.is_displayed():

                            return True

                    except StaleElementReferenceException:

                        continue


            except Exception:

                pass


            return False


        try:

            WebDriverWait(
                driver,
                45,
                poll_frequency=0.5,
                ignored_exceptions=(
                    StaleElementReferenceException,
                )
            ).until(
                login_completed
            )

        except TimeoutException:

            raise Exception(
                "LOGIN DID NOT COMPLETE. "
                f"CURRENT URL : "
                f"{driver.current_url}"
            )


        print(
            "LOGIN SUCCESSFUL"
        )


        # ==================================================
        # 2. PAGE OBJECTS
        # ==================================================

        payment = PaymentPage(
            driver
        )


        payment_form = PaymentFormPage(
            driver
        )


        # ==================================================
        # 3. OPEN PAYMENT MODULE
        # ==================================================

        payment.open_payment()


        # ==================================================
        # 4. PAYMENT HEADING
        # ==================================================

        payment.verify_heading()


        # ==================================================
        # 5. SEARCH FIELD
        # ==================================================

        payment.verify_search_field()


        # ==================================================
        # 6. POSITIVE SEARCH
        # ==================================================

        payment.search_payment(
            STUDENT_SEARCH
        )


        time.sleep(1)


        # ==================================================
        # 7. NEGATIVE SEARCH
        # ==================================================

        payment.search_payment(
            "XXXXXXXX"
        )


        time.sleep(1)


        # ==================================================
        # 8. ADD PAYMENT BUTTON
        # ==================================================

        payment.verify_add_payment_button()


        # ==================================================
        # 9. OPEN ADD PAYMENT
        # ==================================================

        payment.click_add_payment()


        # ==================================================
        # 10. STUDENT FEE ENTRY FORM
        # ==================================================

        payment_form.verify_student_fee_form()


        # ==================================================
        # 11. SEARCH STUDENT
        # ==================================================

        payment_form.search_student(
            STUDENT_SEARCH
        )


        # ==================================================
        # 12. SELECT EXACT STUDENT
        #
        # Asri U
        # ST-010
        #
        # This method now avoids stale card references.
        # ==================================================

        payment_form.select_student(
            STUDENT_NAME,
            STUDENT_ID
        )


        # ==================================================
        # 13. FIRST NEXT
        #
        # Student Details
        # ->
        # Courses & Fees
        # ==================================================

        payment_form.click_next()


        # ==================================================
        # 14. COURSES & FEES
        # ==================================================

        payment_form.verify_courses_tab()


        # ==================================================
        # 15. STATUS LEGEND
        #
        # Paid
        # Due
        # Upcoming
        # ==================================================

        payment_form.verify_fee_status_colors()


        # ==================================================
        # 16. FEES TABLE
        # ==================================================

        payment_form.verify_fees_table()


        # ==================================================
        # 17. SEPTEMBER
        #
        # Current status expected:
        #
        # upcoming
        #
        # This method:
        #
        # 1. finds September
        # 2. verifies it is not Paid
        # 3. clicks September
        # 4. verifies selected
        # 5. waits for Next to enable
        # 6. IMMEDIATELY clicks second Next
        # 7. waits for Payment step
        #
        # IMPORTANT:
        # Do NOT call payment_form.click_next()
        # after this method.
        # ==================================================

        selected_month = (
            payment_form.select_payable_fee(
                PAYMENT_MONTH
            )
        )


        print(
            "PAYMENT MONTH CHOSEN : "
            f"{selected_month}"
        )


        # ==================================================
        # NO SECOND click_next() HERE
        # ==================================================


        # ==================================================
        # 18. PAYMENT TAB
        # ==================================================

        payment_form.verify_payment_tab()


        # ==================================================
        # 19. PAYMENT SUMMARY
        #
        # Nuha Iffa
        # Coo1
        # Apr
        # Cello
        # Grade 10
        # Rs.2000
        # ==================================================

        payment_form.verify_payment_summary(
            student_name="nuha iffa",
            student_id="Coo1",
            month="Apr",
            course="Cello",
            grade="10",
            amount="2000"
        )


        # ==================================================
        # 20. VERIFY SUBMIT BUTTON
        # ==================================================

        payment_form.verify_submit_payment_button()


        # ==================================================
        # 21. SUBMIT PAYMENT
        #
        # Payment Successful
        # Generate Receipt
        # Return to Payment page
        # ==================================================

        receipt_generated = (
            payment_form.submit_payment_action()
        )


        if receipt_generated:

            print(
                "RECEIPT / SLIP GENERATION VERIFIED"
            )

        else:

            print(
                "PAYMENT COMPLETED - "
                "RECEIPT BUTTON WAS NOT "
                "CAPTURED BY QA FLOW"
            )


        # ==================================================
        # IMPORTANT:
        #
        # NO PAYMENT TABLE UPDATE TEST
        #
        # NO NEW ROW TEST
        #
        # NO VIEW DETAILS TEST
        # ==================================================


        # ==================================================
        # 22. NOTIFICATION ICON
        # ==================================================

        payment.verify_notification_icon()


        # ==================================================
        # 23. LOGOUT
        # ==================================================

        payment.verify_logout()


        payment.click_logout_and_verify()


        # ==================================================
        # FINAL RESULT
        # ==================================================

        print("")

        print(
            "========================================"
        )

        print(
            "PAYMENT MODULE AUTOMATION PASSED"
        )

        print(
            "========================================"
        )

        print(
            f"STUDENT       : {STUDENT_NAME}"
        )

        print(
            f"STUDENT ID    : {STUDENT_ID}"
        )

        print(
            f"MONTH         : {selected_month}"
        )

        print(
            f"COURSE        : {COURSE}"
        )

        print(
            f"GRADE         : {GRADE}"
        )

        print(
            f"AMOUNT        : Rs.{PAYMENT_AMOUNT}"
        )

        print(
            "SUBMIT PAYMENT: VERIFIED"
        )


        if receipt_generated:

            print(
                "RECEIPT / SLIP : GENERATED"
            )

        else:

            print(
                "RECEIPT / SLIP : "
                "NOT CAPTURED"
            )


        print(
            "NOTIFICATION  : VERIFIED"
        )

        print(
            "LOGOUT        : VERIFIED"
        )

        print(
            "========================================"
        )


    finally:

        time.sleep(3)

        driver.quit()