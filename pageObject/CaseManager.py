import datetime
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


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

    # *************************** Case Demographics *****************************

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

    # ****************************** Case Details ******************************************
    case_details_xpath = "//*[@id='case-log-select-card-Case Details']"
    case_domain_dropdown_xpath = "//input[@name='domain']"
    case_domain_safety_xpath = "//p[text()='Safety']"
    case_sub_domain_xpath = "//input[@name='subdomain']"
    case_bodily_injury_xpath = "//p[text()='Bodily Injury']"
    case_details_submit_btn_xpath = "//button[@id='case-details-submit-button']"
    calendar_xpath = "//input[@name='incident_date']"
    incident_location_xpath = "//input[@name='incident_location']"
    reported_date_xpath = "//input[@name='reported_date']"
    case_reason_xpath = "//p[contains(text(),'Enter case reason')]"
    case_reason_value_xpath = "//li[@data-value='Body harm/Injury']"
    case_XC_Subject_xpath = "//Input[@name='xc_subject']"
    Case_XC_details_xpath = "//textarea[@name='incident_details']"
    symptom_code_1_xpath = "//*[@id='mui-component-select-temp_code_1']"
    symptom_code_2_xpath = "//*[@id='mui-component-select-temp_code_2']"
    symptom_code_3_xpath = "//*[@id='mui-component-select-temp_code_3']"

    # ******************** Case Products **********************
    case_product_xpath = "//*[@id='case-log-select-card-Product']"
    case_product_action_icon_xpath = '//*[@id="case-product-actionSelect-iconbutton-0"]'
    product_serial_number_xpath = "//input[@name='serial_number']"
    product_purchase_date_xpath = "//input[@name='purchase_date']"
    product_received_Date_xpath = "//input[@name='received_date']"
    product_submit_btn_xpath = '//button[@id="case-product-submit-button"]'

    # *********************Case Notes *********************************
    Case_Notes_Xpath = '//*[@id="case-log-select-card-Case Notes"]'
    case_Notes_title_xpath = "//input[@name='title']"
    case_notes_textarea_xpath = "//textarea[@name='notes']"
    Upload_file_xpath = "//p[contains(text(),'Upload File')]"
    case_notes_email_checkbox_xpath = "//p[contains(text(),'Email')]"
    case_notes_SMS_checkbox_xpath = "//p[contains(text(),'Text message')]"
    send_attachment_xpath = "//button[@id='case-notes-attachment-button']"
    case_notes_close_btn_cssSelector = "div[class='css-148qabf'] button[type='button']"

    # ************************************ Case Returns *******************************
    Returns_xpath = "//*[@id='case-log-select-card-Returns']"
    safety_returns_xpath = '//*[@id="case-return-select-box-Safety"]'
    return_reason_drop_down_list_xpath = '//*[@id="mui-component-select-reason"]'
    wrong_product_xpath = "//li[@data-value='Wrong product']"
    Incorrect_Quantity_xpath = "//li[@data-value='Incorrect Quantity']"
    Defective_Product_xpath = "//li[@data-value='Defective Product']"
    Undelivered_xpath = "//li[@data-value='Undelivered']"
    Return_to_Shipper_xpath = "//li[@data-value='Return to Shipper']"

    RMA_Btn_xpath = "//button[@id='case-return-generateRma-button']"
    return_expected_drop_down_list_xpath = "//*[@id='mui-component-select-product_expected']"
    return_expected_value_xpath = "//*[@data-value='Consumer confirmed product return']"
    Next_btn_xpath = "//*[@id='case-return-submit-button']"
    generate_shipping_label_xpath = "//*[@id='case-return-generateShipping-button']"
    was_replacement_ordered_xpath = '//*[@id="mui-component-select-replacement_ordered"]'
    replacement_ordered_value_xpath = '//li[@data-value="true"]'
    order_confirmation_num_xpath = '//input[@name="confirmation_number"]'
    save_btn_xpath = '//button[@id="case-return-submit-button"]'
    warranty_returns_xpath = '//*[@id="case-return-select-box-Warranty"]'

    # ***************************  Case ActivityLog ************************
    case_Activity_log_xpath = '//*[@id="case-log-select-card-Activity Log"]'
    activity_new_btn_xpath = '//*[@id="case-activityLog-new-button"]'
    activity_type_xpath = '//input[@name="type"]'
    activity_description_xpath = '//textarea[@name="description"]'
    Save_btn_xpath = '//*[@id="case-addActivity-submit-button"]'

    case_escalation_xpath = "//button[contains(text(),'CASE ESCALATION')]"
    Assign_to_agent_xpath = '//input[@name="assigned_to_account_id"]'
    escalation_reason_xpath = '//textarea[@name="reason"]'
    Low = '//input[@value="Low"]'
    medium = '//input[@value="Medium"]'
    High = '//input[@value="High"]'
    send_btn = '//button[@type="submit"]'
    yes_btn = '//button[@id="confirmation-dialog-action-button"]'
    success_dialog_close_btn = '//button[@id="alert-dialog-okay-button"]'
    case_tasks_xpath = "//button[contains(text(),'CASE TASKS')]"
    select_category_xpath = '//*[@id="mui-component-select-category"]'
    category_zero_xpath = '//li[@data-value="Category 0"]'
    Task_notes_xpath = '//textarea[@name="notes"]'
    Assign_to_Agent_xpath = '//input[@name="assigned_to_account_id"]'
    assign_task_btn_xpath = "//button[contains(text(),'ASSIGN TASK')]"

    case_reminders_xpath = "//button[contains(text(),'CASE REMINDERS')]"
    category_xpath = '//*[@id="mui-component-select-category"]'
    category_zero = '//li[@data-value="Category 0"]'
    reminder_due_date_xpath = '//input[@name="due_date"]'
    Reminder_notes_xpath = '//textarea[@name="notes"]'

    Hourly_xpath = '//input[@value="Hourly"]'
    daily_xpath = '//input[@value="Daily"]'
    weekly_xpath = '//input[@value="Weekly"]'
    assign_to_agent_xpath = '//input[@name="assigned_to_account_id"]'
    Activate_xpath = "//button[contains(text(),'ACTIVATE')]"
    Close_Xpath = '//button[@id="dialog-close-iconbutton"]'

    # *********************************** Case Insurance ****************************
    Insurance_xpath = '//*[@id="case-log-select-card-Insurance"]'
    first_name = '//input[@name="first_name"]'
    last_name_xpath = '//input[@name="last_name"]'
    carrier_xpath = '//input[@name="carrier"]'
    bin_xpath = '//input[@name="bin"]'
    Policy_num_xpath = '//input[@name="policy_number"]'
    dob_xpath = '//input[@name="dob"]'
    effective_date_xpath = '//input[@name="effective_date"]'
    front_of_insurance_card = '//*[@id="card_front_path-0"]'
    back_of_insurance = '//*[@id="card_back_path-0"]'
    insurance_save_btn = '//*[@id="case-insurance-submit-button"]'

    # ******************** Case Disposition *******
    disposition_xpath = '//*[@id="case-disposition-menu-iconbutton"]'
    closed_xpath = "//li[contains(text(),'Closed')]"

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

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
        element = self.driver.find_element(By.XPATH, self.case_demo_confirm_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    # ----CASE_DETAILS-----

    def click_case_details_module(self):
        self.driver.find_element(By.XPATH, self.case_details_xpath).click()

    def click_caseDomain_Dropdown(self):
        self.driver.find_element(By.XPATH, self.case_domain_dropdown_xpath).click()

    def click_Safety_Domain(self):
        self.driver.find_element(By.XPATH, self.case_domain_safety_xpath).click()

    def click_sub_domain(self):
        self.driver.find_element(By.XPATH, self.case_sub_domain_xpath).click()

    def click_case_bodily_injury(self):
        self.driver.find_element(By.XPATH, self.case_bodily_injury_xpath).click()

    def click_case_details_submit_btn(self):
        self.driver.find_element(By.XPATH, self.case_details_submit_btn_xpath).click()

    def IncidentDate(self):
        calendar_input = self.driver.find_element(By.XPATH, self.calendar_xpath)
        calendar_input.click()

        # Get the date for 7 days in the past
        past_date = datetime.now() - timedelta(days=3)

        specified_time = "02:30"
        PM = "PM"

        # Format the past date as a string
        formatted_date = past_date.strftime("%m/%d/%Y") + "" + specified_time + "" + PM
        # Change format as needed

        # Send the formatted date to the calendar input
        calendar_input.send_keys(formatted_date)

    def setIncidentLocation(self):
        location_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.incident_location_xpath))
        )

        # Send the location name
        location_input.send_keys("Hyderabad")

        time.sleep(3)

        location_input.send_keys(Keys.ARROW_DOWN)

        time.sleep(1)

        # Send ENTER to select the highlighted suggestion
        location_input.send_keys(Keys.ENTER)

        # Optional: Wait to ensure the selection is processed
        time.sleep(3)

    def setReportedDate(self):
        Reported_Date = self.driver.find_element(By.XPATH, self.reported_date_xpath)
        Reported_Date.click()  # Click to open the calendar
        specified_time = "02:30"
        PM = "PM"

        # Get the current date and format it as a string
        current_date = datetime.now().strftime("%m/%d/%Y") + "" + specified_time + "" + PM  # Change format as needed

        # Send the formatted date to the calendar input
        Reported_Date.send_keys(current_date)

    def clickCaseReason(self):
        self.driver.find_element(By.XPATH, self.case_reason_xpath).click()

    def setCaseReason(self):
        self.driver.find_element(By.XPATH, self.case_reason_value_xpath).click()

    def setCaseXCSubject(self):
        self.driver.find_element(By.XPATH, self.case_XC_Subject_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_XC_Subject_xpath).send_keys("Testing")

    def setCase_XC_details(self):
        self.driver.find_element(By.XPATH, self.Case_XC_details_xpath).clear()
        self.driver.find_element(By.XPATH, self.Case_XC_details_xpath).send_keys("Testing")

    def clickSymptomCode_1(self):
        self.driver.find_element(By.XPATH, self.symptom_code_1_xpath).click()
        time.sleep(2)

    def setSymptomCode_1(self):
        self.driver.find_element(By.XPATH, "//li[@data-value='01']").click()

    def clickSymptomCode_2(self):
        self.driver.find_element(By.XPATH, self.symptom_code_2_xpath).click()
        time.sleep(2)

    def setSymptomCode_2(self):
        self.driver.find_element(By.XPATH, "//li[@data-value='01']").click()

    def clickSymptomCode_3(self):
        self.driver.find_element(By.XPATH, self.symptom_code_3_xpath).click()

    def setSymptomCode_3(self):
        self.driver.find_element(By.XPATH, "//li[@data-value='01']").click()

    # Case Product

    def clickCaseProduct(self):
        self.driver.find_element(By.XPATH, self.case_product_xpath).click()

    def clickCaseProductActionIcon(self):
        self.driver.find_element(By.XPATH, self.case_product_action_icon_xpath).click()

    def setProductSerialNumber(self):
        self.driver.find_element(By.XPATH, self.product_serial_number_xpath).clear()
        self.driver.find_element(By.XPATH, self.product_serial_number_xpath).send_keys("1234567890")

    def setProductPurchaseDate(self):
        calendar_input = self.driver.find_element(By.XPATH, self.product_purchase_date_xpath)
        calendar_input.click()

        # Get the date for 7 days in the past
        past_date = datetime.now() - timedelta(days=7)

        specified_time = "02:30"
        PM = "PM"

        # Format the past date as a string
        formatted_date = past_date.strftime("%m/%d/%Y") + "" + specified_time + "" + PM
        # Change format as needed

        # Send the formatted date to the calendar input
        calendar_input.send_keys(formatted_date)

    def setProductReceivedDate(self):
        calendar_input = self.driver.find_element(By.XPATH, self.product_received_Date_xpath)
        calendar_input.click()

        # Get the date for 7 days in the past
        past_date = datetime.now() - timedelta(days=5)

        specified_time = "02:30"
        PM = "PM"

        # Format the past date as a string
        formatted_date = past_date.strftime("%m/%d/%Y") + "" + specified_time + "" + PM
        # Change format as needed

        # Send the formatted date to the calendar input
        calendar_input.send_keys(formatted_date)

    def clickProductConfirmBtn(self):
        element = self.driver.find_element(By.XPATH, self.product_submit_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def clickCaseNotes(self):
        self.driver.find_element(By.XPATH, self.Case_Notes_Xpath).click()

    def setCaseNotesTitle(self):
        self.driver.find_element(By.XPATH, self.case_Notes_title_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_Notes_title_xpath).send_keys("QA_Case Notes")

    def setCaseNotes(self):
        self.driver.find_element(By.XPATH, self.case_notes_textarea_xpath).clear()
        self.driver.find_element(By.XPATH, self.case_notes_textarea_xpath).send_keys("Testing")

    def caseNotesUploadFile(self):
        self.driver.find_element(By.XPATH, self.Upload_file_xpath).click()

    def caseNotesEmailCheckBox(self):
        element = self.driver.find_element(By.XPATH, self.case_notes_email_checkbox_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        # self.driver.find_element(By.XPATH, self.case_notes_email_checkbox_xpath).click()

    def caseNotesSMSCheckBOX(self):
        self.driver.find_element(By.XPATH, self.case_notes_SMS_checkbox_xpath).click()

    def sendAttachmentXpath(self):
        self.driver.find_element(By.XPATH, self.send_attachment_xpath).click()

    def caseNotesCloseBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.case_notes_close_btn_cssSelector).click()

    def setCaseReturns(self):
        self.driver.find_element(By.XPATH, self.Returns_xpath).click()

    def Return_type(self):
        safety_return = self.driver.find_element(By.XPATH, self.safety_returns_xpath)
        warranty_return = self.driver.find_element(By.XPATH, self.warranty_returns_xpath)

        if safety_return.is_displayed():
            print("interacting with safety_return.")
            return_type = self.driver.find_element(By.XPATH, self.safety_returns_xpath)
            return_type.click()
        elif warranty_return.is_displayed():
            print("interacting with warranty_return.")
            return_type = self.driver.find_element(By.XPATH, self.warranty_returns_xpath)
            return_type.click()
        else:
            print("Neither return type is selected")

        time.sleep(2)

    def clickReturnReason(self, value):
        self.driver.find_element(By.XPATH, self.return_reason_drop_down_list_xpath).click()
        time.sleep(1)

        if value == 'Wrong product':
            list_item = self.driver.find_element(By.XPATH, self.wrong_product_xpath)
        elif value == "Incorrect Quantity":
            list_item = self.driver.find_element(By.XPATH, self.Incorrect_Quantity_xpath)
        elif value == 'Defective Product':
            list_item = self.driver.find_element(By.XPATH, self.Defective_Product_xpath)
        elif value == 'Undelivered':
            list_item = self.driver.find_element(By.XPATH, self.Undelivered_xpath)
        elif value == 'Return to Shipper':
            list_item = self.driver.find_element(By.XPATH, self.Return_to_Shipper_xpath)
        else:
            list_item = self.driver.find_element(By.XPATH, self.wrong_product_xpath)
        time.sleep(2)
        list_item.click()

    def GenerateRMA(self):
        self.driver.find_element(By.XPATH, self.RMA_Btn_xpath).click()
        time.sleep(3)

    def ReturnExpected(self, value):
        self.driver.find_element(By.XPATH, self.return_expected_drop_down_list_xpath).click()
        time.sleep(2)
        if value == 'Consumer confirmed product return':
            self.driver.find_element(By.XPATH, "//*[@data-value='Consumer confirmed product return']").click()
        elif value == 'Consumer confirmed product will not be returned':
            self.driver.find_element(By.XPATH,
                                     "//*[@data-value='Consumer confirmed product will not be returned']").click()
        elif value == "Unable to contact consumer":
            self.driver.find_element(By.XPATH, "//*[@data-value='Unable to contact consumer']").click()
        elif value == "Awaiting consumer response":
            self.driver.find_element(By.XPATH, "//*[@data-value='Awaiting consumer response']").click()
        else:
            self.driver.find_element(By.XPATH, "//*[@data-value='Consumer confirmed product return']").click()
        time.sleep(2)

    def clickReturnNextBtn(self):
        element = self.driver.find_element(By.XPATH, self.Next_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def generateShippingLabel(self):
        shipping_label = self.driver.find_element(By.XPATH, self.generate_shipping_label_xpath)
        if shipping_label.is_displayed():
            shipping_label.click()
            time.sleep(3)
            self.clickReturnNextBtn()
        else:
            self.clickReturnNextBtn()

    def wasReplacementOrdered(self, value):
        element = self.driver.find_element(By.XPATH, self.was_replacement_ordered_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        # self.driver.find_element(By.XPATH, self.was_replacement_ordered_xpath).click()
        if value == "Yes":
            list_item = self.driver.find_element(By.XPATH, '//li[@data-value="true"]')
        else:
            list_item = self.driver.find_element(By.XPATH, '//li[@data-value="false"]')
        list_item.click()

    def OrderConfirmationNum(self):
        self.driver.find_element(By.XPATH, self.order_confirmation_num_xpath).clear()
        self.driver.find_element(By.XPATH, self.order_confirmation_num_xpath).send_keys("12345678")
        self.clickReturnNextBtn()

    def caseActivityLog(self):
        wait = WebDriverWait(self.driver, 5)
        ActivityLog = wait.until(EC.visibility_of_element_located((By.XPATH, self.case_Activity_log_xpath)))
        ActivityLog.click()

    def clickNewActivity(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.activity_new_btn_xpath))).click()

    def clickNewActivityType(self):
        wait = WebDriverWait(self.driver, 2)
        ActivityType = wait.until(EC.visibility_of_element_located((By.XPATH, self.activity_type_xpath)))
        ActivityType.click()
        ActivityType.send_keys(Keys.ARROW_DOWN)
        ActivityType.send_keys(Keys.ENTER)

    def setActivityDescription(self):
        self.driver.find_element(By.XPATH, self.activity_description_xpath).send_keys("Testing")

    def clickDialogueSaveBtn(self):
        wait = WebDriverWait(self.driver, 2)
        save_btn = wait.until(EC.visibility_of_element_located((By.XPATH, self.Save_btn_xpath)))
        save_btn.click()

    def clickCaseEscalationTab(self):
        wait = WebDriverWait(self.driver, 2)
        CaseEscalation = wait.until(EC.visibility_of_element_located((By.XPATH, self.case_escalation_xpath)))
        CaseEscalation.click()

    def CaseEscalationAssignToAgent(self):
        wait = WebDriverWait(self.driver, 2)
        CaseEscalationAgent = wait.until(EC.visibility_of_element_located((By.XPATH, self.Assign_to_agent_xpath)))
        CaseEscalationAgent.click()
        CaseEscalationAgent.send_keys(Keys.ARROW_DOWN)
        CaseEscalationAgent.send_keys(Keys.ENTER)

    def setCaseEscalationReason(self):
        wait = WebDriverWait(self.driver, 2)
        EscalationReason = wait.until(EC.visibility_of_element_located((By.XPATH, self.escalation_reason_xpath)))
        EscalationReason.clear()
        EscalationReason.send_keys("Testing")

    def CaseSeverityLevel(self, value):
        if value == 'Low':
            element = self.driver.find_element(By.XPATH, self.Low)
        elif value == 'Medium':
            element = self.driver.find_element(By.XPATH, self.medium)
        else:
            element = self.driver.find_element(By.XPATH, self.High)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def CaseEscalationSendBtn(self):
        self.driver.find_element(By.XPATH, self.send_btn).click()

    def CaseEscalationYesBtn(self):
        self.driver.find_element(By.XPATH, self.yes_btn).click()

    def CaseEscalationSuccessDialogueCloseBtn(self):
        self.driver.find_element(By.XPATH, self.success_dialog_close_btn).click()

    def clickCaseTasksTab(self):
        wait = WebDriverWait(self.driver, 2)
        CaseTasksTab = wait.until(EC.visibility_of_element_located((By.XPATH, self.case_tasks_xpath)))
        CaseTasksTab.click()

    def clickCategory(self):
        wait = WebDriverWait(self.driver, 2)
        categoryDropdown = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_category_xpath)))
        categoryDropdown.click()

    def clickCategoryZero(self):
        wait = WebDriverWait(self.driver, 2)
        categoryZero = wait.until(EC.visibility_of_element_located((By.XPATH, self.category_zero_xpath)))
        categoryZero.click()

    def setCaseTasksNotes(self):
        wait = WebDriverWait(self.driver, 3)
        TaskNotes = wait.until(EC.visibility_of_element_located((By.XPATH, self.Task_notes_xpath)))
        TaskNotes.clear()
        TaskNotes.send_keys("testing")

    def clickTaskAssignToAgent(self):
        wait = WebDriverWait(self.driver, 3)
        CaseEscalationAgent = wait.until(EC.visibility_of_element_located((By.XPATH, self.Assign_to_agent_xpath)))
        CaseEscalationAgent.click()
        CaseEscalationAgent.send_keys(Keys.ARROW_DOWN)
        CaseEscalationAgent.send_keys(Keys.ENTER)

    def clickAssignTaskBtn(self):
        wait = WebDriverWait(self.driver, 3)
        AssignTask = wait.until(EC.visibility_of_element_located((By.XPATH, self.assign_task_btn_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", AssignTask)
        AssignTask.click()

    def ClickCaseRemindersTab(self):
        wait = WebDriverWait(self.driver, 3)
        CaseReminderTab = wait.until(EC.visibility_of_element_located((By.XPATH, self.case_reminders_xpath)))
        CaseReminderTab.click()

    def ClickReminderCategory(self):
        wait = WebDriverWait(self.driver, 3)
        ReminderCategory = wait.until(EC.visibility_of_element_located((By.XPATH, self.category_xpath)))
        ReminderCategory.click()

    def clickReminderCategoryZero(self):
        wait = WebDriverWait(self.driver, 3)
        Category0 = wait.until(EC.visibility_of_element_located((By.XPATH, self.
                                                                 category_zero)))
        Category0.click()

    def clickReminderDueDateCalender(self):
        wait = WebDriverWait(self.driver, 3)
        due_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, self.reminder_due_date_xpath)))
        due_date_input.click()

        future_date = "12/30/2024"
        specified_time = "02:30"
        AM_PM = "PM"

        formatted_date = future_date + " " + specified_time + " " + AM_PM

        # Send the formatted date to the calendar input
        due_date_input.send_keys(formatted_date)

    def CaseReminderNotes(self):
        wait = WebDriverWait(self.driver, 3)
        ReminderNotes = wait.until(EC.visibility_of_element_located((By.XPATH, self.Reminder_notes_xpath)))
        ReminderNotes.clear()
        ReminderNotes.send_keys("Testing")

    def setReminderFrequency(self, value):
        if value == 'Hourly':
            self.driver.find_element(By.XPATH, self.Hourly_xpath).click()
        elif value == 'Daily':
            self.driver.find_element(By.XPATH, self.daily_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.weekly_xpath).click()

    def ReminderAssignToAgent(self):
        wait = WebDriverWait(self.driver, 3)
        ReminderAgent = wait.until(EC.visibility_of_element_located((By.XPATH, self.assign_to_agent_xpath)))
        ReminderAgent.click()
        ReminderAgent.send_keys(Keys.ARROW_DOWN)
        ReminderAgent.send_keys(Keys.ENTER)

    def clickActiveBtn(self):
        Active_Button = self.driver.find_element(By.XPATH, self.Activate_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Active_Button)
        Active_Button.click()

    def clickClose(self):
        self.driver.find_element(By.XPATH, self.Close_Xpath).click()

    def clickInsurance(self):
        self.driver.find_element(By.XPATH, self.Insurance_xpath).click()

    def setFirstName(self):
        first_name = self.driver.find_element(By.XPATH, self.first_name)
        first_name.clear()
        first_name.send_keys("QA")

    def setLastName(self):
        last_name = self.driver.find_element(By.XPATH, self.last_name_xpath)
        last_name.clear()
        last_name.send_keys("Testing")

    def setCarrier(self):
        carrier = self.driver.find_element(By.XPATH, self.carrier_xpath)
        carrier.clear()
        carrier.send_keys("12345")

    def setBinNumber(self):
        Bin = self.driver.find_element(By.XPATH, self.bin_xpath)
        Bin.clear()
        Bin.send_keys("123456")

    def setPolicyNumber(self):
        PolicyNumber = self.driver.find_element(By.XPATH, self.Policy_num_xpath)
        PolicyNumber.clear()
        PolicyNumber.send_keys("12345678")

    def setDOB(self):
        wait = WebDriverWait(self.driver, 3)
        DOB = wait.until(EC.visibility_of_element_located((By.XPATH, self.dob_xpath)))
        DOB.click()

        future_date = "12/30/2000"
        specified_time = "02:30"
        AM_PM = "PM"

        formatted_date = future_date + " " + specified_time + " " + AM_PM

        # Send the formatted date to the calendar input
        DOB.send_keys(formatted_date)

    def setEffectiveDate(self):
        wait = WebDriverWait(self.driver, 3)
        EffectiveDate = wait.until(EC.visibility_of_element_located((By.XPATH, self.effective_date_xpath)))
        EffectiveDate.click()

        future_date = "12/30/2000"
        specified_time = "02:30"
        AM_PM = "PM"

        formatted_date = future_date + " " + specified_time + " " + AM_PM

        # Send the formatted date to the calendar input
        EffectiveDate.send_keys(formatted_date)

    def UploadInsuranceCardFrontImage(self):
        self.driver.find_element(By.XPATH, self.front_of_insurance_card).click()

    def UploadInsuranceCardBackImage(self):
        self.driver.find_element(By.XPATH, self.back_of_insurance).click()

    def ClickInsuranceSaveBtn(self):
        self.driver.find_element(By.XPATH, self.insurance_save_btn).click()

    def clickDisposition(self):
        self.driver.find_element(By.XPATH, self.disposition_xpath).click()

    def setDisposition(self, value):
        if value == "Closed":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Closed')]").click()
        elif value == "New":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'New')]").click()
        elif value == "In Progress":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'In Progress')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Waiting for consumer')]").click()




