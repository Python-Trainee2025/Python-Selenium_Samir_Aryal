import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")


credentials = []
username = driver.find_element(By.ID, "login_credentials")
for i in credentials:
    print(i)
    credentials.append(i)
print(username.text)
time.sleep(2)

