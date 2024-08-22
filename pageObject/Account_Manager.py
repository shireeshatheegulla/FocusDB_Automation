from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account_Manager:
    control_center_btn_xpath = "//span[text()='Control Center']"
    account_btn_xpath = "//span[text()='Account Manager']"
    add_account_btn = "//button[@id='account-manager-add-button']"
    acc_first_name_xpath = "//input[@name='first_name']"
    acc_last_name_xpath = "//input[@name='last_name']"
    acc_role_dropdown_xpath = "//p[text()='Select Role']"
    acc_department_xpath = "//input[@name='department']"
    acc_phone_xpath = "//input[@name='phone']"
    acc_email_xpath = "//input[@name='email']"
    acc_address_xpath = "//input[@name='address']"
    acc_unit_xpath = "//input[@name='unit']"
    acc_state_dropdown_id = "//div[@id='mui-component-select-state']"
    acc_city_xpath = "//input[@name='city']"
    acc_zipcode_xpath = "//input[@name='zip_code']"
    acc_create_btn_xpath = "//button[@id='account-add-submit-button']"

    def __init__(self, driver):
        self.dropdown_element = None
        self.accRole = None
        self.driver = driver
        driver.maximize_window()

    def clickControlCenterBtn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.control_center_btn_xpath))).click()

    def clickAccountManagerBtn(self):
        self.driver.find_element(By.XPATH, self.account_btn_xpath).click()

    def clickAddAccountBtn(self):
        self.driver.find_element(By.XPATH, self.add_account_btn).click()

    def setAccountFirstName(self, first_name):
        self.driver.find_element(By.XPATH, self.acc_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.acc_first_name_xpath).send_keys(first_name)

    def setAccountLastName(self, last_name):
        self.driver.find_element(By.XPATH, self.acc_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.acc_last_name_xpath).send_keys(last_name)

    def setAccountRole(self):
        self.accRole = self.driver.find_element(By.XPATH, self.acc_role_dropdown_xpath)
        self.accRole.click()

        # self.accRole.send_keys(Keys.ARROW_UP)
        # # self.accRole.send_keys(Keys.ARROW_DOWN)
        # self.accRole.send_keys(Keys.ARROW_UP, Keys.ENTER)
        # # self.driver.find_element(By.XPATH, self.acc_role_dropdown_xpath).send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    def setRole(self):
        self.driver.find_element(By.XPATH, '//li[contains(text(),"ADMINISTRATOR")]').click()
        #
        # # Create a Select object from the dropdown element
        # dropdown = Select(self.dropdown_element)
        #
        # # Select an option by visible text
        # dropdown.select_by_visible_text("Option 2")
        # elements = self.driver.find_element(By.ID, "menu-role_id")
        # # elements.click()
        # for element in elements:
        #     if element.text == "ADMINISTRATOR":
        #         element.click()
        #         break

    def setAccountDepartment(self, department):
        self.driver.find_element(By.XPATH, self.acc_department_xpath).send_keys(department)

    def setAccountPhoneNumber(self, Phone_number):
        self.driver.find_element(By.XPATH, self.acc_phone_xpath).send_keys(Phone_number)

    def setAccountEmail(self, email):
        self.driver.find_element(By.XPATH, self.acc_email_xpath).send_keys(email)

    def setAccountAddress(self, address):
        self.driver.find_element(By.XPATH, self.acc_address_xpath).send_keys(address)

    def setAccountUnit(self, unit):
        self.driver.find_element(By.XPATH, self.acc_unit_xpath).send_keys(unit)

    def clickAccountState(self):
        self.driver.find_element(By.XPATH, self.acc_state_dropdown_id).click()

    def setAccountState(self):
        self.driver.find_element(By.XPATH, '//li[@data-value="Florida"]').click()

    def setAccountCity(self, city):
        self.driver.find_element(By.XPATH, self.acc_city_xpath).send_keys(city)

    def setAccountZipCode(self, zipcode):
        self.driver.find_element(By.XPATH, self.acc_zipcode_xpath).send_keys(zipcode)

    def clickAccountCreateButton(self):
        self.driver.find_element(By.XPATH, self.acc_create_btn_xpath).click()
