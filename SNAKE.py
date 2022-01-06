# -*- coding: utf-8 -*-
"""
Janvi Vora
CS 521 Spring 2021
Term Project
"""

# import modules
from freegames import square, vector
from random import *
import turtle as t


t.title("Snake")  # Screen color and title
root = t.Screen()._root

t.bgcolor('black')

food = vector(0, 0)
snake = [vector(20, 0)]
aim = vector(0, -20)

def change_dir(x, y):  # Change the snake's direction
    aim.x = x
    aim.y = y

def boundary(head):   # Return's true if head is in the boundaries
    return -200 < head.x < 190 and -200 < head.y < 190

def move():   # Move's snake forward one segment
    head = snake[-1].copy()
    head.move(aim)

    if not boundary(head) or head in snake:
        square(head.x, head.y, 8, 'red')
        t.update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    t.clear()

    for body in snake:
        square(body.x, body.y, 9, 'white')

    square(food.x, food.y, 9, 'purple')
    t.update()
    t.ontimer(move, 100)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: change_dir(0, 10), 'Up')
t.onkey(lambda: change_dir(0, -10), 'Down')
t.onkey(lambda: change_dir(10, 0), 'Right')
t.onkey(lambda: change_dir(-10, 0), 'Left')
move()
t.done()