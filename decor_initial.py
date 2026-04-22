from turtle import *
from decor import *

#le dessin du décor principal est instantané
tracer(0)

#fonction qui effectue un déplacement de la tortue
def deplacement(x,y,t):
    t.up()
    t.goto(x,y)
    t.down()

#fonction qui dessine le cadre autour de la fenetre
def cadreBleu(x,y,l,t):
    deplacement(x,y,t)
    t.color("blue")
    t.pensize(3)
    for i in range(4):
        t.forward(l)
        t.right(90)
    t.pensize(1)

#fonction qui dessine le titre du jeu
def intitule(t):
    deplacement(-200,-20,t)
    t.color("yellow")
    t.write("Pacman Game",font=('Rogue Hero 3D',45,'normal'))
    deplacement(6,-40,t)
    t.write("Jeu de memory",font=('Orbitron',20,'normal'))

def caseNiveau(coorNiveau,diffNiveau,t):
    t.ht()
    for i in range(4):
        t.color("white")
        t.up()
        t.goto(coorNiveau[i],-130)
        t.down()
        t.setheading(0)
        t.begin_fill()
        for e in range(2):
            t.forward(80)
            t.left(90)
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.goto(coorNiveau[i]+10,-105)
        t.color("black")
        t.write("niveau "+str(i+1),font=('Orbitron',12,'normal'))
        t.up()
        t.goto(coorNiveau[i]+10,-125)
        t.down()
        t.write(diffNiveau[i],font=('Orbitron',12,'normal'))
    
#fonction qui dessine tout le décor principale
def decor1(t):
    setworldcoordinates(-400,-400,400,400)
    bgcolor("black")
    points(-380,380,t)
    pacman(-200, -200, 60, 120,t)
    pacman(-200, 280, 60, 120,t)
    pacman(280, 280, 60, 120,t)
    pacman(280, -200, 60, 120,t)
    cadreBleu(-350,350,700,t)
    cadreBleu(-360,360,719,t)
    intitule(t)
    cerise(-70,280,5,t)
    cerise(-70,-210,5,t)
    cerise(-240,100,5,t)
    cerise(260,100,5,t)
    fraise(50,270,5,t)
    fraise(50,-210,5,t)
    fraise(-260,-50,5,t)
    fraise(240,-50,5,t)
    
