from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Waits:


    def __init__(self,driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )


    def click(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )


    def visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )


    def presence(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )


    def invisible(self, locator):

        return self.wait.until(
            EC.invisibility_of_element(locator)
        )