from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AnalyzerPage:

    FILE_UPLOAD = (By.ID, "file-input")

    JOB_ROLE_INPUT = (
        By.ID,
        "job-role-input"
    )

    ANALYZE_BTN = (
        By.ID,
        "analyze-btn"
    )

    NEW_ANALYSIS_BUTTON = (
        By.ID,
        "new-analysis-btn"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Logout']"
    )

    ERROR_BANNER = ( By.ID, "error-banner")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def upload_resume(self, path):

        file_input = self.wait.until(
            EC.presence_of_element_located(
                self.FILE_UPLOAD
            )
        )

        file_input.send_keys(path)


    def enter_jd(self, jd):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.JOB_ROLE_INPUT
            )
        )

        field.clear()
        field.send_keys(jd)

    def analyze(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.ANALYZE_BTN
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.ANALYZE_BTN
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def verify_analysis_completed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.NEW_ANALYSIS_BUTTON
            )
        )

    def click_new_analysis(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.NEW_ANALYSIS_BUTTON
            )
        ).click()

    def verify_back_to_upload_screen(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.ANALYZE_BTN
            )
        )

    def logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT_BUTTON
            )
        ).click()

    def get_error_banner(self):

        return self.wait.until(
            EC.visibility_of_element_located(
               self.ERROR_BANNER
            )
       )