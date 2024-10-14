import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Agent_Manager:
    control_center_btn_xpath = "//span[text()='Control Center']"
    agent_btn_xpath = "//a[@id='side-navigation-select-item-Agent Manager']"
    add_agent_btn_xpath = "//button[@id='agent-manager-add-button']"
    agent_first_name_xpath = "//input[@name='first_name']"
    agent_last_name_xpath = "//input[@name='last_name']"
    agent_role_xpath = "//div[@id='mui-component-select-role_id']"
    agent_role_write_xpath = "//li[text()='Agent (write)']"
    agent_role_read_xpath = "//li[text()='Agent (read-only)']"
    agent_phone_xpath = "//input[@name='phone']"
    agent_email_xpath = "//input[@name='email']"
    agent_experience_xpath = "//div[@id='mui-component-select-experience_level']"
    agent_level1_xpath = "//li[text()='Level 1']"
    agent_level2_xpath = "//li[text()='Level 1']"
    agent_level3_xpath = "//li[text()='Level 1']"
    agent_next_btn_xpath = "//button[text()='NEXT']"
    assign_campaign_xpath = "//input[@name='accessToCampaigns']"
    agent_email_checkbox_xpath = "//p[text()='EMAIL']"
    agent_SMS_checkbox_xpath = "//p[text()='TEXT SMS']"
    agent_invitation_xpath = "//button[@id='agent-add-submit-button']"

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def clickControlCenterBtn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.control_center_btn_xpath))).click()

    def clickAgentManagerBtn(self):
        self.driver.find_element(By.XPATH, self.agent_btn_xpath).click()

    def clickAddAgentBtn(self):
        self.driver.find_element(By.XPATH, self.add_agent_btn_xpath).click()

    def setAgentFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.agent_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.agent_first_name_xpath).send_keys(firstname)

    def setAgentLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.agent_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.agent_last_name_xpath).send_keys(lastname)

    def setAgentRole(self, role=None):
        self.driver.find_element(By.XPATH, self.agent_role_xpath).click()
        if role == "Agent (write)":
            list_item = self.driver.find_element(By.XPATH, self.agent_role_write_xpath)
        # elif value == "Agent (read-only)":
        #     self.list_item = self.driver.find_element(By.XPATH, self.case_service_48H_xpath)
        else:
            list_item = self.driver.find_element(By.XPATH, self.agent_role_read_xpath)
        time.sleep(1)
        list_item.click()

    def setAgentPhone(self, phone):
        self.driver.find_element(By.XPATH, self.agent_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.agent_phone_xpath).send_keys(phone)

    def setAgentEmail(self, email):
        self.driver.find_element(By.XPATH, self.agent_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.agent_email_xpath).send_keys(email)

    def setAgentExperience(self, experience=None):
        self.driver.find_element(By.XPATH, self.agent_experience_xpath).click()
        time.sleep(1)
        if experience == "Level 1":
            experience_level = self.driver.find_element(By.XPATH, self.agent_level1_xpath)
        elif experience == "Level 2":
            experience_level = self.driver.find_element(By.XPATH, self.agent_level2_xpath)
        elif experience == "Level 3":
            experience_level = self.driver.find_element(By.XPATH, self.agent_level3_xpath)
        else:
            experience_level = self.driver.find_element(By.XPATH, self.agent_level1_xpath)
        time.sleep(1)
        experience_level.click()

    def setAgentNextBtn(self):
        self.driver.find_element(By.XPATH, self.agent_next_btn_xpath).click()

    def setAgentCampaign(self):
        self.driver.find_element(By.XPATH, self.assign_campaign_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.assign_campaign_xpath).send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    def setAgentInvitation(self):
        self.driver.find_element(By.XPATH, self.agent_SMS_checkbox_xpath).click()
        self.driver.find_element(By.XPATH, self.agent_email_checkbox_xpath).click()

    def clickAgentInvitation(self):
        self.driver.find_element(By.XPATH, self.agent_invitation_xpath).click()