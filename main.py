import numpy as np

def numberOfHundreds( N ) :
  # Your code goes here
  ttt = np.floor( N / 1000 ) 
  return np.floor( (N-1000*ttt) / 100 )

# This calls the function you have written to check if it works
print( numberOfHundreds(3260) )
