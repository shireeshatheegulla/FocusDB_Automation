import pytest
from pageObject.LoginPage import LoginPage
from pageObject.CaseManager import CaseManager
import time


@pytest.mark.usefixtures("driver")
class Test_CaseManager:
    baseURL = "https://phil.testd.com/logon"
    email = "anu.d@blocmatrix.com"
    password = "test"

    firstname = "QA_case"
    lastname = "Testing"
    member_id = "9090909090"
    case_phone = "8080808080"
    case_mail = "test@test.com"
    shipping_address = "Hyderabad"
    shipping_city = "Hyderabad"
    zipcode = "50001"

    def test_Case(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        # self.lp.clickRecaptcha()
        time.sleep(25)
        self.lp.clickLogon()
        self.case = CaseManager(self.driver)
        self.case.clickCase_Manager_btn()

        # Continue with other actions
        self.case.clickOpenCasesBtn()
        self.case.clickAllCampaignsBtn()
        time.sleep(2)
        self.case.clickCampaignBox()
        self.case.clickAddNewCaseButton()
        self.case.clickCaseOriginPhone()
        self.case.setConsumer_lastname("siri")
        self.case.clickValidate_btn()
        self.case.clickOkayBtn()
        self.case.clickEligibleCheckbox()
        self.case.clickNextBtn()
        time.sleep(2)
        self.case.setCaseFirstName(self.firstname)
        self.case.setCaseLastName(self.lastname)
        self.case.setCaseMemberId(self.member_id)
        self.case.setCasePhone(self.case_phone)
        self.case.setCaseEmail(self.case_mail)
        self.case.setCaseShippingAddress(self.shipping_address)
        self.case.setCaseShippingCity(self.shipping_city)
        self.case.setCaseShippingState()
        time.sleep(1)
        self.case.setShippingState()
        self.case.setShippingZipCode(self.zipcode)
        self.case.clickShippingMailingCheckBox()

        # self.driver.execute_script("window.scrollBy(0, 4000);")
        # self.driver.execute_script("window.scrollBy(0, 4000);")
        # # self.driver.execute_script("window.scrollBy(0, -100);")
        time.sleep(10)
        self.case.clickCaseConfirmBtn()
        time.sleep(10)

        self.driver.quit()
