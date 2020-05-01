"""Script: process file data"""

import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import glob #to create file name from variable
import matplotlib.pyplot as plt
import numpy as np

#import functions
from Parse_File import get_date, case_num

total_num = 0
x_axis = []
y_axis = []

#extract data from press releases
with open("daily_new_cases.txt", "w+") as file:
    file.write("Date" + 7*" " + "New Cases\n")
    for name in glob.glob('[0-9][0-9][0-9][0-9]-[0-9][0-9]*.txt'):
        number = case_num(name)
        date = get_date(name)
        if number:
            file.write(f"{date:{10}} {number}\n")
            total_num = total_num + int(number)
            x_axis.append(date)
            y_axis.append(int(number))

print("Created new file of daily new cases.")
print(f"Total number of cases: {total_num}")

#plot daily new cases
plt.plot(y_axis)
plt.grid(axis='y', linestyle='-')
plt.xlabel('days since first case')
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
#ax.axes.yaxis.set_ticks([])
plt.show()
