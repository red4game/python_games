import pygame
from pygame.locals import *
"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
screen = pygame.display.set_mode((750, 750))

background_menu = pygame.image.load("accueil.png").convert()
background_menu = pygame.transform.scale(background_menu, (750,750))


backgroundN1 = pygame.image.load("fond.jpg")
backgroundN1 = pygame.transform.scale(backgroundN1, (750,750))

backgroundN2 = pygame.image.load("fond.jpg")
backgroundN2 = pygame.transform.scale(backgroundN2, (750,750))

tableau = [0] * 15
n = 0
with open("tableau.txt", "r") as fichier:
    for ligne in fichier:
        tableau[n] = ligne
        n += 1

icone = pygame.image.load("doge.png").convert_alpha()
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption("simulation A* labyrinthe DK")


proceed = 1
menu = 1
niveau1 = 0
niveau2 = 0

sprite_case = pygame.image.load("mur.png").convert_alpha()
sprite_case = pygame.transform.scale(sprite_case, (50,50))

sprite_depart = pygame.image.load("depart.png").convert_alpha()
sprite_depart = pygame.transform.scale(sprite_depart, (50,50))

sprite_arrive = pygame.image.load("arrivee.png").convert_alpha()
sprite_arrive = pygame.transform.scale(sprite_arrive, (50,50))

personnage_droite = pygame.image.load("dk_droite.png").convert_alpha()
personnage_droite = pygame.transform.scale(personnage_droite, (50,50))

personnage_gauche = pygame.image.load("dk_gauche.png").convert_alpha()
personnage_gauche = pygame.transform.scale(personnage_gauche, (50,50))

personnage_haut = pygame.image.load("dk_haut.png").convert_alpha()
personnage_haut = pygame.transform.scale(personnage_haut, (50,50))

personnage_bas = pygame.image.load("dk_bas.png").convert_alpha()
personnage_bas = pygame.transform.scale(personnage_bas, (50,50))

personnage = personnage_droite

X = 0
Y = 0

pygame.key.set_repeat(400, 30)

pygame.time.Clock().tick(30)

pygame.display.flip()

affichage = 1

while proceed:
    while menu:
        screen.blit(background_menu, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                proceed = 0
                menu = 0
            if event.type == KEYDOWN and event.key == K_F1:
                niveau1 = 1
                menu = 0
                screen.blit(backgroundN1, (0, 0))
            if event.type == KEYDOWN and event.key == K_F2:
                niveau2 = 1
                menu = 0
                screen.blit(backgroundN2, (0, 0))

    while niveau1 == 1:
        #événement de fermeture
        for event in pygame.event.get():
            if event.type == QUIT:
                proceed = 0
                niveau1 = 0
            #deplacement personnage
            if event.type == KEYDOWN :
                if event.key == K_UP and Y - 50 >= 0:
                    if tableau[int((Y-50)/50)][int(X/50)] != "m":
                        Y -= 50
                        personnage = personnage_haut
                        screen.blit(backgroundN1, (0, 0))
                        affichage = 1
                if event.key == K_DOWN and Y + 50 <= 700:
                    if tableau[int((Y+50)/50)][int(X/50)] != "m":
                        Y += 50
                        personnage = personnage_bas
                        screen.blit(backgroundN1, (0, 0))
                        affichage = 1
                if event.key == K_RIGHT and X + 50 <= 700:
                    if tableau[int(Y/50)][int((X+50)/50)] != "m":
                        X += 50
                        personnage = personnage_droite
                        screen.blit(backgroundN1, (0, 0))
                        affichage = 1
                if event.key == K_LEFT and X - 50 >= 0:
                    if tableau[int(Y / 50)][int((X - 50) / 50)] != "m":
                        X -= 50
                        personnage = personnage_gauche
                        screen.blit(backgroundN1, (0,0))
                        affichage = 1


        #affichage du niveau
        while affichage:
            for lignes in range(15):
                for case in range(15):
                    if tableau[lignes][case] == "m":
                        position_x = case * 50
                        position_y = lignes * 50
                        screen.blit(sprite_case, (position_x, position_y))
                        screen.blit(sprite_depart, (0,0))
                        screen.blit(sprite_arrive, (700,700))
                        screen.blit(personnage, (X, Y))
            affichage = 0
        pygame.display.flip()

        #condition de victoire.
        if X == 700 and Y == 700:
            X = 0
            Y = 0
            menu = 1
            affichage = 1
            niveau1 = 0


    while niveau2 == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                proceed = 0
                niveau2 = 0
        screen.blit(backgroundN2, (0, 0))
        pygame.display.flip()