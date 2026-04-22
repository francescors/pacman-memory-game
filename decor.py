from turtle import *
from cherry import *
from strawberry import *

ht()

#la fonction déplacement est récuoérée du module cherry/strawberry

#fonction qui dessine tous les points autour de la fenetre
def points(x,y,t):
    while x < 390:
        deplacement(x,380,t)
        t.begin_fill()
        t.color("yellow")
        t.circle(5)
        t.end_fill()
        x+=40
    while y > -390:
        deplacement(380,y,t)
        t.begin_fill()
        t.color("yellow")
        t.circle(5)
        t.end_fill()
        y-=40
    x-=40
    while x > -390:
        deplacement(x,-380,t)
        t.begin_fill()
        t.color("yellow")
        t.circle(5)
        t.end_fill()
        x-=40
    y+=40
    while y < 390:
        deplacement(-380,y,t)
        t.begin_fill()
        t.color("yellow")
        t.circle(5)
        t.end_fill()
        y+=40

#fonction qui dessine pacman
def pacman(x,y,rayon,inclinaison,t):
    #l'inclinaison correspond à celle du pacman
    deplacement(x,y,t)
    t.setheading(inclinaison)
    t.down()
    t.color("yellow")
    t.begin_fill()
    t.circle(rayon,300)
    t.left(90)
    t.forward(rayon)
    t.right(120)
    t.forward(rayon)
    t.end_fill()
    t.setheading(inclinaison+250)
    t.forward(-rayon/2)
    t.color("black")
    t.begin_fill()
    t.circle(rayon/7)
    t.end_fill()
    t.setheading(0)

#fonction qui dessine le titre du jeu
def titre(x,y,t):
    deplacement(x,y,t)
    t.color("yellow")
    t.write("Pacman Game",font=('Rogue Hero 3D',30,'normal'))
  
#fonction qui dessine le carré de l'avancement
def cadreAvancement(t):
    deplacement(-110,340,t)
    t.color("white")
    t.write("TENTATIVES PERDUES",font=('Orbitron',15,'bold'))
    deplacement(-150,300,t)
    t.color("blue")
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(30)
        t.left(90)

#fonction qui dessine le numéro a coté des cases
def numeroCase(liste,t):
    i=1
    for el in liste:
        deplacement(el[0]-16,el[1]-3,t)
        c=color()
        t.color("yellow")
        t.write(str(i),font=('Arial',12,'normal'))
        t.color(c[0])
        i+=1

#fonction qui dessine tout le décor principal
def decor(t):
    t.ht()
    setworldcoordinates(-400,-400,400,400)
    bgcolor("black")
    points(-380,380,t)
    pacman(-210, -200, 60, 120,t)
    pacman(-200, 260, 40, 90,t)
    pacman(280, 310, 60, 130,t)
    pacman(300, -250, 40, 150,t)
    cerise(-280, -30, 5,t)
    cerise(320,100,5,t)
    fraise(-320, 100, 5, t)
    fraise(280, -30,5, t)
    cadreAvancement(t)
    titre(-135,-250,t)
