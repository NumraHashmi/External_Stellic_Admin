
import time
import unittest
from time import sleep

# Third-party
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.appointments_page import Appointments
from pageObjects.login_page import Login
from utilities.constants import LoginCreds


class TestAppointment(unittest.TestCase):
    email = LoginCreds.USERNAME.value
    password = LoginCreds.PASSWORD.value
    url = LoginCreds.LOGIN_URL.value
    prog_name = "Testing New_program_2023"

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('ignore-certificate-errors')

        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    def test_a_check_page_title(self):
        login_page = Login(self.driver)
        login_page.setEmail(self.email)
        login_page.setPassword(self.password)
        login_page.clickContinue()
        appointment = Appointments(self.driver)
        appointment.click_appointment_tab()
        appointment.click_create_time_block()
        appointment.custom_block()
        appointment.appointment_slot()
        time.sleep(10)
