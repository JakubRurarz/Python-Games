

import turtle
import os

wn = turtle.Screen()
wn.title("ping pong by Rurarz")
wn.bgcolor("cornflowerblue")
wn.setup(width=800, height= 600)
wn.tracer(0)

#wynik
score_a = 0
score_b = 0

#paletka 1
padldle_a = turtle.Turtle()
padldle_a.speed(0)
padldle_a.shape("square")
padldle_a.color("darkorchid1")
padldle_a.shapesize(stretch_wid=5, stretch_len= 1)
padldle_a.penup()
padldle_a.goto(-350, 0)

#paletka 2
padldle_b = turtle.Turtle()
padldle_b.speed(0)
padldle_b.shape("square")
padldle_b.color("darkorchid1")
padldle_b.shapesize(stretch_wid=5, stretch_len= 1)
padldle_b.penup()
padldle_b.goto(+350, 0)

#pilka
pilka = turtle.Turtle()
pilka.speed(0)
pilka.shape("circle")
pilka.color("deeppink1")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 0.6
pilka.dy = 0.6

#napis
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gracz A: 0  Gracz B: 0", align="center",font=("courier", 24, "normal"))

#funkcje
def paddle_a_up():
    y = padldle_a.ycor()
    y += 20 
    padldle_a.sety(y)

def paddle_a_down():
    y = padldle_a.ycor()
    y -= 20 
    padldle_a.sety(y)

def paddle_b_up():
    y = padldle_b.ycor()
    y += 20 
    padldle_b.sety(y)

def paddle_b_down():
    y = padldle_b.ycor()
    y -= 20 
    padldle_b.sety(y)

#bindy
wn.listen()
#1
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#2
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main loop
while True:
    wn.update()

#ruch pilki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)

#Granice
    if pilka.ycor() > 290:
        pilka.sety(290)
        pilka.dy *= -1

    if pilka.ycor() < -290:
        pilka.sety(-290)
        pilka.dy *= -1
    
    if pilka.xcor() > 350:
        
        score_a += 1
        pen.clear()
        pen.write("Gracz A: {}  Gracz B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        pilka.goto(0, 0)
        pilka.dx *= -1


    if pilka.xcor() < -350:
        
        score_b += 1
        pen.clear()
        pen.write("Gracz A: {}  Gracz B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        pilka.goto(0, 0)
        pilka.dx *= -1

# kolizje
    if pilka.xcor() < -340 and pilka.ycor() < padldle_a.ycor() + 50 and pilka.ycor() > padldle_a.ycor() - 50:
        pilka.dx *= -1 
        
        
    
    elif pilka.xcor() > 340 and pilka.ycor() < padldle_b.ycor() + 50 and pilka.ycor() > padldle_b.ycor() - 50:
        pilka.dx *= -1
        
        
        