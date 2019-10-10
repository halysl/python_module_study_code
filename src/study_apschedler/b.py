from a import test_Schedule
import time

def main():
    test_Schedule.start()
    while 1:
        # do your stuff...
        time.sleep(10)
        print(time.time())


if __name__ == "__main__":
    main()
