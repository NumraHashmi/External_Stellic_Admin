#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Defines tests related to Students Feature"""
import glob
# Standard library
import os
import random
import re
import time
from datetime import date
from datetime import datetime
import unittest
import requests
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
    url = "https://duke.py3.tw.qa.stellic.com"
    path_name = "pathway_2023"

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
    def test_a_All_students_email(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        stud = Students(self.driver)
        stud.delete_exsisting_all_studnets_files()
        stud.click_download_button()
        stud.click_export()
        self.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(75)
        if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\students.csv"):
            assert True
        else:
            assert False
    def test_b_All_students_audit_standard_planned(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        stud = Students(self.driver)
        stud.delete_exsisting_studnet_audit_files()
        stud.click_print_all_students_report()
        stud.select_planned()
        # self.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        stud.click_create_audit_report()
        time.sleep(760)
        today = date.today()
        file_date = today.strftime("%m-%d-%y")
        folder = r"C:\Users\Techwards TB-03\Downloads"
        file_name = str('Student_audit' + '_' + file_date)
        print(file_name)
        for f in os.listdir(folder):
            if f.startswith(file_name):
                path_f = os.path.join(folder, f)
                if os.path.isfile(path_f):
                    assert True
                    os.remove(path_f)
                    if not os.path.exists(f):
                        print("Deleted successfully")
                    else:
                        pass
                else:
                    assert False
    # def test_c_All_students_audit_standard_official(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.delete_exsisting_all_studnets_files()
    #     stud.click_print_all_students_report()
    #     stud.click_audit_report()
    #     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    #     time.sleep(120)
    #     if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\"):
    #         assert True
    #     else:
    #         assert False
    # def test_d_All_students_audit_compact_planned(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.delete_exsisting_all_studnets_files()
    #     stud.click_print_all_students_report()
    #     stud.select_compact()
    #     stud.select_planned()
    #     stud.click_audit_report()
    #     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    #     time.sleep()
    #     if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\students.csv"):
    #         assert True
    #     else:
    #         assert False
    # def test_e_All_students_audit_compact_official(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.delete_exsisting_all_studnets_files()
    #     stud.select_compact()
    #     stud.click_print_all_students_report()
    #     stud.click_audit_report()
    #     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    #     time.sleep(120)
    #     if os.path.isfile(r"C:\Users\Techwards TB-03\Downloads\students.csv"):
    #         assert True
    #     else:
    #         assert False



    # def test_f_Individual_students_audit_standard_planned(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.select_random_student()
    #     time.sleep(5)
    #     stud.get_student_name()
    #     stud.click_audit_report()
    #     stud.select_planned()
    #     stud.click_create_audit_report()
    #     time.sleep(10)
    #     print(stud.student_name)
    #     student_name_for_report = stud.student_name.replace(" ", "_")
    #     print(student_name_for_report)
    #     today = date.today()
    #     file_date = today.strftime("%m-%d-%Y")
    #     folder = r"C:\Users\Techwards TB-03\Downloads"
    #     file_name=str(student_name_for_report+'_audit_'+ file_date)
    #     print(file_name)
    #     # file_name_path = os.path.join(folder,file_name)
    #     # print(file_name_path)
    #     for f in os.listdir(folder):
    #         if f.startswith(file_name):
    #             path_f = os.path.join(folder,f )
    #             if os.path.isfile(path_f):
    #                 os.remove(path_f)
    #                 if not os.path.exists(f):
    #                     print("Deleted successfully")
    #                 else:
    #                     pass
    #             else:
    #                 assert False
    #
    #
    #
    # def test_g_Individual_students_audit_standard_official(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.select_random_student()
    #     time.sleep(10)
    #     stud.get_student_name()
    #     stud.click_audit_report()
    #     stud.click_create_audit_report()
    #     time.sleep(10)
    #     print(stud.student_name)
    #     student_name_for_report = stud.student_name.replace(" ", "_")
    #     print(student_name_for_report)
    #     today = date.today()
    #     file_date = today.strftime("%m-%d-%y")
    #     folder = r"C:\Users\Techwards TB-03\Downloads"
    #     downloads_folder = os.path.expanduser("~\Downloads")
    #     os.chdir(downloads_folder)
    #     files = sorted(glob.glob("*.pdf"), key=os.path.getctime, reverse=True)
    #     for f in files:
    #         if f.startswith(student_name_for_report) and f.endswith(file_date):
    #             path_f = os.path.join(folder, f)
    #             print(path_f)
    #         else:
    #             print('Failed')
    #
    # def test_h_Individual_students_audit_compact_planned(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.select_random_student()
    #     time.sleep(10)
    #     stud.get_student_name()
    #     stud.click_audit_report()
    #     stud.select_planned()
    #     stud.select_compact()
    #     stud.click_create_audit_report()
    #     time.sleep(10)
    #     print(stud.student_name)
    #     student_name_for_report = stud.student_name.replace(" ", "_")
    #     print(student_name_for_report)
    #     today = date.today()
    #     file_date = today.strftime("%m-%d-%y")
    #     folder = r"C:\Users\Techwards TB-03\Downloads"
    #     downloads_folder = os.path.expanduser("~\Downloads")
    #     os.chdir(downloads_folder)
    #     files = sorted(glob.glob("*.pdf"), key=os.path.getctime, reverse=True)
    #     for f in files:
    #         if f.startswith(student_name_for_report) and f.endswith(file_date):
    #             path_f = os.path.join(folder, f)
    #             print(path_f)
    #         else:
    #             print('Failed')
    # def test_i_Individual_students_audit_compact_official(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     login_page = Login(self.driver)
    #     login_page.setEmail(self.email)
    #     login_page.setPassword(self.password)
    #     login_page.clickContinue()
    #     stud = Students(self.driver)
    #     stud.select_random_student()
    #     time.sleep(10)
    #     stud.get_student_name()
    #     stud.click_audit_report()
    #     stud.select_compact()
    #     stud.click_create_audit_report()
    #     time.sleep(10)
    #     print(stud.student_name)
    #     student_name_for_report = stud.student_name.replace(" ", "_")
    #     print(student_name_for_report)
    #     today = date.today()
    #     file_date = today.strftime("%m-%d-%Y")
    #     downloads_folder = os.path.expanduser("~\Downloads")
    #     os.chdir(downloads_folder)
    #     files = sorted(glob.glob("*"), key=os.path.getctime, reverse=True)
    #     latest_file = files[0]
    #
    #     if latest_file.split(".")[0] == student_name_for_report :
    #             assert True
    #             path_f = os.path.join(downloads_folder, latest_file)
    #             os.remove(path_f)
    #             if not os.path.exists(path_f):
    #                 print("Deleted successfully")
    #             else:
    #                 pass
    #     else:
    #         assert False

    def test_j_Individual_student_plan(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        stud = Students(self.driver)
        stud.select_random_student()
        time.sleep(10)
        stud.delete_exsisting_studnet_plan_files()
        time.sleep(5)
        stud.click_planner()
        stud.click_sidebyside_view()
        stud.click_download_button_individual_plan()
        stud.click_create_plan_report()
        time.sleep(10)
        today = date.today()
        file_date = today.strftime("%m-%d-%y")
        folder = r"C:\Users\Techwards TB-03\Downloads"
        file_name=str('Student_plan'+'_'+ file_date)
        print(file_name)
        for f in os.listdir(folder):
                if f.startswith(file_name):
                    path_f = os.path.join(folder,f )
                    if os.path.isfile(path_f):
                        assert True
                        os.remove(path_f)
                        if not os.path.exists(f):
                            print("Deleted successfully")
                        else:
                            pass
                    else:
                        assert False


    @classmethod
    def tearDownClass(self):
        sleep(5)
        self.driver.close()
