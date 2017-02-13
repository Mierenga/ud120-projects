###
# decision trees
###

### good day to windsurf?

    SUN ^
        | x x x x o o o o
        | x x x x o o o o    # o, yes it is
        | x x x x o o o o
        | x x x x x x x x
        | x x x x x x x x
        | x x x x x x x x
        +--------------->
                    WIND

    +---------------------+
    |  well, is it windy? |
    +---------------------+
    +-----+         +-----+
    | no  |         | yes |
    +-----+         +-----+
       |               |
       x            +---------------------+
                    |  well, is it sunny? |
                    +---------------------+
                    +-----+         +-----+
                    | no  |         | yes |
                    +-----+         +-----+
                       |               |
                       x               o

## terms:
- axis-parallel decision lines : re-read the term
- entropy : measure of impurity in a bunch of examples


## strategy: break up graph into axis-parallel decision lines
        y
        ^
        | o o o o o o o o
        | o o o o o o o o    
        | o o o o x x x x
        | o o o o x x x x
        | x x x x x x x x
        | x x x x x x x x
        +---------------> x
        0  1  2  3  4  5

let's do a vertical (y-parallel) split  
  
        y
        ^                   #                 +-----+
       6| o o o o|o o o o   # now we can ask  | x<3 | ?
       5| o o o o|o o o o   #                 +-----+
       4| o o o o|x x x x   # and will only have to use a subset of the graph 
       3| o o o o|x x x x   # to complete our classification
       2| x x x x|x x x x   # 
       1| x x x x|x x x x   #
        +---------------> x #
        0  1  2  3  4  5    #      

then a separate x-parallel split for each side of y-parallel split  
  
        y
        ^                   #                 +-----+
       6| o o o o|o o o o   # now we can ask  | x<3 | 
       5| o o o o|o o o o   #                 +-----+
                  -------   #                  y    n
       4| o o o o|x x x x   #                /       \
       3| o o o o|x x x x   #           +-----+     +-----+
         --------           #           | y<2 |     | y<5 |
       2| x x x x|x x x x   #           +-----+     +-----+
       1| x x x x|x x x x   #            y   n       y   n
        +---------------> x #            |   |       |   | 
        0  1  2  3  4  5    #            x   o       x   o 

## controlling entropy
control how a DT decides where to split the data  

    entropy = ∑ -((P[i]) * log2(P[i]))
or   

    for class in set
        entropy += class * log2(class) * (-1)

- if all examples are same class: entropy = 0
- if all examples are a diff class: entropy = 1


## information gain ([video](https://classroom.udacity.com/courses/ud120/lessons/2258728540/concepts/24325985460923#))
- *entropy(parent)* minus the weighted average of all *entropy(children)*
- decision tree algorithm maximizes the information gain
- analyze each potential split based on training features and choose the one with the most information gain

## bias-variance dilemma ([video](https://classroom.udacity.com/courses/ud120/lessons/2258728540/concepts/24402485560923))
- too much bias -> unable to adapt
- too much variance -> unstable  

#### find the right tradeoff


## decision trees with sklearn ([docs](http://scikit-learn.org/stable/modules/tree.html))

- from sklearn import tree
- tree.DecisionTreeClassifier()
- tuning parameters for DecisionTreeClassifier
    - min_samples_split: if I have less samples than this in my node, I cannot split again, and I become a leaf
        - aka, when do I have to become a leaf?
        - default=2
        - make it larger to avoid overfitting
    - criterion: 'gini', 'entropy'




---  
[back: svm](svm.md)   
[up](toc.md)   
[next: cyoa](cyoa.md)
---  

