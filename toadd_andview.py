#!/usr/bin/python3
"""Class: Task"""

from datetime import datetime
from time import time

class Task:
    def __init__(self, title):
        self.title = title
        self.date = datetime.now()
        self.time = time()
        self.status = False

    def add_to_list(self):
        self.lis.append(self)

    def viewtasks(self):
        print(f'Title: {task.title}, Date: {task.date}, Time: {task.time}')

    def completed(self):
        self.status = True


tasklist = []

handle1 = input('Enter title: ')
# handle2 = input('Enter date: ')
# handle3 = input('Enter time: ')


tas = Task(handle1)
tasklist.append(tas)
for task in tasklist:
    task.viewtasks()
