import pytest

from pageObject.LoginPage import LoginPage
from pageObject.Role_Manager import Role_manager
import time
import json

# local_storage_file = "C:/Users/91990/PycharmProjects/python-selenium-automation/assets/localStorageData.json"


@pytest.mark.usefixtures("driver")
class Test_Role_manager:
    baseURL = "https://dev-focus.testd.com"
    email = "anu+june13@testd.com"
    password = "Test@123"

    role_name = "QA_selenium_role"

    def test_role_manager(self, driver):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        #
        # with open(local_storage_file, 'r') as file:
        #     local_storage_data = json.load(file)

        self.driver.get(self.baseURL)

        # Wait for the page to load completely
        time.sleep(2)

        # Set each item in localStorage
        # for key, value in local_storage_data.items():
        #     if isinstance(value, (dict, list)):
        #         value = json.dumps(value)
        #     self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        #
        # # Refresh the page to apply localStorage changes
        # self.driver.refresh()

        # Wait for the refreshed page to load
        # time.sleep(5)

        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickRecaptcha()

        # self.lp.clickRecaptcha()
        # time.sleep(25)
        self.lp.clickLogon()
        time.sleep(10)

        self.role = Role_manager(self.driver)
        self.role.clickControlCenterBtn()
        self.role.clickNavbarRole()
        self.role.clickAddRoleBtn()
        self.role.setRoleName(self.role_name)
        self.role.clickCreateRoleBtn()
        time.sleep(2)
        self.role.dragAndDropRoles()
        time.sleep(5)
        self.role.clickSaveBtn()
        time.sleep(3)
