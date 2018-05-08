import os
os.system("color A")
state = "not_finished"
X = 1
line = 6
row = 0
#on va définir le contenu de notre tableau
# case = [["■"] * playlonnes for _ in range(lignes)]
case = [["■"] * 12 for _ in range(12)]

#indication du stade de jeu pour voir si un joueur à gagner 
while state == "not_finished":
    
    #affichage du tableau de score et de playonne
    print("player", X, "choose a column")
    print("")
    print("  1 2 3 4 5 6 7  ")
    
    #actualisation du tableau
    print("_________________")
    print("║",case[1][1], case[2][1], case[3][1], case[4][1], case[5][1], case[6][1], case[7][1], "║")
    print("║",case[1][2], case[2][2], case[3][2], case[4][2], case[5][2], case[6][2], case[7][2], "║")
    print("║",case[1][3], case[2][3], case[3][3], case[4][3], case[5][3], case[6][3], case[7][3], "║")
    print("║",case[1][4], case[2][4], case[3][4], case[4][4], case[5][4], case[6][4], case[7][4], "║")
    print("║",case[1][5], case[2][5], case[3][5], case[4][5], case[5][5], case[6][5], case[7][5], "║")
    print("║",case[1][6], case[2][6], case[3][6], case[4][6], case[5][6], case[6][6], case[7][6], "║")


    # choix le la colonne à jouer
    
    print("")
    print("please choose a value on your keyboard to choose a column")
    play = input()
    while not (play == "1" or play == "2" or play == "3" or play == "4" or play == "5" or play == "6" or play == "7"):
        print("your value is incorrect please choose another")
        play = input()
    play = int(play)
    
        
    #mise en place du pion
    while case[play][line] == "X" or case[play][line] == "O":
        line -= 1           
    if X == 1:
        case[play][line] = "X"
    if X == 2:
        case[play][line] = "O"
            
            
        #vérification de la position des pions aux alentours + conditions de victoires pour le joueur 1
    if  X == 1:
        for tic in range(4):
            if case[play+tic][line+tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):        
            if case[play-tic][line+tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):
            if case[play+tic][line-tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):
            if case[play-tic][line-tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):
            if case[play+tic][line] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):
            if case[play-tic][line] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
        for tic in range(4):
            if case[play][line+tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play][line-tic] == "X":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

#vérification de la position des pions aux alentours + conditions de victoires pour le joueur 2
    if  X == 2:
        
        for tic in range(4):
            if case[play+tic][line+tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play-tic][line+tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play+tic][line-tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play-tic][line-tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play+tic][line] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0

        for tic in range(4):
            if case[play-tic][line] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
            
        for tic in range(4):
            if case[play][line+tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0
                    
        for tic in range(4):
            if case[play][line-tic] == "O":
                row += 1
        if row == 4:
            state = "finished"
        else:
            row = 0


        
    #reinitialisation de la hauteur de ligne
    line = 6

    
    #alternance du joueur
    if X == 1:
        X = 2
    elif X == 2:
        X = 1

#affichage du score final de la partie ainsi que le numéro du gagnant.
print("_________________")
print("║",case[1][1], case[2][1], case[3][1], case[4][1], case[5][1], case[6][1], case[7][1], "║")
print("║",case[1][2], case[2][2], case[3][2], case[4][2], case[5][2], case[6][2], case[7][2], "║")
print("║",case[1][3], case[2][3], case[3][3], case[4][3], case[5][3], case[6][3], case[7][3], "║")
print("║",case[1][4], case[2][4], case[3][4], case[4][4], case[5][4], case[6][4], case[7][4], "║")
print("║",case[1][5], case[2][5], case[3][5], case[4][5], case[5][5], case[6][5], case[7][5], "║")
print("║",case[1][6], case[2][6], case[3][6], case[4][6], case[5][6], case[6][6], case[7][6], "║")
print("")
print("")

if X == 2:
    print("player 1 wins")
if X == 1:
    print("player 2 wins")
print("GG WP")





