from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_welcome_message(self, username):
        """Verify Welcome user message """
        hello_message = self.wait_until_find_element(value=self.constants.WELCOME_MESSAGE_XPATH)
        # assert f"Hello" in hello_message.text
        assert hello_message.text == f"Hello {username.lower()}, your feed is empty."

    def logout(self):
        """Sign OUT from Account"""
        self.wait_until_element_enebled(value=self.constants.SIGN_OUT_BUTTON_XPATH).click()
