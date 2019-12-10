'''
try:
    output = 10/0
    num=int(input("Enter a number"))

except:
    print ("invalid input")
    '''
try:
    output = 10/0
    num=int(input("Enter a number"))

except ZeroDivisionError as err:
    print (err)

except ValueError as err1:
    print (err1)

print ("cross check if other statements print or not")
