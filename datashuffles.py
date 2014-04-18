#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"

import csv
from collections import defaultdict


def put_csv_in_shoplist():
    shoplist = []
    with open('test_train.csv', 'rb') as testfile:
        reader = csv.reader(testfile, delimiter=',', quotechar='|')
        for row in reader:
            shoplist.append(row)
    return shoplist
    #print headless_list[0][0]
    #return headless_list

def remove_header():
    wholeshoplist = []
    wholeshoplist = put_csv_in_shoplist()
    wholeshoplist.pop(0)
    headlesslist = wholeshoplist
    return headlesslist




def count_points_per_customer():
    customer_estimates = defaultdict(list)
    customerpoints = []
    #print remove_header()
    customerpoints = remove_header()
    for point in customerpoints:
        customer_id = point[0]
        #print point, customer_id
        customer_estimates[customer_id].append(1)
        if point[3] == '0':
            3
        #print customer_id, customer_estimates[customer_id]
    return customer_estimates

def total_customer_points():
    countedpoints =count_points_per_customer()
    total_customer = defaultdict(int)
    for customer in countedpoints:
        total_customer[customer]= len(countedpoints[customer])
    return total_customer


#def make_dict








