import pytest
from conftest import BaseTest
from constants.base import BaseConst


@pytest.mark.parametrize("browser", [BaseConst.CHROME])
class TestPosts(BaseTest):
    @pytest.fixture(scope="function")
    def main_page(self, open_start_page, random_user):
        """Register new user and return main page"""
        main_page = open_start_page.reg_new_user(random_user)
        return main_page

    def test_create_post(self, main_page, random_user):
        """
        Pre-conditions:
            1.Register user
        Steps:
            2.Click 'Create post' button
            3.Fill Title and Body
            4. Click 'Save new post' button
            5.Verify post(Title, Body, Creator, Successful message )
        Expected:
            New Post created successfully
        """
        user = random_user.user_name
        title = 'Title'
        body = 'Body'
        create_post_page = main_page.click_create_post_button()
        post = create_post_page.create_post(title=title, body=body)
        post.verify_post(title, body, user)
