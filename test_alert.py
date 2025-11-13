import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def alert(driver):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demoqa.com/alerts")

    alert = driver.find_element(By.ID, "alertButton")
    alert.click()
    time.sleep(2)