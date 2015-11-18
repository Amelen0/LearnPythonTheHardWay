#! usr/bin/ env Python3
# stopwatch.py

import time

try:
    while True:
      input()
      lapTime = round(time.time() - lastTime, 2)
      totalTime = round(time.time() - startTime, 2)
      print('Lap #%s:')
