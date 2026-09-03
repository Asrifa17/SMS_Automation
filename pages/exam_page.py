import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ExamPage(BasePage):


    # ==========================
    # Navigation
    # ==========================

    EXAM_MENU = (
        By.XPATH,
        "//span[normalize-space()='Exam']"
    )


    ADD_EXAM_BUTTON = (
        By.CSS_SELECTOR,
        "button.exam-add-btn"
    )

    # ==========================
    # Search Exam
    # ==========================

    SEARCH_EXAM = (
        By.CSS_SELECTOR,
        "input.exam-search-input"
    )


    # ==========================
    # Exam Form
    # ==========================

    COURSE = (
        By.NAME,
        "courseId"
    )


    GRADE = (
        By.NAME,
        "grade"
    )


    EXAM_TYPE = (
        By.NAME,
        "examType"
    )


    EXAM_DATE = (
        By.NAME,
        "examDate"
    )


    START_TIME = (
        By.NAME,
        "startTime"
    )


    END_TIME = (
        By.NAME,
        "endTime"
    )


    CREATE_GROUP_BUTTON = (
        By.CSS_SELECTOR,
        "button.addexam-create-group-btn"
    )


    # ==========================
    # Validation Messages
    # ==========================
    COURSE_ERROR = (
        By.XPATH,
        "//*[contains(text(),'Please select a course')]"
    )

    GRADE_ERROR = (
        By.XPATH,
        "//*[contains(text(),'Please select a grade')]"
    )

    EXAM_TYPE_ERROR = (
        By.XPATH,
        "//*[contains(text(),'Please select a type')]"
    )


    # ==========================
    # Student Selection
    # ==========================

    STUDENT_CARD = (
        By.CSS_SELECTOR,
        "div.exam-student-card"
    )


    NEXT_BUTTON = (
        By.CSS_SELECTOR,
        "button.next-btn"
    )



    # ==========================
    # Group Page
    # ==========================

    GROUP_NAME = (
        By.XPATH,
        "//input[@placeholder='Enter Group Name (Required)']"
    )


    CREATE_GROUP_CONFIRM = (
        By.CSS_SELECTOR,
        "button.create-btn.floating-create-btn"
    )



    # ==========================
    # Final
    # ==========================

    GROUP_DISPLAY_NAME = (
        By.NAME,
        "groupName"
    )


    CREATE_EXAM_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(@class,'addexam-submit-btn')]"
    )

    # ==========================
    # Update Success Message
    # ==========================

    SUCCESS_TOAST = (
        By.XPATH,
        "//*[contains(text(),'Exam updated successfully') or contains(text(),'exam updated successfully') or contains(text(),'successfully')]"
    )
    # ==========================
    # Edit Exam
    # ==========================

    EDIT_ICON = (
        By.CSS_SELECTOR,
        "img.exam-edit-icon"
    )


    EDIT_GROUP_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Edit Group')]"
    )


    UPDATE_GROUP_SAVE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Update Group')]"
    )


    UPDATE_EXAM_BUTTON = (
        By.CSS_SELECTOR,
        "button.addexam-submit-btn"
    )



    EXAM_TABLE = (
        By.XPATH,
        "//div[contains(text(),'Theory')]"
    )

    # ==========================
    # Delete Exam
    # ==========================

    DELETE_ICON = (
        By.CSS_SELECTOR,
        "img.exam-delete-icon"
    )

    DELETE_CONFIRM_BUTTON = (
        By.CSS_SELECTOR,
        "button.DeleteModal-delete"
    )

    DELETE_SUCCESS_TOAST = (
        By.CSS_SELECTOR,
        "div.toast-delete"
    )


    # ==========================
    # Open Exam
    # ==========================

    def open_exam_page(self):

        self.click(
            self.EXAM_MENU
        )

        time.sleep(2)

        print(
            "EXAM PAGE OPENED"
        )

    # ==========================
    # Search Exam
    # ==========================

    def search_exam(self, exam_name):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_EXAM
            )
        )

        search.clear()

        search.send_keys(
            exam_name
        )

        time.sleep(3)

        print(
            "EXAM SEARCHED :",
            exam_name
        )

    # ==========================
    # Add Exam
    # ==========================

    def click_add_exam(self):

        self.click(
            self.ADD_EXAM_BUTTON
        )

        time.sleep(2)

        print(
            "ADD EXAM FORM OPENED"
        )



    # ==========================
    # Dropdown
    # ==========================

    def select_dropdown(
            self,
            locator,
            value
    ):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )


        Select(
            dropdown
        ).select_by_visible_text(
            value
        )



    # ==========================
    # Positive Fill Details
    # ==========================

    def fill_exam_details(
            self,
            course,
            grade,
            exam_type,
            date,
            start,
            end
    ):


        self.select_dropdown(
            self.COURSE,
            course
        )


        self.select_dropdown(
            self.GRADE,
            grade
        )


        self.select_dropdown(
            self.EXAM_TYPE,
            exam_type
        )


        self.enter_text(
            self.EXAM_DATE,
            date
        )


        self.enter_text(
            self.START_TIME,
            start
        )


        self.enter_text(
            self.END_TIME,
            end
        )


        print(
            "EXAM DETAILS ENTERED"
        )



    # ==========================
    # Negative
    # TC_Exam_NEG_001
    # Empty Course Validation
    # ==========================

    def fill_exam_details_negative(
            self,
            exam_type,
            date,
            start,
            end
    ):


        # Course intentionally empty

        # Grade intentionally empty


        self.select_dropdown(
            self.EXAM_TYPE,
            exam_type
        )


        self.enter_text(
            self.EXAM_DATE,
            date
        )


        self.enter_text(
            self.START_TIME,
            start
        )


        self.enter_text(
            self.END_TIME,
            end
        )


        print(
            "NEGATIVE EXAM DETAILS ENTERED"
        )



    def verify_empty_course_validation(self):


        course_error = self.wait.until(
            EC.visibility_of_element_located(
                self.COURSE_ERROR
            )
        )


        grade_error = self.wait.until(
            EC.visibility_of_element_located(
                self.GRADE_ERROR
            )
        )


        assert course_error.text == (
            "Please select a course"
        )


        assert grade_error.text == (
            "Please select a grade"
        )


        print(
            "EMPTY COURSE AND GRADE VALIDATION PASSED"
        )

    # ==================================================
    # TC_Exam_NEG_002 Verification
    # Empty Grade Validation
    # ==================================================

    def verify_empty_grade_validation(self):

        grade_error = self.wait.until(
            EC.visibility_of_element_located(
                self.GRADE_ERROR
            )
        )


        assert grade_error.text == (
            "Please select a grade"
        )


        print(
            "EMPTY GRADE VALIDATION PASSED"
        )


    # ==========================
    # Create Group
    # ==========================

    def create_group(
            self,
            student_name,
            group_name
    ):


        self.click(
            self.CREATE_GROUP_BUTTON
        )


        print(
            "OPENING STUDENT SELECTION"
        )


        self.wait.until(
            EC.url_contains(
                "student-selection"
            )
        )


        cards = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.STUDENT_CARD
            )
        )


        print(
            "STUDENTS FOUND:",
            len(cards)
        )


        selected = False


        for card in cards:


            if student_name.lower() in card.text.lower():


                checkbox = card.find_element(
                    By.CSS_SELECTOR,
                    "input[type='checkbox']"
                )


                self.driver.execute_script(
                    "arguments[0].click();",
                    checkbox
                )


                selected = True

                break



        if not selected:

            raise Exception(
                "Student not found : "
                + student_name
            )



        print(
            "STUDENT SELECTED"
        )



        next_btn = self.wait.until(
            EC.presence_of_element_located(
                self.NEXT_BUTTON
            )
        )


        self.wait.until(
            lambda d:
            next_btn.is_enabled()
        )


        next_btn.click()


        print(
            "NEXT CLICKED"
        )



        group = self.wait.until(
            EC.visibility_of_element_located(
                self.GROUP_NAME
            )
        )


        group.send_keys(
            group_name
        )


        print(
            "GROUP NAME ENTERED"
        )



        create_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.CREATE_GROUP_CONFIRM
            )
        )


        create_btn.click()


        time.sleep(3)


        print(
            "GROUP CREATED"
        )

    # ==========================
    # Edit Exam Flow
    # ==========================

    def click_edit_exam(self):

        self.click(
            self.EDIT_ICON
        )

        time.sleep(3)

        print(
            "EDIT EXAM OPENED"
        )


    def change_exam_type(
            self,
            exam_type
    ):

        self.select_dropdown(
            self.EXAM_TYPE,
            exam_type
        )

        print(
            "EXAM TYPE CHANGED"
        )


    def click_edit_group(self):

        self.click(
            self.EDIT_GROUP_BUTTON
        )

        time.sleep(3)

        print(
            "EDIT GROUP OPENED"
        )


    def click_next(self):

        self.click(
            self.NEXT_BUTTON
        )

        time.sleep(3)

        print(
            "NEXT BUTTON CLICKED"
        )


    def update_group_save(self):

        self.click(
            self.UPDATE_GROUP_SAVE_BUTTON
        )

        time.sleep(5)

        print(
            "UPDATE GROUP & SAVE CLICKED"
        )


    def update_exam(self):

        self.click(
            self.UPDATE_EXAM_BUTTON
        )

        time.sleep(5)

        print(
            "UPDATE EXAM CLICKED"
        )

    def verify_update_success(self):

        time.sleep(3)

        print("========== PAGE TEXT AFTER UPDATE ==========")

        print(
            self.driver.find_element(
                By.TAG_NAME,
                "body"
            ).text
        )

        print("============================================")


    def verify_updated_exam(self):

        page = self.driver.page_source


        assert "Theory" in page

        assert "NEW" in page

        assert "8/17/2026" in page


        print(
            "UPDATED EXAM TABLE VERIFIED"
        )

    # ==========================
    # Delete Exam Flow
    # ==========================

    def delete_exam(self):

        # Click delete icon

        delete_icon = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_icon
        )

        print(
            "DELETE ICON CLICKED"
        )

        # Verify delete confirmation popup

        confirm_button = self.wait.until(
            EC.visibility_of_element_located(
                self.DELETE_CONFIRM_BUTTON
            )
        )

        assert confirm_button.is_displayed()

        print(
            "DELETE CONFIRMATION POPUP DISPLAYED"
        )

        # Now confirm delete

        confirm_button.click()

        print(
            "DELETE BUTTON CLICKED"
        )

        # Verify success toast

        toast = self.wait.until(
            EC.visibility_of_element_located(
                self.DELETE_SUCCESS_TOAST
            )
        )

        print(
            "DELETE TOAST:",
            toast.text
        )

        assert (
                "Exam deleted"
                in toast.text
        )

        print(
            "EXAM DELETE SUCCESS VERIFIED"
        )

    # ==========================
    # Save Exam
    # ==========================

    def save_exam(self):

        print(
            "CURRENT URL AFTER GROUP:",
            self.driver.current_url
        )


        print(
            self.driver.find_element(
                By.TAG_NAME,
                "body"
            ).text
        )


        time.sleep(5)



    # ==========================
    # Verify Exam
    # ==========================

    def verify_exam_created(
            self,
            course,
            group_name
    ):


        page = self.driver.page_source


        assert course in page


        assert group_name in page


        print(
            "EXAM VERIFICATION PASSED"
        )

    # ==========================
    # Verify Search Result
    # ==========================

    def verify_search_result(self, value):

        rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "tr.exam-row"
        )

        assert len(rows) > 0

        found = False

        for row in rows:

            if value.lower() in row.text.lower():
                found = True

                print(
                    "FILTER RESULT FOUND:",
                    row.text
                )

                break

        assert found, (
            "Search result not found"
        )

        print(
            "SEARCH VERIFICATION PASSED"
        )