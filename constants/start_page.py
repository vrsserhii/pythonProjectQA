class StartPageConstants:
    # SIGN_REG
    SIGN_UP_USERNAME_XPATH = ".//*[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//*[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//*[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[text()='Sign up for OurApp']"
    # SIGN_IN
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Invalid username / password"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
