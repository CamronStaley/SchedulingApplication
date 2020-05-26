import tkinter as tk
from schedule import *
from datetime import datetime
import os
from calWidget import *


class Table:

    task_col = 0
    dur_col = 1
    dep_col = 2

    def __init__(self):
        format = 'Formats must be as the following: '
        date_format = 'Start Date: yyyy, mm, dd'
        duration_format = 'Duration as number of days: #'
        dep_format = 'Dependencies: previous task, previous task, ect'
        self.fields = []
        self.master = tk.Tk()
        self.buttons = {}
        self.dates = {}
        tk.Label(self.master, text="Table Name: ").grid(row=0, column=0)
        tk.Label(self.master, text="Task").grid(row=1, column=0)
        tk.Label(self.master, text="Start Date").grid(row=1, column=1)
        tk.Label(self.master, text="Duration").grid(row=1, column=2)
        tk.Label(self.master, text="Dependencies").grid(row=1, column=3)

        tk.Label(self.master, text=format).grid(row=2, column=5)
        tk.Label(self.master, text=duration_format).grid(row=3, column=5)
        tk.Label(self.master, text=dep_format).grid(row=4, column=5)
        self.rows = 2
        self.columns = 4

    def create_gantt(self):
        schedule = Schedule()
        name = self.fields[0][0].get()
        schedule.create_gantt(name)
        it = 0
        strings = []
        for row in self.fields:
            it += 1
            strings.clear()
            for data in row:
                if len(data.get()) != 0:
                    strings.append(data.get())

            if len(strings) == 2:
                schedule.add_new_task(strings[0], self.dates[it], int(strings[1]))

            elif len(strings) == 3:
                dependencies = strings[2].split(', ')
                dep = []
                for depend in dependencies:
                    dep.append(schedule.tasks.get(depend))
                schedule.add_new_task(strings[0], self.dates[it], int(strings[1]), dep)

        schedule.create_svg(name + '.svg', datetime(2020, 5, 26))
        os.system(name + '.svg')

    def print_sel(self, cal, col, root):
        self.buttons[col].set(cal.selection_get())
        date = self.buttons[col].get()
        date = date.split('-')
        date = (date[0] + ', ' + date[1] + ', ' + date[2])
        date = datetime.strptime(date, '%Y, %m, %d')
        self.dates[col] = date
        root.destroy()

    def get_date(self, x):
        root = tk.Tk()
        s = ttk.Style(root)
        s.theme_use('clam')
        top = tk.Toplevel(root)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=lambda calendar=cal, col=x, r=root: self.print_sel(calendar, col, r)).pack()
        root.withdraw()

    def create_table(self, num_tasks):

        self.rows += num_tasks
        e1 = tk.Entry(self.master)
        e1.grid(row=0, column=1)
        temp = [e1]
        self.fields.append(temp)

        for x in range(2, self.rows):
            temp = []
            for y in range(0, self.columns):
                if y is not 1:
                    e1 = tk.Entry(self.master)
                    e1.grid(row=x, column=y)
                    temp.append(e1)
                else:
                    btn_text = tk.StringVar()
                    tk.Button(self.master, textvariable=btn_text, command=lambda col=x: self.get_date(col), height=1,
                                    width=15).grid(row=x, column=y)
                    btn_text.set('Select Date')
                    self.buttons[x] = btn_text
            self.fields.append(temp)

        tk.Button(self.master, text='Quit', command=lambda: self.master.quit).grid(row=self.rows + 1, column=1,
                                                                                   sticky=tk.W, pady=4)
        tk.Button(self.master, text='Generate Gantt', command=lambda: self.create_gantt()).grid(row=self.rows + 1,
                                                                                                column=0, sticky=tk.W,
                                                                                                pady=4)
        self.rows += 1

    def display(self):
        self.master.mainloop()
