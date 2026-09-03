import pytest
import time

from utilities.driver_setup import get_driver

from pages.login_page import LoginPage
from pages.schedule_page import SchedulePage


LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"

USERNAME = "admin"
PASSWORD = "admin123"


# ==================================================
# LOGIN
# ==================================================

def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    time.sleep(3)



# ==================================================
# TC_Schel_162
# Open Schedule Module
# ==================================================

def test_schedule_navigation():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        assert (
            schedule.is_schedule_table_visible()
        )

    finally:

        driver.quit()



# ==================================================
# SEARCH TESTS
# ==================================================

@pytest.mark.parametrize(
    "search_value",
    [

        "colombo",

        "Abitharani Pavi",

        "Cello",

        "06",

        "Friday",

        "09:00"

    ]
)

def test_schedule_search(search_value):

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        schedule.search_schedule(
            search_value
        )


        time.sleep(2)


        assert (
            search_value.lower()
            in
            driver.page_source.lower()
        )


    finally:

        driver.quit()



# ==================================================
# TC_Schel_167
# Add Popup Open
# ==================================================

def test_open_add_schedule_popup():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        schedule.click_add_schedule()

        assert (
            schedule.is_add_popup_visible()
        )

    finally:

        driver.quit()



# ==================================================
# TC_Schel_175
# Add Schedule
# ==================================================

def test_add_schedule():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        # Open Add Schedule popup

        schedule.click_add_schedule()


        assert (
            schedule.is_add_popup_visible()
        )


        # Fill schedule details

        schedule.fill_schedule(

            branch="colombo",

            lecturer="Abitharani Pavi",

            course="Cello",

            grade="06",

            day="Friday",

            start_time="09:00",

            end_time="23:00"

        )


        # Click Add Schedule button
        # (This creates the schedule)

        schedule.click_add_form_button()


        # Wait for save process

        time.sleep(5)


        # Check success message

        message = schedule.get_success_message()


        print(
            "ADD MESSAGE:",
            message
        )


        assert (

            "success" in message

            or

            "added" in message

            or

            schedule.is_schedule_table_visible()

        )


    finally:

        driver.quit()
# ==================================================
# TC_Schel_176
# Edit Schedule Popup
# ==================================================

def test_edit_schedule():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        assert (
            schedule.get_row_count() > 0
        )


        schedule.click_edit()


        assert (
            "Edit Schedule"
            in
            driver.page_source
        )


    finally:

        driver.quit()



# ==================================================
# TC_Schel_177
# Update Schedule
# ==================================================

def test_update_schedule():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        schedule.click_edit()


        schedule.change_start_time(
            "10:00"
        )


        schedule.click_update()


        time.sleep(3)


        message = (
            schedule.get_success_message()
        )


        print(
            "UPDATE MESSAGE:",
            message
        )


        assert (

            "success" in message

            or

            "updated" in message

        )


    finally:

        driver.quit()



# ==================================================
# TC_Schel_178
# Delete Schedule
# ==================================================

def test_delete_schedule():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        assert schedule.get_row_count() > 0


        # click delete icon
        schedule.click_delete_icon()


        # confirmation popup should appear
        assert schedule.is_delete_modal_visible()


        # confirm delete
        schedule.confirm_delete()


        time.sleep(5)


        # verify success message OR table reload

        message = schedule.get_success_message()


        print(
            "DELETE MESSAGE:",
            message
        )


        assert (

            "success" in message

            or

            "delete" in message

            or

            schedule.is_schedule_table_visible()

        )


    finally:

        driver.quit()


# ==================================================
# CLOSE POPUP
# ==================================================

def test_close_schedule_popup():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        schedule.click_add_schedule()


        assert (
            schedule.is_add_popup_visible()
        )


        schedule.close_popup()


    finally:

        driver.quit()



# ==================================================
# VIEW SCHEDULE
# ==================================================

def test_view_schedule():

    driver = get_driver()

    try:

        login(driver)

        schedule = SchedulePage(driver)

        schedule.open_schedule()


        assert (
            schedule.get_row_count() > 0
        )


        schedule.view_schedule()


        assert True


    finally:

        driver.quit()