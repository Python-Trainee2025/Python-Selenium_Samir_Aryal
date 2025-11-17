# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
#
# @pytest.mark.parametrize("username,password", [
#     ("standard_user", "secret_sauce"),
#     ("problem_user", "secret_sauce"),
#     ("performance_glitch_user", "secret_sauce")
# ])
# def test_saucedemo_flow(username, password):
#
#     chrome_options = Options()
#     driver = webdriver.Chrome(options=chrome_options)
#
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")
#
#     # ---- LOGIN ----
#     driver.find_element(By.ID, "user-name").send_keys(username)
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(1.5)
#
#
#
#     # ---- ADD ITEMS TO CART (2 items) ----
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
#     time.sleep(1)
#
#     # ---- VIEW CART ----
#     driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
#     time.sleep(1)
#
#     # Check both items are in the cart
#     cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
#     cart_item_names = [item.text for item in cart_items]
#
#     assert "Sauce Labs Backpack" in cart_item_names
#     assert "Sauce Labs Bike Light" in cart_item_names
#
#     # ---- REMOVE ONE ITEM ----
#     driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
#     time.sleep(1)
#
#     # ---- GO BACK TO PRODUCTS PAGE ----
#     driver.find_element(By.ID, "continue-shopping").click()
#     time.sleep(1)
#
#     # ---- OPEN PRODUCT DETAIL PAGE ----
#     driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
#     time.sleep(1)
#
#     # ---- ADD PRODUCT TO CART ----
#     driver.find_element(By.XPATH, "(//a[@id='item_1_title_link'])[1]").click()
#     time.sleep(1)
#
#
#     time.sleep(2)
#     driver.quit()



import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
])
def test_saucedemo_flow(username, password):

    # ---- CHROME OPTIONS TO DISABLE PASSWORD BREACH POPUP ----
    chrome_options = Options()
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # ---- LOGIN ----
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1.5)

    # Verify login succeeded (important for parameterization)
    assert "inventory" in driver.current_url, f"{username} FAILED to log in."

    # ---- ADD ITEMS TO CART ----
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(1)

    # ---- VIEW CART ----
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # ---- VERIFY ITEMS IN CART ----
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_item_names = [item.text for item in cart_items]

    assert "Sauce Labs Backpack" in cart_item_names
    assert "Sauce Labs Bike Light" in cart_item_names

    # ---- REMOVE ONE ITEM ----
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(1)

    # ---- BACK TO PRODUCTS PAGE ----
    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(1)

    # ---- OPEN PRODUCT DETAIL PAGE ----
    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
    time.sleep(1)

    # ---- ADD PRODUCT TO CART ----
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(1)

    # ---- VERIFY FINAL CART ----
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    final_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    final_names = [item.text for item in final_items]

    assert "Sauce Labs Bolt T-Shirt" in final_names
    assert "Sauce Labs Backpack" not in final_names  # removed earlier

    driver.quit()



