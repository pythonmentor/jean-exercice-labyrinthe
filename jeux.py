import pickle

# 
i = 0
with open("labyrinthe.txt", "r") as mon_fichier:
    mon_labyrinthe = mon_fichier.readlines()

    print("1. Lecture du fichier labyrinthe.txt ligne par ligne:\n")

    for i, elt in enumerate(mon_labyrinthe):
        print("À la ligne {} se trouve {}".format(i,elt))

