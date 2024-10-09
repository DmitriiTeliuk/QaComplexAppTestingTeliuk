import datetime
from selenium.webdriver.common.by import By
from constants.post_page import PostPageConst
from pages.base_page import BasePage
from pages.decor import new_logdecor
from pages.header import Header
from pages.post_edit_page import PostEditPage


class PostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConst()
        self.header = Header(self.driver)

    @new_logdecor
    def verify_post(self, title, body, user):
        """Verify post by Title + Body + Creator"""
        # check title
        element_title = self.wait_until_find_element(by=By.XPATH, value=self.constants.POST_TITLE_XPATH)
        assert element_title.text == title

        # check body
        element_body = self.wait_until_find_element(by=By.XPATH,
                                                    value=self.constants.POST_BODY_XPATH.format(post_body=body))
        assert element_body.text == body
        date_now = datetime.datetime.today()

        # check creator
        expected_creator = self.constants.POSTED_BY_MESSAGE.format(user_name=user.lower(),
                                                                   date=date_now.strftime("%m/%d/%Y"))
        actual_creator = self.wait_until_find_element(by=By.XPATH, value=self.constants.POSTED_BY_XPATH).text
        assert actual_creator == expected_creator
        return PostPage(self.driver)

    def check_successful_message(self):
        """Check successful message after post is created"""
        successful_message = self.wait_until_find_element(by=By.XPATH,
                                                          value=self.constants.POST_IS_CREATED_MESSAGE_XPATH)
        expected_message = self.constants.SUCCESS_MESSAGE_TEXT
        assert successful_message.text == expected_message
        assert successful_message.is_displayed()

    @new_logdecor
    def click_edit_post_button(self):
        """Click  edit post button"""
        self.wait_until_find_element(by=By.XPATH, value=self.constants.POST_EDIT_BUTTON).click()
        return PostEditPage(self.driver)
