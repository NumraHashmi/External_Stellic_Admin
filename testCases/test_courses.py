#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Courses Feature"""

# Standard library
import os.path
import time
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.courses_page import Courses
from pageObjects.login_page import Login
from utilities.constants import LoginCreds


class TestCourses(unittest.TestCase):
    email = LoginCreds.USERNAME.value
    password = LoginCreds.PASSWORD.value
    url = LoginCreds.LOGIN_URL.value
    prog_name = "Testing New_program_2023"

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('ignore-certificate-errors')

        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_a_check_page_title(self):
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        course = Courses(self.driver)
        course.click_courses_tab()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Course Catalog":
            assert True
        else:
            assert False

    def test_b_download_past_files(self):
        course = Courses(self.driver)
        course.delete_exsisting_past_files()
        course.click_courses_tab()
        course.click_course_demand_report()
        course.select_past_course_demand_report()
        time.sleep(30)
        if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\PAST_course_demand.csv"):
            assert True
        else:
            assert False

        time.sleep(10)

    def test_c_download_current_files(self):
        course = Courses(self.driver)
        course.delete_exsisting_current_files()
        course.click_courses_tab()
        course.click_course_demand_report()
        course.select_current_course_demand_report()
        time.sleep(20)
        if os.path.isfile(
            r"C:\Users\Techwards TB-03\Downloads\CURRENT_course_demand.csv"
        ):
            assert True
        else:
            assert False
        time.sleep(10)

    def test_d_download_future_files(self):
        course = Courses(self.driver)
        course.delete_exsisting_future_files()
        course.click_course_demand_report()
        course.select_future_course_demand_report()
        time.sleep(30)
        if os.path.isfile(
            r"C:\Users\Techwards TB-03\Downloads\FUTURE_course_demand.csv"
        ):
            assert True
        else:
            assert False
        time.sleep(20)

    @classmethod
    def tearDownClass(self):
        sleep(5)
        self.driver.close()
