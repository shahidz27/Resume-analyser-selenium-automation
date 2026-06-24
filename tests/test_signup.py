import uuid

from pages.signup_page import SignupPage
from pages.analyzer_page import AnalyzerPage


def test_valid_signup(driver):

    email = f"qa_{uuid.uuid4().hex[:8]}@gmail.com"
    password = "Password@123"

    signup = SignupPage(driver)
    signup.open()

    signup.signup(
        email=email,
        password=password
    )

    analyzer = AnalyzerPage(driver)

    assert analyzer.verify_back_to_upload_screen().is_displayed()






def test_valid_signup(driver):

    email = f"qa_{uuid.uuid4().hex[:8]}@gmail.com"
    password = "Password@123"

    signup = SignupPage(driver)
    signup.open()

    signup.signup(
        email=email,
        password=password
    )

    analyzer = AnalyzerPage(driver)

    assert analyzer.verify_back_to_upload_screen().is_displayed()



def test_duplicate_signup(driver):

    email = f"qa_{uuid.uuid4().hex[:8]}@gmail.com"
    password = "Password@123"

    signup = SignupPage(driver)

    # First signup
    signup.open()

    signup.signup(
        email=email,
        password=password
    )

    signup.open()
    signup.signup(
        email=email,
        password=password
    )

    assert "already" in driver.page_source.lower()