import datetime
import schedule

def ku():
    s = datetime.datetime.now().time().second
    s = 60 if s == 0 else s
    if s % 5 == 0:
        print("Ку" * (s // 5))


schedule.every().seconds.do(ku)
while True:
    schedule.run_pending()