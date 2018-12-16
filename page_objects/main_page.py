import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from page_objects.signin_page import SignInPage


class MainPage(object):
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.driver = web_driver
        self.driver.get("https://demo.diprella.com")

        # Instantiating web elements
        self.diprella_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main__wrapper")))
        self.signin_link = self.driver.find_element_by_css_selector(".header__nav-link")

    def click_on_signin_link(self):
        self.signin_link.click()
        return SignInPage(self.driver)
