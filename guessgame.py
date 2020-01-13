################Guessing game############
secret_word = "lion"
guess = ""
count = 0
out_of_guess = False
while count<3:
    if guess != secret_word:
        guess=input("Enter your guess: ")
    else:
        out_of_guess=True
    count+=1

if out_of_guess:
    print("You win")
else:
    print("You lost")
#########################################
