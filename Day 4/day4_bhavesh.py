import math 

def isPerfectSquare(x):
  
  if (x>=0):
    sq = int(math.sqrt(x))
    
    return ((sq*sq)==x)
  return false


x=36

if(isPerfectSquare(x)):
  print("True")
  else: 
    print("No")
