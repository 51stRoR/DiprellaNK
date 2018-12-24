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
        request.cls.webdriver_path = os.path.join("web_drivers", "geckodriver")
    elif pytest.config.getoption("--chrome"):
        request.cls.webdriver = webdriver.Chrome
        request.cls.webdriver_path = os.path.join("web_drivers", "chromedriver")
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


#### Dealing with the test failure. Taking the page screenshot ###
def pytest_exception_interact(node, call, report):
    if report.failed:
        attach(
            node.instance.initialized_webdriver.get_screenshot_as_png(),
            name="Screenshot of the Diprella page on test fail",
            attachment_type=attachment_type.PNG
        )
