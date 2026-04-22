from turtle import *

#module qui permet de dessiner une fraise en pixel

#fonction qui dessine un rectangle de "pixel"
def rectangle(longueur,t):
    t.begin_fill()
    for i in range(2):
        t.forward(longueur*2)
        t.right(90)
        t.forward(longueur)
        t.right(90)
    t.end_fill()

#fonction qui dessine un carré de "pixel"
def carre(longueur,t):
    t.begin_fill()
    for i in range(4):
        t.forward(longueur)
        t.right(90)
    t.end_fill()

#fonction qui effectue un déplacement de la tortue
def deplacement(x,y,t):
    t.up()
    t.goto(x,y)
    t.down()

#fonction qui dessine une fraise en pixel
def fraise(x,y,longueur,t):
    #on dessine les pixels verts
    t.color("green")
    deplacement(x,y,t)
    rectangle(longueur,t)
    deplacement(x,y-longueur,t)
    rectangle(longueur,t)
    deplacement(x-2*longueur,y-2*longueur,t)
    rectangle(longueur,t)
    deplacement(x,y-2*longueur,t)
    rectangle(longueur,t)
    deplacement(x+2*longueur,y-2*longueur,t)
    rectangle(longueur,t)
    deplacement(x-longueur,y-3*longueur,t)
    rectangle(longueur,t)
    deplacement(x+longueur,y-3*longueur,t)
    rectangle(longueur,t)

    #on dessine les pixels rouges
    t.color("red")
    deplacement(x-3*longueur,y-3*longueur,t)
    rectangle(longueur,t)
    deplacement(x+3*longueur,y-3*longueur,t)
    rectangle(longueur,t)
    #création de boucle pour améliorer le temps d'exécution
    o=0
    for i in range(3):
        s=0
        for e in range(5):
            deplacement(x+(-4+s)*longueur,y+(-4+o)*longueur,t)
            rectangle(longueur,t)
            s=s+2
        o=o-1

    n=0
    for i in range(2):
        s=0
        for e in range(4):
            deplacement(x+(-3+s)*longueur,y+(-7+n)*longueur,t)
            rectangle(longueur,t)
            s=s+2
        n=n-1

    m=0
    for i in range(3):
        deplacement(x+(-2+m)*longueur,y-9*longueur,t)
        rectangle(longueur,t)
        m=m+2

    deplacement(x-longueur,y-10*longueur,t)
    rectangle(longueur,t)
    deplacement(x+longueur,y-10*longueur,t)
    rectangle(longueur,t)
    deplacement(x,y-11*longueur,t)
    rectangle(longueur,t)

    #on dessine les pixels blancs
    t.color("white")
    deplacement(x-2*longueur,y-5*longueur,t)
    carre(longueur,t)
    deplacement(x-longueur,y-8*longueur,t)
    carre(longueur,t)
    deplacement(x+longueur,y-10*longueur,t)
    carre(longueur,t)
    deplacement(x+longueur,y-6*longueur,t)
    rectangle(longueur,t)
    deplacement(x+longueur,y-7*longueur,t)
    rectangle(longueur,t)
