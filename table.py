import tkinter as tk


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
        tk.Button(self.master, text='Quit', command=self.master.quit).grid(row=self.rows + 1, column=0, sticky=tk.W,
                                                                           pady=4)
        tk.Button(self.master, text='Show', command=self.display_data).grid(row=self.rows + 1, column=1, sticky=tk.W,
                                                                            pady=4)
        self.rows += 1

    def display(self):
        self.master.mainloop()
