#This version runs the classifer for A through G.
import nltk
import csv

def first_feature (row):
	
	day = row[3]
	state = row[5]
	location = row[6]
	groupSize = row[7]
	homeOwner = row[8]
	carAge = row[9]
	carValue = row[10]
	ageOldest = row[11]
	ageYoungest = row[12]
	marriedCouple = row[13]
	cPrevious = row[14]
	durationPrevious = row[15]

	features = {}
	features["day"] = state
	features["state"] = day
	features["location"] = location
	features["groupSize"] = groupSize
	features["homeOwner"] = homeOwner
	features["carAge"] = carAge
	features["carValue"] = carValue
	features["ageOldest"] = ageOldest
	features["ageYoungest"] = ageYoungest
	features["marriedCouple"] = marriedCouple
	features["cPrevious"] = cPrevious
	
	#print state
	#return {'state':state}
	return features

with open('purchasepoints.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	#17 to 23
	for i in range(17,24):
		data = ([(row, row[i]) for row in reader])
		#print row,row[i],i
		#Run it for A through G
		featuresets = [(first_feature(r), a) for (r, a) in data]
		train_set, test_set = featuresets[48504:], featuresets[:48505]
		classifier = nltk.NaiveBayesClassifier.train(train_set)
		#Display details
		print "Accuracy is:", nltk.classify.accuracy(classifier, test_set)
		print classifier.show_most_informative_features(5)
		csvfile.seek(0) #inportant for resetting the file pointer and avoiding the empty bins in next iteration

	##data = ([(row, row[23]) for row in reader])
	#for row in reader:
		#print ', '.join(row)
		#first_feature(row)

	##featuresets = [(first_feature(r), a) for (r, a) in data]
	##train_set, test_set = featuresets[47000:], featuresets[:50009]
	##classifier = nltk.NaiveBayesClassifier.train(train_set)

	#classifier.classify(first_feature('CA'))
	##print "Accuracy is:", nltk.classify.accuracy(classifier, test_set)
	#print nltk.classify.accuracy(classifier, test_set)

	##print classifier.show_most_informative_features(5)