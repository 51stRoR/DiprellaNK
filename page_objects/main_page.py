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
        self.driver = web_driver
        self.diprella_header = 0
        self.signin_link = 0

    def get_mainpage_url(self, url):
        self.driver.get(url)
        self.diprella_header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main__wrapper")))
        self.signin_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,".header__nav-url")))
        return self

    def click_on_signin_link(self):
        self.signin_link.click()
        return SignInPage(self.driver)
