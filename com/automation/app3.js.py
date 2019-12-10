'''right_word="sonia"
guess_word = ""
count =5
while guess_word!=right_word:
    if count>0:
        guess_word = input("Guess my name:")
        if guess_word != right_word:
            print("tyr again")
            count -=1
            if count==0:
                print("your chances are over")
                break
if guess_word==right_word:
    print ("This time you are correct")
    '''

right_word="sonia"
guess_word = ""
count = 5


for i in range(count):
    guess_word = input("Guess my name:")
    if guess_word==right_word:
        print ("You win the Game!!")
        break
    elif i ==4 :
        print ("you have lost the game")
    else:
        print("try again")
        count -=1




