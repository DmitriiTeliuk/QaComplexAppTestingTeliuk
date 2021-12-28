from selenium.webdriver.common.by import By
from constants.create_post_page import CreatePostConst
from pages.base_page import BasePage
from pages.decor import new_logdecor


class CreatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostConst()
        from pages.header import Header
        self.header = Header(self.driver)

    @new_logdecor
    def create_post(self, title, body):
        """Creates post with provided title/article"""
        from pages.post_page import PostPage
        self.fill_field(By.XPATH, self.constants.POST_TITLE_FIELD_XPATH, some_value=title)
        self.fill_field(By.XPATH, self.constants.POST_BODY_FIELD_XPATH, some_value=body)
        self.wait_until_find_element(by=By.XPATH, value=self.constants.SAVE_NEW_POST_BUTTON).click()
        return PostPage(self.driver)
