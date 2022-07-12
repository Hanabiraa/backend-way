"""
task link -> https://stepik.org/lesson/24473/step/2?unit=6777

Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
"""

import csv
import os
import time
from collections import Counter

print(os.getcwd())
os.chdir('./python-way/sandbox/tasks/stepik/data')
print(os.getcwd())

with open('crimes.csv', 'r') as f:
    reader = csv.DictReader(f)
    date_template_ = r'%m/%d/%Y %I:%M:%S %p'
    target_year = 2015
    crimes = [
        crime['Primary Type']
        for crime in reader
        if time.strptime(crime['Date'], date_template_).tm_year == target_year
    ]
    print(Counter(crimes).most_common(1)[0][0])
