###
# choose your own algorithm
###

## algorithm choices:
- k nearest neighbors
    - classic, simple, easy to understand
- random forest
    - "ensemble methods"
- adaboost (aka boosted decision tree)j
    - "ensemble methods"

## ensemble methods
meta classifiers built from (usually) decision trees
many opinions, one final answer

## process
1. do some research, get a general understanding
2. find sklearn docs
3. deploy it
4. use it to make predictions
5. evaluate it, what is the accuracy?

## k nearest neighbors

#### classification with sklearn ([docs](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html))
- from sklearn.neighbors import KNeighborsClassifier
    - RadiusNeighborsClassifier also available

## random forest
#### classification with sklearn ([docs](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html))
- from sklearn.ensemble import RandomForestClassifier

## adaboost
#### classification with sklearn ([docs](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html))
- from sklearn.neighbors import AdaBoostClassifier 

---
## [this project's code examples](../choose_your_own/your_algorithm.py)
---  
[back: decision trees](decision_trees.md)   
[up](toc.md)   
[next: cyoa](cyoa.md)
---  

