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
from page_objects.userworkspace_page import UserWorkspacePage


class SignInPage(object):
    def __init__(self, web_driver):
        self.driver = web_driver
        self.diprella_logo = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login__logo")))
        self.signup_link = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login__image-container-btn")))
        self.facebook_login = self.driver.find_element_by_xpath("//a[@class='social__icons-box-link facebook']")
        self.google_login = self.driver.find_element_by_xpath("//a[@class='social__icons-box-link google']")
        self.linkedin_login = self.driver.find_element_by_xpath("//a[@class='social__icons-box-link linkedin']")
        self.email_field = self.driver.find_element_by_xpath("//input[@formcontrolname='email' and @type='text']")
        self.password_field = self.driver.find_element_by_xpath(
            "//input[@formcontrolname='password' and @type='password']")
        self.signin_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.incorrect_email_message = 0
        self.incorrect_pass_message = 0

    def enter_email(self, email):
        self.email_field.send_keys(email)
        return self

    def enter_password(self, password):
        self.password_field.send_keys(password)
        return self

    def click_on_signin_button_correct_creds(self):
        self.signin_button.send_keys(Keys.ENTER)
        return UserWorkspacePage(self.driver)

    def click_on_signin_button_incorrect_email(self):
        self.signin_button.send_keys(Keys.ENTER)
        self.incorrect_email_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='error__text' and ( \
                           contains(text(), 'Not valid email') or contains(text(), 'Forbidden')\
                           )]")
            ))
        return self

    def click_on_signin_button_incorrect_pass(self):
        self.signin_button.send_keys(Keys.ENTER)
        self.incorrect_pass_message = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='error__text' and contains(text(), 'Forbidden')]")
            ))
        return self
