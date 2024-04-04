import pytest
from selenium import webdriver


class WebDriverSetup:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(20)


@pytest.fixture(scope="class")
def browser(request):
    web_driver_setup = WebDriverSetup()
    request.cls.driver = web_driver_setup.driver
    yield
    web_driver_setup.driver.quit()
