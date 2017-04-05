import sched
import time
import urllib.request as ur
from secret import CRON_KEY

s = sched.scheduler(time.time, time.sleep)
KEY = CRON_KEY
count = 0


def run_cron(sc):
    global count
    count += 1
    print("Refreshing email queue for registrer.fsff.no, "
          "it has happend {} times".format(count))
    cron = ur.urlopen(
        "http://registrer.fsff.no/cron?cron_key={}".format(CRON_KEY))
    sl = cron.read()
    s.enter(20, 1, run_cron, (sc,))

s.enter(1, 1, run_cron, (s,))
s.run()
