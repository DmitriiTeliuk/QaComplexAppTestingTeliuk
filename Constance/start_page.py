class StartPageConst:
    # Sign up fields/buttons
    FIELD_NEW_USER_NAME_XPATH = "//input[@id='username-register']"
    FIELD_NEW_USER_EMAIL_XPATH = "//input[@id='email-register']"
    FIELD_NEW_USER_PASSWORD_XPATH = "//input[@id='password-register']"
    BUTTON_SIGN_UP = "//button[@type='submit']"
    # Sing in fields/buttons
    FIELD_SIGN_IN_USER_NAME = "//input[@placeholder='Username']"
    FIELD_SIGN_IN_USER_PASSWORD = "//input[@placeholder='Password']"
    BUTTON_SIGN_IN = "//button[text()='Sign In']"
    # Alerts
    ALERT_NEW_USER_NAME = "//*[@for='username-register']//following-sibling::div"
    ALERT_NEW_USER_EMAIL = "//*[@for='email-register']//following-sibling::div"
    ALERT_NEW_USER_PASSWORD = "//*[@for='password-register']//following-sibling::div"
    ALERT_LOG_IN = "//div[contains(@class,'alert alert-danger text-center')]"
