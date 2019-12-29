import logging
from datetime import datetime, date

#* Time
now = datetime.now()
time = now.strftime('%H:%M:%S').split(':')
year = date.today().year
month = date.today().month
day = date.today().day

logs = 'C:/Users/Neron4ik/Documents/maya/projects/Programming/scripts/logs/'
file_name = 'examaple_{}_{}_{}_{}_{}_{}.log'.format(year, month, day, time[0], time[1], time[2])
final_path = logs + file_name

with open(final_path, 'w') as infile:
    print('')



path = final_path

logging.basicConfig(filename=path,
                    filemode='w',
                    level= logging.DEBUG,
                    format='[%(asctime)s.%(module)s.%(funcName)s.%(lineno)d] %(levelname)s:%(message)s' )



def Foo1():

    a = 1
    if a == 1:
        logging.warning('A is set to 0')
    b = 2
    print(a + b)

def Foo2():
    
    a = 1
    b = 2
    logging.debug('A is 1, b is 2')
    print(a - b)

    logging.warning('This is warning')

    logging.error('This is error')
    
Foo1()
Foo2()