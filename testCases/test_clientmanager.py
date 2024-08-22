import pytest
from pageObject.LoginPage import LoginPage
from pageObject.client_manager import Client_Manager
# from utilities.readProperties import ReadConfig
# from selenium.webdriver.support import expected_conditions as EC

import time
import random


@pytest.mark.usefixtures("driver")
class Test_001_Login:
    baseURL = "https://dev-focus.testd.com"
    email = "anu@testd.com"
    password = "Cherry@12"

    client_name = "QA_selenium_client_july_" + str(random.randint(1, 9999999))
    client_phone = "909090909090"
    client_address = "Hyd"
    client_email = "test@test.com"

    client_primary_firstname = "primary_firstname"
    client_primary_lastname = "primary_lastname"
    client_primary_email = "test@test.com"
    client_primary_phone = "9090909090"
    client_primary_ext = "+91"

    client_secondary_firstname = "secondary_firstname"
    client_secondary_lastname = "secondary_lastname"
    client_secondary_email = "test@test.com"
    client_secondary_phone = "9090909090"
    client_secondary_ext = "+91"

    def test_login(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        # self.lp.clickRecaptcha()
        time.sleep(25)
        self.lp.clickLogon()
        time.sleep(10)

        self.cm = Client_Manager(self.driver)

        self.cm.client_manager_dropdown()

        self.cm.client_manager_active()

        self.cm.client_manager_add_client_button()

        self.cm.setClient_name(self.client_name)
        self.cm.setClient_phone(self.client_phone)
        self.cm.setClient_address(self.client_address)
        self.cm.setClient_email(self.client_email)

        self.cm.setClient_primary_firstname(self.client_primary_firstname)
        self.cm.setClient_primary_lastname(self.client_primary_lastname)
        self.cm.setClient_primary_email(self.client_primary_email)
        self.cm.setClient_primary_phone(self.client_primary_phone)
        self.cm.setClient_primary_ext(self.client_primary_ext)

        self.cm.setClient_secondary_firstname(self.client_secondary_firstname)
        self.cm.setClient_secondary_lastname(self.client_secondary_lastname)
        self.cm.setClient_secondary_email(self.client_secondary_email)
        self.cm.setClient_secondary_phone(self.client_secondary_phone)
        self.cm.setClient_secondary_ext(self.client_secondary_ext)

        self.cm.Client_payment_terms()
        self.cm.Client_payment_terms_value()

        # self.cm.Client_logo()
        time.sleep(3)

        self.cm.Client_save_button()
        time.sleep(5)

        self.lp.clickLogout()
        time.sleep(3)
        self.lp.click_btn_Logout_yes()
        time.sleep(2)
