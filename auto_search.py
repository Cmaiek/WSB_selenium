from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://encrypted.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("wsb tester wroclaw")
elem.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "res")))

driver.quit()
