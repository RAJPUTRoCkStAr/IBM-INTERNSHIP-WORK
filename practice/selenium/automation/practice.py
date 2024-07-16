import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




driver = webdriver.Chrome()



driver.get("https://www.google.com/")


input_field = driver.find_element(By.CLASS_NAME,"gLFyf")

input_field.send_keys("Tech With Tim")
input_field.send_keys(Keys.ENTER)

# WebDriverWait(driver,5).until(
#     ec.presence_of_element_located((By.PARTIAL_LINK_TEXT,"sunday"))
# )

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
link.click()

time.sleep(38)
driver.quit()