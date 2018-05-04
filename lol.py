state = "not_finished"
X = 1
#voici le tableau de base
line0 = "_________________"
line1 = "║ ■ ■ ■ ■ ■ ■ ■ ║"
line2 = "║ ■ ■ ■ ■ ■ ■ ■ ║"
line3 = "║ ■ ■ ■ ■ ■ ■ ■ ║"
line4 = "║ ■ ■ ■ ■ ■ ■ ■ ║"
line5 = "║ ■ ■ ■ ■ ■ ■ ■ ║"
line6 = "║ ■ ■ ■ ■ ■ ■ ■ ║"

#split du tableau pour avoir la valeur du caractère
case1 = line1.split(" ")
case2 = line2.split(" ")
case3 = line3.split(" ")
case4 = line4.split(" ")
case5 = line5.split(" ")
case6 = line6.split(" ")
while state == "not_finished":

    #affichage du tableau
    print("player", X, "choose a collumn")
    print("")
    print("  1 2 3 4 5 6 7  ")
    #toute les case de la ligne 1 -> attribution dans des variables pour avoir les caractères en raw
    case11 = case1[1]
    case12 = case1[2]
    case13 = case1[3]
    case14 = case1[4]
    case15 = case1[5]
    case16 = case1[6]
    case17 = case1[7]

 #toute les case de la ligne 2 -> attribution dans des variables pour avoir les caractères en raw
    case21 = case2[1]
    case22 = case2[2]
    case23 = case2[3]
    case24 = case2[4]
    case25 = case2[5]
    case26 = case2[6]
    case27 = case2[7]

 #toute les case de la ligne 3 -> attribution dans des variables pour avoir les caractères en raw
    case31 = case3[1]
    case32 = case3[2]
    case33 = case3[3]
    case34 = case3[4]
    case35 = case3[5]
    case36 = case3[6]
    case37 = case3[7]

 #toute les case de la ligne 4 -> attribution dans des variables pour avoir les caractères en raw
    case41 = case4[1]
    case42 = case4[2]
    case43 = case4[3]
    case44 = case4[4]
    case45 = case4[5]
    case46 = case4[6]
    case47 = case4[7]

 #toute les case de la ligne 5 -> attribution dans des variables pour avoir les caractères en raw
    case51 = case5[1]
    case52 = case5[2]
    case53 = case5[3]
    case54 = case5[4]
    case55 = case5[5]
    case56 = case5[6]
    case57 = case5[7]

 #toute les case de la ligne 6 -> attribution dans des variables pour avoir les caractères en raw
    case61 = case6[1]
    case62 = case6[2]
    case63 = case6[3]
    case64 = case6[4]
    case65 = case6[5]
    case66 = case6[6]
    case67 = case6[7]


    #actualisation du tableau
    print("_________________")
    print("║",case11, case12, case13, case14, case15, case16, case17, "║")
    print("║",case21, case22, case23, case24, case25, case26, case27, "║")
    print("║",case31, case32, case33, case34, case35, case36, case37, "║")
    print("║",case41, case42, case43, case44, case45, case46, case47, "║")
    print("║",case51, case52, case53, case54, case55, case56, case57, "║")
    print("║",case61, case62, case63, case64, case65, case66, case67, "║")


    # choix le la colonne à jouer
    
    print("")
    print("please choose a value on your keyboard to choose a column")
    play = int(input())
    if play > 7:
        print("your value is incorect, please choose another value")
        
    #mise en place du pion
    for col in range(1,7):
        if play == col:
            poss = "X"
            line = 0
            line += 1
            while poss == "X" or poss == "O":
                line += 1
                coll = str(col)
                linne = str(7-line)
                poss = "case"+linne+coll
                pos = poss.split(" ")
                print(pos[0])
            if X == 1:
               pos[0] = "X"
            if X == 2:
               poss = "O"

    #alternance du joueur
    if X == 1:
        X = 2
    elif X == 2:
        X = 1


