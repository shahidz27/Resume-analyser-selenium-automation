import uuid
from pathlib import Path

from pages.signup_page import SignupPage
from pages.analyzer_page import AnalyzerPage


BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DATA_DIR = BASE_DIR / "test_data"


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

    resume_path = TEST_DATA_DIR / "sample_resume.docx"

    assert resume_path.exists(), (
        f"File not found: {resume_path}"
    )

    analyzer.upload_resume(str(resume_path))

    analyzer.enter_jd("software engineer")

    analyzer.analyze()

    assert analyzer.verify_analysis_completed().is_displayed()


def test_analysis_without_job_description(driver):

    analyzer = signup_and_open_dashboard(driver)

    resume_path = TEST_DATA_DIR / "sample_resume.docx"

    assert resume_path.exists(), (
        f"File not found: {resume_path}"
    )

    analyzer.upload_resume(str(resume_path))

    analyzer.analyze()

    assert analyzer.verify_analysis_completed().is_displayed()


def test_upload_invalid_file(driver):

    analyzer = signup_and_open_dashboard(driver)

    invalid_file = TEST_DATA_DIR / "sample_upload_test.txt"

    assert invalid_file.exists(), (
        f"File not found: {invalid_file}"
    )

    analyzer.upload_resume(str(invalid_file))

    error = analyzer.get_error_banner()

    assert error.is_displayed()