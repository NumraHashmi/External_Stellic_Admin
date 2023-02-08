#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Staff Feature"""

# Standard library
import os
import time
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.login_page import Login
from pageObjects.staff_page import Staff
from utilities.constants import LoginCreds


class TestStaff(unittest.TestCase):
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
            ChromeDriverManager().install(), options=chrome_options
        )

    # test_download_users
    def test_A(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        staff = Staff(self.driver)
        staff.click_staff_tab()
        staff.delete_exsisting_files()
        staff.click_download_users()
        if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\users.csv"):
            assert True

        time.sleep(20)

    # test_group_users of 0 members and deletes them
    def test_B(self):
        staff = Staff(self.driver)
        staff.click_staff_tab()
        staff.click_groups_tab()
        staff.select_delete_group()

    # test to create a new group of users
    def test_C(self):
        staff = Staff(self.driver)
        staff.click_create_group()
        staff.click_group_name(self.group_name)
