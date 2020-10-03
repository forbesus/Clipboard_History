#!/usr/bin/env python3.8

from functions import create_folder, create_file_dynamic, append_file
from clipboard import paste
from os import chdir
from time import sleep
from variables import folder, limit

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

