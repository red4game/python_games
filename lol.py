state = "not_finished"
X = 1
line = 1
puis = 0
#on va définir le contenu de notre tableau
# case = [["■"] * collonnes for _ in range(lignes)]
case = [["■"] * 12 for _ in range(12)]

#indication du stade de jeu pour voir si un joueur à gagner 
while state == "not_finished":
    
    #affichage du tableau de score et de colonne
    print("player", X, "choose a collumn")
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
    for col in range(1,8):
        if play == col:
            linne = 7-line
            while case[col][linne] == "X" or case[col][linne] == "O":
                line += 1
                linne = 8-line
            if X == 1:
               case[col][linne] = "X"
            if X == 2:
               case[col][linne] = "O"
            line = 1

            
        #verification de la condition de victoire
    if  X == 1 and col-4 > 0 and col+4 < 8 and linne-4 > 0 and linne+4 < 7:
        for loop in range(4):
            if case[col+loop][linne+loop] == "X" or case[col-loop][linne-loop] == "X" or case[col+loop][linne-loop] == "X" or case[col-loop][linne+loop] == "X" or case[col+loop][linne] == "X" or case[col-loop][linne] == "X" or case[col][linne+loop] == "X" or case[col][linne-loop] == "X":
                puis +=1
            
    elif  X == 2 and col-4 > 0 and col+4 < 8 and linne-4 > 0 and linne+4 < 7:
        for num in range(0,3):
            if case[col+num][linne+num] == "O" or case[col-num][linne-loop] == "O" or case[col+loop][linne-loop] == "O" or case[col-loop][linne+loop] == "O" or case[col+loop][linne] == "O" or case[col-loop][linne] == "O" or case[col][linne+loop] == "O" or case[col][linne-loop] == "O":
                puis += 1
    print(puis)
    if puis == 4:
        state = "finished"
        
    print(state)
    #alternance du joueur
    if X == 1:
        X = 2
    elif X == 2:
        X = 1
    puis = 0
print("GG WP")
print("_________________")
print("║",case[1][1], case[2][1], case[3][1], case[4][1], case[5][1], case[6][1], case[7][1], "║")
print("║",case[1][2], case[2][2], case[3][2], case[4][2], case[5][2], case[6][2], case[7][2], "║")
print("║",case[1][3], case[2][3], case[3][3], case[4][3], case[5][3], case[6][3], case[7][3], "║")
print("║",case[1][4], case[2][4], case[3][4], case[4][4], case[5][4], case[6][4], case[7][4], "║")
print("║",case[1][5], case[2][5], case[3][5], case[4][5], case[5][5], case[6][5], case[7][5], "║")
print("║",case[1][6], case[2][6], case[3][6], case[4][6], case[5][6], case[6][6], case[7][6], "║")



