import time
from plyer import notification

while True:
    print("Please Drink some Water!")
    notification.notify(title="Please Drink Some Water!", message = "You need to drink some water",)
    time.sleep(60*60)
