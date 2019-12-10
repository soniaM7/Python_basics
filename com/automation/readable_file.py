file=open("readable_file_use.py","r")


for employee in file.readlines():
    print (employee)

file.close()
