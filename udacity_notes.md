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

## maximize the distance of the dividing line between the two classes
`-------------------------`      
`             |           `
`    x   x    |   o  o    `
`     x x x   |   o   oo  `
`   x   x     |    o  o   `
`             |           `
`-------------------------`

## terms
- margin: maximizes distance to nearest point
- robustness: maximized by having an even margin

## want to maximize the margin without misclassifying and data points:
-------------------------       
          \ 
    x   x  \  o  o
     x x x  \ o  oo
   x   x     \ o o 
             x\
-------------------------       

## what about outliers?
-------------------------       
          \                 # do the best we can with the margin by ignoring the outlier
    x   x  \  o  o          # note the outlier
     x x x  \ o  oo
   x   x     \ o o 
     o        \
-------------------------
     ^
  outlier


## what if no line will make sense?
-------------------------
            y
            |
        o  o|   o o 
      o   x | x  o          z will be small for points near the origin (i.e., x)
     o   x x| xx            z will be larger for points farther from the origin (i.e., o)
------------+------------x
     o     x|xx    o
      o  x  |   o  o
        o   | o o
            |
-------------------------
                 +-----+
            x -->|     |
            y -->| SVM |--> label
z = x^2 + y^2 -->|     |
                 +-----+
-------------------------
            z
            |
     o  o o |o  o  o       
      o  o  |o  o o        z will be small for points near the origin (i.e., x)
     x x  xx| xx x x           z will be larger for points farther from the origin (i.e., o)
------------+------------x
            |
            |
            |
-------------------------


