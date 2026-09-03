from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():

    options = Options()
    options.add_argument("--start-maximized")

    driver_path = ChromeDriverManager().install()

    print("DRIVER PATH =", driver_path)

    service = Service(driver_path)

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver