import pytest

from pageObject.LoginPage import LoginPage
from pageObject.Role_Manager import Role_manager
import time


@pytest.mark.usefixtures("driver")
class Test_Role_manager:
    baseURL = "https://dev-focus.testd.com"
    email = "anu@testd.com"
    password = "Cherry@12"

    role_name = "QA_selenium_role"

    def test_role_manager(self, driver):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        # self.lp.clickRecaptcha()
        time.sleep(25)
        self.lp.clickLogon()
        time.sleep(10)

        self.role = Role_manager(self.driver)
        self.role.clickControlCenterBtn()
        self.role.clickNavbarRole()
        self.role.clickAddRoleBtn()
        self.role.setRoleName(self.role_name)
        self.role.clickCreateRoleBtn()
        self.role.dragAndDropRoles()
        time.sleep(5)
        self.role.clickSaveBtn()
        time.sleep(3)




