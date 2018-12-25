import sys
import csv
import pytest
import os
from selenium import webdriver
from allure_commons._allure import attach
from allure import attachment_type

from page_objects.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--firefox", action='store_true', default=False, help="Start Firefox WebDriver")
    parser.addoption("--chrome", action='store_true', default=False, help="Start Google Chrome WebDriver")
    parser.addoption("--input-data", action='store', help="path to file with input data")


@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    if pytest.config.getoption("--firefox"):
        request.cls.webdriver = webdriver.Firefox
        if sys.platform == 'win32':
            request.cls.webdriver_path = os.path.join("web_drivers", "windows", "geckodriver.exe")
        elif sys.platform == 'linux':
            request.cls.webdriver_path = os.path.join("web_drivers", "linux", "geckodriver")
        else:
            raise ValueError("Only Windows and Linux are supported")
    elif pytest.config.getoption("--chrome"):
        request.cls.webdriver = webdriver.Chrome
        if sys.platform == 'win32':
            request.cls.webdriver_path = os.path.join("web_drivers", "windows", "chromedriver.exe")
        elif sys.platform == 'linux':
            request.cls.webdriver_path = os.path.join("web_drivers", "linux", "chromedriver")
        else:
            raise ValueError("Only Windows and Linux are supported")
    else:
        raise ValueError("Browsers except Firefox and Chrome not allowed")


@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path)
    request.cls.main_page = MainPage(request.cls.initialized_webdriver)

    def driver_close():
        request.cls.initialized_webdriver.quit()

    request.addfinalizer(driver_close)


def pytest_generate_tests(metafunc):
    params_list = list()
    with open((pytest.config.getoption("--input-data")), 'r') as data:
        params_list = list(csv.reader(data))
    metafunc.parametrize("url, email, password, incorrect_email, incorrect_password", tuple(params_list))
