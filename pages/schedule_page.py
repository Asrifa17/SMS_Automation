import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage



class SchedulePage(BasePage):


    # ==========================
    # Navigation
    # ==========================

    SCHEDULE_MENU = (
        By.XPATH,
        "//span[normalize-space()='Schedule']"
    )


    # ==========================
    # Main page
    # ==========================

    SEARCH_BOX = (
        By.CSS_SELECTOR,
        "input[placeholder='Search...']"
    )


    ADD_BUTTON = (
        By.CSS_SELECTOR,
        "button.schedule-add-btn"
    )


    TABLE_ROWS = (
        By.CSS_SELECTOR,
        "tbody tr"
    )



    # ==========================
    # Modal
    # ==========================

    MODAL = (
        By.CSS_SELECTOR,
        ".addScheduleForm-modal-content"
    )


    CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "img.addScheduleForm-cancel-icon"
    )



    # ==========================
    # Fields
    # ==========================

    BRANCH = (
        By.ID,
        "branch_id"
    )


    LECTURER = (
        By.ID,
        "user_id"
    )


    COURSE = (
        By.ID,
        "course_id"
    )


    GRADE = (
        By.ID,
        "grade_id"
    )


    DAY = (
        By.CSS_SELECTOR,
        ".addScheduleForm-dropdown-toggle"
    )


    START_TIME = (
        By.ID,
        "startTime"
    )


    END_TIME = (
        By.ID,
        "endTime"
    )



    # ==========================
    # Buttons
    # ==========================

    ADD_FORM_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'addScheduleForm-button-btn') and normalize-space()='Add Schedule']"
    )


    UPDATE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Update']"
    )


    FINAL_SUBMIT = (
        By.CSS_SELECTOR,
        "button.addScheduleForm-submit-btn"
    )



    # ==========================
    # Table icons
    # ==========================

    EDIT_ICON = (
        By.XPATH,
        "(//img[@alt='Edit'])[1]"
    )


    DELETE_ICON = (
        By.XPATH,
        "(//img[@alt='Delete'])[1]"
    )


    VIEW_ICON = (
        By.XPATH,
        "(//img[@alt='View'])[1]"
    )



    # ==========================
    # Delete modal
    # ==========================

    DELETE_MODAL = (
        By.CSS_SELECTOR,
        ".DeleteModal-content"
    )


    DELETE_CONFIRM = (
        By.CSS_SELECTOR,
        "button.DeleteModal-delete"
    )



    # ==========================
    # Success
    # ==========================

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Success') or contains(text(),'success')]"
    )



    # ==========================
    # Open Schedule
    # ==========================

    def open_schedule(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SCHEDULE_MENU
            )
        ).click()


        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )



    # ==========================
    # Search
    # ==========================

    def search_schedule(self,text):

        box=self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        box.clear()

        box.send_keys(text)



    # ==========================
    # Add popup
    # ==========================

    def click_add_schedule(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BUTTON
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


        self.wait.until(
            EC.visibility_of_element_located(
                self.MODAL
            )
        )



    def is_add_popup_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.MODAL
                )
            ).is_displayed()

        except:

            return False



    # ==========================
    # Dropdown
    # ==========================

    def select_dropdown(self,locator,value):

        element=self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )


        dropdown=Select(element)


        for option in dropdown.options:

            if option.text.strip().lower()==value.lower():

                dropdown.select_by_value(
                    option.get_attribute("value")
                )

                return


        raise Exception(
            f"{value} not found"
        )



    def wait_grade_loaded(self):

        self.wait.until(
            lambda d:
            len(
                Select(
                    d.find_element(
                        *self.GRADE
                    )
                ).options
            ) > 1
        )



    # ==========================
    # Fill
    # ==========================

    def fill_schedule(
        self,
        branch,
        lecturer,
        course,
        grade,
        day,
        start_time,
        end_time
    ):


        self.select_dropdown(
            self.BRANCH,
            branch
        )


        self.select_dropdown(
            self.LECTURER,
            lecturer
        )


        self.select_dropdown(
            self.COURSE,
            course
        )


        self.wait_grade_loaded()


        self.select_dropdown(
            self.GRADE,
            grade
        )


        self.select_day(day)


        self.enter_text(
            self.START_TIME,
            start_time
        )


        self.enter_text(
            self.END_TIME,
            end_time
        )



    # ==========================
    # Day
    # ==========================

    def select_day(self,day):

        self.click(
            self.DAY
        )


        checkbox=(
            By.XPATH,
            f"//input[@value='{day}']"
        )


        box=self.wait.until(
            EC.element_to_be_clickable(
                checkbox
            )
        )


        if not box.is_selected():

            box.click()


    # ==========================
    # Add
    # ==========================

    def click_add_form_button(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_FORM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(5)

        return self.get_success_message()

    def click_final_submit(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINAL_SUBMIT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ==========================
    # Edit Update
    # ==========================

    def click_edit(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_ICON
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


        self.wait.until(
            EC.visibility_of_element_located(
                self.UPDATE_BUTTON
            )
        )



    def change_start_time(self,time):

        field=self.wait.until(
            EC.visibility_of_element_located(
                self.START_TIME
            )
        )

        field.clear()

        field.send_keys(time)



    def click_update(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.UPDATE_BUTTON
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    # ==========================
    # Delete
    # ==========================

    def click_delete_icon(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_ICON
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


        self.wait.until(
            EC.visibility_of_element_located(
                self.DELETE_MODAL
            )
        )



    def is_delete_modal_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_MODAL
                )
            ).is_displayed()

        except TimeoutException:

            return False



    def confirm_delete(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


        self.wait.until(
            EC.invisibility_of_element_located(
                self.DELETE_MODAL
            )
        )

    def delete_schedule(self):

        self.click_delete_icon()

        self.confirm_delete()

        time.sleep(5)


    # ==========================
    # View
    # ==========================

    def view_schedule(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    # ==========================
    # Close
    # ==========================

    def close_popup(self):

        button=self.wait.until(
            EC.element_to_be_clickable(
                self.CLOSE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    # ==========================
    # Table
    # ==========================

    def get_row_count(self):

        return len(
            self.driver.find_elements(
                *self.TABLE_ROWS
            )
        )


    def is_schedule_table_visible(self):

        return self.get_row_count()>0



    # ==========================
    # Success
    # ==========================

    def get_success_message(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS_MESSAGE
                )
            ).text.lower()

        except:

            return ""
