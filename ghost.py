from turtle import *
from math import *

#dessine le fantome (qui est la case qui cache l'objet dans le jeu) 
def fantome(x,y,longueur):
    up()
    goto(x,y)
    down()
    setheading(0)
    hideturtle()
    begin_fill()
    color("blue")
    left(90)
    forward(longueur)
    circle(-(longueur/2), 180)
    forward(longueur)
    right(90)
    a = longueur/4
    hypo = sqrt((a/2)**2 + 4**2)
    rad = asin(sin(4/hypo))
    angle = rad * 180 / pi
    right(angle)
    #partie qui fait les triangles du fantome
    for i in range(4):
        forward(hypo)
        left(2*angle)
        forward(hypo)
        left(180+(2*(90-angle)))
    end_fill()
    #partie qui dessine les yeux du fantome
    s = 0 #permet de dessiner les deux yeux
    for e in range(2):
        setheading(140)
        up()
        goto(x+(longueur/4)+s,y+(longueur-5))
        down()
        color("yellow")
        begin_fill()
        for i in range(2):
            circle(-longueur/5,90)
            circle(-longueur/10,90)
        end_fill()
        forward(4)
        begin_fill()
        color("black")
        circle(-longueur/20)
        end_fill()
        s=s+longueur/3
