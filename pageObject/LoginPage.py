from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxyless

import time

from selenium.webdriver.support import wait
from selenium_recaptcha_solver import RecaptchaSolver


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
        email_input = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute(
            "value") == email, f"Expected email '{email}' but got '{email_input.get_attribute('value')}'"
        assert email

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickRecaptcha(self):
        solver = RecaptchaSolver(driver=self.driver)

        try:
            # Increase the timeout to 10 seconds to give the iframe time to load
            recaptcha_iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]'))
            )
            print("reCAPTCHA iframe located.")

            # Solve the reCAPTCHA by passing the iframe to the solver
            solver.click_recaptcha_v2(iframe=recaptcha_iframe)

        except TimeoutException:
            print("TimeoutException: reCAPTCHA iframe not found within the given time.")

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
