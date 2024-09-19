import time
from plyer import notification

if __name__ == "__main__":
    user = input("What message you want? : ")
    timer = int(input("After how much time? : "))
    times = int(input("How many times?"))
    i = 1
    while i<=times:
        notification.notify(
            title = "ALERT!!!",
            message = user,
            timeout = 10
        )
        i += 1
        time.sleep(timer)


