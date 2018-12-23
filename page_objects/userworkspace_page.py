import time
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from allure_commons._allure import step, attach
from allure import attachment_type
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains


class UserWorkspacePage(object):
    def __init__(self, web_driver):
        self.driver = web_driver
        self.diprella_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main__wrapper")))
        self.diprella_logo = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__logo")))
        self.course_search = self.driver.find_element_by_xpath("//input[@id='search' and @type='text']")
        self.recommendations = self.driver.find_element_by_xpath("//section[@class='recomendations'][1]")
        self.popular = self.driver.find_element_by_xpath("//section[@class='recomendations'][2]")
        self.lector_menu = 0
        self.user_menu = 0
        attach(
            self.driver.get_screenshot_as_png(),
            name="User workspace page screenshot",
            attachment_type=attachment_type.PNG
        )

    @step("Opening Lector menu")
    def open_lector_menu(self):
        action_chains.ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath("//nav/a/span[text()='Лектор']")
        ).click().perform()
        time.sleep(0.5)
        self.lector_menu = self.driver.find_element_by_xpath("//div[@class='lecturer__dropdown']")
        attach(
            self.driver.get_screenshot_as_png(),
            name="User workspace page with opened Lector menu",
            attachment_type=attachment_type.PNG
        )
        return self

    @step("Opening User menu")
    def open_user_menu(self):
        action_chains.ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector("a.home__header-nav-link:nth-child(2)")
        ).click().perform()
        time.sleep(0.5)
        self.user_menu = self.driver.find_element_by_xpath("//div[@class='user__dropdown']")
        attach(
            self.driver.get_screenshot_as_png(),
            name="User workspace page with opened User menu",
            attachment_type=attachment_type.PNG
        )
        return self
