from selenium.webdriver.common.by import By
from constance.main_page import MainPageConst
from pages.base_page import BasePage
from pages.decor import new_logdecor
from pages.start_page import StartPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = MainPageConst()

    @new_logdecor
    def is_displayed_create_post_button(self):
        """Create post button is displayed"""
        create_post_button = self.wait_until_find_element(by=By.XPATH, value=self.constance.CREATE_POST_BUTTON_XPATH)
        assert create_post_button.is_displayed()
        # self.log.info("'create post' button is displayed")

    @new_logdecor
    def log_out(self):
        """Log out button is clicked"""
        self.wait_until_find_element(by=By.XPATH, value=self.constance.LOG_OUT_BUTTON_XPATH).click()
        # self.log.info("'Log out' button clicked")
        return StartPage(self.driver)
