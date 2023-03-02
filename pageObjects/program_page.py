#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Program for program related web-page"""
import random
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
    drp_requirement_shared = "//a[contains(text(),'Shared Requirement')]"
    drp_requirement_universal = "//a[contains(text(),'Universal Requirement')]"
    name_textbox = "//input[@placeholder='New requirement name']"
    scope_dropdown = "//select[@aria-label='scope type']"
    drp_scope_type_program = "//option[@label='program']"
    drp_scope_type_department = "//option[@label='department']"
    drp_scope_type_school = "//option[@label='school']"
    drp_scope_type_university_wide = "//option[@label='university-wide']"
    drp_primary_department_for_program = "//input[@placeholder='Search for a Program']"
    department_xpath = "//li[contains(@id, 'option-')]"
    drp_primary_department_for_department = "//input[@placeholder='Type department name or code']"
    drp_primary_department_for_school = "//input[@placeholder='Type school name or code']"
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

    def select_shared_requirement(self):
        requirement = (
            WebDriverWait(self.driver, 15)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_requirement_shared)
                )
            )
            .click()
        )
        time.sleep(10)

    def select_universal_requirement(self):
        requirement = (
            WebDriverWait(self.driver, 15)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_requirement_universal)
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

    def scope_type_program(self):
        program = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_scope_type_program)
                )
            )
            .click()
        )
        time.sleep(10)
    def scope_type_department(self):
        program = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_scope_type_department)
                )
            )
            .click()
        )
        time.sleep(10)
    def scope_type_school(self):
        program = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_scope_type_school)
                )
            )
            .click()
        )
        time.sleep(10)
    def scope_type_univeristy(self):
        program = (
            WebDriverWait(self.driver, 30)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.drp_scope_type_university_wide)
                )
            )
            .click()
        )
        time.sleep(10)

    def primary_depart_prog(self):
        department = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.drp_primary_department_for_program)
                )
            )
            .click()
        )

    def primary_depart_department(self):
        department = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.drp_primary_department_for_department)
                )
            )
            .click()
        )
    def primary_depart_school(self):
        department = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.drp_primary_department_for_school)
                )
            )
            .click()
        )
    def department_option(self):
        # bcs_core = (
        #     WebDriverWait(self.driver, 10)
        #     .until(
        #         expected_conditions.presence_of_element_located(
        #             (By.XPATH, self.department_xpath)
        #         )
        #     )
        #     .click()
        # )
        lst = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,self.department_xpath)
            )
        )
        random.choice(lst).click()
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
