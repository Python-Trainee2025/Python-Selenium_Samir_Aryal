'''
move_to element
click
context click
click and hold
perform
key Down
key up

'''
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_demo_action():
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    print("Page Title: ", driver.title)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    time.sleep(4)
    actions= ActionChains(driver)
    product=driver.find_element(By.CLASS_NAME,'inventory_item_name ')
    actions.move_to_element(product).click().perform()
    time.sleep(4)
    desc=driver.find_element(By.CLASS_NAME,'inventory_details')
    print(desc.text)
    driver.quit()