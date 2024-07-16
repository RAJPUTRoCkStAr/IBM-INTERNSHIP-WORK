from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import schedule
import time
from datetime import datetime
import pytz

    
def classjoin():
    url = "https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_OGI5NzEwMmYtOGNmYi00ZDE4LWE0OWYtM2IyYjVhMDQzNjA5%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%2522ad06ef22-d6dc-4a55-b4c1-c3a158f5f147%2522%252c%2522Oid%2522%253a%2522f5189c02-948d-412e-b57d-ddba1481ffc7%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=9b291eb1-1102-425f-a8d2-482af9f1fdff&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true" 
    driver = webdriver.Chrome()
    driver.get(url)

    join_btn = driver.find_element(By.XPATH,"//div[@class='buttonsContainer']//button[1]")
    join_btn.click()

    input_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Type your name']"))
        )
    input_name.send_keys("Sumit Kumar Singh Bengaluru")


    last_btn = driver.find_element(By.ID, "prejoin-join-button")
    last_btn.click()

    time.sleep(10800)

    driver.quit()
def job_with_timezone():
    now = datetime.now(pytz.timezone('Asia/Kolkata'))
    if now.hour == 10 and now.minute == 30:
        classjoin()
schedule.every().monday.do(job_with_timezone)
schedule.every().wednesday.do(job_with_timezone)
schedule.every().friday.do(job_with_timezone)
while True:
    schedule.run_pending()