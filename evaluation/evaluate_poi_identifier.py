#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# split into training / testing set
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=0)

# fit on training data
clf.fit(features_train, labels_train)
# predict labels based on test data
pred = clf.predict(features_test)
# convert numpy array to list
pred_list = list(pred)
print "Q28. Number of Persons of Interest (POI) in test set: ", pred_list.count(1)
print "Q29. Total number of people in test set: ", len(pred_list)

import numpy
# init predictions as all non-POIS
pred_all_non_pois = numpy.zeros(len(labels_test))
# check all non-pois predictions for accuracy
accuracy = accuracy_score(labels_test, pred_all_non_pois)
print "Q30. Accuracy if predictions are all non-POIs: ", accuracy

true_pos = []
for index, item in enumerate(pred_list):
    if (item == 1 and labels_test[index] == item):
        # true positive
	true_pos.append(1)
print "Q31. Number of true positives: ", len(true_pos)

from sklearn.metrics import precision_score
precision = precision_score(labels_test, pred)
print "Q32. Precision score: ", precision

from sklearn.metrics import recall_score
recall = recall_score(labels_test, pred)
print "Q33. Recall score: ", recall

print ""
print "=== Metrics of dummy sample data ==="
dummy_pred = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
dummy_true = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_pos = []
for index, item in enumerate(dummy_pred):
    if (item == 1 and dummy_true[index] == item):
        # true positive
	true_pos.append(1)
print "Q34. Number of true positives: ", len(true_pos)

true_neg = []
for index, item in enumerate(dummy_pred):
    if (item == 0 and dummy_true[index] == item):
        # true negative
	true_neg.append(1)
print "Q35. Number of true negatives: ", len(true_neg)

false_pos = []
for index, item in enumerate(dummy_pred):
    if (item == 1 and dummy_true[index] != item):
        # false positive
	false_pos.append(1)
print "Q36. Number of false positives: ", len(false_pos)

false_neg = []
for index, item in enumerate(dummy_pred):
    if (item == 0 and dummy_true[index] != item):
        # false negative
	false_neg.append(1)
print "Q37. Number of false negatives: ", len(false_neg)

precision = precision_score(dummy_true, dummy_pred)
print "Q38. Precision score: ", precision

recall = recall_score(dummy_true, dummy_pred)
print "Q39. Recall score: ", recall


#correct_preds = [x for x in labels_test if x in pred]
#print correct_preds
#for label in pred_list:
