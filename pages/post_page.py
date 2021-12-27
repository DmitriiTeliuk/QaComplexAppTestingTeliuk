import datetime
from time import sleep

from selenium.webdriver.common.by import By
from constants.post_page import PostPageConst
from pages.base_page import BasePage
from pages.header import Header


class PostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConst()
        self.header = Header(self.driver)

    def verify_post(self, title, body, user):
        element_title = self.wait_until_find_element(by=By.XPATH, value=self.constants.POST_TITLE_XPATH)
        # check title
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

        #check successful message
        successful_message = self.wait_until_find_element(by=By.XPATH, value=self.constants.POST_IS_CREATED_MESSAGE_XPATH)
        expected_message = self.constants.SUCCESS_MESSAGE_TEXT
        assert successful_message.text == expected_message
        assert  successful_message.is_displayed()
