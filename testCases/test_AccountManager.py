import pytest
from pageObject.LoginPage import LoginPage
from pageObject.Account_Manager import Account_Manager
import time
import random


@pytest.mark.usefixtures("driver")
class Test_account_manager:
    baseURL = "https://dev-focus.testd.com"
    email = "anu+june13@testd.com"
    password = "Test@123"

    first_name = "QA_Account"
    last_name = "Testing"
    department = "testing"
    Phone_number = "9090909090"
    accEmail = "QA_selenium" + str(random.randint(1, 9999))+"@gmail.com"
    address = "hyderabad"
    city = "Hyderabad"
    zipcode = "500081"

    def test_Account(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickRecaptcha()
        self.lp.clickLogon()
        time.sleep(10)

        self.account = Account_Manager(self.driver)
        self.account.clickControlCenterBtn()
        self.account.clickAccountManagerBtn()
        self.account.clickAddAccountBtn()
        self.account.setAccountFirstName(self.first_name)
        self.account.setAccountLastName(self.last_name)
        self.account.setAccountRole()
        time.sleep(1)
        self.account.setRole()
        self.account.setAccountDepartment(self.department)
        self.account.setAccountPhoneNumber(self.Phone_number)
        self.account.setAccountEmail(self.accEmail)
        self.account.setAccountAddress(self.address)
        self.account.setAccountUnit("1")
        self.account.clickAccountState()
        time.sleep(1)
        self.account.setAccountState()
        self.account.setAccountCity(self.city)
        self.account.setAccountZipCode(self.zipcode)
        self.account.clickAccountCreateButton()
        time.sleep(5)

        self.lp.clickLogout()
        time.sleep(2)
        self.lp.click_btn_Logout_yes()
        time.sleep(2)