# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Renu"
__date__ ="$Apr 3, 2014 3:38:45 PM$"


import csv

def print_matrix(m):
    output={'0':","}
    for l1 in sorted(m):
        for l2 in sorted(m[l1]):
            index = "%s-%s"%(l1,l2)
            output[index]="%s," % index
            output['0']+="%s," % index
            for l3 in sorted(m[l1][l2]):
                for l4 in sorted(m[l1][l2][l3]):
                    output[index]+="%s," % m[l1][l2][l3][l4]
    for out in sorted(output):
        print output[out]

matrix = {'A':{},'B':{},'C':{},'D':{},'E':{},'F':{},'G':{},'C_previous':{}}
matrix2={}
flat = {}
flat2={}
for head in matrix:
    matrix2[head]={}
#    for h2 in head:
#        matrix2[head][h2]=matrix
#print matrix2
with open('test_train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row_count=0
    header={}
    for row in reader:
        if row_count==0:
            head_count=0
            for head in row:
                header[head]=head_count;
                head_count+=1
#            print header
        else:
            outputs = {}
            rec_type=row[header['record_type']]
            for output in matrix:
                index = header[output]
                value = row[index]
#                if not matrix[output].get(value):
#                    matrix[output][value]=0
#                    matrix2[output][value]=matrix
                outputs[output]=value
#            print outputs
            for o1 in outputs:
                key1 = o1
                key2 = outputs[o1]
                for o2 in outputs:
                    key3=o2
                    key4= outputs[o2]
                    col =  "%s%s-%s%s" %(key1,key2,key3,key4)
                    str =  "%s,%s" %(rec_type,col)
#                    print str
                    if not flat.get(col):
                        flat[col]={'0':0,'1':0}
                    if not flat2.get(key1):
                        flat2[key1]={}
                    if not flat2[key1].get(key2):
                        flat2[key1][key2]={}
                    if not flat2[key1][key2].get(key3):
                        flat2[key1][key2][key3]={}
                    if not flat2[key1][key2][key3].get(key4):
                         flat2[key1][key2][key3][key4]=0
                    flat2[key1][key2][key3][key4]+=1
                    
                    flat[col][rec_type]+=1
                    
#                    matrix2[key1][key2][key3][key4]+=1
#                    matrix2[key3][key4][key1][key2]+=1
#                    matrix2[output][value][output][value]=0
#                for output2 in matrix:                    
#                    matrix2[output][value][output2][value]+=1
##                else:
##                    matrix2[output][value][output][value]+=1
##                    print row[index]
#            print row
        
#        print row
        row_count+=1
#print matrix2
#print flat
for i in flat2:
    for j in flat2[i]:
        if not flat2[i][j].get(i):
            flat2[i][j][i]={}
        if not flat2[i][j][i].get(j):
            flat2[i][j][i][j]=0
#print_matrix(flat2)
#print flat2
for f in flat:
    print "%s,%s,%s" % (f, flat[f]['0'],flat[f]['1'])
#print_matrix(matrix2)
#for m in matrix2:
#    str = {}
#    for n in matrix2[m]:
#        str[n]="%s-%s," % (m,n)
#        for o in matrix2[m][n]:
#         str[n]+= "%s,"% matrix2[m][n][o]
#    for s in str:
#        print str[s]
#    print matrix2[m]