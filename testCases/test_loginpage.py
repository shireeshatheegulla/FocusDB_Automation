import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.LoginPage import LoginPage

from utilities.readProperties import ReadConfig
import time
import json

# local_storage_file = "C:/Users/91990/PycharmProjects/python-selenium-automation/assets/localStorageData.json"


# @pytest.mark.usefixtures("add_environment")
@pytest.mark.usefixtures("driver")
class Test_001_Login:
    baseURL = "https://dev-focus.testd.com"
    # ReadConfig.getApplicationURL()

    email = "anu@testd.com"
    # ReadConfig.getuserEmail()
    password = "Cherry@12"

    # ReadConfig.getuserPassword()

    def test_login(self):
        # with open(local_storage_file, 'r') as file:
        #     local_storage_data = json.load(file)

        # Navigate to the base URL
        # self.driver.get(self.baseURL)
        #
        # # Wait for the page to load completely
        # time.sleep(2)
        #
        # # Set each item in localStorage
        # for key, value in local_storage_data.items():
        #     if isinstance(value, (dict, list)):
        #         value = json.dumps(value)
        #     self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        #
        # # Refresh the page to apply localStorage changes
        # self.driver.refresh()
        #
        # # Wait for the refreshed page to load
        # time.sleep(5)

        # self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickRecaptcha()
        self.lp.clickLogon()
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(3)
        self.lp.click_btn_Logout_yes()
        time.sleep(3)
