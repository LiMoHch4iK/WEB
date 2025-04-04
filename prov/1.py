import schedule
import datetime


def func(message_print, check_not):
    hour = datetime.datetime.now().hour
    if hour != 0:
        if check_not[0] <= check_not[1]:
            if not (check_not[0] <= hour <= check_not[1]):
                for i in range(hour):
                    print(message_print)
                print()

        elif check_not[0] > hour > check_not[1]:
            for i in range(hour):
                print(message_print)
            print()


message = input()

silence = input('Введите время молчания (пример ввода: 00-07): ').split('-')
try:
    silence[0], silence[1] = int(silence[0]), int(silence[1])
    assert not (silence[0] < 0 or silence[1] < 0 or silence[1] >= 24 or silence[0] >= 24)
except ValueError:
    quit()
except AssertionError:
    quit()
except IndexError:
    quit()

schedule.every().hour.at(':00').do(func, message_print=message, check_not=silence)

while True:
    schedule.run_pending()
