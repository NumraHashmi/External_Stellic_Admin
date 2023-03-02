#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Program Feature"""

# Standard library
import time
import unittest
import random
import string
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
    email = LoginCreds.USERNAME.value
    password = LoginCreds.PASSWORD.value
    url = LoginCreds.LOGIN_URL.value

    prog_name = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    depart_name = "Test" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    school_name = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    uni_wide = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    prog_name_univ = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    depart_name_univ = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    school_name_univ = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
    uni_wide_univ = "Test_" + random.choice(string.ascii_lowercase) + random.choice(string.digits)
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



    def test_a_create_program(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_shared_requirement()
        program.write_name_of_prog(self.prog_name)
        program.select_scope()
        program.scope_type_program()
        program.primary_depart_prog()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.prog_name:
            assert True
        else:
            assert False
    def test_b_create_department_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_shared_requirement()
        program.write_name_of_prog(self.depart_name)
        program.select_scope()
        program.scope_type_department()
        program.primary_depart_department()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.depart_name:
            assert True
    def test_c_create_school_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_shared_requirement()
        program.write_name_of_prog(self.school_name)
        program.select_scope()
        program.scope_type_school()
        program.primary_depart_school()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.school_name:
            assert True
    def test_d_create_uni_wide_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_shared_requirement()
        program.write_name_of_prog(self.uni_wide)
        program.select_scope()
        program.scope_type_univeristy()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.uni_wide:
            assert True

    def test_e_create_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_universal_requirement()
        program.write_name_of_prog(self.prog_name_univ)
        program.select_scope()
        program.scope_type_program()
        program.primary_depart_prog()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.prog_name_univ:
            assert True
        else:
            assert False
    def test_f_create_department_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_universal_requirement()
        program.write_name_of_prog(self.depart_name_univ)
        program.select_scope()
        program.scope_type_department()
        program.primary_depart_department()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.depart_name_univ:
            assert True

    def test_g_create_school_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_universal_requirement()
        program.write_name_of_prog(self.school_name_univ)
        program.select_scope()
        program.scope_type_school()
        program.primary_depart_school()
        program.department_option()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.school_name_univ:
            assert True

    def test_h_create_uni_wide_program(self):
        driver = self.driver
        driver.get(self.url)
        program = Program(self.driver)
        program.click_programs()
        program.click_create_new()
        program.select_universal_requirement()
        program.write_name_of_prog(self.uni_wide_univ)
        program.select_scope()
        program.scope_type_univeristy()
        program.click_create()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == self.uni_wide_univ:
            assert True

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
