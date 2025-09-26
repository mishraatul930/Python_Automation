from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.ID,'justAnInputBox').click()

def select_values(option_list,value):
    if not value[0] == 'all':
        for ele in option_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in option_list:
                ele.click()
        except Exception as e:
            print(e)


drop_list = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
value_list = ['choice 7']

select_values(drop_list, value_list)