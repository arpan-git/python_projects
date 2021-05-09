def main():
    import time
    from notifypy import Notify
    set_time = input("How long to set a timer for? (hh:mm:ss)\n")
    hr = int(set_time[0:2])
    min = int(set_time[3:5])
    sec = int(set_time[6:8])
    seconds = sec + (60*min) + (3600*hr)
    if type(seconds) == int:
        time.sleep(seconds)
        notification = Notify()
        notification.title = "Timer"
        notification.message = "Time up"
        notification.icon = "D:\Programming\Python\practise\clock.png"
        notification.audio = "D:\Programming\Python\practise\\alarm.wav"
        notification.application_name = "Hello"
        notification.send()
    else:
        print("Time can't be in string form \n")


if __name__ == '__main__':
    main()
