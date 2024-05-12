import datetime
import time
import winsound

def Alarm():
    try:
        alarm_time = input("Enter the time to set in the format : HH:MM AM/PM ")
        alarm_time = datetime.datetime.strptime(alarm_time, '%I:%M %p')
        current_time = datetime.datetime.now()

        while current_time < alarm_time:
            current_time = datetime.datetime.now()

        print("Time to wake up!")
        winsound.Beep(1000, 1000)  # Beep for 1 second
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM format.")
Alarm()