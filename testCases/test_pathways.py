<<<<<<< Updated upstream
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from pageObjects.login_page import Login
from pageObjects.pathways_page import Pathways
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testpathways(unittest.TestCase):

    email = "admin"
    password = "ballroom9"
    url = "https://duke.staging.stellic.com/app/"
    path_name="Test_pathway_2023"
    # advanced_button="//*[contains(text(), 'Continue')]"

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('ignore-certificate-errors')

        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    def test_create_pathway(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        pathway = Pathways(self.driver)
        pathway.click_pathways()
        pathway.click_create_new()
        pathway.write_name_of_pathway(self.path_name)
        pathway.programs()
        pathway.select_prog()
        pathway.click_create()
        act_title = self.driver.title
        if act_title == self.path_name_name:
            assert True
        else:
            assert False


    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
=======
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from pageObjects.login_page import Login
from pageObjects.pathways_page import Pathways
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPathways(unittest.TestCase):
    email = "admin"
    password = "ballroom9"
    url = "https://duke.staging.stellic.com/app/"
    path_name = "Test_Pathway_002"
    # advanced_button="//*[contains(text(), 'Continue')]"

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

    def test_a_navigate_to_pathways(self):
        driver = self.driver
        driver.get(self.url)
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        pathway = Pathways(self.driver)
        pathway.click_pathways()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Pathway Catalog":
            assert True
        else:
            assert False

    def test_b_create_pathway(self):
        pathway = Pathways(self.driver)
        pathway.click_pathways()
        pathway.click_create_new()
        pathway.write_name_of_pathway(self.path_name)
        pathway.programs()
        pathway.select_prog()
        pathway.select_audit()
        pathway.click_create()
        act_title = self.driver.title
        if act_title == self.path_name_name:
            assert True
        else:
            assert False

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
>>>>>>> Stashed changes
