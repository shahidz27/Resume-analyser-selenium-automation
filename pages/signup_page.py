from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import SIGNUP_URL


class SignupPage:

    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SIGNUP_BUTTON = ( By.XPATH, "//button[normalize-space()='Sign Up']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(
            SIGNUP_URL
        )

    def signup(self, email, password):

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.SIGNUP_BUTTON
        ).click()