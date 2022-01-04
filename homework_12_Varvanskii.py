"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(111111, 999999)))

    def test_registration_page(self):
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
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        sleep(1)
        username.send_keys(f"Serhii{self.random_num()}")
        # Find and clean Email
        Email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        Email.clear()
        sleep(0.5)
        Email.send_keys(f"{self.random_num()}@gmail.com")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"224455{self.random_num()}")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        # Click button
        button.click()
        # Find error message
        sleep(0.5)
        # hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        # assert hello_message.text == f"Hello, your feed is empty."
        # message = driver.find_element(by=By.XPATH, value=".//div[@h2]")
        # Verify message
        # assert message.text == f"Hello"

    def test_valid_login(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(0.5)
        username.send_keys(f"Serhii")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"112233445566")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sleep(0.5)
        # Click button
        button.click()
        # find Sign out button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign Out']")
        button.click()
        sleep(0.5)

    def test_login_username_invalid(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(0.5)
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"112233445566")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sleep(0.5)
        # Click button
        button.click()
        # Error message
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"

    def test_login_password_invalid(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(0.5)
        username.send_keys(f"Serhii")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(0.5)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sleep(0.5)
        # Click button
        button.click()
        # Error message
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == "Error"

    def test_invalid_registration_page(self):
        """Sample test"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2.exe")
        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
        username.clear()
        sleep(0.5)
        username.send_keys()
        # Find and clean Email
        Email = driver.find_element(by=By.XPATH, value=".//*[@id='email-register']")
        Email.clear()
        sleep(0.5)
        Email.send_keys()
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//*[@id='password-register']")
        password.clear()
        sleep(0.5)
        password.send_keys()
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        # Click button
        button.click()
        sleep(0.5)
