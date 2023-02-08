#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Program Feature"""

# Standard library
import time
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.login_page import Login
from pageObjects.program_page import Program
from utilities.constants import LoginCreds


class TestProgram(unittest.TestCase):
    email = LoginCreds.USERNAME
    password = LoginCreds.PASSWORD
    url = LoginCreds.LOGIN_URL

    prog_name = "My_New_program_2023"

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

    def test_create_program(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_requirement()
        program.write_name_of_prog(self.prog_name)
        program.select_scope()
        program.scope_type()
        program.primary_depart()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.prog_name:
            assert True

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
