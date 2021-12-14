from selenium.webdriver.common.by import By
from QaComplexAppTestingTeliuk.constance.start_page import StartPageConst
from QaComplexAppTestingTeliuk.pages.base_page import BasePage
from QaComplexAppTestingTeliuk.pages.decor import wait_until_okk


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = StartPageConst()

    def log_in(self, user_name, user_password):
        from QaComplexAppTestingTeliuk.pages.main_page import MainPage
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_NAME_XPATH, some_value=user_name)
        self.log.info("'user name' field filled")
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_PASSWORD_XPATH, some_value=user_password)
        self.log.info("'user password' field filled")
        sign_in_button = self.wait_until_find_visible_and_clickable(by=By.XPATH,
                                                                    value=self.constance.BUTTON_SIGN_IN_XPATH)
        sign_in_button.click()
        self.log.info("'Log in' button clicked")
        return MainPage(self.driver)

    def reg_new_user(self, user_name, user_email, user_password):
        from QaComplexAppTestingTeliuk.pages.main_page import MainPage
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
        self.log.info("'new_user name' field filled")
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_EMAIL_XPATH, some_value=user_email)
        self.log.info("'new_user email' field filled")
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_PASSWORD_XPATH, some_value=user_password)
        self.log.info("'new_user password' field filled")
        self.sign_up_button_click(1)
        self.log.info("'sign up' button clicked")
        return MainPage(self.driver)

    def fill_new_user_name(self, user_name):
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
        self.log.info("'new_user name' field filled")

    def click_sign_in_button(self):
        self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constance.BUTTON_SIGN_IN_XPATH).click()
        self.log.info("'sign in' button clicked")

    def get_new_user_name_field_alert(self):
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constance.ALERT_NEW_USER_NAME_XPATH)
        assert alert.is_displayed()
        self.log.info("'new_user name field alert' is displayed")
        return alert.text

    def get_new_user_email_field_alert(self):
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constance.ALERT_NEW_USER_EMAIL_XPATH)
        assert alert.is_displayed()
        self.log.info("'new_user email field alert' is displayed")
        return alert.text

    def get_new_user_password_field_alert(self):
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constance.ALERT_NEW_USER_PASSWORD_XPATH)
        assert alert.is_displayed()
        self.log.info("'new_user password field alert' is displayed")
        return alert.text

    def is_displayed_login_message_alert(self):
        error_message = self.wait_until_find_element(by=By.XPATH, value=self.constance.ALERT_LOG_IN_XPATH)
        self.log.info("'login alert' is displayed")
        assert error_message.is_displayed()

    @wait_until_okk(timeout=15, period=1)
    def sign_up_button_click(self, verify):
        self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constance.BUTTON_SIGN_UP_XPATH).click()
        if verify:
            # Wait until main_page button appears
            from QaComplexAppTestingTeliuk.constance.main_page import MainPageConst
            assert self.wait_until_find_element(by=By.XPATH, value=MainPageConst.CREATE_POST_BUTTON_XPATH).is_displayed()


