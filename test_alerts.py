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
    driver.get("https://demoqa.com/alerts")
    alert_element=driver.find_element(By.ID,'promtButton')

    time.sleep(2)
    alert_element.click()
    time.sleep(2)

    alert=driver.switch_to.alert
    print(alert.text)
    time.sleep(5)
    alert.send_keys("this is a test ")
    time.sleep(5)
    alert.accept()

    driver.quit()