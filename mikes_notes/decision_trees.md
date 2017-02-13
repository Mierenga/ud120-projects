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
                                        
## decision trees with sklearn ([docs](http://scikit-learn.org/stable/modules/tree.html))

- from sklearn import tree
- tree.DecisionTreeClassifier()
- tuning parameters for DecisionTreeClassifier
    - min_samples_split: if I have less samples than this in my node, I cannot split again, and I become a leaf
        - aka, when do I have to become a leaf?
        - default=2
        - make it larger to avoid overfitting





---  
[back: svm](svm.md)   
[up](toc.md)   
[next: trees](decision_trees.md)
---  

