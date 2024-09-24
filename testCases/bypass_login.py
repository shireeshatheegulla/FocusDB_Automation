from selenium import webdriver
import json
import time

# Path to your localStorage JSON file
local_storage_file = '/assets/localStorageData.json'

# Load the localStorage data from the JSON file
with open(local_storage_file, 'r') as file:
    local_storage_data = json.load(file)

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH

# Open the desired URL where you want to set the localStorage
driver.get('https://dev-focus.testd.com/')  # Replace with your website

# Wait for the page to load completely
time.sleep(2)

# Iterate over the localStorage data and set each item
for key, value in local_storage_data.items():
    # Convert the value back to a string if it's not already
    if isinstance(value, dict) or isinstance(value, list):
        value = json.dumps(value)
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

# Refresh the page to apply the localStorage changes
driver.refresh()

# Now the localStorage is set, and you can interact with the page
time.sleep(100)  # Keep the browser open for a while
