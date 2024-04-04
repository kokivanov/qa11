from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseApp:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html"

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
