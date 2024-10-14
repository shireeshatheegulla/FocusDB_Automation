import pytest

from pageObject.LoginPage import LoginPage
from pageObject.Campaign_Manager import Campaign_Manager
from utilities.readProperties import ReadConfig
from utilities.BaseClass import BaseClass
import time
import random


class Test_001_Campaign(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getuserEmail()
    password = ReadConfig.getuserPassword()
    campaign_name = "QA_selenium_campaign" + str(random.randint(1, 9999))
    phone_number = "9090909090"
    sla_email = "test@test.com"
    SMS_number = "9090909090"
    chat_url = "https://dev-focus.testd.com"

    Disposition_input = "test"
    Description_input = "testing description field"

    product_name = "test"
    model_number = "90909090909090"
    product_code = "890890890890890"
    product_description = "testing description"

    @pytest.mark.sanity
    def test_campaign(self, setup):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        # time.sleep(50)
        self.lp.clickRecaptcha()
        self.lp.clickLogon()

        self.campaign = Campaign_Manager(self.driver)
        time.sleep(3)

        self.campaign.campaign_manager_dropdown()

        self.campaign.campaign_manager_dropdown_active()

        self.campaign.campaign_manager_add_campaign_button()

        self.campaign.setCampaign_name(self.campaign_name)
        self.campaign.Next_button()

        self.campaign.Client_name_dropdown()
        self.campaign.setClient_name()
        self.campaign.Next_button()

        self.campaign.setService_agreement("80/30")
        self.campaign.Next_button()

        self.campaign.setCase_service_agreement("24 hours")
        self.campaign.Next_button()

        self.campaign.setCaseSLA_Phone_btn()
        self.campaign.setCaseSLA_Phone_text(self.phone_number)
        self.campaign.clickSave()

        self.campaign.setCaseSLA_email_btn()
        self.campaign.setCaseSLA_email_text(self.sla_email)
        self.campaign.clickSave()

        self.campaign.setCaseSLA_SMS_btn()
        self.campaign.setCaseSLA_SMS_text(self.SMS_number)
        self.campaign.clickSave()

        self.campaign.setCaseSLA_chat_url_btn()
        self.campaign.setCaseSLA_chat_url_text(self.chat_url)
        self.campaign.clickSave()

        self.campaign.setTimezone_checkbox()
        time.sleep(2)
        self.campaign.setOperational_hours()
        time.sleep(2)
        self.campaign.Next_button()
        time.sleep(1)

        self.campaign.setCase_Domain()
        self.campaign.setDomain()
        time.sleep(1)
        self.campaign.Next_button()
        self.campaign.clickClose_btn()
        time.sleep(1)

        self.campaign.setAssign_agent()
        time.sleep(2)
        self.campaign.Next_button()

        self.campaign.setDisposition_manual()
        self.campaign.setDisposition_textbox(self.Disposition_input)
        self.campaign.setDisposition_description(self.Description_input)
        time.sleep(1)
        self.campaign.clickNext()
        self.campaign.clickClose_btn()
        time.sleep(2)

        self.campaign.setProduct_Manual()
        self.campaign.setProduct_name(self.product_name)
        self.campaign.setModel_number(self.model_number)
        self.campaign.setProduct_code(self.product_code)
        self.campaign.setCountry()
        self.campaign.setProduct_description(self.product_description)
        time.sleep(1)
        self.campaign.clickNext()
        self.campaign.clickClose_btn()
        time.sleep(2)

        self.campaign.clickCaseLog_All_btn()
        time.sleep(1)
        self.campaign.clickNext()

        time.sleep(2)

        self.campaign.setCaseOrigin()
        time.sleep(2)

        self.campaign.clickDone_btn()
        time.sleep(5)

        self.lp.clickLogout()
        time.sleep(3)
        self.lp.click_btn_Logout_yes()
