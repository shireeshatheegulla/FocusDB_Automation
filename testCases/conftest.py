from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import warnings


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or edge")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser", default="chrome")
    # service = Service("C:/Users/91990/PycharmProjects/python-selenium-automation/driver/chromedriver.exe")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1280,720")
        #  chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-browser-side-navigation")
        # chrome_options.add_argument("--disable-gpu-sandbox")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3")

        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.delete_all_cookies()
        driver.execute_cdp_cmd("Network.clearBrowserCache", {})
        driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
        driver.implicitly_wait(10)
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = driver
    yield
    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to use for testing")


# ------code to generate html report--------
@pytest.fixture(scope="session", autouse=True)
def add_environment(metadata):
    metadata["environment"] = {
        "Project Name": "FocusDB",
        "Browser": "Chrome",
        "QA": "Shireesha Theegulla"
    }
