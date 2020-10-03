# Importing required modules
from os import mkdir
from variables import error_folder, dynamic_filename
import datetime


# Function for creating new folder
def create_folder(folder_name):
    created = False
    try:
        mkdir(folder_name)
        created = True
    except FileExistsError:
        pass
    return created


# Function for submitting error
def submit_error(error_text):
    create_folder(error_folder)


# Function for creating dynamic file
def create_file_dynamic(file=dynamic_filename):
    f = open(file, "w")
    string = f"Created on {get_full_datetime()}\n"
    f.write(string)
    f.close()
    return file


# Function for appending into file
def append_file(file_name, data):
    f = open(file_name, "a")
    my_data = f"{get_datetime()}\n" \
              f"------------------------------" \
              f"\n{data}\n" \
              f"_______________________________\n\n\n\n"
    f.write(f"{my_data}\n")
    f.close()


# To Calculate Short DateTime
def get_datetime():
    x = datetime.datetime.now()
    year, month, date = x.year, x.month, x.day
    hour, minute, second, second_ = x.strftime("%I"), x.minute, x.second, x.microsecond
    m = x.strftime("%p")
    now_ = f"{date}/{month}/{year}, {hour}:{minute}:{second}:{str(second_)[0:2]} {m}"
    return now_


# To Calculate Long DateTime
def get_full_datetime():
    x = datetime.datetime.now()
    year, month, date = x.year, x.strftime("%B"), x.day
    week, day, week_ = x.strftime("%A"), x.strftime("%j"), x.strftime("%U")
    hour, minute, second, second_ = x.strftime("%I"), x.minute, x.second, x.microsecond
    m = x.strftime("%p")
    now_ = f"{week}, {date} {month} {year}, " \
           f"{hour}:{minute}:{second}:{str(second_)[0:2]} {m} -- {int(day)} th Day & {int(week_)} th Week\n"
    return now_
