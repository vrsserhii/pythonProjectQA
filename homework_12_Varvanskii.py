"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def random_num(self):
        """Generate random number"""
        return str(random.choice(range(111111111111, 999999999999)))

    def test_registration(self):
        """
        - Create driver
        - Open start page
        - Find Username field
        - Put value
        - Find Password field
        - Put value
        - Click on Sign In button
        - Verify error message
        """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username.clear()
        sleep(1)
        username.send_keys(f"userName{self.random_num()}")
        # Find and clean Email field
        email = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email.clear()
        sleep(1)
        email.send_keys(f"{self.random_num()}@gmail.com")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password.clear()
        sleep(1)
        password.send_keys(f"Pwd{self.random_num()}")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        sleep(1)
        # Click button
        button.click()
        # Find  message
        message = driver.find_element(by=By.XPATH, value=".//*[h2]")
        # Verify message after registration
        # assert message.text == "Hello"
