#importe les modules nécéssaires
import turtle
from turtle import *
import random

stylo = Turtle()  # crée une instance de la classe Turtle appelée "stylo"

# redimensionne la fenêtre graphique
screen = turtle.Screen()
screen.setup(1480, 720)

stylo.speed(0)  # règle la vitesse du stylo à la vitesse la plus rapide
colormode(255)  # règle le mode de couleur à 255, ce qui signifie que les couleurs sont spécifiées en RVB avec des valeurs allant de 0 à 255

# définit une fonction pour générer une couleur aléatoire en RVB
def couleur_aleatoire():
    return (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))

# définit une fonction pour déplacer le stylo à un emplacement spécifié sans dessiner
def aller_sans_tracer(x, y):
    stylo.up()
    stylo.goto(x, y)
    stylo.down()

# définit une fonction pour dessiner un rectangle aux coordonnées spécifiées avec une largeur et une hauteur spécifiées
def rectangle(stylo_turtle, x, y, w, h):
    aller_sans_tracer(x, y)
    for i in range(2):
        stylo_turtle.forward(w)
        stylo_turtle.right(-90)
        stylo_turtle.forward(h)
        stylo_turtle.right(-90)

# définit une fonction pour dessiner une fenêtre aux coordonnées spécifiées
def fenetre(stylo_turtle, x, y):
    stylo_turtle.begin_fill()
    rectangle(stylo_turtle, x, y, 30, 30)
    stylo_turtle.fillcolor('#ddd')
    stylo_turtle.end_fill()

# définit une fonction pour dessiner une porte à la forme rectangulaire aux coordonnées spécifiées avec une couleur spécifiée
def porte1(stylo_turtle, x, y, couleur):
    stylo_turtle.begin_fill()
    rectangle(stylo_turtle, x, y, 30, 50)
    stylo_turtle.fillcolor(couleur)
    stylo_turtle.end_fill()

# définit une fonction pour dessiner une porte avec un demi-cercle dessus aux coordonnées spécifiées avec une couleur spécifiée
def porte2(stylo_turtle, x, y, couleur):
    aller_sans_tracer(x, y)
    stylo_turtle.begin_fill()

    stylo_turtle.forward(30)
    stylo_turtle.right(-90)
    stylo_turtle.forward(40)
    stylo_turtle.circle(15, 180) # Trace un demi-cercle de rayon 15 pixels
    stylo_turtle.forward(40)
    stylo_turtle.fillcolor(couleur)
    stylo_turtle.right(-90)

    stylo_turtle.end_fill()

def fenetre_balcon(stylo_turtle, x, y):
    stylo_turtle.begin_fill()
    rectangle(stylo_turtle, x, y, 30, 50)
    stylo_turtle.fillcolor('#ddd')
    stylo_turtle.end_fill()

    stylo_turtle.pensize(3)
    stylo_turtle.goto(x-5, y)
    for i in range(8):
        for j in range(2):
            stylo_turtle.forward(5)
            stylo_turtle.right(-90)
            stylo_turtle.forward(25)
            stylo_turtle.right(-90)
        stylo_turtle.forward(5)

    stylo_turtle.pensize(1)


# Définition de la fonction pour dessiner le toit triangulaire
def toit1(stylo_turtle, x, y_sol, niveau):
    y = y_sol
    for i in range(niveau):
        y += 60
        aller_sans_tracer(x, y)

    # Commencer à remplir la forme avec la couleur noire
    stylo_turtle.begin_fill()
    stylo_turtle.fillcolor("#000000")

    # Dessiner la forme du toit
    stylo_turtle.forward(160)
    stylo_turtle.right(200)
    stylo_turtle.forward(85)
    stylo_turtle.right(320)
    stylo_turtle.forward(85)

    # Finir de remplir la forme
    stylo_turtle.end_fill()
    stylo_turtle.right(200)


# Définition de la fonction pour dessiner le toit écrasé avec les bords arrondis
def toit2(stylo_turtle, x, y_sol, niveau):
    y = y_sol
    for i in range(niveau):
        y += 60
        aller_sans_tracer(x, y)

    # Définir l'épaisseur du stylo pour dessiner le toit 2
    stylo_turtle.pensize(10)

    # Dessiner la forme du toit 2
    stylo_turtle.forward(150)

    # Remettre l'épaisseur du stylo à sa valeur originale
    stylo_turtle.pensize(1)


# Définition de la fonction pour dessiner le rez-de-chaussée
def rdc(stylo_turtle, x, y_sol, couleur_porte):
    # Générer aléatoirement la position des éléments du rez-de-chaussée
    position_aleatoire = ["fenetre", "fenetre", "porte"]
    random.shuffle(position_aleatoire)

    # Générer aléatoirement le type de porte
    type_de_porte = random.randint(1, 2)

    # Dessiner les éléments du rez-de-chaussée selon leur position
    for element in position_aleatoire:
        if element == "fenetre":
            fenetre(stylo_turtle, x, y_sol+20)
        elif element == "porte":
            if type_de_porte == 1:
                porte1(stylo_turtle, x, y_sol, couleur_porte)
            else:
                porte2(stylo_turtle, x, y_sol, couleur_porte)
        x += 40


# Définition de la fonction pour dessiner un étage
def etage(stylo_turtle, x, y_sol):
    # Générer aléatoirement la position des éléments de l'étage avec 1/3 de chance que l'élement soit une fenêtre balcon et 2/3 un fenêtre
    position_aleatoire_elements = []
    for i in range(3):
        nombre_aleatoire = random.randint(1, 3)
        if nombre_aleatoire == 1 or nombre_aleatoire == 2:
            position_aleatoire_elements.append("fenetre")
        elif nombre_aleatoire == 3:
            position_aleatoire_elements.append("fenetre_balcon")

    # Dessiner les éléments de l'étage selon leur position dans la liste position_aleatoire_elements
    for element in position_aleatoire_elements:
        if element == "fenetre":
            fenetre(stylo_turtle, x, y_sol+20)
        elif element == "fenetre_balcon":
            fenetre_balcon(stylo_turtle, x, y_sol)
        x += 40

def toit(stylo_turtle, x, y_sol, niveau):
    # Cette fonction dessine le toit d'un immeuble au hasard en appelant soit toit1() soit toit2()
    # x: la position x de l'immeuble
    # y_sol: la position y du sol de la ville
    # niveau: le nombre d'étages de l'immeuble

    nombre_aleatoire = random.randint(1, 2)
    if nombre_aleatoire == 1:
        toit1(stylo_turtle, x-11.5, y_sol, niveau)
    else:
        toit2(stylo_turtle, x-6, y_sol, niveau)

def immeuble(stylo_turtle, x, y_sol):
    # Cette fonction dessine un immeuble aléatoire en appelant plusieurs fonctions de dessin
    # x: la position x de l'immeuble
    # y_sol: la position y du sol de la ville

    # Choisir un nombre d'étages aléatoire pour l'immeuble
    nombre_etages = random.randint(0, 4)
    # Initialise la position y des étages de l'immeuble
    y_etages = y_sol

    # Dessiner un rectangle pour représenter l'immeuble
    stylo_turtle.begin_fill()
    rectangle(stylo_turtle, x, y_sol, 140, (nombre_etages+1)*60)
    stylo_turtle.fillcolor(couleur_aleatoire())
    stylo_turtle.end_fill()

    # Dessine les élements du rez-de-chaussée de l'immeuble
    rdc(stylo_turtle, x+16, y_sol, couleur_aleatoire())

    # Dessiner les élements de chaque étage de l'immeuble
    for i in range(nombre_etages):
        y_etages += 60
        etage(stylo_turtle, x+16, y_etages)

    # Dessiner le toit de l'immeuble
    toit(stylo_turtle, x, y_sol, nombre_etages+1)

# Définition de la fonction pour dessiner toute la ville prenant en paramètre le stylo_turle, la coordonnée x et la coordonnée y
def ville_entiere(stylo_turle, x, y):

    # Assignation de la position x de la ville à une variable immuable
    x_immutable = x

    # Nombre aléatoire d'immeubles à dessiner entre 1 et 6
    nombre_immeubles_aleatoire_a_dessiner = random.randint(1, 6)

    # Largeur entre les immeubles
    largeur_entre_les_immeubles = 185

    # Boucle pour dessiner les immeubles
    for i in range(nombre_immeubles_aleatoire_a_dessiner):
        # Dessiner un immeuble à la position actuelle de x et y
        immeuble(stylo_turle, x, y)
        # Ajouter la largeur entre les immeubles à x
        x += largeur_entre_les_immeubles
        # Aller sans tracer le stylo à la position actuelle de x et y
        aller_sans_tracer(x, y)

    aller_sans_tracer(x_immutable-50, y)

    # tracer la trait pour faire le sol de la ville
    stylo_turle.pensize(4)
    stylo_turle.forward((largeur_entre_les_immeubles*nombre_immeubles_aleatoire_a_dessiner)+60)
    stylo_turle.pensize(1)

#-----------------------------------------------------------------------

# Appeler la fonction ville_entiere avec les paramètres stylo, -450 et -100
ville_entiere(stylo, -450, -100)

# Cacher la tortue et attendre un clic pour fermer la fenêtre
stylo.hideturtle()
exitonclick()