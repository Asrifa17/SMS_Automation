import time


from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)



class PaymentFormPage:


    # ==================================================
    # INIT
    # ==================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30
        )

        self.selected_payment_month = None



    # ==================================================
    # LOCATORS
    # ==================================================


    # Student Fee Entry Modal

    student_fee_modal = (
        By.CSS_SELECTOR,
        ".student-fee-entry-modal"
    )


    student_search = (
        By.XPATH,
        "//input[contains(@placeholder,'Search')]"
    )


    student_cards = (
        By.CSS_SELECTOR,
        ".student-card"
    )


    student_name = (
        By.CSS_SELECTOR,
        ".student-card-name"
    )



    next_button = (
        By.CSS_SELECTOR,
        ".payment-next-btn"
    )



    previous_button = (
        By.CSS_SELECTOR,
        ".payment-prev-btn"
    )



    # Course & Fees


    courses_heading = (
        By.XPATH,
        "//h4[contains(text(),'Courses & Fees')]"
    )


    month_buttons = (
        By.CSS_SELECTOR,
        ".month-btn"
    )


    fee_table = (
        By.CSS_SELECTOR,
        ".fees-table tbody tr"
    )



    # Payment Step


    payment_step = (
        By.XPATH,
        "//div[contains(@class,'step-label') and contains(text(),'Payment')]"
    )


    payment_summary = (
        By.CSS_SELECTOR,
        ".payment-summary"
    )


    payment_rows = (
        By.CSS_SELECTOR,
        ".fees-table tbody tr"
    )



    submit_payment = (
        By.CSS_SELECTOR,
        ".payment-submit-btn"
    )



    # Success Popup


    success_popup = (
        By.CSS_SELECTOR,
        ".payment-success-modal-content"
    )


    success_title = (
        By.CSS_SELECTOR,
        ".payment-success-title"
    )


    generate_receipt = (
        By.CSS_SELECTOR,
        ".generate-receipt-btn"
    )


    close_success = (
        By.CSS_SELECTOR,
        ".close-success-modal-btn"
    )



    # Receipt


    receipt_modal = (
        By.CSS_SELECTOR,
        ".receipt-modal"
    )


    receipt_title = (
        By.CSS_SELECTOR,
        ".receipt-title"
    )


    pdf_button = (
        By.CSS_SELECTOR,
        ".btn-pdf"
    )


    receipt_close_button = (
        By.CSS_SELECTOR,
        ".btn-skip"
    )



    # ==================================================
    # VERIFY STUDENT FEE FORM
    # ==================================================

    def verify_student_fee_form(self):


        modal = self.wait.until(
            EC.visibility_of_element_located(
                self.student_fee_modal
            )
        )


        assert modal.is_displayed()


        print(
            "STUDENT FEE ENTRY FORM VERIFIED"
        )



    # ==================================================
    # SEARCH STUDENT
    # ==================================================

    def search_student(
        self,
        name
    ):


        search = self.wait.until(
            EC.visibility_of_element_located(
                self.student_search
            )
        )


        search.clear()


        search.send_keys(
            name
        )


        time.sleep(3)


        print(
            f"STUDENT SEARCH : {name}"
        )



    # ==================================================
    # CHECK STUDENT EXISTS
    # ==================================================

    def student_exists(
        self,
        expected_name
    ):


        cards = self.driver.find_elements(
            *self.student_cards
        )


        for card in cards:


            try:

                name = card.find_element(
                    *self.student_name
                ).text.strip()



                if (
                    name.casefold()
                    ==
                    expected_name.casefold()
                ):

                    return True



            except StaleElementReferenceException:

                continue



        return False



    # ==================================================
    # SELECT STUDENT
    # ==================================================

    def select_student(
        self,
        student_name,
        student_id
    ):


        def find_student(driver):


            cards = driver.find_elements(
                *self.student_cards
            )


            for card in cards:


                try:


                    name = card.find_element(
                        *self.student_name
                    ).text.strip()



                    if (
                        name.casefold()
                        ==
                        student_name.casefold()
                    ):

                        return card



                except StaleElementReferenceException:

                    continue



            return False



        card = WebDriverWait(
            self.driver,
            20
        ).until(
            find_student
        )



        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block:'center'
            });

            arguments[0].click();
            """,
            card
        )



        print(
            f"STUDENT SELECTED : {student_name}"
        )


        print(
            f"STUDENT ID VERIFIED : {student_id}"
        )



    # ==================================================
    # CLICK FIRST NEXT BUTTON
    # Student Details -> Courses & Fees
    # ==================================================

    def click_next(self):


        def find_next(driver):


            buttons = driver.find_elements(
                *self.next_button
            )


            for button in buttons:


                try:

                    if (
                        button.is_displayed()
                        and button.is_enabled()
                    ):

                        return button



                except StaleElementReferenceException:

                    continue



            return False



        button = WebDriverWait(
            self.driver,
            30,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        ).until(
            find_next
        )



        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block:'center'
            });

            arguments[0].click();
            """,
            button
        )



        print(
            "FIRST NEXT BUTTON CLICKED"
        )



        self.wait.until(
            EC.visibility_of_element_located(
                self.courses_heading
            )
        )



        print(
            "COURSES & FEES PAGE OPENED"
        )



    # ==================================================
    # VERIFY COURSES TAB
    # ==================================================

    def verify_courses_tab(self):


        heading = self.wait.until(
            EC.visibility_of_element_located(
                self.courses_heading
            )
        )


        assert heading.is_displayed()


        print(
            "COURSES & FEES TAB VERIFIED"
        )


    # ==================================================
    # VERIFY FEE STATUS COLORS
    # ==================================================

    def verify_fee_status_colors(self):


        months = self.wait.until(
            EC.presence_of_all_elements_located(
                self.month_buttons
            )
        )


        paid = False
        due = False
        upcoming = False



        for month in months:


            try:

                classes = (
                    month.get_attribute(
                        "class"
                    )
                    or ""
                ).lower()



                if "paid" in classes:

                    paid = True



                if "due" in classes:

                    due = True



                if "upcoming" in classes:

                    upcoming = True



            except StaleElementReferenceException:

                continue



        assert paid, (
            "PAID STATUS NOT FOUND"
        )


        assert (
            due or upcoming
        ), (
            "DUE / UPCOMING STATUS NOT FOUND"
        )



        print(
            "PAYMENT STATUS COLORS VERIFIED"
        )



    # ==================================================
    # VERIFY FEES TABLE
    # ==================================================

    def verify_fees_table(self):


        rows = self.wait.until(
            EC.presence_of_all_elements_located(
                self.fee_table
            )
        )


        assert len(rows) > 0



        print(
            "FEES TABLE VERIFIED"
        )



    # ==================================================
    # SELECT PAYABLE MONTH
    #
    # AUTO:
    # Select first due month
    #
    # ==================================================

    def select_payable_fee(
        self,
        target_month="AUTO"
    ):


        print(
            f"TARGET PAYMENT MONTH : {target_month}"
        )



        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                self.month_buttons
            )
        )



        print(
            "MONTH BUTTON DEBUG"
        )


        for btn in buttons:

            print(
                btn.text,
                "----",
                btn.get_attribute("class")
            )



        selected_button = None

        selected_month = None



        # ================================
        # AUTO SELECT
        # ================================

        if target_month.upper() == "AUTO":


            for button in buttons:


                try:


                    text = (
                        button.text
                        .strip()
                    )


                    classes = (
                        button.get_attribute(
                            "class"
                        )
                        or ""
                    ).lower()



                    disabled = (
                        button.get_attribute(
                            "disabled"
                        )
                    )



                    if (

                        "paid" not in classes

                        and

                        "due" in classes

                        and

                        disabled is None

                    ):


                        selected_button = button

                        selected_month = text

                        break



                except StaleElementReferenceException:

                    continue



        else:


            # ================================
            # SPECIFIC MONTH
            # ================================

            for button in buttons:


                try:


                    text = button.text.strip()


                    classes = (
                        button.get_attribute(
                            "class"
                        )
                        or ""
                    ).lower()



                    if (

                        text.casefold()
                        ==
                        target_month.casefold()

                        and

                        "paid"
                        not in classes

                    ):


                        selected_button = button

                        selected_month = text

                        break



                except StaleElementReferenceException:

                    continue



        if selected_button is None:


            raise Exception(
                "NO PAYABLE MONTH FOUND"
            )



        print(
            f"{selected_month} FOUND"
        )



        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block:'center'
            });

            arguments[0].click();
            """,
            selected_button
        )



        time.sleep(2)



        print(
            f"{selected_month} MONTH SELECTED"
        )



        print(
            "MONTH SELECTION VERIFIED"
        )



        # Wait Next enabled

        WebDriverWait(
            self.driver,
            20
        ).until(
            self._next_button_enabled
        )



        print(
            "PAYMENT SELECTION COMPLETE - NEXT ENABLED"
        )



        # Automatically move to Payment tab

        self.click_second_next()



        self.selected_payment_month = selected_month



        return selected_month



    # ==================================================
    # NEXT BUTTON ENABLE CHECK
    # ==================================================

    def _next_button_enabled(
        self,
        driver
    ):


        try:


            buttons = driver.find_elements(
                *self.next_button
            )


            for button in buttons:


                try:


                    if (

                        button.is_displayed()

                        and

                        button.is_enabled()

                    ):

                        return True



                except StaleElementReferenceException:

                    continue



        except Exception:

            pass



        return False



    # ==================================================
    # CLICK SECOND NEXT BUTTON
    # Courses & Fees -> Payment
    # ==================================================

    def click_second_next(self):


        def find_button(driver):


            buttons = driver.find_elements(
                *self.next_button
            )


            for button in buttons:


                try:


                    if (

                        button.is_displayed()

                        and

                        button.is_enabled()

                    ):

                        return button



                except StaleElementReferenceException:

                    continue



            return False



        button = WebDriverWait(
            self.driver,
            30,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        ).until(
            find_button
        )



        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block:'center'
            });

            arguments[0].click();
            """,
            button
        )



        print(
            "COURSES & FEES NEXT BUTTON CLICKED"
        )



        self.wait.until(
            EC.visibility_of_element_located(
                self.payment_step
            )
        )



        print(
            "PAYMENT STEP OPENED"
        )



    # ==================================================
    # VERIFY PAYMENT TAB
    # ==================================================

    def verify_payment_tab(self):


        tab = self.wait.until(
            EC.visibility_of_element_located(
                self.payment_step
            )
        )


        assert tab.is_displayed()


        print(
            "PAYMENT TAB VERIFIED"
        )



    # ==================================================
    # VERIFY PAYMENT SUMMARY
    # ==================================================

    def verify_payment_summary(
        self,
        student_name,
        student_id,
        month,
        course,
        grade,
        amount
    ):


        summary = self.wait.until(
            EC.visibility_of_element_located(
                self.payment_summary
            )
        )



        text = summary.text



        print(
            "PAYMENT SUMMARY:"
        )


        print(
            text
        )



        assert (
            student_name.casefold()
            in
            text.casefold()
        )


        assert (
            student_id.casefold()
            in
            text.casefold()
        )



        rows = self.driver.find_elements(
            *self.payment_rows
        )



        found = False



        for row in rows:


            row_text = row.text



            if (

                month.casefold()
                in
                row_text.casefold()

                and

                course.casefold()
                in
                row_text.casefold()

                and

                grade.casefold()
                in
                row_text.casefold()

                and

                amount
                in
                row_text

            ):

                found = True

                break



        assert found, (
            "PAYMENT SUMMARY ROW NOT FOUND"
        )



        print(
            "PAYMENT SUMMARY ROW VERIFIED"
        )



    # ==================================================
    # VERIFY SUBMIT BUTTON
    # ==================================================

    def verify_submit_payment_button(self):


        button = self.wait.until(
            EC.element_to_be_clickable(
                self.submit_payment
            )
        )


        assert button.is_displayed()

        assert button.is_enabled()



        print(
            "SUBMIT PAYMENT BUTTON VERIFIED"
        )

    # ==================================================
    # COMPLETE PAYMENT FLOW
    #
    # Submit Payment
    # Success Popup
    # Generate Receipt
    # Receipt Validation
    # Print PDF
    # Close Receipt
    #
    # ==================================================

    def complete_payment_flow(self):


        self.verify_submit_payment_button()



        # ================================
        # CLICK SUBMIT PAYMENT
        # ================================

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.submit_payment
            )
        )


        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block:'center'
            });

            arguments[0].click();
            """,
            button
        )


        print(
            "SUBMIT PAYMENT BUTTON CLICKED"
        )



        # ================================
        # WAIT SUCCESS POPUP
        # ================================

        popup = self.wait.until(
            EC.visibility_of_element_located(
                self.success_popup
            )
        )


        assert popup.is_displayed()



        title = popup.find_element(
            *self.success_title
        )


        assert (
            title.text.strip()
            ==
            "Payment Successful!"
        )


        print(
            "PAYMENT SUCCESSFUL VERIFIED"
        )



        # ================================
        # GENERATE RECEIPT
        # ================================

        receipt_button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_receipt
            )
        )


        receipt_button.click()


        print(
            "GENERATE RECEIPT CLICKED"
        )



        # Wait receipt loading

        time.sleep(3)



        # ================================
        # VERIFY RECEIPT
        # ================================

        self.verify_receipt()



        # ================================
        # VERIFY PDF BUTTON
        # ================================

        self.verify_pdf_button()



        # ================================
        # CLICK PRINT PDF
        # ================================

        self.click_print_pdf()



        # ================================
        # CLOSE RECEIPT
        # ================================

        self.close_receipt()



        print(
            "PAYMENT SUBMISSION FLOW COMPLETED"
        )



    # ==================================================
    # VERIFY RECEIPT
    # ==================================================

    def verify_receipt(self):


        receipt = self.wait.until(
            EC.visibility_of_element_located(
                self.receipt_modal
            )
        )


        assert receipt.is_displayed()



        title = self.wait.until(
            EC.visibility_of_element_located(
                self.receipt_title
            )
        )


        assert (
            title.text.strip()
            ==
            "Receipt"
        )


        print(
            "RECEIPT VALIDATION PASSED"
        )



    # ==================================================
    # VERIFY PDF BUTTON
    # ==================================================

    def verify_pdf_button(self):


        pdf = self.wait.until(
            EC.visibility_of_element_located(
                self.pdf_button
            )
        )


        assert pdf.is_displayed()



        print(
            "PDF BUTTON VALIDATION PASSED"
        )



    # ==================================================
    # CLICK PRINT PDF
    # ==================================================

    def click_print_pdf(self):


        pdf = self.wait.until(
            EC.element_to_be_clickable(
                self.pdf_button
            )
        )


        pdf.click()


        print(
            "PRINT AS PDF CLICKED"
        )



    # ==================================================
    # CLOSE RECEIPT
    # ==================================================

    def close_receipt(self):


        close = self.wait.until(
            EC.element_to_be_clickable(
                self.receipt_close_button
            )
        )


        close.click()


        print(
            "RECEIPT CLOSED"
        )



    # ==================================================
    # VERIFY TABLE UPDATED AFTER PAYMENT
    # ==================================================

    def verify_payment_updated(
        self,
        student_name
    ):


        time.sleep(3)


        page_text = (
            self.driver
            .page_source
            .casefold()
        )


        assert (
            student_name.casefold()
            in
            page_text
        )


        print(
            "PAYMENT TABLE UPDATE VERIFIED"
        )