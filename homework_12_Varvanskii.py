"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(11111, 99999)))

    def test_registration(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(1)
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='password']")
        password.clear()
        sleep(1)
        button = driver.find_element(by=By.XPATH, value=".//button[text() = 'Sign In']")
        button.click()
        sleep(1)
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username.clear()
        sleep(1)
        # username.send_keys(f"userName{self.random_num()}")
        # Find and clean Email field
        email = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email.clear()
        sleep(1)
        # email.send_keys(f"{self.random_num()}@gmail.com")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password.clear()
        sleep(1)
        # password.send_keys(f"Pwd{self.random_num()}")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        sleep(1)
        # Click button
        button.click()
        # Find  message
        # message = driver.find_element(by=By.XPATH, value=".//*[h2/text()]")  # /html/body/div[2]/div/h2/text()[1]
        # Verify message after registration
        # assert message.text == "Hello"
