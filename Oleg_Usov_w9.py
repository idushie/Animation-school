import re
from datetime import date, datetime
import logging
import os

#! Current data and time for export file

now = datetime.now()
time = now.strftime('%H:%M:%S').split(':')
year = date.today().year
month = date.today().month
day = date.today().day

#! Find directory and create folder
this_file = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file)
logs =  os.path.join(this_dir, 'logs')

#! Exeption if folder already exists
try:
    os.mkdir(logs)
except OSError:
    print('Creation faild')

#! Name of export file
file_name = r'\log_{}_{}_{}_{}_{}_{}.log'.format(year, month, day, time[0], time[1], time[2])
final_Path = logs + file_name


logging.basicConfig(filename= final_Path,
                    filemode= 'w',
                    level= logging.DEBUG,
                    format='%(message)s')

#! Decoratar, open file, do something, close file
def file_path(file_path):

    def decorator(func):
    
        def wrapper(*args, **kwargs):
        
            file_name = file_path

            file_open = open(file_name, 'r')
            
            data = file_open.read().split()

            filtered_file_name = file_name + '_filtered.txt'
            result_file = open(filtered_file_name,'w')

            for digit in func(data):
                print (digit)
                result_file.write(digit + '\n')

            file_open.close()
            result_file.close()

        return wrapper

    return decorator

#! Find digits and filter it
@file_path('dump.txt')
def search_for_digits(source = None):
    
    for number, line in enumerate(source):
        
        regexp = re.match(r'\A[+-]?(?!0{2,6})\d{1,6}(\.\d*)?\Z', line) #TODO refactor with lamda
        
        add_number = number +1
        
        if regexp:
            logging.debug('line ' + str(add_number) +': ' + line + ' -' + ' test passed')

            yield regexp.group()

        else:
            logging.debug('line ' + str(add_number) +':' + line + ' -' + ' test failed')


search_for_digits()

