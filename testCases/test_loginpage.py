import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.LoginPage import LoginPage

from utilities.readProperties import ReadConfig
import time


@pytest.mark.usefixtures("add_environment")
@pytest.mark.usefixtures("driver")
class Test_001_Login:
    baseURL = "https://dev-focus.testd.com"
    # ReadConfig.getApplicationURL()

    email = "anu@testd.com"
    # ReadConfig.getuserEmail()
    password = "Cherry@12"

    # ReadConfig.getuserPassword()

    def test_login(self):
        # self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(5)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        time.sleep(30)

        self.lp.clickLogon()
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(3)
        self.lp.click_btn_Logout_yes()
        time.sleep(3)
