import numpy as np
dealer1=[[10,12,45,43,64,67],[74,46,23,45,54,87],[23,75,87,42,41,56],
         [23,54,71,86,53,43],[23,35,65,67,97,54],[35,54,56,68,87,43],
         [23,43,46,57,43,23],[35,43,34,65,52,76],[31,32,23,43,54,45],[31,12,23,34,34,45]]
dealer2=[[23,43,54,56,76,78],[23,43,54,56,67,86],[34,54,67,98,76,34],
         [53,54,65,76,87,32],[21,37,48,84,84,37],[24,23,40,54,67,70],
         [35,85,58,96,71,75],[21,23,54,56,67,31],[51,18,24,25,36,47],[13,24,25,63,64,75]]
    
print(dealer1)
print(dealer2)

# Find yearwise sales of each item by both the dealers
print("Year wise sales Dealer 1 : ",np.sum(dealer1,axis=0))
print("Year wise sales Dealer 2 : ",np.sum(dealer2,axis=0))

# Find yearwise sales of all items for each dealer
print("yearwise sales of all items by dealer1: ",np.sum(dealer1,axis=1))
print("yearwise sales of all items by dealer2: ",np.sum(dealer2,axis=1))

# Display sales of a particular year for each dealer
print("sales of a particular year of dealer1: ",np.sum(dealer1,axis=1))
print("sales of a particular year of dealer2: ",np.sum(dealer2,axis=1))

# Display sales of TV and freeze for each dealer
tvfridge1=np.sum(dealer1,axis=0)
print("sales of TV and freeze of dealer1: ",tvfridge1[0:2])
tvfridge2=np.sum(dealer2,axis=0)
print("sales of TV and freeze of dealer1: ",tvfridge2[0:2])
