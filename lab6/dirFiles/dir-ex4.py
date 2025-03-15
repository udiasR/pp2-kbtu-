import os

def count_lines(file_path):
    counter = 0
    with open(file_path, 'r') as file:         #with statement ensures the file automatically closes after reading.
        for line in file:
            counter += 1
    return counter


print("Number of lines:", count_lines(r"/home/hp/Documents/pp2-kbtu-/lab7/new.py"))