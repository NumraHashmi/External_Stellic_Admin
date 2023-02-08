#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Courses for course related web-page"""

# Standard library
import os
import re
import time

# Third-party
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Courses:
    courses_tab_button = "//a[@href='/app/courses']"
    course_demand_report_button = "//button[@class='standard-btn dropdown-toggle']"
    past_course_report_option = "//div[contains(text(),'Past courses')]"
    future_course_report_option = "//div[contains(text(),'Future courses')]"
    current_course_report_option = "//div[contains(text(),'Current courses')]"

    def __init__(self, driver):
        self.driver = driver

    def click_courses_tab(self):
        courses = (
            WebDriverWait(self.driver, 20)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.courses_tab_button)
                )
            )
            .click()
        )

        print('courses tab: ', courses)

        time.sleep(10)

    def click_course_demand_report(self):
        course_demand_report = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.course_demand_report_button)
                )
            )
            .click()
        )
        time.sleep(10)

    def select_past_course_demand_report(self):
        course_demand_report = (
            WebDriverWait(self.driver, 20)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.past_course_report_option)
                )
            )
            .click()
        )
        time.sleep(10)

    def select_future_course_demand_report(self):
        course_demand_report = (
            WebDriverWait(self.driver, 20)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.future_course_report_option)
                )
            )
            .click()
        )
        time.sleep(10)

    def select_current_course_demand_report(self):
        course_demand_report = (
            WebDriverWait(self.driver, 20)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.current_course_report_option)
                )
            )
            .click()
        )
        time.sleep(10)

    def delete_exsisting_past_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        files = []
        for f in os.listdir(folder):
            if f.startswith('PAST'):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass

    def delete_exsisting_current_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        for f in os.listdir(folder):
            if f.startswith('CURRENT'):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass

    def delete_exsisting_future_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        for f in os.listdir(folder):
            if f.startswith('FUTURE'):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass
