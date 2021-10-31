# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:46:39 2021

@author: joao.ferreira
"""

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
   
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    #detectar colisão com a comida
    if snake.head.distance(food)<15:
        food.refresh()
        score.soma_se()
        snake.extensao()
        
    #detectar colisão com a parede
    if snake.head.xcor()>280 or snake.head.xcor()< (-280) or snake.head.ycor()>280 or snake.head.ycor()< (-280):
        score.over()
        game_is_on=False
        
    #detectar colisão com a calda
    for segment in snake.segments[1:]:        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.over()
        
        
        

screen.exitonclick()