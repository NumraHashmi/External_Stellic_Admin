#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Login for login related web-page"""

# Third-party
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    textbox_email_xpath = "//input[@placeholder='email id']"
    textbox_password_xpath = "//input[@placeholder='password']"

    button_continue_txt = '//button[contains(text(), Continue)]'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        email_textbox = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.textbox_email_xpath)
            )
        )
        email_textbox.send_keys(email)

    def setPassword(self, password):
        password_textbox = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.textbox_password_xpath)
            )
        )
        password_textbox.send_keys(password)

    def clickContinue(self):
        login_button = (
            WebDriverWait(self.driver, 10)
            .until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.button_continue_txt)
                )
            )
            .click()
        )

    def clickLogout(self):
        print("hi")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//button[id="basic-button"]')
            )
        ).click()
        logout_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.button_logout_text_sign_out)
            )
        )
        logout_button.click()
