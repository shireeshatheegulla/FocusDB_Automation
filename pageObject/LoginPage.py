from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxyless

import time

from selenium.webdriver.support import wait


class LoginPage:
    textbox_email_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    button_logon_xpath = "//button[text()='LOG ON ']"
    navbar_logout_text_xpath = "//span[contains(text(),'Logout')]"
    btn_logout_xpath = "//button[text()='Yes']"
    continue_xpath = "/html/body/div[3]/div[3]/div/div[2]/button[1]"

    def __init__(self, driver):
        self.logout_button = None
        self.driver = driver
        driver.maximize_window()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        assert email

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    # def clickRecaptcha(self): # recaptcha_iframe = self.driver.find_element(By.XPATH, "//iframe[
    # @title='reCAPTCHA']") # self.driver.switch_to.frame(recaptcha_iframe) # site_key = self.driver.find_element(
    # By.XPATH, "//div[@class='rc-anchor-alert']").get_attribute('data-sitekey') #
    # self.driver.switch_to.default_content() # # # Use 2Captcha to solve reCAPTCHA # api_key =
    # 'YOUR_2CAPTCHA_API_KEY' # client = AnticaptchaClient(api_key) # task = NoCaptchaTaskProxyless(
    # site_key=site_key, url=self.driver.current_url) # job = client.createTask(task) # job.join() # token =
    # job.get_solution_response() # # # Enter the token into the reCAPTCHA response field and submit the form #
    # self.driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = arguments[0]',
    # token) # self.driver.find_element(By.XPATH, "//form").submit()
    #
    #     recaptcha_element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'g-recaptcha'))
    #     )
    #
    #     # Extract the site key from the reCAPTCHA element
    #     site_key = recaptcha_element.get_attribute('data-sitekey')
    #
    #     print(f"Site key: {site_key}")

    def clickLogon(self, xpath=None):
        self.driver.find_element(By.XPATH, self.button_logon_xpath).click()
        try:
            element = self.driver.find_element(By.XPATH, self.continue_xpath)
            print("Element found")
            element.click()  # Perform the click action
        except NoSuchElementException:
            print("Element not found")
        # if
        #     self.driver.find_element(By.XPATH, self.continue_xpath).click()
        # else:
        #     self.driver.find_element(By.XPATH, self.button_logon_xpath).click()

    def clickLogout(self):
        # self.driver.find_element(By.XPATH, self.navbar_logout_text_xpath).click()
        logout = WebDriverWait(self.driver, 10)
        self.logout_button = logout.until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Logout')]"))).click()

    def click_btn_Logout_yes(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
