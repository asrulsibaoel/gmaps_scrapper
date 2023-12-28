# Import required modules

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# username and access_key is important to run your test on LambdaTest
username = "asrulsibaoel"
access_key = "tvjPqbuUw41FA0M3c0a2gmVpdsropKGtvbL3V4w8iBJ4kJ8jE6"


# Capabilities define the OS, Browser name, and other necessary details
lt_options = {
    "user": username,
    "accessKey": access_key,
    "build": "First build",
    "name": "First Test",
    "platformName": "Windows 10",
    "video": True,
    "w3c": True,  # informing latest Selenium 4 being used
    "browserName": "Chrome",
    "browserVersion": "114.0",
    "selenium_version": "4.8.0",
}


def test_app():
    # To run the test on the platform
    remote_url = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    browser_options = ChromeOptions()
    browser_options.add_argument("--ignore-certificate-errors")
    browser_options.add_argument("--headless")

    # adding the capability to the chrome
    browser_options.set_capability("LT:Options", lt_options)

    # initializing remote server
    driver = webdriver.Remote(command_executor=remote_url, options=browser_options)
    driver.get("https://www.amazon.com/")
    search_for_key = driver.find_element(By.ID, "twotabsearchtextbox")
    search_for_key.send_keys("iphone 14")
    search_btn = driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
    search_btn.click()
    driver.close()
