# 1. Use the csv module
# 2. Create a csv file
# 3. In every line of the csv file you must write the number and fib(number)
# Docs - https://docs.python.org/3/library/csv.html

'''
    Example:

    fib(0) =, 0
    fib(1) =, 1
    fib(2) =, 1
    fib(3) =, 5
    ...

'''

import csv
from module_example import fib

with open('fib.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile, delimiter=',')

    for i in range(20):       

        #fib_col1="fib("+ str(i) +")"
        fib_col1=f"fib({i})"
        fib_col2=fib(i)
        fib_line=[fib_col1,fib_col2]
       
        writer.writerow(fib_line)