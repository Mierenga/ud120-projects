###
# naive bayes
###

- map features to a label

## terms
- sensitivity: P(Pos|C)
- specitivity: P(Pos|¬C)

Example for the probablity of having cancer
given a test with known sensitivity and specitivity:

                P(C)                                
         /-------+-------\
         |               |
      P(Pos|C)   +   P(Pos|¬C)  ==  P(Pos)          # relative probablities
         |               |
      ÷ P(Pos)        ÷ P(Pos)                      # normalization
         |               |
         V               V
      P(C|Pos)   +  P(¬C|Pos)  ==  1                # add up to 1


- called naive because order is not accounted

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

##### we need another input into the SVM
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
let's try adding feature z = |x|, where x is the distance from the y axis   

    -------------------------
                z
                |         o
                |xxxx   o oo      # now the data is divided into two areas
                |x xx  oo oo     
              xx| xxx o o        
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
              xx| xxx/o o        
    ------------+--/---------x
                |/ oo
               /|o   o
              / |
    -------------------------






















