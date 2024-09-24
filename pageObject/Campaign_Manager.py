import time

from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Campaign_Manager:
    campaign_Manager_xpath = "//*[text()='Campaign Manager']"
    campaign_Manager_active_campaign_xpath = "//*[@id='side-navigation-select-item-Active']/div/span"
    campaign_manager_add_campaign_button_id = "campaign-manager-add-button"

    campaign_name_xpath = '//input[@name="name"]'
    campaign_name_next_button_xpath = "//*[@id='campaign-add-submit-form']/div[2]/div[3]/button[2]"
    campaign_Client_field_xpath = "//input[@name='temp_client']"

    agent_agreement_xpath = "//p[text()='Choose Service Level Agreement']"
    agent_agreement_8030_xpath = "//li[contains(text(),'80/30')]"
    agent_agreement_8020_xpath = "//li[contains(text(),'80/20')]"
    agent_agreement_9010_xpath = "//li[contains(text(),'90/10')]"

    case_service_xpath = "//p[text()='Choose Case Service Level Agreement']"
    case_service_24H_xpath = "//li[contains(text(),'24 hours')]"
    case_service_48H_xpath = "//li[contains(text(),'48 hours')]"
    case_service_72H_xpath = "//li[contains(text(),'72 hours')]"
    case_service_1week_xpath = "//li[contains(text(),'1 week')]"
    case_service_2week_xpath = "//li[contains(text(),'2 week')]"

    case_SLA_phone_btn_xpath = "//p[contains(text(),'phone number')]"
    case_SLA_Phone_text_xpath = "//input[@name='phone']"
    Case_SLA_save_btn_xpath = "//button[@id='campaign-operations-save-button']"

    case_SLA_email_btn_xpath = "//p[contains(text(),'email address')]"
    case_SLA_email_text_xpath = "//input[@name='email']"

    case_SLA_SMS_btn_xpath = "//p[contains(text(),'SMS number')]"
    case_SLA_SMS_text_xpath = "//input[@name='sms_number']"

    case_SLA_chat_url_xpath = "//p[contains(text(),'chat url address')]"
    case_SLA_chat_url_text_xpath = "//input[@name='chat_url']"

    case_SLA_eastern_checkbox_xpath = "//span[text()='Eastern']"
    case_SLA_central_checkbox_xpath = "//span[text()='Central']"
    case_SLA_mountain_checkbox_xpath = "//span[text()='Mountain']"
    case_SLA_pacific_checkbox_xpath = "//span[text()='Pacific']"

    case_SLA_Monday_Ios_btn_xpath = "(//input[@type='checkbox'])[1]"

    case_domain_manual_xpath = "//p[text()='Manual']"
    case_domain_input_xpath = "//input[@name='selectedCampaign']"
    case_domain_close_btn_xpath = "//button[contains(text(),'CLOSE')]"

    disposition_Manual_btn_xpath = "//p[text()='Manual']"
    disposition_textbox_xpath = "//input[@name='disposition']"
    disposition_description_box_xpath = "//textarea[@name='description']"
    disposition_Next_button = "//button[text()='NEXT']"

    product_manual = "//p[contains(text(),'Manual')]"
    product_name = "//input[@name='name']"
    model_number = "//input[@name='model_number']"
    product_code = "//input[@name='product_code']"
    product_description = "//input[@name='description']"
    product_country = "//input[@name='temp_country']"

    case_add_all_btn = "//button[@id='case-log-add-all']"
    Done_btn = "//button[text()='DONE']"

    def __init__(self, driver):
        self.case_origin_drop = None
        self.case_origin_drag = None
        self.country = None
        self.target_element = None
        self.source_element = None
        self.actions = None
        self.element = None
        self.Safety_domain = None
        self.switch = None
        self.list_item = None
        self.a_list = None
        self.driver = driver
        driver.maximize_window()

    def campaign_manager_dropdown(self):
        self.driver.find_element(By.XPATH, self.campaign_Manager_xpath).click()

        # Wait for the dropdown options to be visible (adjust the XPath as needed)
        wait = WebDriverWait(self.driver, 5)
        options_visible = wait.until(
            EC.visibility_of_element_located((By.XPATH, "YOUR_OPTIONS_XPATH")))  # Replace with actual XPath

        # Assert that the options are visible
        assert options_visible.is_displayed(), "Dropdown options are not visible!"

    def campaign_manager_dropdown_active(self):
        self.driver.find_element(By.XPATH, self.campaign_Manager_active_campaign_xpath).click()

    def campaign_manager_add_campaign_button(self):
        self.driver.find_element(By.ID, self.campaign_manager_add_campaign_button_id).click()

    def setCampaign_name(self, campaign_name):
        self.driver.find_element(By.XPATH, self.campaign_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.campaign_name_xpath).send_keys(campaign_name)

    def Next_button(self):
        self.driver.find_element(By.XPATH, self.campaign_name_next_button_xpath).click()

    def Client_name_dropdown(self):
        self.driver.find_element(By.XPATH, self.campaign_Client_field_xpath).click()

    def setClient_name(self):
        self.driver.find_element(By.XPATH, self.campaign_Client_field_xpath).send_keys(Keys.ARROW_UP, Keys.ENTER)

    def setService_agreement(self, value):
        self.driver.find_element(By.XPATH, self.agent_agreement_xpath).click()
        time.sleep(1)
        if value == "80/30":
            self.a_list = self.driver.find_element(By.XPATH, self.agent_agreement_8030_xpath)
        elif value == "80/20":
            self.a_list = self.driver.find_element(By.XPATH, self.agent_agreement_8020_xpath)
        elif value == "90/10":
            self.a_list = self.driver.find_element(By.XPATH, self.agent_agreement_9010_xpath)
        else:
            self.a_list = self.driver.find_element(By.XPATH, self.agent_agreement_8030_xpath)
        time.sleep(1)
        self.a_list.click()

    def setCase_service_agreement(self, value):
        self.driver.find_element(By.XPATH, self.case_service_xpath).click()
        time.sleep(1)
        if value == "24 hours":
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_24H_xpath)
        elif value == "48 hours":
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_48H_xpath)
        elif value == "72 hours":
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_72H_xpath)
        elif value == "1 week":
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_1week_xpath)
        elif value == "2 week":
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_2week_xpath)
        else:
            self.list_item = self.driver.find_element(By.XPATH, self.case_service_24H_xpath)
        time.sleep(1)
        self.list_item.click()

    def setCaseSLA_Phone_btn(self):
        self.driver.find_element(By.XPATH, self.case_SLA_phone_btn_xpath).click()

    def setCaseSLA_Phone_text(self, phone_number):
        self.driver.find_element(By.XPATH, self.case_SLA_Phone_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_SLA_Phone_text_xpath).send_keys(phone_number)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.Case_SLA_save_btn_xpath).click()

    def setCaseSLA_email_btn(self):
        self.driver.find_element(By.XPATH, self.case_SLA_email_btn_xpath).click()

    def setCaseSLA_email_text(self, sla_email):
        self.driver.find_element(By.XPATH, self.case_SLA_email_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_SLA_email_text_xpath).send_keys(sla_email)

    def setCaseSLA_SMS_btn(self):
        self.driver.find_element(By.XPATH, self.case_SLA_SMS_btn_xpath).click()

    def setCaseSLA_SMS_text(self, SMS_number):
        self.driver.find_element(By.XPATH, self.case_SLA_SMS_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_SLA_SMS_text_xpath).send_keys(SMS_number)

    def setCaseSLA_chat_url_btn(self):
        self.driver.find_element(By.XPATH, self.case_SLA_chat_url_xpath).click()

    def setCaseSLA_chat_url_text(self, chat_url):
        self.driver.find_element(By.XPATH, self.case_SLA_chat_url_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_SLA_chat_url_text_xpath).send_keys(chat_url)

    def setTimezone_checkbox(self):
        self.driver.find_element(By.XPATH, self.case_SLA_eastern_checkbox_xpath).click()

    def setOperational_hours(self):
        self.switch = self.driver.find_element(By.XPATH, self.case_SLA_Monday_Ios_btn_xpath)
        if not self.switch.is_selected():
            self.switch.click()

    def setCase_Domain(self):
        self.driver.find_element(By.XPATH, self.case_domain_manual_xpath).click()

    def setDomain(self):
        self.element = self.driver.find_element(By.XPATH, self.case_domain_input_xpath)
        self.element.click()
        self.element.send_keys(Keys.ARROW_DOWN)
        self.element.send_keys(Keys.ARROW_DOWN)
        self.element.send_keys(Keys.ENTER)

        time.sleep(2)

    def clickClose_btn(self):
        self.element = self.driver.find_element(By.XPATH, self.case_domain_close_btn_xpath).click()

    def setAssign_agent(self):
        self.source_element = self.driver.find_element(By.CSS_SELECTOR, "#campaign-aa-dnd-availableBox-0")
        self.target_element = self.driver.find_element(By.CSS_SELECTOR, "#campaign-aa-dnd-selectedArea")

        self.actions = ActionChains(self.driver)

        self.actions.click_and_hold(self.source_element).move_by_offset(200, 0).move_to_element(
            self.target_element).release().perform()

        time.sleep(3)

    def setDisposition_manual(self):
        self.driver.find_element(By.XPATH, self.disposition_Manual_btn_xpath).click()

    def setDisposition_textbox(self, Disposition_input):
        self.driver.find_element(By.XPATH, self.disposition_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.disposition_textbox_xpath).send_keys(Disposition_input)

    def setDisposition_description(self, Description_input):
        self.driver.find_element(By.XPATH, self.disposition_description_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.disposition_description_box_xpath).send_keys(Description_input)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.disposition_Next_button).click()

    def setProduct_Manual(self):
        self.driver.find_element(By.XPATH, self.product_manual).click()

    def setProduct_name(self, name):
        self.driver.find_element(By.XPATH, self.product_name).clear()
        self.driver.find_element(By.XPATH, self.product_name).send_keys(name)

    def setModel_number(self, model_number):
        self.driver.find_element(By.XPATH, self.model_number).clear()
        self.driver.find_element(By.XPATH, self.model_number).send_keys(model_number)

    def setProduct_code(self, Product_code):
        self.driver.find_element(By.XPATH, self.product_code).clear()
        self.driver.find_element(By.XPATH, self.product_code).send_keys(Product_code)

    def setCountry(self):
        self.country = self.driver.find_element(By.XPATH, self.product_country)
        self.country.click()
        self.country.send_keys(Keys.ARROW_UP, Keys.ENTER)

    def setProduct_description(self, Product_description):
        self.driver.find_element(By.XPATH, self.product_description).clear()
        self.driver.find_element(By.XPATH, self.product_description).send_keys(Product_description)

    def clickCaseLog_All_btn(self):
        self.driver.find_element(By.XPATH, self.case_add_all_btn).click()

    def setCaseOrigin(self):
        self.case_origin_drag = self.driver.find_element(By.CSS_SELECTOR, "#campaign-case_origins-dnd-availableBox-0")
        self.case_origin_drop = self.driver.find_element(By.CSS_SELECTOR, "#campaign-case_origins-dnd-selectedArea")

        self.actions = ActionChains(self.driver)

        self.actions.click_and_hold(self.case_origin_drag).move_by_offset(200, 0).move_to_element(
            self.case_origin_drop).release().perform()

        time.sleep(2)

    def clickDone_btn(self):
        self.driver.find_element(By.XPATH, self.Done_btn).click()
