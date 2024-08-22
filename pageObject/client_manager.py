

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Client_Manager:
    Client_manager_xpath = "//*[text()='Client Manager']"
    Client_manager_active_xpath = "//*[@id='side-navigation-select-item-Active']/div/span"
    Add_client_button_xpath = "//*[@id='client-manager-add-button']"

    Client_name_xpath = '//input[@name="name"]'
    Client_phone_xpath = "//input[@name='phone']"
    Client_address_xpath = "//input[@name='address']"
    Client_email_xpath = "//input[@name='email']"

    Client_primary_first_name_xpath = "//input[@name='primary_first_name']"
    Client_primary_last_name_xpath = "//input[@name='primary_last_name']"
    Client_primary_email_xpath = "//input[@name='primary_email']"
    Client_primary_phone_xpath = "//input[@name='primary_phone']"
    Client_primary_ext_xpath = "//input[@name='primary_ext']"

    Client_secondary_first_name_xpath = "//input[@name='secondary_first_name']"
    Client_secondary_last_name_xpath = "//input[@name='secondary_last_name']"
    Client_secondary_email_xpath = "//input[@name='secondary_email']"
    Client_secondary_phone_xpath = "//input[@name='secondary_phone']"
    Client_secondary_ext_xpath = "//input[@name='secondary_ext']"
    Payment_terms_xpath = "//*[text()='Select payment terms']"
    payment_term_value_xpath = "//*[@id='menu-payment_terms']/div[3]/ul/li[4]"
    Client_image_Xpath = "//*[@id='client-dialog-submit-form']/div[2]/div[3]/div/div/div/div/label/img"

    Client_save_button_xpath = "//*[@id='client-dialog-submit-button']"

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def client_manager_dropdown(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Client Manager']")))
        # self.driver.Client_manager_xpath.click()
        self.driver.find_element(By.XPATH, self.Client_manager_xpath).click()

    def client_manager_active(self):
        self.driver.find_element(By.XPATH, self.Client_manager_active_xpath).click()

    def client_manager_add_client_button(self):
        self.driver.find_element(By.XPATH, self.Add_client_button_xpath).click()

    def setClient_name(self, client_name):
        self.driver.find_element(By.XPATH, self.Client_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_name_xpath).send_keys(client_name)

    def setClient_phone(self, client_phone):
        self.driver.find_element(By.XPATH, self.Client_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_phone_xpath).send_keys(client_phone)

    def setClient_address(self, client_address):
        self.driver.find_element(By.XPATH, self.Client_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_address_xpath).send_keys(client_address)

    def setClient_email(self, client_email):
        self.driver.find_element(By.XPATH, self.Client_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_email_xpath).send_keys(client_email)

    # client primary details :

    def setClient_primary_firstname(self, client_primary_firstname):
        self.driver.find_element(By.XPATH, self.Client_primary_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_primary_first_name_xpath).send_keys(client_primary_firstname)

    def setClient_primary_lastname(self, client_primary_lastname):
        self.driver.find_element(By.XPATH, self.Client_primary_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_primary_last_name_xpath).send_keys(client_primary_lastname)

    def setClient_primary_email(self, client_primary_email):
        self.driver.find_element(By.XPATH, self.Client_primary_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_primary_email_xpath).send_keys(client_primary_email)

    def setClient_primary_phone(self, client_primary_phone):
        self.driver.find_element(By.XPATH, self.Client_primary_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_primary_phone_xpath).send_keys(client_primary_phone)

    def setClient_primary_ext(self, client_primary_ext):
        self.driver.find_element(By.XPATH, self.Client_primary_ext_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_primary_ext_xpath).send_keys(client_primary_ext)

    # client secondary details :
    def setClient_secondary_firstname(self, client_secondary_firstname):
        self.driver.find_element(By.XPATH, self.Client_secondary_first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_secondary_first_name_xpath).send_keys(client_secondary_firstname)

    def setClient_secondary_lastname(self, client_secondary_lastname):
        self.driver.find_element(By.XPATH, self.Client_secondary_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_secondary_last_name_xpath).send_keys(client_secondary_lastname)

    def setClient_secondary_email(self, client_secondary_email):
        self.driver.find_element(By.XPATH, self.Client_secondary_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_secondary_email_xpath).send_keys(client_secondary_email)

    def setClient_secondary_phone(self, client_secondary_phone):
        self.driver.find_element(By.XPATH, self.Client_secondary_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_secondary_phone_xpath).send_keys(client_secondary_phone)

    def setClient_secondary_ext(self, client_secondary_ext):
        self.driver.find_element(By.XPATH, self.Client_secondary_ext_xpath).clear()
        self.driver.find_element(By.XPATH, self.Client_secondary_ext_xpath).send_keys(client_secondary_ext)

    def Client_payment_terms(self):
        self.driver.find_element(By.XPATH, self.Payment_terms_xpath).click()

    def Client_payment_terms_value(self):
        self.driver.find_element(By.XPATH, self.payment_term_value_xpath).click()

    def Client_logo(self):
        self.driver.find_element(By.XPATH, self.Client_image_Xpath).click()

    def Client_save_button(self):
        self.driver.find_element(By.XPATH, self.Client_save_button_xpath).click()
