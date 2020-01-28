from clipboard import *
from time import sleep

previous = ""
while True:
    data = paste()
    if data != previous:
        print(data)
        previous = data
    else:
        sleep(0.2)
