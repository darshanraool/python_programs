import numpy as np
lst1=[]
lst2=[]
lst3=[]
lst4=[]
for i in range(1,21):
    #a=int(input(f"Enter {i} value: "))
    if i<6:
        lst1.append(i)
    elif i<11:
        lst2.append(i)
    elif i<16:
        lst3.append(i)
    else:
        lst4.append(i)
        
# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)

array1=np.array((lst1,lst2))
array2=np.array((lst3,lst4))
print("List1: ",array1)
print("List2: ",array2)

print("Addition: ",array1+array2)
print("Subtraction: ",array1-array2)
print("Multiplication: ",array1*array2)
print("Expo: ",np.exp(array1))
        
        
        

