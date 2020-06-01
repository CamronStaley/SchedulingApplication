import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from schedule import *
from datetime import datetime
import os


# this class contains the table gui
class Table:

    task_col = 0
    dur_col = 1
    dep_col = 2

    def __init__(self):

        self.fields = []
        self.master = tk.Tk()
        self.date_vars = {}
        self.dates = {}
        self.dep_strings = {}
        self.dep_vars = {}
        # creating labels
        tk.Label(self.master, text="Table Name: ").grid(row=0, column=0)
        tk.Label(self.master, text="Task").grid(row=1, column=0)
        tk.Label(self.master, text="Start Date").grid(row=1, column=1)
        tk.Label(self.master, text="Duration").grid(row=1, column=2)
        tk.Label(self.master, text="Dependencies").grid(row=1, column=3)

        self.rows = 2
        self.columns = 4

    # go through the data fields and get the data to put into the gantt chart
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
            # has no dependencies (just task and duration)
            if len(strings) == 2 and it not in self.dep_strings:
                schedule.add_new_task(strings[0], self.dates[it], int(strings[1]))
            # has dependencies
            elif len(strings) == 2:
                print("In has dependencies")
                print(it)
                print(self.dep_strings[it])
                schedule.add_new_task(strings[0], self.dates[it], int(strings[1]), schedule.get_task_list(self.dep_strings[it]))
        name = name.replace(' ', '_')
        schedule.create_svg(name + '.svg', datetime(2020, 5, 26))
        os.system(name + '.svg')

    # returns the date selection
    def print_sel(self, cal, col, root):
        self.date_vars[col].set(cal.selection_get())
        date = self.date_vars[col].get()
        date = date.split('-')
        date = (date[0] + ', ' + date[1] + ', ' + date[2])
        date = datetime.strptime(date, '%Y, %m, %d')
        self.dates[col] = date
        root.destroy()

    def add_deps(self, dep, loc):
        if dep not in self.dep_strings[loc]:
            temp = ''
            self.dep_strings[loc].append(dep)
            for value in self.dep_strings[loc]:
                temp += value + ', '
            temp = temp[0:len(temp) - 2]
            print(temp)
            self.dep_vars[loc].set(temp)

    def get_deps(self, y):
        self.dep_strings[y] = []
        root = tk.Tk()
        frame = Frame(root)
        frame.pack(fill=BOTH, expand=True)
        it = 0
        for row in self.fields:
            it += 1
            strings = []
            for data in row:
                if len(data.get()) != 0:
                    strings.append(data.get())
            if len(strings) > 1 and it < y:
                tk.Button(frame, text=strings[0], command=lambda dep=strings[0], loc=y: self.add_deps(dep, loc)).pack(fill=BOTH, expand=True)
        tk.Button(frame, text='ok', command=lambda: root.destroy()).pack(fill=BOTH, expand=True)

    # prints the gui for date selection
    def get_date(self, x):
        root = tk.Tk()
        s = ttk.Style(root)
        s.theme_use('clam')
        top = tk.Toplevel(root)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=2, day=5)
        cal.pack(fill="both", expand=True)
        button = tk.Button(top, text="ok", command=lambda calendar=cal, col=x, r=root: self.print_sel(calendar, col, r)).pack()
        root.withdraw()

    # generates the table and buttons
    def create_table(self, num_tasks):

        self.rows += num_tasks
        e1 = tk.Entry(self.master)
        e1.grid(row=0, column=1)
        temp = [e1]
        self.fields.append(temp)

        for x in range(2, self.rows):
            temp = []
            for y in range(0, self.columns):
                # if it is not date selection then add an entry
                if y is 1:
                    btn_text = tk.StringVar()
                    tk.Button(self.master, textvariable=btn_text, command=lambda col=x: self.get_date(col), height=1,
                              width=15).grid(row=x, column=y)
                    btn_text.set('Select Date')
                    self.date_vars[x] = btn_text
                elif y is 3:
                    btn_text = tk.StringVar()
                    tk.Button(self.master, textvariable=btn_text, command=lambda row=x: self.get_deps(row), height=1,
                              width=15).grid(row=x, column=y)
                    btn_text.set('Select Dependencies')
                    self.dep_vars[x] = btn_text
                else:
                    e1 = tk.Entry(self.master)
                    e1.grid(row=x, column=y)
                    temp.append(e1)
                # if it is date selection add a button
            self.fields.append(temp)
        tk.Button(self.master, text='Quit', command=lambda: self.master.destroy()).grid(row=self.rows + 1, column=1,
                                                                                   sticky=tk.W, pady=4)
        tk.Button(self.master, text='Generate Gantt', command=lambda: self.create_gantt()).grid(row=self.rows + 1,
                                                                                                column=0, sticky=tk.W,
                                                                                                pady=4)
        self.rows += 1

    def display(self):
        self.master.mainloop()
