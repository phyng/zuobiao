# coding: utf-8

import csv



with open('2014data.csv', 'rb') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        row = [x.decode('utf-8') for x in row]
        if i == 0:
            print row
