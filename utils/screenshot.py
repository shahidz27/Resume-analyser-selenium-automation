from datetime import datetime


def take_screenshot(driver):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_name = (
        f"screenshots/failure_{timestamp}.png"
    )

    driver.save_screenshot(file_name)

    return file_name