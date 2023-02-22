#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Appointments for appointments related web-page"""
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



class Appointments:
    appointment_tab_button = "//a[@href='/app/appointments']"
    create_time_block = "//button[contains(text(), 'Create Time Block')]"
    custom_time_block = "//*[contains(text(),'Custom Time Block')]"
    next_button = "//*[contains(text(),'Next')]"

    def __init__(self, driver):
        self.driver = driver

    def click_appointment_tab(self):
        appointments = (
            WebDriverWait(self.driver, 20)
            .until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH,self.appointment_tab_button )
                )
            )
            .click()
        )


        time.sleep(10)
    def click_create_time_block(self):
        WebDriverWait(self.driver, 20).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.create_time_block)
                )
        ).click()




        time.sleep(10)
    def custom_block(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.custom_time_block)
            )
        ).click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.next_button)
            )
        ).click()

    def appointment_slot(self):
        time.sleep(15)
        start_time = "09:00"
        end_time = "15:00"

        # get the list of day elements
        days=WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, "//th[contains(@class,'fc-day-header')]"
            )))

        # iterate over the days
        for day in days:

            # only click on the days from Monday to Wednesday
            if day.text.upper() in ["MON", "TUE", "WED"]:

                day.click()

                # iterate over the time slots
                timeslots = day.find_elements(By.CLASS_NAME,"fc-axis")
                for timeslot in timeslots:
                    if timeslot.text >= start_time and timeslot.text <= end_time:
                        # click on the timeslot
                        # timeslot.click()
                        self.driver.execute_script("arguments[0].click();", timeslot)
                print("sucessfull")

