#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"
__date__ ="$Apr 10, 2014 4:55:44 PM$"

import csv
target_cols=['A','B','C','D','E','F','G','C_previous']
f = open('change.csv','w')
last = open('last_2.csv','w')
head_str = []
last_1=[]
last_2=[]
with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row_count=0
    header={}
    previous_row = ""
    previous_id = ""
    cum_change=0
    for row in reader:
        if row_count==0:
            head_count=0
            for head in row:
                header[head]=head_count;
                head_count+=1
                head_str.append(head)
            header['total_change']=head_count
            head_str.append('total_change')
            head_count+=1
            header['cum_change']=head_count
            head_str.append('cum_change')
            for col in target_cols:
                header["old_%s"%col]=head_count
                head_count+=1
                head_str.append("old_%s"%col)
            f.write("%s\n"% ",".join(head_str))
            last.write("%s\n"% ",".join(head_str))
        else:
            outputs = {}
            customer_id = row[0]
            copy_row = list(row)
            total_change = 0
            
            for col in target_cols:
                col_id = header[col]
                copy_row.append(row[col_id])
                val = 0
                if customer_id==previous_id:
                    if row[col_id]<>previous_row[col_id]:
                        val =1
                else:
                    cum_change=0
                copy_row[col_id]= "%s"% val
                total_change+=val
                cum_change+=val
            f.write("%s,%s,%s\n"% (",".join(copy_row),total_change, cum_change))
#            print row[header['shopping_pt']]
            shopping_pt = row[header['shopping_pt']]
            if shopping_pt=="1":
                if len(last_1)>0:
                    last.write("%s\n"%",".join(last_1))
                    last.write("%s\n"%",".join(last_2))
                    last_1=[]
                    last_2=[]    
                last.write("%s\n"%",".join(copy_row))
                
#            if customer_id<>previous_id and row_count>1:
#                last.write("%s\n"%",".join(last_1))
#                last.write("%s\n"%",".join(last_2))
#                last_1=[]
#                last_2=[]
#            else:
            last_1 = list(last_2)
            last_2 = list(copy_row)
            previous_row = row
            previous_id = row[0]
        row_count+=1
    last.write("%s\n"%",".join(last_1))
    last.write(",".join(last_2))
                
