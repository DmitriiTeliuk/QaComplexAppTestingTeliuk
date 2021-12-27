import pytest

from conftest import BaseTest
from constants.base import BaseConst
from pages.data_for_tests import User
from pages.decor import create_driver
from pages.start_page import StartPage


@pytest.mark.parametrize("browser", [BaseConst.CHROME])
class TestPosts(BaseTest):
    @pytest.fixture(scope="function")
    def main_page(self, open_start_page, random_user):
        """Register new user and return main page"""
        main_page = open_start_page.reg_new_user(random_user)
        return main_page

    def test_create_post(self, main_page,random_user):
        user= random_user.user_name
        title = 'Title'
        body = 'Body'
        create_post_page = main_page.click_create_post_button()
        post = create_post_page.create_post(title=title, body=body)
        post.verify_post(title, body, user)
