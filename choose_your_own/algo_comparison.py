#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')

from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

clfs = {"KNeighbors":  KNeighborsClassifier(),
        "AdaBoost" : AdaBoostClassifier(),
        "RandomForest (estimators 100)" : RandomForestClassifier(n_estimators = 100),
        "GaussianNB" : GaussianNB(),
        "SVM Linear" : SVC(kernel="linear"),
        "DecisionTree (min split 5)" : DecisionTreeClassifier(min_samples_split=5),
        "DecisionTree (min split 2)" : DecisionTreeClassifier(min_samples_split=2)
        }


for name, clf in clfs.iteritems():
    print "########################"
    print "Used classifier: ", name
    print "Start training ..."
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time:", round(time() - t0, 3), "s"

    print "Start predicting ..."
    t0 = time()
    pred = clf.predict(features_test)
    print "Training time:", round(time() - t0, 3), "s"

    accuracy = accuracy_score(labels_test, pred)
    print "Accuracy: ", accuracy
    print ""

    try:
        prettyPicture(clf, features_test, labels_test, name.replace(" ", "_"))
    except NameError:
        pass