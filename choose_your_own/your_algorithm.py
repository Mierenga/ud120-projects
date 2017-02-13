#!/usr/bin/python

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

## K nearest neighbors
from sklearn.neighbors import KNeighborsClassifier
clfk = KNeighborsClassifier()
clfk.fit(features_train, labels_train)
print 'k nearest neighbors: ', clfk.score(features_test, labels_test)

# random forest
from sklearn.ensemble import RandomForestClassifier
clfr = RandomForestClassifier()
clfr.fit(features_train, labels_train)
print 'random forest: ', clfr.score(features_test, labels_test)

# adaboost
from sklearn.ensemble import AdaBoostClassifier
clfa = AdaBoostClassifier()
clfa.fit(features_train, labels_train)
print 'adaboost: ', clfa.score(features_test, labels_test)


try:
    prettyPicture(clfk, features_test, labels_test, "knn.png")
    prettyPicture(clfr, features_test, labels_test, "ran.png")
    prettyPicture(clfa, features_test, labels_test, "ada.png")
except NameError:
    print 'name error'
    pass
