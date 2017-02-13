#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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




#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(C=100.0, kernel='rbf')

# fit the model
t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", time()-t0, "s"

# use the model
t0 = time()
clf.predict(feature_test)
print "prediction time: ", time()-t0, "s"
print clf.score(features_test, labels_test) 
#########################################################


