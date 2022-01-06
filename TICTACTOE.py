# -*- coding: utf-8 -*-
"""
Janvi Vora
CS 521 Spring 2021
Term Project
Game - TIC-TAC-TOE
"""
def user_input(): #takes in user's choice 
    user1 = input("Please pick 'X' or 'O':")
    while True:
        if user1.upper() == 'X':
            user2='O'
            print("You've choosen " + user1 + ". User 2 will be " + user2)
            return user1.upper(),user2
        elif user1.upper() == 'O':
            user2='X'
            print("You've choosen " + user1 + ". User 2 will be " + user2)
            return user1.upper(),user2
        else:
            user1 = input("Please pick 'X' or 'O' ")
            
def tictactoe_board(board): #creates the board for the game
    blankBoard="""
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|

"""

    for i in range(1,10):
        if (board[i] == 'X' or board[i] == 'O'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def alphabet_position(board, alphabet, position): 
    board[position] = alphabet
    return board

def space_check(board, position): 
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win(board, mark): #winning possibilities
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def user_choice(board): 
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't free. Please choose between 1 and 9 : ")
    return choice

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    players=user_input() #takes the user's choice
    board = ['#'] * 10   #initializes the game's board
    while True:
        game_on=full_board_check(board)  # Set's the game 
        while not game_on:
            position = user_choice(board)
            if i % 2 == 0:
                alphabet = players[1]
            else:
                alphabet = players[0]
            
            alphabet_position(board, alphabet, int(position))
            tictactoe_board(board)  # Check the board
            i += 1
            if win(board, alphabet):
                print("You won !")
                break
            