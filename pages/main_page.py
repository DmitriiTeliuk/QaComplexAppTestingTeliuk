from selenium.webdriver.common.by import By

from QaComplexAppTestingTeliuk.Constance.main_page import MainPageConst
from QaComplexAppTestingTeliuk.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = MainPageConst()

    def is_displayed_create_post_button(self):
        create_post_button = self.driver.find_element(by=By.XPATH, value=self.constance.CREATE_POST_BUTTON)
        assert create_post_button.is_displayed()

