secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = True

while guess != secret_word and out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess :")
        guess_count += 1
    else:
        out_of_guesses = False

    
if not(out_of_guesses):
    print("Out of guesses. You lost")
else:
    print("You win!")
