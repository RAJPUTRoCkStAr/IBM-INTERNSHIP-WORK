import schedule
import time
from datetime import datetime
import pytz
def job():
    print("I'm working...")
def job_with_timezone():
    now = datetime.now(pytz.timezone('Asia/Kolkata'))
    if now.hour == 10 and now.minute == 4:
        job()
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().friday.at("10:03").do(job)
schedule.every().minute.do(job_with_timezone)
schedule.every().minute.at(":17").do(job)

def job_with_argument(name):
    print(f"I am {name}")

schedule.every(10).seconds.do(job_with_argument, name="Peter")

while True:
    schedule.run_pending()
    time.sleep(1)

#so like this we can schedule for the things we want to do at specific time