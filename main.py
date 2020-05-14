from apiCalls import *
from table import *

test1 = Schedule()
test1.create_gantt('Test1')
test1.add_new_task('T1', datetime.date(2020, 11, 20), 6)
test1.add_new_task('T2', datetime.date(2020, 11, 26), 3, [test1.tasks.get('T1')])
test1.add_new_task('T2', datetime.date(2020, 1, 29), 2, [test1.tasks.get('T1'), test1.tasks.get('T2')])
test1.create_svg('test1.svg', datetime.date(2020, 11, 20))

temp = Table()
temp.create_table(10)
temp.display()
