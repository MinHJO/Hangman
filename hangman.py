import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.words = self.read_words('C:/Users/cmh06/Downloads/words.csv')
        self.word, self.hint = self.choose_word()

        self.guesses = []
        self.chance = 5

        self.create_widgets()
    
    # read words file
    def read_words(self, filename):
        words = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                words.append(line.strip().split(','))
        return words

    # choose a word in words file
    def choose_word(self):
        random.shuffle(self.words)
        word_l = random.choice(self.words)
        return word_l[0].upper(), word_l[1].upper()

    # display word and guess
    def display_word(self):
        display = ""
        for char in self.word:
            # if input char is in the word
            if char in self.guesses:
                display += char
            # if input char is not in the word
            else:
                display += "_ "
        return display
    
    def check_guess(self):
        current_display = self.display_word()
        self.display_label.config(text=current_display)

        if current_display == self.word:
            messagebox.showinfo("Congratulations", "Congratulations!")
            self.reset_game()
        elif self.chance == 0:
            messagebox.showinfo("Game Over", f"The word was {self.word}.")
            self.reset_game()

    def make_guess(self):
        guess = self.entry.get().upper()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        elif guess in self.guesses:
            messagebox.showwarning("Duplicate Guess", "Try another.")
        else:
            self.guesses.append(guess)
            if guess not in self.word:
                self.chance -= 1
            self.check_guess()

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.word, self.hint = self.choose_word()
        self.guesses = []
        self.chance = 5
        self.display_label.config(text=self.display_word())
        self.hint_label.config(text = f"HINT: {self.hint}")

    def create_widgets(self):
        tk.Label(self.master, text="Welcome to Hangman Game!", font=("Helvetica", 16)).pack(pady=10)

        self.display_label = tk.Label(self.master, text = self.display_word(), font = ("Helvetica", 18))
        self.display_label.pack()

        self.hint_label = tk.Label(self.master, text = f"HINT: {self.hint}", font = ("Helvetica", 12))
        self.hint_label.pack()

        tk.Label(self.master, text = "Enter your guess:").pack()
        self.entry = tk.Entry(self.master, width = 5, font = ("Helvetica", 14))
        self.entry.pack(pady=10)

        tk.Button(self.master, text="Guess", command=self.make_guess, font=("Helvetica", 14)).pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()