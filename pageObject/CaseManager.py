from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CaseManager:
    case_manager_btn_xpath = '//span[text()="Case Manager"]'
    case_manager_open_btn = "//a[@href= '/case-manager/OPEN']"
    All_campaigns_button_xpath = "//button[@id='case-manager-selectArrow-iconbutton']"
    select_campaign = "//input[@name='selectedCampaign']"
    case_manager_add_button = "//button[@id='case-manager-add-button']"
    case_origin_xpath = "//p[text()='Phone']"
    consumer_lastname_xpath = "//input[@name='last_name']"
    validation_btn_xpath = "//button[@id='case-consumerValidation-submit-button']"
    validation_okay_btn = "//button[@id='alert-dialog-okay-button']"
    eligible_checkbox_xpath = "//span[text()='ELIGIBLE']"
    next_btn_xpath = "//button[text()='NEXT']"

    # case demographics

    case_firstname_xpath = "//input[@name='first_name']"
    case_lastname_xpath = "//input[@name='last_name']"
    case_member_id_xpath = "//input[@name='member_id']"
    case_phone_xpath = "//input[@name='phone']"
    case_email_xpath = "//input[@name='email']"

    case_shipping_address_xpath = "//input[@name='shipping_address']"

    case_shipping_city_xpath = "//input[@name='shipping_city']"

    case_shipping_state = "//div[@id='mui-component-select-shipping_state']"

    case_shipping_zip_code = "//input[@name='shipping_zip_code']"

    case_shipping_mailing_checkbox = "//input[@name='is_mailing_shipping_same']"

    case_mailing_address_xpath = "//input[@name='mailing_address']"

    case_mailing_city_xpath = "//input[@name='mailing_city']"

    case_mailing_state_xpath = "//div[@id='mui - component - select - mailing_state']"

    case_mailing_zipcode = "//input[@name='mailing_zip_code']"

    case_demo_confirm_btn_xpath = "//button[text()='CONFIRM']"

    def __init__(self, driver):
        self.driver = driver
        # driver.maximize_window()

    def clickCase_Manager_btn(self):
        # self.driver.find_element(By.XPATH, self.case_manager_btn_xpath).click()
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.case_manager_btn_xpath))).click()

    def clickOpenCasesBtn(self):
        # self.driver.find_element(By.XPATH, self.case_manager_open_btn).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.case_manager_open_btn))).click()

    def clickAllCampaignsBtn(self):
        # self.driver.find_element(By.XPATH, self.All_campaigns_button_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.All_campaigns_button_xpath))).click()

    def clickCampaignBox(self):
        # self.driver.find_element(By.XPATH, self.select_campaign).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.select_campaign))).click()
        self.driver.find_element(By.XPATH, self.select_campaign).send_keys(Keys.ARROW_UP, Keys.ENTER)

    def clickAddNewCaseButton(self):
        self.driver.find_element(By.XPATH, self.case_manager_add_button).click()

    def clickCaseOriginPhone(self):
        self.driver.find_element(By.XPATH, self.case_origin_xpath).click()

    def setConsumer_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.consumer_lastname_xpath).send_keys(lastname)

    def clickValidate_btn(self):
        self.driver.find_element(By.XPATH, self.validation_btn_xpath).click()

    def clickOkayBtn(self):
        self.driver.find_element(By.XPATH, self.validation_okay_btn).click()

    def clickEligibleCheckbox(self):
        self.driver.find_element(By.XPATH, self.eligible_checkbox_xpath).click()

    def clickNextBtn(self):
        self.driver.find_element(By.XPATH, self.next_btn_xpath).click()

    def setCaseFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.case_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_firstname_xpath).send_keys(firstname)

    def setCaseLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.case_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_lastname_xpath).send_keys(lastname)

    def setCaseMemberId(self, member_id):
        self.driver.find_element(By.XPATH, self.case_member_id_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_member_id_xpath).send_keys(member_id)

    def setCasePhone(self, case_phone):
        self.driver.find_element(By.XPATH, self.case_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_phone_xpath).send_keys(case_phone)

    def setCaseEmail(self, case_mail):
        self.driver.find_element(By.XPATH, self.case_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_email_xpath).send_keys(case_mail)

    def setCaseShippingAddress(self, shipping_address):
        self.driver.find_element(By.XPATH, self.case_shipping_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_shipping_address_xpath).send_keys(shipping_address)

    def setCaseShippingCity(self, shipping_city):
        self.driver.find_element(By.XPATH, self.case_shipping_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_shipping_city_xpath).send_keys(shipping_city)

    def setCaseShippingState(self):
        self.driver.find_element(By.XPATH, self.case_shipping_state).click()

    def setShippingState(self):
        self.driver.find_element(By.XPATH, '//li[@data-value="Florida"]').click()

    def setShippingZipCode(self, zipcode):
        self.driver.find_element(By.XPATH, self.case_shipping_zip_code).clear()
        self.driver.find_element(By.XPATH, self.case_shipping_zip_code).send_keys(zipcode)

    def clickShippingMailingCheckBox(self):
        self.driver.find_element(By.XPATH, self.case_shipping_mailing_checkbox).click()

    def clickCaseConfirmBtn(self):
        element = self.driver.find_element(By.XPATH, self.case_demo_confirm_btn_xpath).click()
        # Wait until the element is visible

        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.ID, "case-demographics-submit-form"))  # Replace with your
        #     # element's locator
        # )
        # # Interact with the element
        # # element.click()
        # self.driver.execute_script("arguments[0].click();", element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
