import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage



# ---------------------------------------
# TC-001 Verify valid login functionality
# ---------------------------------------

def test_valid_login(driver):

    # Open Login Page
    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )


    # Login object
    login = LoginPage(driver)


    # Enter credentials
    login.login(
        "admin",
        "admin123"
    )


    wait = WebDriverWait(
        driver,
        10
    )


    # Verify Dashboard loaded
    dashboard = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )


    assert dashboard.is_displayed()


    print(
        "VALID LOGIN TEST PASSED"
    )



# ---------------------------------------
# TC-002 Verify logout functionality
# ---------------------------------------

def test_logout_functionality(driver):


    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )


    login = LoginPage(driver)


    login.login(
        "admin",
        "admin123"
    )


    wait = WebDriverWait(
        driver,
        10
    )


    # Wait dashboard
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )


    print(
        "LOGIN SUCCESSFUL"
    )


    # Click logout menu

    logout_menu = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/span'
            )
        )
    )


    driver.execute_script(
        "arguments[0].click();",
        logout_menu
    )


    print(
        "LOGOUT MENU CLICKED"
    )


    time.sleep(2)



    # Click confirmation logout button

    logout_confirm = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/button[2]'
            )
        )
    )


    logout_confirm.click()


    print(
        "LOGOUT BUTTON CLICKED"
    )



    # Verify redirected login page

    username = wait.until(
        EC.visibility_of_element_located(
            (
                By.NAME,
                "username"
            )
        )
    )


    assert username.is_displayed()


    print(
        "LOGOUT SUCCESSFUL - LOGIN PAGE DISPLAYED"
    )