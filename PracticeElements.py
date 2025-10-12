# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.find_element(By.ID,'userName').send_keys('Atul')
driver.find_element(By.ID,'userEmail').send_keys('mishraatul930@gmail.com')


