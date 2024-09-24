import pytest
from pageObject.LoginPage import LoginPage
from pageObject.Agent_Manager import Agent_Manager
import time
import random


@pytest.mark.usefixtures("driver")
class Test_agent_manager:
    baseURL = "https://dev-focus.testd.com"
    email = "anu+june13@testd.com"
    password = "Test@123"

    firstname = "QA_Agent"
    lastname = "Testing"
    phone = "9090909090"
    agentEmail = "QA_selenium" + str(random.randint(1, 9999)) + "@gmail.com"

    def test_Account(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        # self.lp.clickRecaptcha()
        time.sleep(25)
        self.lp.clickLogon()
        time.sleep(10)

        self.agent = Agent_Manager(self.driver)
        self.agent.clickControlCenterBtn()
        self.agent.clickAgentManagerBtn()
        self.agent.clickAddAgentBtn()
        self.agent.setAgentFirstName(self.firstname)
        self.agent.setAgentLastName(self.lastname)
        self.agent.setAgentRole("Agent (write)")
        self.agent.setAgentPhone(self.phone)
        self.agent.setAgentEmail(self.agentEmail)
        self.agent.setAgentExperience("Level 1")
        self.agent.setAgentNextBtn()
        time.sleep(3)
        self.agent.setAgentCampaign()
        self.agent.setAgentInvitation()
        self.agent.clickAgentInvitation()
        time.sleep(5)

