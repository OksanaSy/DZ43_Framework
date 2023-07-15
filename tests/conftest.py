import datetime
import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from helpers.book import Book
from helpers.project_helpers import get_browser_name, get_screenshot_directory, create_screenshots_directory
from helpers.user import User
from helpers.account import Account
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@pytest.fixture()
def driver():
    browser_name = get_browser_name()
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unknown browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    yield login_page

@pytest.fixture(scope='session')
def valid_account():
    return Account('FirstName', 'MidName', 'LastName', 'Female', '40030', 'Sumy')


@pytest.fixture(scope='session')
def valid_user():
    return User('sydoruk.ok@gmail.com', 'P2ssw0rd')


@pytest.fixture(scope='session')
def locked_out_user():
    return User('sydoruk.ok@gmail.com', 'pswd')


@pytest.fixture(scope='session', autouse=True)
def create_screenshot_directory():
    create_screenshots_directory()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # import pdb; pdb.set_trace()
        driver = item.funcargs["login_page"].driver

        file_name = f"{item.name}_{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.png"
        file_path = os.path.join(get_screenshot_directory(), file_name)
        driver.save_screenshot(file_path)


@pytest.fixture(scope='session')
def book_n():
    return Book('Python Crash Course: A Hands-On, Project-Based Introduction to Programming')
