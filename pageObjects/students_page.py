#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Staff for student related web-page"""

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

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.login_page import Login


class Students:
    students_summary = "//div[@class = 'program-result-summary']"
    print_audit_report_button = "//i[@aria-label='Print']"
    planner_tab = "//a[contains(@href,'/app/audit/plan?student_username=labernathy')]"
    side_by_side_view = "//button[contains(text(),'side-by-side view')]"
    print_plan_report = "//i[@aria-label='Print']"

    def __init__(self, driver):
        self.driver = driver
    def select_random_student(self):

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='advisee-basic']")
            )
        )
        students = self.driver.find_elements(
            By.XPATH, "//div[@class='advisee-basic']"
        )
        student = random.choice(students)
        student.click()
        time.sleep(15)

    def click_audit_report(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self.print_audit_report_button)
            )
        )
