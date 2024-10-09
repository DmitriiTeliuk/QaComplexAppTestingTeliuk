from selenium.webdriver.common.by import By

from constants.header import HeaderConst
from constants.post_edit_page import PostEditPageConst
from pages.base_page import BasePage


class PostEditPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostEditPageConst()
        self.header = HeaderConst()

    def update_post_title(self, new_title):
        self.fill_field(by=By.XPATH, locator=self.constants.POST_TITLE_XPATH, some_value=new_title)

    def update_post_body(self, new_body):
        self.fill_field(by=By.XPATH, locator=self.constants.POST_BODY_FIELD_XPATH, some_value=new_body)

    def click_update_button(self):
        self.wait_until_find_element(by=By.XPATH, value=self.constants.UPDATE_POST_BUTTON).click()
        success_msg = self.wait_until_find_element(by=By.XPATH, value=self.constants.SUCCESSFUL_UPDATE_MESSAGE_XPATH)
        assert success_msg.is_displayed()

    def click_back_to_post_page_link(self):
        from pages.post_page import PostPage
        self.wait_until_find_element(by=By.XPATH, value=self.constants.BACK_TO_POST_PAGE_LINK).click()
        return PostPage(self.driver)
