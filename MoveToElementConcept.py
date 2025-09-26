# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com/")
driver.maximize_window()

# login_ele = driver.find_element(By.XPATH,"//div[text()='Login']")
# time.sleep(5)
action_chains = ActionChains(driver)
# action_chains.move_to_element(login_ele).click().perform()
travel_policies = driver.find_element(By.XPATH,"//div[text()='Travel Policies']")
action_chains.move_to_element(travel_policies).perform()
time.sleep(5)
passenger_support = driver.find_element(By.XPATH,"//div[text()='Passenger Support']")
passenger_support.click()


time.sleep(5)
