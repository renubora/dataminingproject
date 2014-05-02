#This version runs the random forest classifer for A through G.
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction import DictVectorizer
import csv


features_list=["customer_ID", "day", "state",  "group_size","homeowner","car_age", "age_oldest", "age_youngest","married_couple","C_previous"]

# add to features:
# car_value (bin),risk_factor, cost, prev_actual_A, prev_actual_B, prev_actual_C, prev_actual_D, prev_actual_E, prev_actual_F, prev_actual_G, 1_actual_A,1_actual_B,1_actual_C,1_actual_D,1_actual_E,1_actual_F,1_actual_G

# continue to discard features:
# shopping_pt,time,
# continue to ignore that demographics change across small % of points

# FOR NAIVE BAYES- maybe bucket cost and add it?
# FOR NAIVE BAYES- For test set, when zip matches a training set zip, and there are more than 25 customers, try using zip instead of state (so two different Naive bayes sets and predictions to combine)


#maybe try location sometimes  duration_previous,A,B,C,D,E,F,G,,prev_A,d1_A,1_actual_A,d2_A,prev_actual_A,prev_B,d1_B,1_actual_B,d2_B,prev_actual_B,prev_C,d1_C,1_actual_C,d2_C,prev_actual_C,prev_D,d1_D,1_actual_D,d2_D,prev_actual_D,prev_E,d1_E,1_actual_E,d2_E,prev_actual_E,prev_F,d1_F,1_actual_F,d2_F,prev_actual_F,prev_G,d1_G,1_actual_G,d2_G,prev_actual_G,prev_C_previous,d1_C_previous,1_actual_C_previous,d2_C_previous,prev_actual_C_previous,order
target_list = ["A","B","C","D","E","F","G"]
#target_list = ["A","B"]

#Question- what is array shape needed for input (X), and for y (target)
#Question: should I convert categorical variables to integers:
# http://stackoverflow.com/questions/15821751/how-to-use-dummy-variable-to-represent-categorical-data-in-python-scikit-learn-r
#Question- wonder about +1 to target values

#    print header_map

header_map = {}

test_file = "test_v2_first_0_last_1.csv"

output_file = "RF_output.csv"

def loadHeader(row):
    global header_map
#    cols = row.split(',')
    for i in range(0,len(row)):
        header_map[row[i]]=i

raw_data = []
train_data = []
test_data = []
output = {}


### Try dictionary vectorization
###
###

def make_list_of_dictionaries():
    #train_file = "train_first_0_last_1.csv"
    train_file = "shortplay_first_0_last_1.csv"

    list_dict_file = []
    dict_file = csv.DictReader(open(train_file))
    for row in dict_file:
        list_dict_file.append(row)
    return list_dict_file




# Create the random forest object which will include all the parameters
# for the fit
forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the Survived labels and create the decision trees
#forest = forest.fit(train_data[0::,1::],train_data[0::,0])
#forest = forest.fit(train_data[0::,1::],train_data[0::,0])

# Take the same decision trees and run it on the test data
#output = forest.predict(test_data)



