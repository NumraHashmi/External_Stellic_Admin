#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines class Staff for staff related web-page"""

# Third-party
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Staff:
    staff_tab_xpath = "//a[@href='/app/staff']"
    download_users_xpath = (
        "//a[@aria-label='Export name and email of all the users into csv']"
    )
    groups_tab = "//a[contains(text(),'Groups')]"
    delete_group_xpath = "//button[contains(text(), 'delete group')]"
    ok_button_xpath = "//button[contains(text(), 'OK')]"
    create_group_button = "//button[contains(text(),'Create new group')]"
    group_name_placeholder = "//select[@aria-label='new group name']"

    def __init__(self, driver):
        self.driver = driver

    def click_staff_tab(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.staff_tab_xpath)
            )
        ).click()

    def click_download_users(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.download_users_xpath)
            )
        ).click()

    def delete_exsisting_files(self):
        # Standard library
        import os

        folder = r"C:\Users\Techwards TB-03\Downloads"
        for f in os.listdir(folder):
            if f.startswith('users') and f.endswith('.csv'):
                path_f = os.path.join(folder, f)
                os.remove(path_f)
                if not os.path.exists(f):
                    print("Deleted successfully")
            else:
                pass

    def click_groups_tab(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.groups_tab))
        ).click()

    def select_delete_group(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_all_elements_located(
                (By.TAG_NAME, "user-info")
            )
        )
        users = self.driver.find_elements(By.TAG_NAME, "user-info")
        for members in users:
            m = members.find_element(By.TAG_NAME, "a")
            if '0 members' in m.text.strip():
                m.click()
                WebDriverWait(self.driver, 20).until(
                    expected_conditions.element_to_be_clickable(
                        (By.XPATH, self.delete_group_xpath)
                    )
                ).click()
                WebDriverWait(self.driver, 20).until(
                    expected_conditions.element_to_be_clickable(
                        (By.XPATH, self.ok_button_xpath)
                    )
                ).click()

                break

    def click_create_group(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.create_group_button)
            )
        ).click()

    def click_group_name(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.group_name_placeholder)
            )
        ).sendkeys()
