from time import sleep

from constants.main_page import MainPageConstants
from constants.start_page import StartPageConstants
from pages.base import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def register(self, username_value, email_value, password_value):
        """Registration user"""
        from pages.main_page import MainPage
        # fill username
        self.fill_field(locator=self.constants.SIGN_UP_USERNAME_XPATH, value=username_value)
        # fill email
        self.fill_field(locator=self.constants.SIGN_UP_EMAIL_XPATH, value=email_value)
        # fill password
        self.fill_field(locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields were filled with register values")
        # Click on Sign Up button
        sleep(1)  # Correct
        # self._click_on_sign_up_button()
        self.wait_until_element_enebled(value=self.constants.SIGN_UP_BUTTON_XPATH).click()
        self.log.debug("User was registered")
        return MainPage(self.driver)

    @wait_until_ok()
    def _click_on_sign_up_button(self):
        """Click on button until it disappear"""
        self.log.info("Here")
        self.wait_until_element_enebled(value=self.constants.SIGN_UP_BUTTON_XPATH).click()
        # Verify Welcome message
        self.is_element_exists(value=MainPageConstants.WELCOME_MESSAGE_XPATH)
        self.log.info()

    def login(self, username_value, password_value):
        from pages.main_page import MainPage
        """Login valid User"""
        # fill username, password
        self.fill_field(locator=self.constants.SIGN_IN_USERNAME_XPATH, value=username_value)
        self.fill_field(locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=password_value)
        self.log.debug("Fields are filled")
        # Click sign in button
        sign_in_button = self.wait_until_element_enebled(value=self.constants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        self.log.debug("Clicked on 'Sign in'")
        return MainPage(self.driver)

    def verify_incorrect_login(self):
        """ Verify Error message invalid login"""
        # Find incorrect message
        message = self.wait_until_find_element(value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        # Verify message
        assert message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT
