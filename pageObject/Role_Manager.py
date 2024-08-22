import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Role_manager:
    control_center_btn_xpath = "//span[text()='Control Center']"
    navbar_Role_manager_xpath = "//a[@id='side-navigation-select-item-Role Manager']"
    add_role_xpath = "//button[@id='role-manager-add-button']"
    role_name_xpath = "//input[@name='name']"
    role_create_btn_xpath = "//button[contains(text(),'CREATE')]"
    role_drag_xpath = "//div[@id='role-modules-dnd-availableArea']"
    role_drop_xpath = "//div[@id='role-modules-dnd-selectedArea']"

    def __init__(self, driver):
        self.target_element = None
        self.source_element = None
        self.actions = None
        self.driver = driver
        driver.maximize_window()

    def clickControlCenterBtn(self):
        self.driver.find_element(By.XPATH, self.control_center_btn_xpath).click()

    def clickNavbarRole(self):
        self.driver.find_element(By.XPATH, self.navbar_Role_manager_xpath).click()

    def clickAddRoleBtn(self):
        self.driver.find_element(By.XPATH, self.add_role_xpath).click()

    def setRoleName(self, role_name):
        self.driver.find_element(By.XPATH, self.role_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.role_name_xpath).send_keys(role_name)

    def clickCreateRoleBtn(self):
        self.driver.find_element(By.XPATH, self.role_create_btn_xpath).click()

    def dragAndDropRoles(self):
        # # Find all source elements
        # self.source_element = self.driver.find_elements(By.CSS_SELECTOR, "#role-modules-dnd-availableArea")
        # self.target_element = self.driver.find_element(By.CSS_SELECTOR, '#role-modules-dnd-selectedArea')
        #
        # self.actions = ActionChains(self.driver)
        #
        # # for source_element in source_elements:
        # self.actions.click_and_hold(self.source_element).move_by_offset(0, 100).move_to_element(self.target_element).release().perform()
        # # Optionally add a pause if needed
        # # time.sleep(1)
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        self.source_element = wait.until(
            EC.visibility_of_element_located((By.ID, 'role-modules-dnd-availableArea')))
        self.target_element = wait.until(EC.visibility_of_element_located((By.ID, 'role-modules-dnd-selectedArea')))

        self.actions = ActionChains(self.driver)
        self.actions.click_and_hold(self.source_element).move_to_element(self.target_element).release().perform()

        time.sleep(3)

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, "//button[@id='role-modules-submit-button']").click()
