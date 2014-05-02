#This version runs the classifer for A through G.

import csv



last = open('renu.csv','w')

with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        print row[3]




