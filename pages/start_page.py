from selenium.webdriver.common.by import By
from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.decor import wait_until_okk, new_logdecor



class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConst()

    @new_logdecor
    def log_in(self, user):
        """Try to Log in"""
        from pages.header import Header
        self.fill_field(By.XPATH, self.constants.FIELD_SIGN_IN_USER_NAME_XPATH, some_value=user.user_name)
        self.fill_field(By.XPATH, self.constants.FIELD_SIGN_IN_USER_PASSWORD_XPATH, some_value=user.user_password)
        sign_in_button = self.wait_until_find_visible_and_clickable(by=By.XPATH,
                                                                    value=self.constants.BUTTON_SIGN_IN_XPATH)
        sign_in_button.click()
        return Header(self.driver)

    @new_logdecor
    def reg_new_user(self, user):
        """New user is registered"""
        from pages.header import Header
        self.fill_field(By.XPATH, self.constants.FIELD_NEW_USER_NAME_XPATH, some_value=user.user_name)
        self.fill_field(By.XPATH, self.constants.FIELD_NEW_USER_EMAIL_XPATH, some_value=user.user_mail)
        self.fill_field(By.XPATH, self.constants.FIELD_NEW_USER_PASSWORD_XPATH, some_value=user.user_password)
        self.sign_up_button_click(1)
        return Header(self.driver)

    @new_logdecor
    def fill_new_user_name(self, user_name):
        """Fill new user name on start page """
        self.fill_field(By.XPATH, self.constants.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)

    @new_logdecor
    def click_sign_in_button(self):
        """Click Sign in Button"""
        self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constants.BUTTON_SIGN_IN_XPATH).click()

    @new_logdecor
    def get_new_user_name_field_alert(self):
        """New user name alert is displayed"""
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constants.ALERT_NEW_USER_NAME_XPATH)
        assert alert.is_displayed()
        return alert.text

    @new_logdecor
    def get_new_user_email_field_alert(self):
        """New user email alert is displayed"""
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constants.ALERT_NEW_USER_EMAIL_XPATH)
        assert alert.is_displayed()
        return alert.text

    @new_logdecor
    def get_new_user_password_field_alert(self):
        """New user password alert is displayed"""
        alert = self.wait_until_find_visible_and_clickable(by=By.XPATH,
                                                           value=self.constants.ALERT_NEW_USER_PASSWORD_XPATH)
        assert alert.is_displayed()
        return alert.text

    @new_logdecor
    def is_displayed_login_message_alert(self):
        """Login alert is displayed"""
        error_message = self.wait_until_find_element(by=By.XPATH, value=self.constants.ALERT_LOG_IN_XPATH)
        assert error_message.is_displayed()

    @wait_until_okk(timeout=15, period=1)
    @new_logdecor
    def sign_up_button_click(self, verify):
        """Click Sign up button"""
        self.wait_until_find_visible_and_clickable(by=By.XPATH, value=self.constants.BUTTON_SIGN_UP_XPATH).click()
        if verify:
            # Wait until main_page button appears
            from constants.header import HeaderConst
            assert self.wait_until_find_element(by=By.XPATH,
                                                value=HeaderConst.CREATE_POST_BUTTON_XPATH).is_displayed()
