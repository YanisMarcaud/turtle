import turtle
from turtle import *
import random

stylo = Turtle()

#redimensionner la fenêtre
screen = turtle.Screen()
screen.setup(1480, 720)

stylo.speed(0)
colormode(255)

def aller_sans_tracer(x, y):
    stylo.up()
    stylo.goto(x, y)
    stylo.down()

# Définition de la fonction pour dessiner le toit 1
def toit1(stylo_turtle, x, y_sol, niveau):
    y = y_sol
    for i in range(niveau):
        y += 60
        aller_sans_tracer(x, y)

    # Commencer à remplir la forme avec la couleur noire
    stylo_turtle.begin_fill()
    stylo_turtle.fillcolor("#000000")

    # Dessiner la forme du toit 1
    stylo_turtle.forward(160)
    stylo_turtle.right(200)
    stylo_turtle.forward(85)
    stylo_turtle.right(320)
    stylo_turtle.forward(85)

    # Finir de remplir la forme
    stylo_turtle.end_fill()
    stylo_turtle.right(200)

toit1(stylo, 2, 2, 2)