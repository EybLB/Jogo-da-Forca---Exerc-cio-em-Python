import random

# Reading TXT file
file_handle = open(r"randomlist.txt")

# Sets the range of possible words to choose based on list length, then chooses a random word from file and converts it to uppercase
words = file_handle.readlines()
qty_words = len(words)
random_number = random.randint(0, qty_words - 1)
chosen = words[random_number]
chosen = chosen.upper()

# Converts chosen word into a list and removes the '\n' as the last element.
# Then creates an assistant "blank" list and a variable for tracking attemps.
game_word = list(chosen)
game_word.pop()
hidden_word = ["_"] * len(game_word)
attempts = 0

print("\n*****Hangman Game!*****\n")
print(hidden_word, "\n")

while attempts < 5:
    win = False
    guess = str(input("Type your letter:\n"))
    guess = guess.upper()
    if guess in game_word:
        for i in range(0, len(game_word)):
            if guess == game_word[i]:
                print("Well done!!")
                hidden_word[i] = guess
                if "_" not in hidden_word:
                    print("\n*****You won!!*****")
                    win = True
                else:
                    pass
        print("\n")
        print(hidden_word)
        print("\n")

    else:
        try_again = 4 - attempts
        print("\n>>>Ooops! Try another letter!")
        print(">>>You still have: " + str(try_again) + " attempts!\n")
        attempts = attempts + 1

    if win:
        break

if attempts == 5:
    print("*****No more attempts!*****")
    print("*****You lost!*****")
