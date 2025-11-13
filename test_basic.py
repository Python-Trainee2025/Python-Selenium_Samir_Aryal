import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_demo():
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    print("Page Title: ", driver.title)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    #explicit
    wait=WebDriverWait(driver,30)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"title")))
    driver.quit()