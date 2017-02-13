###
# support vector machines
###

### maximize the distance of the dividing line between the two classes
    -------------------------
                 |           
        x   x    |   o  o    
         x x x   |   o   oo  
       x   x     |    o  o   
                 |           
    -------------------------

## terms
- margin: maximizes distance to nearest point
- robustness: maximized by having an even margin

## want to maximize the margin without misclassifying any data points:
    -------------------------       
              \ 
        x   x  \  o  o
         x x x  \ o  oo
       x   x     \ o o 
                 x\
    -------------------------       

### what about outliers?
    -------------------------       
              \                 # do the best we can with the margin by 
        x   x  \  o  o          # ignoring the outlier
         x x x  \ o  oo         
       x   x     \ o o 
         o        \
    -------------------------
         ^
      outlier


### what if no line will make sense?
    -------------------------
                y
                |
            o  o|   o o 
          o   x | x  o          
         o   x x| xx            
    ------------+------------x
         o     x|xx    o        
          o  x  |   o  o        
            o   | o o
                |
    -------------------------

##### we need another input (feature) into the SVM
                     +-----+
                x -->|     |
                y -->| SVM |--> label
    z = x^2 + y^2 -->|     |
                     +-----+

##### plot of z axis (x^2 + y^2) 
    -------------------------
                z
                |
         o  o o |o  o  o       
          o  o  |o  o o         # z is small for points near the origin (i.e., x data)
         x x  xx| xx x x        # z is larger for points farther from the origin (i.e., o data)
    ------------+------------x
                |
                |
                |
    -------------------------
the derived feature separates the data linearly so the SVM can work

## strategy: add a derived feature that can divide the data linearly
    -------------------------
                y
      o         |        
         o  x x |x  x   o  o      # this data cannot be divided with a straight line
      o  o   x  |x  x  o  o      
        o o   xx| xx  o o        
    ------------+------------x
             o  |  o
           o    |o
                |
    -------------------------
how can we make the divider linear?  
add feature z = |x|, where x is the distance from the y axis   

    -------------------------
                z
                |         o
                |xxxx   o oo      # now the data is divided into two areas
                |x xx  oo oo     
                | xxx o o        
    ------------+------------x
                |  oo
                |o   o
                |
    -------------------------

    -------------------------
                z
                |       / o
                |xxxx  /o oo      # we can draw a straight line between them 
                |x xx /oo oo     
                | xxx/o o        
    ------------+--/---------x
                |/ oo
               /|o   o
              / |
    -------------------------

## kernel trick

hyper calc
low-d space    --->    high-d space

    {                          kernels
        non-separable           --->    separable
        non-linear separation   <---    solution
    }
    {
        x1 y                    --->    x1 x2 x3 x4 x5
        non-linear separation   <---    solution
    }

- find a solution in the much larger separable set  
- reapply the solution in the non-separable space  
- you now have a non-linear separation  

## SVMs with sklearn ([docs](http://scikit-learn.org/stable/modules/svm.html#svm))
- several SVMs available
- sklearn.svm.SVC is the 'support vector classifier'
    - kernel: what type of divider will we use
        - linear        : straight line
        - poly          : 
        - rbf (default) : custom squiggly lines
        - sigmoid
        - precomputed
    - C: controls tradeoff between smooth decision boundary & classifying training points correctly 
        - helps with balancing between custom fitting and generalizing, to avoid overfitting
        - larger C gives a more custom curve
    - gamma: how squiggly can the line get?
        - 1.0 might give you a very straight line while 1000 can be very curvy

## strategy: avoid overfitting
- play with parameters C, gamma, kernel
- use tools to automatically detect overfitting
  
  
  
---  
[back: naive bayes](naive_bayes.md)  
[up](toc.md)   
[next: decision trees](decision_trees.md)
---  


