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
        actions = ActionChains(self.driver)

        # Wait until the target element is present
        target_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="role-modules-dnd-selectedArea"]'))
        )

        # Get all source elements
        source_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="role-modules-dnd-availableArea"]/*'))
        )

        # Loop through each source element and perform drag and drop
        for source_element in source_elements:
            # Start the drag-and-drop operation
            actions.click_and_hold(source_element).perform()
            start_time = time.time()

            # Calculate the distance to drag (adjust as needed)
            distance = 100  # Example: 100 pixels downward

            # Perform the drag action over 200 milliseconds
            while (time.time() - start_time) < 0.2:
                actions.move_by_offset(0, distance / 2).perform()
                time.sleep(0.1)  # Sleep to control the duration of the drag

            actions.move_to_element(target_element).release().perform()

            # Optional: Pause for 2 seconds to observe the drag-and-drop action
            time.sleep(1)  # Adjust the sleep time as needed

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, "//button[@id='role-modules-submit-button']").click()
