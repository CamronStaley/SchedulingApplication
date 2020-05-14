import datetime
import gantt


class Schedule:

    def __init__(self):
        gantt.define_font_attributes(fill='black', stroke='black',   stroke_width=0, font_family="Verdana")
        self.chart = None
        self.tasks = {}

    def create_gantt(self, title):
        self.chart = gantt.Project(name=title)

    def add_new_task(self, name, start, duration, dependencies=[]):

        if len(dependencies) > 0:
            task = gantt.Task(name=name, start=start, duration=duration, depends_of=dependencies)
        else:
            task = gantt.Task(name=name, start=start, duration=duration)
        self.chart.add_task(task)
        self.tasks[name] = task

    def create_svg(self, filename, today_date):
        self.chart.make_svg_for_tasks(filename=filename, today=today_date)

