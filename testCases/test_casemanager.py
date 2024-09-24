import pytest
from pageObject.LoginPage import LoginPage
from pageObject.CaseManager import CaseManager
import time
import warnings
import json


# from testCases.bypass_login import local_storage_data
# local_storage_file = "C:/Users/91990/PycharmProjects/python-selenium-automation/assets/localStorageData.json"


@pytest.mark.usefixtures("driver")
class Test_CaseManager:
    baseURL = "https://dev-focus.testd.com"
    email = "anu+june13@testd.com"
    password = "Test@123"

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
        self.lp.clickRecaptcha()
        # time.sleep(25)
        self.lp.clickLogon()
        #
        # Wait for the page to load completely
        # time.sleep(2)
        # with open(local_storage_file, 'r') as file:
        #     local_storage_data = json.load(file)

        # Navigate to the base URL
        # self.driver.get(self.baseURL)

        # Wait for the page to load completely
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

        # Wait for the refreshed page to load
        time.sleep(5)
        self.case = CaseManager(self.driver)
        self.case.clickCase_Manager_btn()

        # Continue with other actions
        self.case.clickOpenCasesBtn()
        self.case.clickAllCampaignsBtn()
        time.sleep(2)
        self.case.clickCampaignBox()
        time.sleep(3)
        self.case.clickAddNewCaseButton()
        time.sleep(1)
        self.case.clickCaseOriginPhone()
        time.sleep(1)
        self.case.setConsumer_lastname("siri")
        time.sleep(1)
        self.case.clickValidate_btn()
        time.sleep(1)
        self.case.clickOkayBtn()
        self.case.clickEligibleCheckbox()
        self.case.clickNextBtn()
        self.case.setCaseFirstName(self.firstname)
        time.sleep(1)
        self.case.setCaseLastName(self.lastname)
        time.sleep(1)
        self.case.setCaseMemberId(self.member_id)
        time.sleep(1)
        self.case.setCasePhone(self.case_phone)
        time.sleep(1)
        self.case.setCaseEmail(self.case_mail)
        time.sleep(1)
        self.case.setCaseShippingAddress(self.shipping_address)
        time.sleep(1)
        self.case.setCaseShippingCity(self.shipping_city)
        time.sleep(1)
        self.case.setCaseShippingState()
        time.sleep(1)
        self.case.setShippingState()
        time.sleep(1)
        self.case.setShippingZipCode(self.zipcode)
        time.sleep(1)
        self.case.clickShippingMailingCheckBox()
        time.sleep(1)
        self.case.clickCaseConfirmBtn()
        time.sleep(5)

        self.case.click_case_details_module()
        self.case.click_caseDomain_Dropdown()
        self.case.click_Safety_Domain()
        time.sleep(2)
        self.case.click_sub_domain()
        self.case.click_case_bodily_injury()
        self.case.click_case_details_submit_btn()
        self.case.IncidentDate()
        time.sleep(2)
        self.case.click_case_details_submit_btn()
        time.sleep(2)
        self.case.setIncidentLocation()
        time.sleep(2)
        self.case.click_case_details_submit_btn()
        time.sleep(2)
        self.case.setReportedDate()
        self.case.click_case_details_submit_btn()
        time.sleep(2)
        self.case.clickCaseReason()
        time.sleep(2)
        self.case.setCaseReason()
        self.case.click_case_details_submit_btn()

        self.case.setCaseXCSubject()
        self.case.setCase_XC_details()
        time.sleep(2)
        self.case.click_case_details_submit_btn()
        time.sleep(5)

        self.case.clickSymptomCode_1()
        self.case.setSymptomCode_1()
        time.sleep(3)
        self.case.clickSymptomCode_2()
        time.sleep(2)
        self.case.setSymptomCode_2()
        time.sleep(3)
        self.case.clickSymptomCode_3()
        self.case.setSymptomCode_3()
        time.sleep(2)
        self.case.click_case_details_submit_btn()
        time.sleep(10)

        self.case.clickCaseProduct()
        time.sleep(2)
        self.case.clickCaseProductActionIcon()
        self.case.setProductSerialNumber()
        self.case.setProductPurchaseDate()
        time.sleep(2)
        self.case.setProductReceivedDate()
        time.sleep(2)
        self.case.clickProductConfirmBtn()
        time.sleep(10)

        self.case.clickCaseNotes()
        self.case.setCaseNotesTitle()
        self.case.setCaseNotes()
        time.sleep(2)
        self.case.caseNotesEmailCheckBox()
        time.sleep(1)
        self.case.caseNotesSMSCheckBOX()
        time.sleep(1)
        self.case.sendAttachmentXpath()
        self.case.caseNotesCloseBtn()
        time.sleep(10)

        self.case.setCaseReturns()
        self.case.Return_type()
        self.case.clickReturnReason("Wrong product")
        self.case.GenerateRMA()
        self.case.ReturnExpected("Consumer confirmed product return")
        self.case.clickReturnNextBtn()
        self.case.generateShippingLabel()
        time.sleep(3)
        self.case.clickReturnNextBtn()
        time.sleep(3)
        self.case.wasReplacementOrdered("Yes")
        time.sleep(2)
        self.case.OrderConfirmationNum()

        time.sleep(5)

        self.case.caseActivityLog()
        self.case.clickNewActivity()
        self.case.clickNewActivityType()
        self.case.setActivityDescription()
        self.case.clickDialogueSaveBtn()
        time.sleep(5)

        self.case.clickCaseEscalationTab()
        self.case.CaseEscalationAssignToAgent()
        self.case.setCaseEscalationReason()
        self.case.CaseSeverityLevel('Low')
        self.case.CaseEscalationSendBtn()
        self.case.CaseEscalationYesBtn()
        self.case.CaseEscalationSuccessDialogueCloseBtn()
        time.sleep(5)

        self.case.clickCaseTasksTab()
        self.case.clickCategory()
        self.case.clickCategoryZero()
        self.case.setCaseTasksNotes()
        self.case.clickTaskAssignToAgent()
        self.case.clickAssignTaskBtn()
        time.sleep(5)

        self.case.ClickCaseRemindersTab()
        self.case.ClickReminderCategory()
        self.case.clickReminderCategoryZero()
        self.case.clickReminderDueDateCalender()
        self.case.CaseReminderNotes()
        self.case.setReminderFrequency('Hourly')
        self.case.ReminderAssignToAgent()
        self.case.clickActiveBtn()
        self.case.clickClose()
        time.sleep(5)

        self.case.clickInsurance()
        self.case.setFirstName()
        self.case.setLastName()
        self.case.setCarrier()
        self.case.setBinNumber()
        self.case.setPolicyNumber()
        self.case.setDOB()
        self.case.setEffectiveDate()
        # self.case.UploadInsuranceCardFrontImage()
        # self.case.UploadInsuranceCardBackImage()
        self.case.ClickInsuranceSaveBtn()

        time.sleep(5)

        self.case.clickDisposition()
        self.case.setDisposition("Closed")

        time.sleep(5)

        self.driver.quit()
