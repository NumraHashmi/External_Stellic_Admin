#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Program for program related web-page"""

# Standard library
import time

# Third-party
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Program:
    programs_tab = "//a[@href='/app/programs']"
    create_new_button = "//button[@aria-label='create new']"
    drp_requirement = "//a[contains(text(),'Shared Requirement')]"
    name_textbox = "//input[@placeholder='New requirement name']"
    scope_dropdown = "//select[@aria-label='scope type']"
    drp_scope_type = "//option[@label='program']"
    drp_primary_department = "//input[@placeholder='Search for a Program']"
    department_xpath = "//li[contains(@id, 'option-0')]"
    create_button = "//button[contains(text(),'Create')]"

    def __init__(self, driver):
        self.driver = driver

    def click_programs(self):
        programs_button = (
            WebDriverWait(self.driver, 25)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.programs_tab)
                )
            )
            .click()
        )
        time.sleep(10)

    def click_create_new(self):
        create_new = (
            WebDriverWait(self.driver, 15)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.create_new_button)
                )
            )
            .click()
        )
        time.sleep(5)

    def select_requirement(self):
        requirement = (
            WebDriverWait(self.driver, 15)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_requirement)
                )
            )
            .click()
        )
        time.sleep(10)

    def write_name_of_prog(self, prog_name):
        name = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.name_textbox)
                )
            )
            .send_keys(prog_name)
        )
        time.sleep(10)

    def select_scope(self):
        try:
            dropdown_scope = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.scope_dropdown)
                )
            )
        except TimeoutError:
            print("Element not found")

    def scope_type(self):
        program = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_scope_type)
                )
            )
            .click()
        )
        time.sleep(10)

    def primary_depart(self):
        department = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.drp_primary_department)
                )
            )
            .click()
        )

    def department_option(self):
        bcs_core = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.department_xpath)
                )
            )
            .click()
        )
        time.sleep(10)

    def click_create(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.create_button)
                )
            ).click()
        except TimeoutError:
            print("Time out")
