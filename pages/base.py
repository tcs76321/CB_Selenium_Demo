import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_loader import load_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = load_config()["timeout"]

    def open(self, url):
        time.sleep(1)
        self.driver.get(url)

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()