import os
import uuid

from pages.signup_page import SignupPage
from pages.analyzer_page import AnalyzerPage


def create_user():
    return (
        f"qa_{uuid.uuid4().hex[:8]}@gmail.com",
        "Password@123"
    )


def signup_and_open_dashboard(driver):

    email, password = create_user()

    signup = SignupPage(driver)
    signup.open()

    signup.signup(
        email=email,
        password=password
    )

    return AnalyzerPage(driver)


def test_resume_analysis_success(driver):

    analyzer = signup_and_open_dashboard(driver)

    resume_path = os.path.abspath(
        "test_data/sample_resume.docx"
    )

    analyzer.upload_resume(resume_path)

    analyzer.enter_jd(
        "software engineer"
    )

    analyzer.analyze()

    assert analyzer.verify_analysis_completed().is_displayed()


def test_analysis_without_job_description(driver):

    analyzer = signup_and_open_dashboard(driver)

    resume_path = os.path.abspath(
        "test_data/sample_resume.docx"
    )

    analyzer.upload_resume(resume_path)

    analyzer.analyze()

    assert analyzer.verify_analysis_completed().is_displayed()#should be able to upload without jd




def test_upload_invalid_file(driver):

    analyzer = signup_and_open_dashboard(driver)

    invalid_file = os.path.abspath(
        "test_data/sample_upload_test.txt"
    )

    analyzer.upload_resume(invalid_file)

    error = analyzer.get_error_banner()

    assert error.is_displayed()