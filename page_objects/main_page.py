import pytest
from selenium import webdriver
from allure_commons._allure import step, attach
from allure import attachment_type
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.signin_page import SignInPage


class MainPage(object):
    def __init__(self, web_driver: WebDriver):
        self.driver = web_driver
        self.diprella_header = 0
        self.signin_link = 0

    @step("Getting url for tests and initialization of the Main page")
    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.diprella_header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main__wrapper")))
        self.signin_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__nav-link")))
        attach(
            self.driver.get_screenshot_as_png(),
            name="Main Page screenshot",
            attachment_type=attachment_type.PNG
        )
        return self

    @step("Clicking on the Signin link")
    def click_on_signin_link(self):
        self.signin_link.click()
        return SignInPage(self.driver)
