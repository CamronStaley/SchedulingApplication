import tkinter as tk
from apiCalls import *
from datetime import datetime


class Table:

    def __init__(self):
        self.fields = []
        self.master = tk.Tk()
        tk.Label(self.master, text="Table Name: ").grid(row=0, column=0)
        tk.Label(self.master, text="Task").grid(row=1, column=0)
        tk.Label(self.master, text="Date").grid(row=1, column=1)
        tk.Label(self.master, text="Duration").grid(row=1, column=2)
        tk.Label(self.master, text="Dependencies").grid(row=1, column=3)
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
            if len(strings) > 1:
                date = datetime.strptime(strings[1], '%Y, %m, %d')
                schedule.add_new_task(strings[0], date, int(strings[2]))
        schedule.create_svg(name + '.svg', datetime(2020, 11, 20))

    def display_data(self):
        for row in self.fields:
            print()
            for data in row:
                print(data.get(), end=' ')

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
        tk.Button(self.master, text='Quit', command=lambda: self.master.quit).grid(row=self.rows + 1, column=0,
                                                                                 sticky=tk.W, pady=4)

        tk.Button(self.master, text='Show', command=lambda: self.display_data).grid(row=self.rows + 1, column=1,
                                                                                    sticky=tk.W, pady=4)

        tk.Button(self.master, text='Generate Gantt', command=lambda: self.create_gantt()).grid(row=self.rows + 1,
                                                                                                column=2, sticky=tk.W,
                                                                                                pady=4)
        self.rows += 1

    def display(self):
        self.master.mainloop()
