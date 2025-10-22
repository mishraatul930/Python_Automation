import pytest

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = None


@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("----------------Setup Activated-------------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.google.com")
    driver.maximize_window()

    yield
    print("-----------------------teardown Activated-------------------")
    driver.quit()

def test_google_title(init_driver):
    assert "Google1" in driver.title, "Title does not match"

def test_google_search(init_driver):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")