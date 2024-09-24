import time

from selenium.webdriver.common.action_chains import ActionChains
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
        dashboard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='role-modules-dnd-availableBox-0']"))
        )
        target_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='role-modules-dnd-selectedArea']"))
        )

        # Initialize ActionChains
        actions = ActionChains(self.driver)

        # Perform the drag-and-drop action
        # actions.drag_and_drop(dashboard, target_element).perform()
        actions.click_and_hold(dashboard).move_to_element(target_element).release().perform()

        # Pause for 2 seconds to observe the result
        time.sleep(5)

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, "//button[@id='role-modules-submit-button']").click()
