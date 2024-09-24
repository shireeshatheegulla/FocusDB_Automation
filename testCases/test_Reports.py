import pytest

from pageObject.LoginPage import LoginPage
from pageObject.Reports import Reports
import time


@pytest.mark.usefixtures("driver")
class Test_Reports_Module:
    baseURL = "https://dev-focus.testd.com"
    email = "anu+june13@testd.com"
    password = "Test@123"

    def test_Reports(self, driver):
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
        # time.sleep(25)
        self.lp.clickLogon()
        time.sleep(10)
        self.report = Reports(self.driver)
        self.report.clickReports()
        self.report.clickCampaign()
        self.report.clickExport()
        time.sleep(5)
        self.report.selectCampaignReportCheckBoxes()
        self.report.dialog_okay_btn()
        time.sleep(2)
        self.report.closeBtn()
        time.sleep(5)

        self.report.clickCase()
        time.sleep(3)
        self.report.clickExport()
        time.sleep(3)
        self.report.CaseReport()
        time.sleep(2)
        self.report.dialog_okay_btn()
        time.sleep(2)
        self.report.closeBtn()
        time.sleep(3)

        self.report.ClickAgentReport()
        self.report.clickExport()
        time.sleep(2)
        self.report.dialog_okay_btn()
        time.sleep(3)
        self.report.AgentReportCheckBoxes()
        self.report.dialog_okay_btn()
        self.report.closeBtn()

        self.driver.quit()
