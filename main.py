#THIS IS HOW YOU MAKE A COMMENT

#--VARIABLES-#
#The below code shows how to create varibles, initialize them with values, as well as perform basic
#mathematical results on them while print out results
x = 5
y = 3.5
print("The value of x is:", x)
print("The value of y is:", y)
z = x + y
print("The value of x+y is:", z)
z = x - y
print("The value of x-y is:", z)
z = x * y
print("The value of x*y is:", z)
z = x / y
print("The vale of x/y is:", z)
z = x % y
print("The remainder of x/y is:", z)
print()

#In python you can also create variables to be other arbitrary things such as strings which can then be concatenated:
x = "Kentucky"
y = "Lexington"
z = y + ", " + x
print("The value of x is:", x)
print("The value of y is:", y)
print("The value of z is:", z)
print()


#--LISTS--#
#One useful data type in python is lists... here we will see how lists can be created, concatenated together, accessed, get their lengths,
#the removal of elements, etc
myList = [2.5, 32, 100, -4.8, 0.333]
print("myList is as follows: ", myList)
listLength = len(myList)
print("The length of myList is:", listLength)
firstElement = myList[0]        #NOTE THAT INDEXING BEGINS FROM 0 AND NOT 1
print("The first element of myList is:", firstElement)
secondElement = myList[1]
print("The second element of myList is:", secondElement)
lastElement = myList[listLength-1]
print("The last element of myList is:", lastElement)

myList2 = ["house", "car", "boat", "bike", "plane"]
print("myList2 is as follows:", myList2)
#List concatenation
myList3 = myList + myList2
print("myList3 is as follows:", myList3)
#List elemental removal
myList.remove(32)
print("myList with 32 element removed is now:", myList)
print()


#--VECTOR MATHEMATICS--#
#In order to do vector or matrix-wise mathematics it will be helpful to use the 'numpy' library (although you could also use lists and lists within lists...
#but this would be much less optimized for fast computation at the compiler and hardware level)

#First we will import the numpy library (Note that all imports are typically placed at the beginning of a python file following best coding practices)
import numpy as np
#Now we will create some arrays and matrices
x = np.array([1.3, 2.3, -4.4, -3.2, 5.0])
y = np.array([ [3,4,5], [-2, -1, 0], [9,8,7] ])
print("The value of x is:", x)
print("The value of y is:\n", y)
#You can also create an array of all zeros simply with
z = np.zeros(5, dtype=float)
print("The value of z is:", z)
