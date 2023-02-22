import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class Pathways:
    pathway_tab = "//a[@href='/app/pathways']"
    create_new_button = "//button[text()='Create New']"
    name_textbox = "//input[@placeholder='New Pathway Name']"
    programs_addressed = "//input[@placeholder='Search Program Name']"
    programs_list = "//li[contains(@id, 'option-0')]"
    audit_dropdown = "//select[@aria-label='select audit for Forest Resource Management [N-FRM-MF]']"
    any_option = "//option"
    create_button = "//button[contains(text(),'Create')]"

    def __init__(self, driver):
        self.driver = driver

    def click_pathways(self):
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.pathway_tab)
                )
            ).click()
            time.sleep(10)
        except TimeoutError:
            print("Timeout")

    def click_create_new(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.create_new_button)
            )
        ).click()
        time.sleep(5)

    def programs(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.programs_addressed)
            )
        ).click()
        time.sleep(10)

    def write_name_of_pathway(self, path_name):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.name_textbox)
            )
        ).send_keys(path_name)
        time.sleep(10)

    def select_prog(self):
        try:
            dropdown_scope = (
                WebDriverWait(self.driver, 10)
                .until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, self.programs_list)
                    )
                )
                .click()
            )
        except TimeoutError:
            print("Element not found")

    def select_audit(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.audit_dropdown)
                )
            ).click()
        except TimeoutError:
            print("Element not found")
        all_options = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_all_elements_located()
                (By.TAG_NAme,self.any_option))

        random_audit = random.choice(all_options).click()



    def click_create(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.create_button)
                )
            ).click()
        except TimeoutError:
            print("Time out")
