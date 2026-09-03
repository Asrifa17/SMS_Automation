import time

from pages.login_page import LoginPage
from pages.exam_page import ExamPage


LOGIN_URL = (
    "https://aradanaqa.pineappleai.cloud/login"
)


def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        "admin",
        "admin123"
    )

    time.sleep(3)



def test_create_exam(driver):


    login(driver)


    exam = ExamPage(driver)



    # Open Exam Module

    exam.open_exam_page()



    # Open Add Exam

    exam.click_add_exam()



    # Fill Exam Details

    exam.fill_exam_details(

        course="Flute",

        grade="10",

        exam_type="Practical",

        date="2026-11-12",

        start="08:00",

        end="10:00"

    )



    # Create Group

    exam.create_group(
        student_name="hfgf fhfh",
        group_name="Floo"
    )



    # Create Exam

    exam.save_exam()



    # Verify exam created

    exam.verify_exam_created(
        course="Flute",
        group_name="Floo"
    )



    print(
        "EXAM MODULE AUTOMATION PASSED"
    )
