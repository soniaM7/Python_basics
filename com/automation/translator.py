

def translator(name):
    translate=""

    for letter in name:
        if letter in "AEIOUaeiou":
            translate = translate + "g"
        else:
            translate = translate + letter
    print (translate)






translator("sonia")
