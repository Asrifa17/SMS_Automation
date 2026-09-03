from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class SchedulePage(BasePage):

    SCHEDULE = (
        By.XPATH,
        "//span[text()='Schedule']"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Add Schedule')]"
    )


    SEARCH = (
        By.XPATH,
        "//input[@placeholder='Search...']"
    )


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


    ADD_FORM_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Add Schedule')]"
    )


    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )


    UPDATE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Update Schedule')]"
    )


    CLOSE_BUTTON = (
        By.CLASS_NAME,
        "addScheduleForm-cancel-icon"
    )


    VIEW_BUTTON = (
        By.XPATH,
        "(//img[contains(@src,'eye')])[1]"
    )


    EDIT_BUTTON = (
        By.XPATH,
        "(//img[contains(@src,'edit')])[1]"
    )


    DELETE_BUTTON = (
        By.XPATH,
        "(//img[contains(@src,'delete')])[1]"
    )


    TABLE_ROWS = (
        By.XPATH,
        "//tbody/tr"
    )


    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Schedule added')]"
    )


    UPDATED_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Schedule updated')]"
    )


    DELETE_CONFIRM = (
        By.XPATH,
        "//*[contains(text(),'cannot be undone')]"
    )



    def open_schedule(self):

        self.click(self.SCHEDULE)



    def click_add_schedule(self):

        self.click(self.ADD_BUTTON)



    def select_dropdown(self, locator, value):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        Select(element).select_by_visible_text(value)



    def select_day(self, day):

        self.click(self.DAY)

        checkbox = (
            By.XPATH,
            f"//input[@value='{day}']"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(
                checkbox
            )
        )

        if not element.is_selected():

            element.click()



    def fill_schedule(
            self,
            branch,
            lecturer,
            course,
            grade,
            day,
            start,
            end
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


        self.select_dropdown(
            self.GRADE,
            grade
        )


        self.select_day(day)


        self.enter_text(
            self.START_TIME,
            start
        )


        self.enter_text(
            self.END_TIME,
            end
        )



    def add_schedule_submit(self):

        self.click(
            self.ADD_FORM_BUTTON
        )



    def submit_main_form(self):

        self.click(
            self.SUBMIT_BUTTON
        )



    def update_schedule(self):

        self.click(
            self.UPDATE_BUTTON
        )



    def search(self,text):

        self.enter_text(
            self.SEARCH,
            text
        )



    def rows_count(self):

        return len(
            self.driver.find_elements(
                *self.TABLE_ROWS
            )
        )



    def close_popup(self):

        self.click(
            self.CLOSE_BUTTON
        )



    def open_edit(self):

        self.click(
            self.EDIT_BUTTON
        )



    def delete_schedule(self):

        self.click(
            self.DELETE_BUTTON
        )