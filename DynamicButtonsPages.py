from selenium.webdriver.common.by import By
from .BaseApp import BaseApp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicButtonsLocator:
    START_BUTTON = (By.ID, "button00")
    BUTTON_ONE = (By.ID, "button01")
    BUTTON_TWO = (By.ID, "button02")
    BUTTON_THREE = (By.ID, "button03")
    ALL_BUTTONS_CLICKED_TEXT = (By.ID, "buttonmessage")


class SearchHelper(BaseApp):
    def click_button_zero(self):
        button_one = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button00")))
        self.find_element(DynamicButtonsLocator.START_BUTTON).click()

    def click_button_one(self):
        button_one = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button01")))
        self.find_element(DynamicButtonsLocator.BUTTON_ONE).click()

    def click_button_two(self):
        button_two = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button02")))
        self.find_element(DynamicButtonsLocator.BUTTON_TWO).click()

    def click_button_three(self):
        button_three = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button03")))
        self.find_element(DynamicButtonsLocator.BUTTON_THREE).click()

    def verify_all_buttons_clicked_text(self):
        return self.find_element(DynamicButtonsLocator.ALL_BUTTONS_CLICKED_TEXT).text
