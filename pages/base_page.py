import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, by, locator, some_value):
        user_field = self.wait_until_find_element(by=by, value=locator)
        # user_field = self.driver.find_element(by=by, value=locator)
        self.log.info("Field found")
        user_field.clear()
        user_field.send_keys(some_value)

    def wait_until_find_element(self, by, value):
        """Wait unlit element is found"""
        return self.wait.until(EC.presence_of_element_located(locator=(by, value)))

    def wait_until_find_visible_and_clickable(self, by, value):
        element = self.wait_until_find_element(by, value)
        return self.wait.until(EC.element_to_be_clickable(element))