from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class ReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # =====================================================
    # REPORT PAGE LOCATORS (KEEP OLD PASSED LOCATORS)
    # =====================================================

    report_menu = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[1]/div/div[2]/a[9]"
    )

    payment_report = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div/div/div[1]/div"
    )

    exam_report = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div/div/div[2]"
    )

    result_report = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div/div/div[3]"
    )

    # =====================================================
    # RESULT REPORT LOCATORS
    # =====================================================

    search_box = (
        By.XPATH,
        "//input[@placeholder='Search...']"
    )

    dropdowns = (
        By.CSS_SELECTOR,
        "select.rr-dropdown"
    )

    result_rows = (
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    view_icon = (
        By.XPATH,
        "//img[@alt='View']"
    )

    # Popup

    result_popup = (
        By.CSS_SELECTOR,
        ".rr-modal"
    )

    popup_title = (
        By.CSS_SELECTOR,
        ".rr-modal-header h3"
    )

    popup_student = (
        By.CSS_SELECTOR,
        ".rr-modal p strong"
    )

    close_popup = (
        By.CSS_SELECTOR,
        ".rr-close-icon"
    )

    generate_pdf_button = (
        By.XPATH,
        "//button[contains(text(),'Generate PDF')]"
    )

    # =====================================================
    # NAVIGATION METHODS
    # =====================================================

    def open_report_page(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                self.report_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def open_payment_report(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                self.payment_report
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def open_exam_report(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                self.exam_report
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def open_result_report(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                self.result_report
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # =====================================================
    # RESULT SEARCH
    # =====================================================

    def search_student(self, name):
        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.clear()

        search.send_keys(name)

        time.sleep(3)

    def get_result_count(self):
        rows = self.driver.find_elements(
            *self.result_rows
        )

        return len(rows)

    # =====================================================
    # FILTERS
    # =====================================================

    def select_course(self, course):
        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.dropdowns
            )
        )

        Select(
            dropdowns[0]
        ).select_by_visible_text(
            course
        )

        time.sleep(3)

    def select_grade(self, grade):
        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.dropdowns
            )
        )

        Select(
            dropdowns[1]
        ).select_by_visible_text(
            grade
        )

        time.sleep(3)

    def select_exam(self, exam):
        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.dropdowns
            )
        )

        Select(
            dropdowns[2]
        ).select_by_visible_text(
            exam
        )

        time.sleep(5)

    # =====================================================
    # VIEW RESULT
    # =====================================================

    def click_view_result(self):
        view = self.wait.until(
            EC.element_to_be_clickable(
                self.view_icon
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            view
        )

        time.sleep(3)

        print(
            "VIEW ICON CLICKED"
        )

    def verify_result_popup(self):
        popup = self.wait.until(
            EC.visibility_of_element_located(
                self.result_popup
            )
        )

        title = popup.find_element(
            *self.popup_title
        ).text

        student = popup.find_element(
            *self.popup_student
        ).text

        print(
            "POPUP TITLE:",
            title
        )

        print(
            "STUDENT:",
            student
        )

        return (
                title == "Result Details"
                and len(student) > 0
        )

    def close_result_popup(self):
        close = self.wait.until(
            EC.element_to_be_clickable(
                self.close_popup
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close
        )

        time.sleep(2)

        print(
            "POPUP CLOSED"
        )

    # =====================================================
    # PDF
    # =====================================================

    def click_generate_pdf(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_pdf_button
            )
        )

        button.click()

        time.sleep(5)

        print(
            "PDF BUTTON CLICKED"
        )

    # =====================================================
    # ADD / UPDATE RESULT
    # TC_Report_198
    # hh hhh : AB -> B
    # =====================================================

    add_button = (
        By.XPATH,
        "//button[contains(text(),'Add')]"
    )

    # Course / Grade / Exam dropdowns
    add_dropdowns = (
        By.CSS_SELECTOR,
        "select.rr-add-dropdown"
    )

    # Update button
    update_button = (
        By.CSS_SELECTOR,
        ".rr-update-btn"
    )

    def click_add_button(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(5)

        print(
            "ADD RESULT PAGE OPENED"
        )

    def select_add_course(self, course):

        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.add_dropdowns
            )
        )

        Select(
            dropdowns[0]
        ).select_by_visible_text(
            course
        )

        time.sleep(3)

        print(
            "COURSE SELECTED"
        )

    def select_add_grade(self, grade):

        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.add_dropdowns
            )
        )

        Select(
            dropdowns[1]
        ).select_by_visible_text(
            grade
        )

        time.sleep(3)

        print(
            "GRADE SELECTED"
        )

    def select_add_exam(self, exam):

        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                self.add_dropdowns
            )
        )

        Select(
            dropdowns[2]
        ).select_by_visible_text(
            exam
        )

        time.sleep(5)

        print(
            "EXAM SELECTED"
        )

    def update_student_result(self, student, result):

        # Find student name

        student_element = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{student}')]"
                )
            )
        )

        print(
            "STUDENT FOUND:",
            student_element.text
        )

        # Get all result dropdowns

        dropdowns = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    "select.rr-add-result-dropdown"
                )
            )
        )

        print(
            "RESULT DROPDOWNS COUNT:",
            len(dropdowns)
        )

        # Find dropdown related to selected student

        target_dropdown = None

        for dropdown in dropdowns:

            try:

                parent = dropdown.find_element(
                    By.XPATH,
                    "./ancestor::*[self::div or self::tr][1]"
                )

                if student in parent.text:
                    target_dropdown = dropdown
                    break


            except:

                continue

        # If parent search fails,
        # use student position

        if target_dropdown is None:

            print(
                "DIRECT MATCH FAILED - USING INDEX"
            )

            students = self.driver.find_elements(
                By.XPATH,
                "//*[contains(text(),'AB')]"
            )

            for index, item in enumerate(students):

                if student in item.text:
                    target_dropdown = dropdowns[index]
                    break

        if target_dropdown is None:
            raise Exception(
                f"Result dropdown not found for {student}"
            )

        # Change result

        Select(
            target_dropdown
        ).select_by_visible_text(
            result
        )

        print(
            "RESULT CHANGED:",
            student,
            "->",
            result
        )

        time.sleep(2)

        # Click update button

        update_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".rr-update-btn"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            update_btn
        )

        print(
            "UPDATE BUTTON CLICKED"
        )

        # Handle success alert

        time.sleep(2)

        try:

            alert = self.driver.switch_to.alert

            print(
                "ALERT:",
                alert.text
            )

            alert.accept()


        except:

            pass

        time.sleep(5)


    # =====================================================
    # VERIFY UPDATED RESULT
    # =====================================================

    def verify_student_result(self, student, result):

        time.sleep(3)

        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table tbody tr"
        )


        for row in rows:

            row_text = row.text.strip()


            print(
                "CHECKING ROW:",
                row_text
            )


            if student in row_text:


                if result in row_text:

                    print(
                        "RESULT VERIFIED:",
                        row_text
                    )

                    return True


                else:

                    print(
                        "WRONG RESULT:",
                        row_text
                    )

                    return False


        raise Exception(
            f"{student} not found"
        )