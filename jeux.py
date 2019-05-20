# Lecture du fichier labyrinthe.txt
with open("labyrinthe.txt", "r") as mon_fichier:
     mon_labyrinthe = mon_fichier.readlines()

chemins = []
murs = []
largeur = None
hauteur = None
depart = None
arrivee = None
# Chargement du labyrinthe depuis le fichier labyrinthe.txt
def labyrinthe_charger_depuis_fichier(nom_fichier):
    main()
    depart_et_arrivee_du_joueur()
    return {
        "chemins": chemins, 
        "murs": murs, 
        "hauteur": hauteur, 
        "largeur": largeur, 
        "depart": depart, 
        "arrivee": arrivee
    }
        
def main():      
        print("Lecture du fichier labyrinthe.txt ligne par ligne:\n")
        print(mon_labyrinthe)

        print("Determination de la position des chemins et des murs: ")
        for i, ligne in enumerate(mon_labyrinthe):
            for j, caractere in enumerate(ligne.strip()):
                if caractere == '.':
                    chemins.append((i, j))
                    
                elif caractere == '#':
                    murs.append((i, j))
                   

            print("Les chemins ", chemins,)
            print("Les murs", murs)

        print("Détermination de la largeur et la hauteur du labyrinthe:")
        hauteur = len(mon_labyrinthe)
        largeur = len(mon_labyrinthe[0].strip())

        print("La largeur vaut: ", largeur)
        print("La hauteur vaut: ", hauteur)

        
        
# Détermination de la position de départ et d'arrivée du joueur
def depart_et_arrivee_du_joueur():
    chaine = " ".join(mon_labyrinthe)
    #depart
    depart = chaine.replace("...#######", "D..#######").strip()


    f = open("labyrinthe.txt", "w")
    ecriture_1 = f.write(depart)

    # arrivee
    arrivee = depart.replace("########.#", "########A#").strip()

    f = open("labyrinthe.txt", "w")
    ecriture_1 = f.write(arrivee)

# Chargement du fichier labyrinthe.txt et execution des methodes main(), depart_et_arrivee_du_joueur()
labyrinthe_charger_depuis_fichier("labyrinthe.txt")