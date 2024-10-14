import requests
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium_recaptcha_solver import RecaptchaSolver


class LoginPage:
    textbox_email_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    button_logon_xpath = "//button[text()='LOG ON ']"
    navbar_logout_text_xpath = "//span[contains(text(),'Logout')]"
    btn_logout_xpath = "//button[text()='Yes']"
    continue_xpath = "/html/body/div[3]/div[3]/div/div[2]/button[1]"
    Decline_xpath = '//span[contains(text(),"Decline")]'
    Accept_Xpath = '//*[@id="path-1-inside-1_1881_243843"]'

    API_KEY = '18e475d9bfc2649b1eb67f58798b29b2'  # Replace with your actual API key
    SITE_KEY = '6LdgsDEbAAAAAC0v0GlymSqOQ2Gh2iZh1r6rcZ9n'  # Replace with the site key of the reCAPTCHA
    PAGE_URL = 'https://dev-focus.testd.com'  # Replace with the URL of the page containing reCAPTCHA

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def setEmail(self, email):
        email_input = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        email_input.clear()
        email_input.send_keys(email)
        assert email_input.get_attribute(
            "value") == email, f"Expected email '{email}' but got '{email_input.get_attribute('value')}'"

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

    def clickLogon(self):
        self.driver.find_element(By.XPATH, self.button_logon_xpath).click()
        try:
            element = self.driver.find_element(By.XPATH, self.continue_xpath)
            print("Element found")
            element.click()  # Perform the click action
        except NoSuchElementException:
            print("Element not found")

        # assert '/dashboard' in self.driver.baseURL

    def IncomingCall(self):
        try:
            wait_for_element = WebDriverWait(self.driver, 10)
            decline_button = wait_for_element.until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Decline']")))

            # Log visibility and enabled state
            print(f"Is visible: {decline_button.is_displayed()}")
            print(f"Is enabled: {decline_button.is_enabled()}")
            decline_button.click()
            if decline_button.is_displayed():
                decline_button.click()
                print("element clicked")
                time.sleep(10)
            else:
                print("can't click the element")

            # Click using JavaScript as a fallback
            # self.driver.execute_script("arguments[0].click();", decline_button)
            # decline_button.click()

        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(5)

    def clickLogout(self):
        element = WebDriverWait(self.driver, 5)

        try:
            # Wait for the logout element to be present
            logout = element.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Logout')]"))
            )
            logout.click()  # Click the logout button
            print("Logout button clicked.")

        except TimeoutException:
            print("TimeoutException: Logout element not found within the given time.")

    def click_btn_Logout_yes(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
