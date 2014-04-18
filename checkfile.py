#! /usr/bin/env python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"

import csv


def checkheader():
	with open('last_2.csv', 'rb') as testfile:
		first_line = testfile.readline()

		rowheaderlist = first_line.split(',')
		print "rowheaderlist [0] =", rowheaderlist[0]
		print

		return rowheaderlist[0]






