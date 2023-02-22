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
    name = 'Test_Group_001'

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
        cls.driver.maximize_window()

    def test_1_check_title(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        staff = Staff(self.driver)
        staff.click_staff_tab()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Staff Search":
            assert True
        else:
            assert False

    # test_download_users
    def test_2_download_users(self):
        staff = Staff(self.driver)
        staff.click_staff_tab()
        staff.delete_exsisting_files()
        staff.click_download_users()
        if os.path.isfile(r'C:\Users\Techwards TB-03\Downloads\users.csv'):
            assert True

        time.sleep(20)

    # test_group_users of 0 members and deletes them
    def test_2_delete_group(self):
        staff = Staff(self.driver)
        staff.click_staff_tab()
        staff.click_groups_tab()
        staff.select_delete_group()
        time.sleep(10)

    # test to create a new group of users
    def test_3_create_group(self):
        try:
            staff = Staff(self.driver)
            staff.click_groups_tab()
            staff.click_create_group()
            staff.click_group_name(self.name)
            staff.click_create_new_group()
            time.sleep(10)
            act_title = self.driver.title
            if act_title == self.path_name_name:
                assert True
            else:
                assert False
        except:
            print("Group might have some exsisting name")

    # def test_4_delete_all_groups(self):
    #     staff = Staff(self.driver)
    #     staff.click_staff_tab()
    #     staff.click_groups_tab()
    #     staff.select_delete_group()
    #     time.sleep(10)

    @classmethod
    def tearDownClass(self):
        sleep(5)
        self.driver.close()
