import pytest
from conftest import BaseTest
from constants.base import BaseConst
from pages.data_for_tests import Post


@pytest.mark.parametrize("browser", [BaseConst.CHROME])
class TestPosts(BaseTest):
    @pytest.fixture(scope="function")
    def main_page(self, open_start_page, random_user):
        """Register new user and return main page"""
        main_page = open_start_page.reg_new_user(random_user)
        return main_page

    @pytest.fixture(scope="function")
    def random_post(self, main_page):
        post = Post()
        post.fill_post_data()
        return post

    @pytest.fixture(scope="function")
    def created_random_post_page(self, main_page, random_post):
        """Creates new post"""
        title = random_post.title
        body = random_post.post_body
        create_post_page = main_page.click_create_post_button()
        post = create_post_page.create_post(title=title, body=body)
        return post

    def test_create_post(self, main_page, random_user, random_post):
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
        title = random_post.title
        body = random_post.post_body
        create_post_page = main_page.click_create_post_button()
        post = create_post_page.create_post(title=title, body=body)
        verified_post = post.verify_post(title, body, user)
        verified_post.check_successful_message()

    def test_edit_post_title(self, created_random_post_page, random_post, random_user):

        """
        Pre-condition:
            1.Create user and add post
        Steps:
            2.Click Edit Button
            3.Change Title
            4.Click Save button
            5.Get back to Post Page and verify new Title
        Expected:
            Title is changed at Post Page
        """
        new_title = 'New Title'
        edit_post_page = created_random_post_page.click_edit_post_button()
        edit_post_page.update_post_title(new_title)
        edit_post_page.click_update_button()
        post_page = edit_post_page.click_back_to_post_page_link()
        post_page.verify_post(title=new_title, body=random_post.post_body, user=random_user.user_name)
