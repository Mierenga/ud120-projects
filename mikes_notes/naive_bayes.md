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


---  
[up](toc.md)    
[next: svm](svm.md)
---  
