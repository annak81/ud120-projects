#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print "Number of features: ", len(features_train[0])



#########################################################
### your code goes here ###

# Reduce the training set to 1% of original data
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn.tree import DecisionTreeClassifier

CList = [40]
for CVal in CList:
    clf = DecisionTreeClassifier(min_samples_split=CVal)
    print "####   Test for min_samples_split = ", CVal, "  ####"
    print "Start training ..."
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time:", round(time() - t0, 3), "s"

    print "Start predicting ..."
    t0 = time()
    pred = clf.predict(features_test)
    print "Predicting time:", round(time() - t0,3), "s"

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(labels_test, pred)
    print "Accuracy: ", accuracy

    answers = [10, 26, 50]
    people = ["Sara", "Chris"]
    for answer in answers:
        print "Answer for email #", answer, "is: ", pred[answer], " => ", people[pred[answer]]

    print "Total emails predicted to be from Sara (0): ", (pred == 0).sum()
    print "Total emails predicted to be from Chris (1): ", (pred == 1).sum()

    print "##################################"

#########################################################


