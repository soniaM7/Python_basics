right_word="sonia"
guess_word = ""

while guess_word != right_word:
    guess_word = input("Guess my name")
    if guess_word != right_word:
        print("tyr again")

print ("This time you are correct")


