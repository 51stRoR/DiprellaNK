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


class UserWorkspacePage(object):
    def __init__(self, web_driver):
        self.driver = web_driver
        self.diprella_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main__wrapper")))
        self.diprella_logo = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__logo")))
        self.course_search = self.driver.find_element_by_xpath("//input[@id='search' and @type='text']")
        self.lector_menu = self.driver.find_element_by_xpath("//nav/a/span[text()='Лектор']")
        # self.notification_menu =  ???
        self.user_menu = self.driver.find_element_by_xpath("//nav/app-profile-dropdown")
        self.recommendations = self.driver.find_element_by_xpath("//section[@class='recomendations'][1]")
        self.popular = self.driver.find_element_by_xpath("//section[@class='recomendations'][2]")
