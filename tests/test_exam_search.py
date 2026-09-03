import time

from pages.login_page import LoginPage
from pages.exam_page import ExamPage



def test_search_exam(driver):


    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )


    login = LoginPage(driver)


    login.login(
        "admin",
        "admin123"
    )


    time.sleep(3)


    exam = ExamPage(driver)


    exam.open_exam_page()


    exam.search_exam(
        "Keyboard"
    )


    exam.verify_search_result(
        "keyboard"
    )


    print(
        "EXAM SEARCH TEST PASSED"
    )