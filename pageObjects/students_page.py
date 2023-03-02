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
    planner_tab = "//a[contains(@href, '/app/audit/plan?')]"
    side_by_side_view = "//a[contains(text(),'side-by-side view')]"
    create_plan_report = "//button[contains(text(),'Create plan report')]"
    print_plan_report = "//i[@aria-label='Print']"
    create_audit_report_button = "//button[contains(text(),'Create audit report')]"
    planned = "//button[contains(text(),'Planned')]"
    format_drpdown = "//select[@aria-label='format']"
    compact = "//option[@label='Compact']"
    download_button_student_plan = "//button[@aria-label='Print Plan Report']"
    all_students_emails_name = "//a[@aria-label='Export name and email of all the students into csv']"
    export_button = "//button[contains(text(),'Export')]"
    print_all_students_report = "//a[@aria-label='Generate audit reports for all these students']"
    student_name = ""

    def __init__(self, driver):
        self.driver = driver

    def click_download_button(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.all_students_emails_name)
            )
        ).click()
    def delete_exsisting_all_studnets_emails_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        files = []
        for f in os.listdir(folder):
            if f.startswith('students') and f.endswith('csv'):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
                else:
                    pass

    def click_export(self):
         WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.export_button)
            )
        ).click()
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
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.print_audit_report_button)
            )
        ).click()
    def select_format(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.format_drpdown)
            )
        ).cl
    def select_compact(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.compact)
            )
        ).click()
    def select_planned(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.planned)
            )
        ).click()


    def click_create_audit_report(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.create_audit_report_button)
            )
        ).click()

    time.sleep(10)

    def get_student_name(self):
       stud_elem = [a.text for a in WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='guide-h1 color-gray100 h500']")))
                     if a.text]
       if stud_elem:
           stud_elem=stud_elem.pop()
           if '\n' in stud_elem:
               self.student_name = stud_elem.split('\n')[0]
       print(self.student_name)
       stud = self.student_name.replace(' ','_')

    def click_print_all_students_report(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.print_all_students_report)
            )
        ).click()
    def click_planner(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.planner_tab)
            )
        ).click()
    def click_sidebyside_view(self):
        # planer_tab = WebDriverWait(self.driver, 30).until(
        #     expected_conditions.element_to_be_clickable(
        #         (By.XPATH, "//div[contains(text(),'Planner')]"
        #          )))
        # webdriver.execute_script("arguments[0].scrollIntoView();", planer_tab)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.side_by_side_view)
            )
        ).click()

    def click_download_button_individual_plan(self):
         planer_tab=WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self. download_button_student_plan)
            )).click()
         # self.execute_script("arguments[0].scrollIntoView();",planer_tab)
    def click_create_plan_report(self):
        students = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.create_plan_report)
            )
        ).click()
    time.sleep(10)
    def delete_exsisting_studnet_plan_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        files = []
        for f in os.listdir(folder):
            if f.startswith("Student_plan"):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass
    def delete_exsisting_studnet_audit_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        files = []
        for f in os.listdir(folder):
            if f.startswith("Student_audit"):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass

