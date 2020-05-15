import tkinter as tk
from apiCalls import *
from datetime import datetime
import os


class Table:

    def __init__(self):
        format = 'Formats must be as the following: '
        date_format = 'Start Date: yyyy, mm, dd'
        duration_format = 'Duration as number of days: #'
        dep_format = 'Dependencies: previous task, previous task, ect'
        self.fields = []
        self.master = tk.Tk()
        tk.Label(self.master, text="Table Name: ").grid(row=0, column=0)
        tk.Label(self.master, text="Task").grid(row=1, column=0)
        tk.Label(self.master, text="Start Date").grid(row=1, column=1)
        tk.Label(self.master, text="Duration").grid(row=1, column=2)
        tk.Label(self.master, text="Dependencies").grid(row=1, column=3)

        tk.Label(self.master, text=format).grid(row=2, column=5)
        tk.Label(self.master, text=date_format).grid(row=3, column=5)
        tk.Label(self.master, text=duration_format).grid(row=4, column=5)
        tk.Label(self.master, text=dep_format).grid(row=5, column=5)
        self.rows = 2
        self.columns = 4

    def create_gantt(self):
        schedule = Schedule()
        name = self.fields[0][0].get()
        schedule.create_gantt(name)
        for row in self.fields:
            strings = []
            for data in row:
                if len(data.get()) != 0:
                    strings.append(data.get())
            if len(strings) == 3:

                date = datetime.strptime(strings[1], '%Y, %m, %d')
                schedule.add_new_task(strings[0], date, int(strings[2]))
            elif len(strings) == 4:
                print(strings[1])
                dep_list = []
                date = datetime.strptime(strings[1], '%Y, %m, %d')
                dependencies = strings[3].split(', ')
                for depend in dependencies:
                    dep_list.append(schedule.tasks.get(depend))
                schedule.add_new_task(strings[0], date, int(strings[2]), dep_list)

        schedule.create_svg(name + '.svg', datetime(2020, 11, 20))
        os.system(name + '.svg')

    def create_table(self, num_tasks):

        self.rows += num_tasks
        e1 = tk.Entry(self.master)
        e1.grid(row=0, column=1)
        temp = [e1]
        self.fields.append(temp)

        for x in range(2, self.rows):
            temp = []
            for y in range(0, self.columns):
                e1 = tk.Entry(self.master)
                e1.grid(row=x, column=y)
                temp.append(e1)
            self.fields.append(temp)
        tk.Button(self.master, text='Quit', command=lambda: self.master.quit).grid(row=self.rows + 1, column=1,
                                                                                   sticky=tk.W, pady=4)

        tk.Button(self.master, text='Generate Gantt', command=lambda: self.create_gantt()).grid(row=self.rows + 1,
                                                                                                column=0, sticky=tk.W,
                                                                                                pady=4)
        self.rows += 1

    def display(self):
        self.master.mainloop()
