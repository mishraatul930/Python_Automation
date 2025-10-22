# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'rct-collapse-btn').click()
driver.find_element(By.XPATH,"//span[text()='Documents']").click()
driver.find_element(By.XPATH,"//span[text()='Downloads']").click()
# driver.find_element(By.CLASS_NAME,'rct-checkbox').click()
time.sleep(5)