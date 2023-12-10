import random

# read words file
def read_words(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            words.append(line.strip().split(','))
    return words

# choose a word in words file
def choose_word(words):
    random.shuffle(words)
    word_l = random.choice(words)
    return word_l[0].upper(), word_l[1].upper()

# display word and guess
def display_word(word, guess):
    display = ""
    for char in word:
        # if input char is in the word
        if char in guess:
            display += char
        # if input char is not in the word
        else:
            display += "_"
    return display

if __name__ == '__main__':
    print("Welcome to Hangman Game!")

    words = read_words('C:/Users/cmh06/Downloads/words.csv')
    word, hint = choose_word(words)
    guesses = []
    chance = 5
   
    while chance > 0:
        print("\nLeft chance : ", chance)
        current_display = display_word(word, guesses)
        print(current_display)

        # if your word is correct
        if current_display == word:
            print("Correct!")
            break

        guess = input("Enter your guess : ").upper()

        # if input is not single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter one single letter.")
            continue
        
        # if input is duplicated
        if guess in guesses:
            print("Already in the word. Enter other letter.")
            continue
        
        # if the input is correct, add the letter in guesses
        guesses.append(guess)
        
        # if the input is incorrect
        if guess not in word:
            chance -= 1
            print("That letter is not in the word. Enter other letter.")
            print("HINT : ", hint)

    if chance == 0:
        print("GAME OVER")
        print("The word is ", word)
        