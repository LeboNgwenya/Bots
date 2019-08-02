import schedule
import time
from src.services import PointsBotDispatcher, BirthdayBotDispatcher, PositivityBotDispcher, ReminderBotDispacher, UserEngagementDispatcher


def send_birthday_message():
    BirthdayBotDispatcher.call()


def send_points_message():
    PointsBotDispatcher.call()

def send_positivity_message():
    PositivityBotDispcher.call()

def send_reminder_message():
    ReminderBotDispacher.call()

def send_engagement_message():
    UserEngagementDispatcher.call()


if __name__ == '__main__':
    schedule.every().day.at("06:00").do(send_birthday_message)
    schedule.every(25).to(30)days.at("06:30").do(send_points_message)
    schedule.every().monday.at("06:00").do(send_positivity_message)
    schedule.every(25).to(30)days.at("08:00").do(send_engagement_message)


    while True:
        schedule.run_pending()
        time.sleep(1)

