'''name =["sonia","kaniak"]

for value in range(len(name)):
    print (name[value])


#2¤2¤2

x= int(input("enter the number"))

def exponent(x):
    count=1
    power=int(input("enter the power"))
    while power!=0:
        count=count *x
        power = power -1
    print (count)

exponent(2)
'''


x= int(input("enter the number"))
y= int(input("Enter the power"))

def exponent(x):
    count=1
    for i in range(y):
        count = count*x
    print (count)
exponent(x)






