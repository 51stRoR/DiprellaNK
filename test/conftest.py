import csv
import pytest
import os
from selenium import webdriver

from page_objects.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--firefox", action='store_true', default=False, help="test on Firefox browser")
    parser.addoption("--chrome", action='store_true', default=False, help="Start Google Chrome WebDriver")
    parser.addoption("--input-data-path", action='store', help="path to file with input data")


@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    if pytest.config.getoption("--firefox"):
        request.cls.webdriver = webdriver.Firefox
        request.cls.webdriver_path = os.path.join("web_drivers", "geckodriver.exe")
    elif pytest.config.getoption("--chrome"):
        request.cls.webdriver = webdriver.Chrome
        request.cls.webdriver_path = os.path.join("web_drivers", "chromedriver.exe")
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
    with open((pytest.config.getoption("--input-data-path")), 'r') as data:
        params_list = list(csv.reader(data))
    metafunc.parametrize("email, password, incorrect_email, incorrect_password", tuple(params_list))
