"""
implicit wait:
driver.implicitly_wait(10)

explicit wait:
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

fluent wait:
wait = WebDriverWait(driver, 10, poll_frequency=1)
element = wait.until(EC.presence_of_element_located((By.ID, "dynamic-element")))
"""