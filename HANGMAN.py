# -*- coding: utf-8 -*-
"""
Janvi Vora
CS 521 Spring 2021
Term Project
Game - HANGMAN
"""
import random

hangman = ["""
H A N G M A N - Python Version

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Python Version

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def displayBoard(hangman, IncorrectLetters, CorrectLetters, selectedWord):
    print(hangman[len(IncorrectLetters)])
    print()

    print('Incorrect Letters:', end=' ')
    for letter in IncorrectLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(selectedWord)

    for i in range(len(selectedWord)):  # replace blanks with correctly guessed letters
        if selectedWord[i] in CorrectLetters:
            blanks = blanks[:i] + selectedWord[i] + blanks[i+1:]

    for letter in blanks:  # show the selected random word 
        print(letter, end=' ')
    print("\n")

def getRandomWord():
    words = ['numpy', 'pandas', 'pytorch', 'matplotlib',
         'tensorFlow', 'seaborn', 'keras', 'scikitlearn']
    word = random.choice(words)
    return word


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

def Replay():
    return input("\nDo you want to play again? ").lower().startswith('y')


IncorrectLetters = ''
CorrectLetters = ''
selectedWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hangman, IncorrectLetters, CorrectLetters, selectedWord)

    guess = getGuess(IncorrectLetters + CorrectLetters)

    if guess in selectedWord:
        CorrectLetters = CorrectLetters + guess

        foundAllLetters = True
        for i in range(len(selectedWord)):
            if selectedWord[i] not in CorrectLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  selectedWord + '"! You have won!')
            gameIsDone = True
    else:
        IncorrectLetters = IncorrectLetters + guess

       

    if gameIsDone:
        if Replay():
            IncorrectLetters = ''
            CorrectLetters = ''
            gameIsDone = False
            selectedWord = getRandomWord()
        else:
            break