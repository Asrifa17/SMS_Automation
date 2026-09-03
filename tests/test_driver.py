from utilities.driver_setup import get_driver


def test_driver():

    driver = get_driver()

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()