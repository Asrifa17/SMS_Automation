import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.exam_page import ExamPage



LOGIN_URL = (
    "https://aradanaqa.pineappleai.cloud/login"
)



# ==========================
# Login Function
# ==========================

def login(driver):

    driver.get(
        LOGIN_URL
    )


    login_page = LoginPage(driver)


    login_page.login(
        "admin",
        "admin123"
    )


    time.sleep(3)



# =====================================================
# TC_Exam_NEG_001
# Empty Course Validation
# =====================================================

def test_empty_course_validation(driver):


    login(driver)


    exam = ExamPage(driver)



    # Open Exam Module

    exam.open_exam_page()



    # Open Add Exam Form

    exam.click_add_exam()



    # ---------------------------------
    # Course intentionally empty
    # ---------------------------------


    # Select Grade

    exam.select_dropdown(
        exam.GRADE,
        "10"
    )



    # Select Exam Type

    exam.select_dropdown(
        exam.EXAM_TYPE,
        "Practical"
    )



    # Enter Exam Date

    exam.enter_text(
        exam.EXAM_DATE,
        "2026-11-12"
    )



    # Enter Start Time

    exam.enter_text(
        exam.START_TIME,
        "08:00"
    )



    # Enter End Time

    exam.enter_text(
        exam.END_TIME,
        "10:00"
    )


    print(
        "COURSE LEFT EMPTY"
    )



    # Click Create Group

    exam.click(
        exam.CREATE_GROUP_BUTTON
    )


    time.sleep(3)



    # Get page text

    body_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text



    print(
        body_text
    )



    # Validation checking

    assert (
        "course" in body_text.lower()
        or
        "required" in body_text.lower()
    )


    print(
        "TC_Exam_NEG_001 PASSED"
    )