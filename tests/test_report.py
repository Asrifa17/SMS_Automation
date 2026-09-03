from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


from pages.login_page import LoginPage
from pages.report_page import ReportPage



URL = "https://aradanaqa.pineappleai.cloud/login"





# =========================================================
# TC_Report_191 - TC_Report_196 - TC_Report_199
# Report Navigation + Filters + PDF
# =========================================================


def test_report_module():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(URL)


    login = LoginPage(driver)


    login.login(
        "admin",
        "admin123"
    )


    wait = WebDriverWait(
        driver,
        15
    )


    dashboard = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )


    assert dashboard.is_displayed()


    print("LOGIN SUCCESSFUL")


    report = ReportPage(driver)



    report.open_report_page()

    print("REPORT PAGE OPENED")


    time.sleep(3)



    report.open_payment_report()

    print("PAYMENT REPORT OPENED")


    time.sleep(3)


    driver.back()

    time.sleep(3)



    report.open_exam_report()

    print("EXAM REPORT OPENED")


    time.sleep(3)


    driver.back()

    time.sleep(3)



    report.open_result_report()

    print("RESULT REPORT OPENED")


    time.sleep(5)



    report.search_student(
        "nuha iffa"
    )


    assert report.get_result_count() > 0


    print("STUDENT SEARCH PASSED")



    report.select_course(
        "Keyboard"
    )

    print("COURSE FILTER PASSED")



    report.select_grade(
        "1"
    )

    print("GRADE FILTER PASSED")



    report.select_exam(
        "keybord"
    )

    print("EXAM FILTER PASSED")



    report.click_generate_pdf()


    print("PDF BUTTON CLICK PASSED")


    driver.quit()





# =========================================================
# TC_Report_197
# View Individual Student Result
# =========================================================


def test_view_student_result():


    driver = webdriver.Chrome()


    driver.maximize_window()


    driver.get(URL)



    login = LoginPage(driver)


    login.login(
        "admin",
        "admin123"
    )



    wait = WebDriverWait(
        driver,
        15
    )


    dashboard = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )


    assert dashboard.is_displayed()


    print("LOGIN SUCCESSFUL")



    report = ReportPage(driver)



    report.open_report_page()


    print("REPORT PAGE OPENED")


    time.sleep(3)



    report.open_result_report()


    print("RESULT REPORT OPENED")


    time.sleep(5)



    report.search_student(
        "Md Muzzamil"
    )


    assert report.get_result_count() > 0


    print("STUDENT SEARCH PASSED")



    report.select_course(
        "Keyboard"
    )


    print("COURSE SELECTED")



    report.select_grade(
        "1"
    )


    print("GRADE SELECTED")



    report.select_exam(
        "keybord"
    )


    print("EXAM SELECTED")



    report.click_view_result()



    assert report.verify_result_popup()


    print(
        "INDIVIDUAL RESULT REPORT OPENED"
    )



    report.close_result_popup()


    print(
        "POPUP CLOSED"
    )



    driver.quit()





# =========================================================
# TC_Report_198
# Update Student Result
# Ramesh Kumar : AB -> B
# =========================================================

def test_update_student_result():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get(URL)


    # LOGIN

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )


    wait = WebDriverWait(
        driver,
        15
    )


    dashboard = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )


    assert dashboard.is_displayed()


    report = ReportPage(driver)



    # OPEN REPORT

    report.open_report_page()

    time.sleep(3)



    # OPEN RESULT REPORT

    report.open_result_report()

    time.sleep(5)



    # CLICK + ADD

    report.click_add_button()



    # SELECT COURSE

    report.select_add_course(
        "Keyboard"
    )



    # SELECT GRADE

    report.select_add_grade(
        "1"
    )



    # SELECT EXAM

    report.select_add_exam(
        "keyboard"
    )



    # ==========================================
    # UPDATE RAMESH KUMAR
    # AB -> B
    # ==========================================

    report.update_student_result(
        "Ramesh Kumar",
        "B"
    )



    time.sleep(5)



    # SEARCH UPDATED STUDENT

    report.search_student(
        "Ramesh Kumar"
    )



    # VERIFY RESULT

    assert report.verify_student_result(
        "Ramesh Kumar",
        "B"
    )


    print(
        "RAMESH KUMAR RESULT UPDATED SUCCESSFULLY"
    )



    # GENERATE PDF

    report.click_generate_pdf()


    print(
        "PDF GENERATED SUCCESSFULLY"
    )


    driver.quit()