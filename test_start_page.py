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

    def test_start_page(self):
        """Sample test"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(3)
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(3)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        # Click button
        button.click()
        # Find error message
        sleep(1)
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"


    def test_invalid_login(self):
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
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(3)
        username.send_keys(f"userName{self.random_num()}")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(3)
        password.send_keys(f"Pwd{self.random_num()}")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sleep(3)
        # Click button
        button.click()
        # Find error message
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"
