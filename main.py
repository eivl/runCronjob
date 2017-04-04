import sched
import time
import urllib.request as ur

s = sched.scheduler(time.time, time.sleep)


def run_cron(sc):
    print("Doing stuff...")
    cron = ur.urlopen("http://registrer.fsff.no/cron?cron_key=8BQlz1y9E1l5Z09yOyiMjLgvY6P9U6YD")
    sl = cron.read()
    s.enter(60, 1, run_cron, (sc,))

s.enter(60, 1, run_cron, (s,))
s.run()
