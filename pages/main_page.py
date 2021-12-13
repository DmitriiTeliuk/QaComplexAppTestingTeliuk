from selenium.webdriver.common.by import By

from QaComplexAppTestingTeliuk.Constance.main_page import MainPageConst
from QaComplexAppTestingTeliuk.pages.base_page import BasePage
from QaComplexAppTestingTeliuk.pages.start_page import StartPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = MainPageConst()

    def is_displayed_create_post_button(self):
        create_post_button = self.wait_until_find_element(by=By.XPATH, value=self.constance.CREATE_POST_BUTTON_XPATH)
        assert create_post_button.is_displayed()
        self.log.info("'create post' button is displayed")

    def log_out(self):
        self.wait_until_find_element(by=By.XPATH, value=self.constance.LOG_OUT_BUTTON_XPATH).click()
        self.log.info("'Log out' button clicked")
        return StartPage(self.driver)
