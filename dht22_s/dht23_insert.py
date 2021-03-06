import os
import datetime
import sqlite3

from time import sleep
#os.chdir('DHT22_py')
import pigpio
pi = pigpio.pi()
import DHT22





while True:
    s = DHT22.sensor(pi, 4)
    s.trigger()
    sleep(0.03)
    humidity = s.humidity() / 1.
    temperature= s.temperature() / 1.
    now_time = datetime.datetime.now()
    print('nowTime : {}'.format(now_time))
    print('humidity : {:3.2f}'.format(s.humidity() / 1.))
    print('temperature : {:3.2f}'.format(s.temperature() / 1.))
    s.cancel()
    sleep(1)
