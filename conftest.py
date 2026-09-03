import pytest
import time

from selenium import webdriver


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    time.sleep(30)

    driver.quit()