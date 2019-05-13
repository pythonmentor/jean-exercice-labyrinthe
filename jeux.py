
with open("labyrinthe.txt", "r") as mon_fichier:
    mon_labyrinthe = mon_fichier.readlines()

    print("1. Lecture du fichier labyrinthe.txt ligne par ligne:\n")

    for i, elt in enumerate(mon_labyrinthe):
        print(i, elt)


    with open("labyrinthe.txt", "r") as fichier:
        mon_fichier_2 = fichier.readline().strip()

        print("4. Calcul de la largeur et la hauteur du labyrinthe:")

        largeur = len(mon_fichier_2)
        print("La largeur du labyrinthe vaut:", largeur)

       
        mon_fichier_3 = fichier.readlines()

        aire_du_labyrinthe = len("".join(mon_fichier_3))


        hauteur = aire_du_labyrinthe / largeur
        print("La hauteur vaut: ", hauteur)


         
        


        
        
        

   

   

        

