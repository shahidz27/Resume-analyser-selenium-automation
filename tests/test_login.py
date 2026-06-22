import uuid

from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.analyzer_page import AnalyzerPage


def test_valid_login(driver):

    email = f"qa_{uuid.uuid4().hex[:8]}@gmail.com"
    password = "Password@123"
    signup = SignupPage(driver)
    signup.open()
    signup.signup(email, password)

    analyzer = AnalyzerPage(driver)

    analyzer.logout()

    login = LoginPage(driver)

    login.login(
        email=email,
        password=password
    )

    assert analyzer.verify_back_to_upload_screen().is_displayed()

from pages.login_page import LoginPage


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login(
        "invalid@gmail.com",
        "WrongPassword123"
    )

    error = login.get_error_message()

    assert error.text == "Invalid credentials"

from pages.login_page import LoginPage


def test_login_with_empty_credentials(driver):

    login = LoginPage(driver)

    login.open()

    login.click_login()

    assert "login" in driver.current_url.lower()