#!/usr/bin/env python3.8

from functions import *
from clipboard import *
from time import sleep

create_folder(folder)
chdir(folder)
while True:
    file = create_file_dynamic()
    previous = ""
    count = 0
    while count <= limit:
        data = paste()
        if data != previous:
            append_file(file, data)
            previous = data
            count += 1
        else:
            sleep(0.2)

