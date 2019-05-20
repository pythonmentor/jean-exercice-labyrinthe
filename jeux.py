def labyrinthe_charger_depuis_fichier(nom_fichier):


    return {
        "chemins": valeur, 
        "murs": valeur, 
        "hauteur": valeur, 
        "largeur": valeur, 
        "depart": valeur, 
        "arrivee": valeur
    }


def main():
    chemins = []
    murs = []
    largeur = None
    hauteur = None

    with open("labyrinthe.txt", "r") as mon_fichier:
        mon_labyrinthe = mon_fichier.readlines()
        hauteur = len(mon_labyrinthe)
        largeur = len(mon_labyrinthe[0].strip())
        print(mon_labyrinthe)

        print("1. Lecture du fichier labyrinthe.txt ligne par ligne:\n")

        for i, ligne in enumerate(mon_labyrinthe):
            for j, caractere in enumerate(ligne.strip()):
                if caractere == '.':
                    chemins.append((i, j))
                elif caractere == '#':
                    murs.append((i, j))

        
main()