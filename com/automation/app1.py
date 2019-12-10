'''
name = input("Enter your name")
print("your name is " + name + "!")
'''
'''
from math import *
add = 2+3
print (add)
'''
'''
is_male= False
if (is_male):
    print ("user input is true ")
else:
    print ("user input is false")
'''
'''
friends = ["sonia", "kanika", "Nisha" , 2, False]
print (friends)
print (friends[0])
print (friends[-1])
print (friends[3])
friends[2] = "sonal"
print (friends[0:])
print (friends[0:3])
print (friends[-1])
'''
friends = ["sonia", "kanika", "Nisha" , 2, False]
birthday = [2,3,5,7,8,12]

friends.extend(birthday)
print (friends)
friends.append(True)
print(friends)
friends.insert(2,False)
print (friends)
friends.remove(False)
print (friends)
friends.pop(-1)
print(friends)
print (friends.index("kanika"))
friends[0] = "testing"
print(friends)
