import schedule
import time
from src.services import PointsBotDispatcher, BirthdayBotDispatcher


def send_birthday_message():
    BirthdayBotDispatcher.call()


def send_points_message():
    PointsBotDispatcher.call()

def sent_positivity_message():
    PositivityBotDispcher.call()

#def send_reminder_message():
# RemiderBotDispacher.cal()

if __name__ == '__main__':
    schedule.every().day.at("06:00").do(send_birthday_message)
    schedule.every(25).to(30)days.at("06:30").do(send_points_message)
    Schedule.every().monday.at("06:00").do(sent_positivity_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
