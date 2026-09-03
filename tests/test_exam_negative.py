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


    login_page = LoginPage(driver)


    login_page.login(
        "admin",
        "admin123"
    )


    time.sleep(3)



# ==================================================
# TC_Exam_NEG_001
# Empty Course + Empty Grade Validation
# ==================================================

def test_empty_course_validation(driver):


    login(driver)


    exam = ExamPage(driver)



    # Open Exam

    exam.open_exam_page()



    # Add Exam

    exam.click_add_exam()



    # Course = EMPTY
    # Grade = EMPTY


    exam.fill_exam_details_negative(

        exam_type="Theory",

        date="2027-09-18",

        start="09:00",

        end="10:00"

    )



    # Click Create Group

    exam.click(
        exam.CREATE_GROUP_BUTTON
    )


    print(
        "CREATE GROUP CLICKED"
    )



    # Verify Course and Grade validation

    exam.verify_empty_course_validation()





# ==================================================
# TC_Exam_NEG_002
# Empty Grade Validation
# ==================================================

def test_empty_grade_validation(driver):


    login(driver)



    exam = ExamPage(driver)



    # Open Exam

    exam.open_exam_page()



    # Add Exam

    exam.click_add_exam()



    # Select Course

    exam.select_dropdown(
        exam.COURSE,
        "Keyboard"
    )



    # Grade = EMPTY



    # Select Exam Type

    exam.select_dropdown(
        exam.EXAM_TYPE,
        "Theory"
    )



    # Enter Exam Date

    exam.enter_text(
        exam.EXAM_DATE,
        "2027-09-18"
    )



    # Enter Start Time

    exam.enter_text(
        exam.START_TIME,
        "09:00"
    )



    # Enter End Time

    exam.enter_text(
        exam.END_TIME,
        "10:00"
    )



    print(
        "EMPTY GRADE DATA ENTERED"
    )



    # Click Create Group

    exam.click(
        exam.CREATE_GROUP_BUTTON
    )


    print(
        "CREATE GROUP CLICKED"
    )



    # Verify Grade validation

    exam.verify_empty_grade_validation()


