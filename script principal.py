from turtle import * 
from decor import *
from objet import *
from decor_initial import *
from ghost import *
import random
import time

#on initialise une varible rejouer avec "oui"
rejouer = "oui"

#tant que la variable rejouer est égale à "oui" alors on joue au memory
while rejouer == "oui":
    # tortue des cases
    ti = Turtle() # décor initial
    td = Turtle() # décor principal
    tc = Turtle() # programme
    
    #on affiche le premier décor (celui initial)
    decor1(ti)

    #liste avec les coordonnées x des cases des niveaux
    coorNiveau = [-190,-90,10,110]
    
    #liste avec les difficultés des niveaux
    diffNiveau=["facile","moyen","difficile","extreme"]

    #on dessine les cases des niveaux
    caseNiveau(coorNiveau,diffNiveau,ti)

    #on initialise les coordonnées de la souris
    mouse_coordinates = [-1, -1]

    #global permet d'utiliser la varible mouse_coordinate meme à l'intérieur de la fonction
    def update_mouse_coordinates(x, y):
        global mouse_coordinates
        mouse_coordinates = [x, y]

    #btn=1 signifie qu'il faut cliquer avec le bouton gauche
    onscreenclick(update_mouse_coordinates, btn=1)

    #récupère coordonnées et les renvoies
    def get_mouse_click():
        global mouse_coordinates
        mouse_coordinates = [-1, -1]
        while mouse_coordinates == [-1, -1]:
            time.sleep(0.01)
            update()
        return mouse_coordinates

    #fonction qui prend la valeur du niveau quand on clique
    nbrNiveau = 0
    while nbrNiveau == 0:
        click = get_mouse_click()
        for el in coorNiveau:
            if click[0]>el and click[0]<el+80:
                if click[1]>-130 and click[1]<-80:
                    nbrNiveau = coorNiveau.index(el)+1

    #la valeur di numero du niveau est un entier, on la converti en string
    nbrNiveau = str(nbrNiveau)
    
    #on efface le décor initial
    ti.reset()

    #liste avec le noms des objets du memory (cerise, pomme, orange, melon, raisin, poire)
    objet = ["C","P","O","M","R","E"]

    #on mélange la liste des objets
    random.shuffle(objet)
    
    #on initialise le nombre de tentatives
    tentatives = 0

    #on initialise une liste coor qui va contenir les coordonnées des cases
    coor = []

    #en fonction du nombre de cases choisies on définit la liste objet 
    #on ajoute a coor les coordonnées exactes pour le nombre spécifique de cases
    if nbrNiveau == "1":
        #on ne prend que les trois premiers objets
        objet = objet[:3]
        coor = [[-190,35], [-34,35], [122,35], [-190,-130], [-34,-130], [122,-130]]
        tentatives = 8
    
    if nbrNiveau == "2":
        #on ne prend que les quatre premiers objets
        objet = objet[:4]
        coor = [[-200,35], [-83,35], [34,35], [151,35], [-200,-130], [-83,-130], [34,-130], [151,-130]]
        tentatives = 7
    
    if nbrNiveau == "3":
        #on ne prend que les cinq premiers objets
        objet = objet[:5]
        coor = [[-220,35], [-126,35], [-32,35], [62,35], [156,35], [-220,-130], [-126,-130], [-32,-130], [62,-130], [156,-130]]
        tentatives = 6
    
    if nbrNiveau == "4":
        #on prend les six objets
        coor = [[-220,35], [-140,35], [-60,35], [20,35], [100,35], [175,35], [-220,-130], [-140,-130], [-60,-130], [20,-130], [100,-130], [175,-130]]
        tentatives = 5

    #on crée une deuxième liste pour avoir les coordonnées dans le désordre
    coor2 = []
    for el in coor:
        coor2.append(el)

    #on crée une deuxième liste d'objet pour crée la paire de chaque objet
    objet2 = []
    for ele in objet:
        objet2.append(ele)
        objet2.append(ele)

    #on mélange la liste qui contient les coordonnées et les objets
    random.shuffle(coor2)
    random.shuffle(objet2)

    #on crée une liste avec 12 différentes couleurs
    couleur = ["red","blue","yellow","darkorange","navy","turquoise","forestgreen","palegreen","lightcoral","dimgrey","darkmagenta","dodgerblue"]

    #on mélange la liste qui contient les couleurs
    random.shuffle(couleur)

    #on initalise une nouvelle liste qui sera la principale
    liste = []

    #on ajoute a la liste des coordonnées l'objet et la lettre "o" (cela signifie que l'objet est caché)
    #ensuite on ajoute a la liste principale toutes les sous-listes contenues dans la liste des coordonnées
    indice = 0
    for el in coor2:
        el.append(objet2[indice]) 
        el.append("o") #signifie que l'objet est couvert
        el.append(couleur[indice])
        #on affecte a la liste les informations de chaque objet
        liste.append(el)
        indice += 1

    #fonction qui dessine la jauge avec l'avancement dans le jeu (tentatives perdues)
    def avancement(x,t):
        t.hideturtle()
        t.setheading(0)
        for e in range(x):
            t.up()
            t.goto(-150,300)
            t.down()
            s=0
            t.color("blue")
            t.begin_fill()
            for f in range(x):
                for i in range(2):
                    #en fonction des tentatives totales, la jauge avance proportionellement
                    t.forward((300/tentatives)+s)
                    t.left(90)
                    t.forward(30)
                    t.left(90)
                s=s+(300/tentatives)
            t.end_fill()
        
    #fonction qui dessine l'objet ou la case qui le cache
    def Objet_ou_Case(listePoly):
        #on prend chaque élément qui caractérise un polygone
        for i in range(len(listePoly)):
            poly = listePoly[i]
            #on dessine l'objet si il n'est pas caché (n pour non il n'est pas caché)
            if poly[3] == "n":
                if poly[2]=="C":
                    ceriseD(poly[0], poly[1], 60, poly[4], tc)
                if poly[2]=="P":
                    pomme(poly[0]+5, poly[1], 15, poly[4], tc)
                if poly[2]=="O":
                    orange(poly[0], poly[1], 20, poly[4], tc)
                if poly[2]=="M":
                    melon(poly[0], poly[1], 20, poly[4], tc)
                if poly[2]=="R":
                    raisin(poly[0], poly[1], 50, poly[4], tc)
                if poly[2]=="E":
                    poire(poly[0]+5, poly[1], 15, poly[4], tc)
            #sinon on dessine la case qui cache l'objet
            else:
                fantome(poly[0], poly[1], 50)
        update()
    
    #on dessine le décor
    decor(td)

    #on dessine le numéro des cases
    numeroCase(coor,td)

    #on cache la tortue des objets
    tc.ht()

    #on dessine les cases
    Objet_ou_Case(liste)

######################################
#         programme principal
######################################

    fin = 0 #variable qui augmente et indique la fin de la boucle
    tentativePerdue = 0  #variable qui compte le nombre de tenatives perdues
    numeroTrouver = [] #liste avec le numéro des cases trouvées

    while fin < len(liste)/2 and tentatives>tentativePerdue:
        #on appelle la tortue (ti) du décor initial car celle-ci n'est plus utilisée
        #dans la partie principale du jeu et on écrit a chaque tour les tentatives restantes
        ti.ht()
        ti.up()
        ti.goto(-110,270)
        ti.down()
        ti.color("white")
        ti.clear()
        ti.write("Tentatives restantes : "+str(tentatives-tentativePerdue),font=('Orbitron',15,'normal'))
        #on initialise la valeur de deux cases à -1
        caseA=-1
        caseB=-1
        #tant que la valeur de la case A est de -1
        while caseA == -1:
            #on récupère les coordonnées du clic
            clic1 = get_mouse_click()
            #en fonction des coordonnées des objets on vérifie à quelle objets correspond
            for el in coor2:
                if clic1[0]>el[0]-10 and clic1[0]<el[0]+60:   #on vérifie les coordonnées en x
                    if clic1[1]>el[1]-10 and clic1[1]<el[1]+80:   #on vérifie les coordonnées en y
                        caseA = coor2.index(el)
            #on vérifie que la case cliquée ne soit pas déjà découverte
            if caseA in numeroTrouver:
                caseA = -1
                
        #on dit que la case séléctionnée n'est pas couverte
        liste[caseA][3] = "n"
        #permet d'effacer les toutes les cases
        reset()
        #on dessine soit les cases soit les objets 
        Objet_ou_Case(liste)          #on verra que la case A

        #tant que la valeur de la case B est de -1
        while caseB == -1:
            #on récupère les coordonnées du clic
            clic2 = get_mouse_click()
            #en fonction des coordonnées des objets on vérifie à quelle objets correspond
            for el in coor2:
                if clic2[0]>el[0]-10 and clic2[0]<el[0]+60:
                    if clic2[1]>el[1]-10 and clic2[1]<el[1]+80:
                        caseB = coor2.index(el)
            #on vérifie que la case cliquée ne soit pas déjà découverte ou égale à celle d'avant
            if caseB in numeroTrouver or caseB==caseA:
                caseB = -1
            
        #on dit que la case séléctionnée n'est pas couverte
        liste[caseB][3] = "n"
        #permet d'effacer les toutes les cases
        reset()
        #on dessine soit les cases soit les objets 
        Objet_ou_Case(liste)       #on verra les cases A et B

        #si le nom de l'objet des deux cases est différents alors ce ne sont pas les memes
        if liste[caseA][2] != liste[caseB][2]:
            #on affiche les deux cases découvertes pendant 1,5 secondes
            time.sleep(1.5)
            #on dit que les cases sont couvertes
            liste[caseA][3] = "o"
            liste[caseB][3] = "o"
            tentativePerdue = tentativePerdue + 1
            avancement(tentativePerdue,td)  #on augmente la jauge
        #sinon c'est les memes
        else:
            numeroTrouver.append(caseA)
            numeroTrouver.append(caseB)
            fin = fin + 1

        #on cache ou pas les cases si celles-ci sont pareilles
        Objet_ou_Case(liste)

    #on efface la phrase qui nous dit les tentatives restantes mais pas la jauge
    ti.clear()

    #si on a gagné
    if fin == len(liste)/2:
        td.up()
        td.goto(-135, 230)
        td.down()
        td.color("white")
        td.write("toutes les cases ont été trouvées",font=('Rogue Hero 3D',13,'normal'))
        #si on a trouvé tous les objets sans avoir perdu de tentative
        if tentativePerdue == 0:
            td.up()
            td.goto(-60, 260)
            td.down()
            td.write("Quelle chance!",font=('Orbitron',14,'normal'))
        td.up()
        td.goto(-120,190)
        td.down()
        td.color("yellow")
        td.write("VOUS AVEZ GAGNE ☺︎",font=('Rogue Hero 3D',20,'normal'))

    #si on a perdu
    if tentativePerdue == tentatives:
        td.up()
        td.goto(-160, 230)
        td.down()
        td.color("white")
        td.write("toutes les cases n'ont pas été trouvées",font=('Rogue Hero 3D',13,'normal'))
        td.up()
        td.goto(-120,190)
        td.down()
        td.color("yellow")
        td.write("VOUS AVEZ PERDU︎ ☹︎",font=('Rogue Hero 3D',20,'normal'))

    #on demande si l'utilisateur veut rejouer
    rejouer = textinput("Rejouer ? : ","Taper 'oui' pour rejouer")
    
    #on efface tous les éléments du jeu
    td.reset()
    tc.reset()
    ti.reset()
    reset()

#on est dans le cas où la personne ne veut plus rejouer, le jeu se termine
#on affiche un "game over"
bgcolor("black")
points(-380,380,td)
td.up()
td.goto(-215,-20)
td.down()
td.color("yellow")
td.write("GAME OVER",font=('Rogue Hero 3D',60,'normal'))

#phrase qui nous indique comment terminer le jeu et fermer la fenetre
td.up()
td.goto(-270,-360)
td.down()
td.color("white")
td.write("Cliquer sur la fenetre pour terminer le jeu !",font=('Rogue Hero 3D',18,'normal'))

#fonction qui permet de fermer la fenetre quand on clique dessus
exitonclick()
