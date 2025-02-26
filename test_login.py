import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def browser():
    # Set up the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Clean up: Close the browser
    driver.quit()

def test_login_with_valid_credentials(browser):
    browser.get("https://demo.guru99.com/Agile_Project/Agi_V1/")
    time.sleep(2)  # Wait for 2 seconds to observe the page load

    login_page = LoginPage(browser)
    login_page.enter_username("1303")
    time.sleep(2)  # Wait for 2 seconds to observe the username input
    login_page.enter_password("Guru99")
    time.sleep(2)  # Wait for 2 seconds to observe the password input
    login_page.click_login()
    time.sleep(2)  # Wait for 2 seconds to observe the login action

    # Wait for the title to contain "Guru99 Bank Customer HomePage"
    WebDriverWait(browser, 5).until(
        EC.title_contains("Guru99 Bank Customer HomePage")
    )
    assert "Guru99 Bank Customer HomePage" in browser.title

def test_login_with_invalid_username(browser):
    browser.get("https://demo.guru99.com/Agile_Project/Agi_V1/")
    time.sleep(2)  # Wait for 2 seconds to observe the page load

    login_page = LoginPage(browser)
    login_page.enter_username("invalid_user")
    time.sleep(2)  # Wait for 2 seconds to observe the username input
    login_page.enter_password("Guru99")
    time.sleep(2)  # Wait for 2 seconds to observe the password input
    login_page.click_login()
    time.sleep(2)  # Wait for 2 seconds to observe the login action

    # Handle the alert or check for an error message on the page
    try:
        alert = browser.switch_to.alert
        assert "User or Password is not valid" in alert.text
        alert.accept()  # Close the alert
    except NoAlertPresentException:
        # If no alert is present, check for an error message on the page
        error_message = login_page.get_error_message()
        assert "User or Password is not valid" in error_message

def test_login_with_invalid_password(browser):
    browser.get("https://demo.guru99.com/Agile_Project/Agi_V1/")
    time.sleep(2)  # Wait for 2 seconds to observe the page load

    login_page = LoginPage(browser)
    login_page.enter_username("1303")
    time.sleep(2)  # Wait for 2 seconds to observe the username input
    login_page.enter_password("invalid_pass")
    time.sleep(2)  # Wait for 2 seconds to observe the password input
    login_page.click_login()
    time.sleep(2)  # Wait for 2 seconds to observe the login action

    # Handle the alert
    alert = browser.switch_to.alert
    assert "User or Password is not valid" in alert.text
    alert.accept()  # Close the alert

def test_login_with_empty_fields(browser):
    browser.get("https://demo.guru99.com/Agile_Project/Agi_V1/")
    time.sleep(2)  # Wait for 2 seconds to observe the page load

    login_page = LoginPage(browser)
    login_page.click_login()
    time.sleep(2)  # Wait for 2 seconds to observe the login action

    # Handle the alert or check for an error message on the page
    try:
        alert = browser.switch_to.alert
        assert "User or Password is not valid" in alert.text
        alert.accept()  # Close the alert
    except NoAlertPresentException:
        # If no alert is present, check for an error message on the page
        error_message = login_page.get_error_message()
        assert "User or Password is not valid" in error_message