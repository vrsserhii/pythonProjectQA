"""Stores tests related to start page"""
import random

import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage(BaseTest):

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(111111, 999999)))

    @pytest.fixture(scope="function")
    def driver(self):
        """Create and return driver and close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return Start Page"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def registered_user(self, start_page):
        """Registered User and return Data"""
        username_value = f"Serhii{self.random_num()}"
        email_value = f"{self.random_num()}@gmail.com"
        password_value = f"224455{self.random_num()}"
        """Fill email, login and password"""
        main_page = start_page.register(username_value, email_value, password_value)
        # Logout
        main_page.logout()

        return username_value, email_value, password_value

    def test_registration_page(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill Username, email, password fields
            - Click on Register button
            - Verify message
        """
        username_value = f"Serhii{self.random_num()}"
        email_value = f"{self.random_num()}@gmail.com"
        password_value = f"224455{self.random_num()}"
        # fill username, email, password fields
        main_page = start_page.register(username_value, email_value, password_value)
        self.log.info("User was registered successfully")
        # Verify registered success
        main_page.verify_welcome_message(username_value)
        self.log.info("Registration was successfully")

    def test_valid_login(self, start_page, registered_user):
        """
        - Preconditions:
            - Open start page
            - Registered user
        - Steps:
            - Fill valid Username, password values
            - Click on sign in button
            - Verify message
        """
        # Init User data from fixture
        username_value, _, password_value = registered_user
        # fill valid values
        main_page = start_page.login(username_value, password_value)
        self.log.info("Logged as '%s'", username_value)
        # verify wellcome message
        main_page.verify_welcome_message(username_value)
        self.log.info("Welcome message was verified")

    def test_login_username_invalid(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill invalid Username, valid password value
            - Click on sign in button
            - Verify Error message
        """
        # fill invalid username
        start_page.login("", "112233445566")
        self.log.info("Fields are filled invalid NAME")
        # verify error message
        start_page.verify_incorrect_login()
        self.log.info("Error message match to expected")

    def test_login_password_invalid(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill invalid Password, valid Username value
            - Click on sign in button
            - Verify Error message
        """
        # fill invalid password
        start_page.login("Serhii", "")
        self.log.info("Fields are filled invalid PASSWORD")
        # verify error  message
        start_page.verify_incorrect_login()
        self.log.info("Error message match to expected")

    def test_invalid_registration_page(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Don't fill the fields Username, email, password
            - Click on Register button
            - Verify message
        """
        username_value = f""
        email_value = f""
        password_value = f""
        # username, email, password fields should be empty
        start_page.register(username_value, email_value, password_value)
        self.log.info("User wasn't registered, Please Enter Values")
