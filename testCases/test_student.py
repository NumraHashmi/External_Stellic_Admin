#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Students Feature"""

# Standard library
import os
import random
import re
import time
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from pageObjects.pathwaypage import Pathways
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.login_page import Login
from pageObjects.students_page import Students


class TestStudents(unittest.TestCase):
    email = "admin"
    password = "ballroom9"
    url = "https://duke.staging.stellic.com/app/"
    path_name = "Test_pathway_2023"

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

    def test_students(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        stud = Students(self.driver)
        stud.select_random_student()
