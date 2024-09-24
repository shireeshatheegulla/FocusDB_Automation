import time
from selenium.webdriver.common.by import By


class Reports:
    Reports_xpath = '//*[@id="side-navigation-select-item-Reports"]'
    # ******************CAMPAIGN REPORT****************************
    campaign = '//*[@id="side-navigation-select-item-Campaign"]'
    export = "//button[text()='EXPORT']"
    client_name = '//input[@name="focusclient_id.name"]'
    client_id = '//input[@name="focusclient_id._id"]'
    campaign_name = '//input[@name="name"]'
    campaign_id = '//input[@name="_id"]'
    contact_phone = '//input[@name="phone"]'
    contact_email = '//input[@name="email"]'
    assigned_agent = '//input[@name="agent_ids"]'
    Total_cases = '//input[@name="cases"]'
    Export_2 = "(//button[text()='EXPORT'])[2]"
    dialog_ok = '//button[@id="alert-dialog-okay-button"]'
    close_report = '//button[@id="dialog-close-iconbutton"]'

    # ******************** Case Report ***********************
    case_xpath = '//*[@id="side-navigation-select-item-Case"]'

    case_id = '//input[@name="_id"]'
    case_client_id = '//input[@name="campaign_id.focusclient_id"]'
    case_campaign_name = '//input[@name="campaign_id.name"]'
    case_campaign_id = '//input[@name="campaign_id._id"]'
    phone = '//input[@name="consumer_id.phone"]'
    email = '//input[@name="consumer_id.email"]'
    start_date = '//input[@name="opened_timestamp"]'
    end_state = '//input[@name="closed_timestamp"]'
    actions = '//input[@name="actions"]'

    # -------------- Agent Report ------------------------->
    agent_xpath = '//*[@id="side-navigation-select-item-Agent"]'
    last_name = '//input[@name="last_name"]'
    first_name = '//input[@name="first_name"]'
    Agent_id = '//input[@name="_id"]'
    Email = '//input[@name="email"]'
    Phone = '//input[@name="phone"]'
    agent_total_cases = '//input[@name="cases"]'
    Total_campaigns = '//input[@name="campaigns"]'
    avg_resolution_time = '//input[@name="avg_resolution"]'
    Agent_actions = '//input[@name="actions"]'

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def clickReports(self):
        self.driver.find_element(By.XPATH, self.Reports_xpath).click()
        assert "Reports" in self.driver.page_source

    def clickCampaign(self):
        self.driver.find_element(By.XPATH, self.campaign).click()
        assert "Campaign" in self.driver.page_source

    def clickExport(self):
        # wait = WebDriverWait(self, 5)
        # export = wait.until(EC.visibility_of_element_located((By.XPATH, self.export)))
        # export.click()
        self.driver.find_element(By.XPATH, self.export).click()
        assert "EXPORT" in self.driver.page_source

    def selectCampaignReportCheckBoxes(self):
        self.driver.find_element(By.XPATH, self.client_name).click()
        self.driver.find_element(By.XPATH, self.client_id).click()
        self.driver.find_element(By.XPATH, self.campaign_name).click()
        self.driver.find_element(By.XPATH, self.campaign_id).click()
        self.driver.find_element(By.XPATH, self.contact_phone).click()
        self.driver.find_element(By.XPATH, self.contact_email).click()
        self.driver.find_element(By.XPATH, self.assigned_agent).click()
        self.driver.find_element(By.XPATH, self.Total_cases).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Export_2).click()

    def dialog_okay_btn(self):
        self.driver.find_element(By.XPATH, self.dialog_ok).click()
        time.sleep(2)

    def closeBtn(self):
        self.driver.find_element(By.XPATH, self.close_report).click()
        time.sleep(5)

    def clickCase(self):
        self.driver.find_element(By.XPATH, self.case_xpath).click()
        time.sleep(5)

    def CaseReport(self):
        self.driver.find_element(By.XPATH, self.case_id).click()
        self.driver.find_element(By.XPATH, self.case_client_id).click()
        self.driver.find_element(By.XPATH, self.case_campaign_name).click()
        self.driver.find_element(By.XPATH, self.case_campaign_id).click()
        self.driver.find_element(By.XPATH, self.phone).click()
        self.driver.find_element(By.XPATH, self.email).click()
        self.driver.find_element(By.XPATH, self.start_date).click()
        self.driver.find_element(By.XPATH, self.end_state).click()
        self.driver.find_element(By.XPATH, self.actions).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Export_2).click()

    def ClickAgentReport(self):
        self.driver.find_element(By.XPATH, self.agent_xpath).click()

    def AgentReportCheckBoxes(self):
        self.driver.find_element(By.XPATH, self.last_name).click()
        self.driver.find_element(By.XPATH, self.first_name).click()
        self.driver.find_element(By.XPATH, self.Agent_id).click()
        self.driver.find_element(By.XPATH, self.Email).click()
        self.driver.find_element(By.XPATH, self.Phone).click()
        self.driver.find_element(By.XPATH, self.agent_total_cases).click()
        self.driver.find_element(By.XPATH, self.Total_campaigns).click()
        self.driver.find_element(By.XPATH, self.avg_resolution_time).click()
        self.driver.find_element(By.XPATH, self.Agent_actions).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Export_2).click()





