from selenium import webdriver


def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-logging"]
    )

    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        options=options
    )

    driver.implicitly_wait(5)

    return driver