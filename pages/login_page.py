from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import LOGIN_URL


class LoginPage:

    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.submit-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR,".error-banner__text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(
            LOGIN_URL
        )

    def enter_email(self, email):

        self.wait.until(
           EC.visibility_of_element_located(
            self.EMAIL
          )
        ).send_keys(email)


    def enter_password(self, password):
        self.driver.find_element(
          *self.PASSWORD
        ).send_keys(password)


    def click_login(self):

        self.driver.find_element(
         *self.LOGIN_BUTTON
        ).click()


    def login(self, email, password):
       self.enter_email(email)
       self.enter_password(password)
       self.click_login()

    def get_error_message(self):
        return self.wait.until(
           EC.visibility_of_element_located(
             self.ERROR_MESSAGE
           )
        )
