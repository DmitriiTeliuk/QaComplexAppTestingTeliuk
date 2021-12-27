from selenium.webdriver.common.by import By
from constants.header import HeaderConst
from pages.base_page import BasePage
from pages.decor import new_logdecor




class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = HeaderConst()

    @new_logdecor
    def is_displayed_create_post_button(self):
        """Create post button is displayed"""
        create_post_button = self.wait_until_find_element(by=By.XPATH, value=self.constance.CREATE_POST_BUTTON_XPATH)
        assert create_post_button.is_displayed()

    @new_logdecor
    def log_out(self):
        """Log out button is clicked"""
        from pages.start_page import StartPage
        self.wait_until_find_element(by=By.XPATH, value=self.constance.LOG_OUT_BUTTON_XPATH).click()
        return StartPage(self.driver)

    @new_logdecor
    def click_create_post_button(self):
        """Click on 'create post' button"""
        from pages.create_post_page import CreatePostPage
        self.wait_until_find_element(by=By.XPATH, value=self.constance.CREATE_POST_BUTTON_XPATH).click()
        return CreatePostPage(self.driver)
