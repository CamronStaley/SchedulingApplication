import datetime
import gantt


# This class used for formating and generating the gantt chart
class Schedule:

    # initialize an empty gantt
    def __init__(self):
        gantt.define_font_attributes(fill='black', stroke='black',   stroke_width=0, font_family="Verdana")
        self.chart = None
        self.tasks = {}

    def get_task_list(self, to_find):
        to_return = []
        for item in to_find:
            to_return.append(self.tasks.get(item))
        return to_return

    # set the name of the gantt
    def create_gantt(self, title):
        self.chart = gantt.Project(name=title)

    # adds a task given the name, start date, duration in days, and 0 to many dependencies
    def add_new_task(self, name, start, duration, dependencies=[]):
        if len(dependencies) > 0:
            task = gantt.Task(name=name, start=start, duration=duration, depends_of=dependencies)
        else:
            task = gantt.Task(name=name, start=start, duration=duration)
        self.chart.add_task(task)
        self.tasks[name] = task

    # generate the chart
    def create_svg(self, filename, today_date):
        self.chart.make_svg_for_tasks(filename=filename, today=today_date)


