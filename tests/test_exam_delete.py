from selenium import webdriver
from pages.login_page import LoginPage
from pages.exam_page import ExamPage

import time


URL = "https://aradanaqa.pineappleai.cloud/login"



def test_delete_exam():


    driver = webdriver.Chrome()

    driver.maximize_window()


    driver.get(URL)


    login = LoginPage(driver)


    login.login(
        "admin",
        "admin123"
    )


    time.sleep(3)


    exam = ExamPage(driver)


    exam.open_exam_page()


    time.sleep(3)


    exam.delete_exam()


    driver.quit()