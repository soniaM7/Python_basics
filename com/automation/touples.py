'''
def coordinate(x, y):
    return (x,y)

print(coordinate(2,3))
'''
'''
is_male=True
is_tall=False

if is_male and is_tall:
    print ("you are a male")
elif is_male and not(is_tall):
    print ("what is this")
'''





def birthday_game():
    guess=4
    print ("You have 5 chances \"Guess my birthday date")
    while guess >= 0:
        birthday_date = int (input())
        if guess==0:
            return ("you have lost the game")

        elif birthday_date ==14:
            return  ("Bra jobbet")
        elif birthday_date!=14:
            print ("try again")
            guess -=1

                       # print ("your chances left" + str(guess))
print (birthday_game())




















