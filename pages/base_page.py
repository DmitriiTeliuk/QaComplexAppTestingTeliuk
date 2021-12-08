import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)

    def fill_field(self, by, locator, some_value):
        user_field = self.driver.find_element(by=by, value=locator)
        user_field.clear()
        user_field.send_keys(some_value)
