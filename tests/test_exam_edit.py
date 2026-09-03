import time

from pages.login_page import LoginPage
from pages.exam_page import ExamPage


LOGIN_URL = (
    "https://aradanaqa.pineappleai.cloud/login"
)



def login(driver):

    driver.get(
        LOGIN_URL
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    time.sleep(3)



# ==================================================
# TC_Exam_191
# Edit Exam Update
# ==================================================

def test_edit_exam_update(driver):


    login(driver)


    exam = ExamPage(driver)



    # Open Exam

    exam.open_exam_page()



    # Click Edit icon

    exam.click_edit_exam()



    # Change Practical -> Theory

    exam.change_exam_type(
        "Theory"
    )



    # Edit Group

    exam.click_edit_group()



    # No student change

    exam.click_next()



    # Update Group

    exam.update_group_save()



    # Update Exam

    exam.update_exam()



    # Verify popup

    exam.verify_update_success()



    # Verify table

    exam.verify_updated_exam()



    print(
        "EDIT EXAM TEST PASSED"
    )