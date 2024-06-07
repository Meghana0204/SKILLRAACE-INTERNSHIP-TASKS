import datetime

def countdown(end_time):
    while True:
        now = datetime.datetime.now()
        if now > end_time:
            print('Time Up!!')
            break
        else:
            time_left = end_time - now
            print('Time left: ', time_left, end="\r")
            time.sleep(1)

# input date and time
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
second = int(input("Enter the second: "))

end_time = datetime.datetime(year, month, day, hour, minute, second)
countdown(end_time)
