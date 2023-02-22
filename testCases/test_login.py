#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Login Feature"""

# Standard library
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.login_page import Login
from utilities.constants import LoginCreds


class TestLogin(unittest.TestCase):
    email = LoginCreds.USERNAME.value
    password = LoginCreds.PASSWORD.value
    url = LoginCreds.LOGIN_URL.value

    # advanced_button="//*[contains(text(), 'Continue')]"

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('ignore-certificate-errors')

        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )
        cls.driver.maximize_window()

    # test_home_page
    def test_a_web_title(self):
        driver = self.driver
        driver.get(self.url)
        act_title = self.driver.title
        if act_title == "Stellic: Academic Planning and Advising Tool":
            assert True
        else:
            assert False

    # test_login
    def test_b_check_login(self):
        driver = self.driver
        driver.get(self.url)

        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        act_title = self.driver.title
        if act_title == "Stellic: Academic Planning and Advising Tool":
            assert True
        else:
            assert False
        # Stay approx 10 secs
        sleep(10)
        # login_page.clickLogout()

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
