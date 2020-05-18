import time
import datetime
import schedule


print(datetime.datetime.now().time())


def job():
    print("Hello from scheduler")


schedule.every().day.at("07:41").do(job)
while True:
    schedule.run_pending()
