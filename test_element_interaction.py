"""
send_keys()	-> element.send_keys("text")
click()-> element.click()
clear()	_>	element.clear()
text ->	print(element.text)
get_attribute()	_> element.get_attribute("href")
"""



import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_demo_list_items():
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    user_list=driver.find_elements(By.XPATH,'//div[@id="login_credentials"]')
    time.sleep(2)
    accepted_user=[]
    for i in user_list:
        print(i.text)
        accepted_user.append(i.text)
    print(accepted_user)
    raw_text=accepted_user[0]
    print(raw_text)
    new_text=raw_text.split("\n")
    print(new_text)
    final=new_text[1:]
    print(final)