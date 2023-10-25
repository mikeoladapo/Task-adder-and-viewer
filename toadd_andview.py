#!/usr/bin/python3
"""Class: Task"""


class Task:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
        self.status = False

    def add_to_list(self):
        self.lis.append(self)

    def viewtasks(self):
        print(f'Title: {task.title}, Date: {task.date}, Time: {task.time}')

    def completed(self):
        self.status = True


tasklist = []

handle1 = input('Enter title: ')
handle2 = input('Enter date: ')
handle3 = input('Enter time: ')


tas = Task(handle1, handle2, handle3)
tasklist.append(tas)
for task in tasklist:
    task.viewtasks()
