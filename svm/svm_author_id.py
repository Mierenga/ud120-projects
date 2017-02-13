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

def reduce_data(features, labels, percentage):
    features = features[:len(features) * percentage / 100]
    labels = labels[:len(labels) * percentage / 100]
    return features, labels


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=10000.0)

#features_train, labels_train = reduce_data(features_train, labels_train, 1)

# fit the model
t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", time()-t0, "s"

# use the model
t0 = time()
pred = clf.predict(features_test)
print "prediction time: ", time()-t0, "s"
print "score: ", clf.score(features_test, labels_test) 
chris = 0
for val in pred:
    if val:
        chris += 1
total = len(pred)
sara = total - chris
print "chris: ", chris
print "sara:  ", sara
print "total: ", total
#########################################################




