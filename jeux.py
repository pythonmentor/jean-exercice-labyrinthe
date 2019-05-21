# Lecture du fichier labyrinthe.txt
# with open("labyrinthe.txt", "r") as mon_fichier:
#      mon_labyrinthe = mon_fichier.readlines()

class Labyrinthe:

    def __init__(self, fichier):
        self.chemins = []
        self.murs = []
        self.hauteur = None
        self.largeur = None
        self.depart = None
        self.arriver = None
        self.fichier = fichier

    def charger(self):
        with open(self.fichier, "r") as mon_fichier:
            mon_labyrinthe = mon_fichier.readlines()

        for i, ligne in enumerate(mon_labyrinthe):
            for j, caractere in enumerate(ligne.strip()):
                if caractere == '.':
                    self.chemins.append((i, j))
                    
                elif caractere == '#':
                    self.murs.append((i, j))

                elif caractere == 'D':
                    self.depart = (i, j)
                    self.chemins.append((i, j))

                elif caractere == 'A':
                    self.arrivee = (i, j)
                    self.chemins.append((i, j))

        self.hauteur = len(mon_labyrinthe)
        self.largeur = len(mon_labyrinthe[0].strip())

    def afficher(self):
        for ligne in range(0, self.hauteur):
            for colonne in range(0, self.largeur):
                if (ligne, colonne) == self.depart:
                    print("D", end='')
                elif (ligne, colonne) == self.arrivee:
                    print("A", end='')
                elif (ligne, colonne) in self.chemins:
                    print(".", end='')
                elif (ligne, colonne) in self.murs:
                    print("#", end='')
            print()

labyrinthe_donnees = {
    "chemins": [], 
    "murs": [], 
    "hauteur": None, 
    "largeur": None, 
    "depart": None, 
    "arrivee": None
}

# Chargement du labyrinthe depuis le fichier labyrinthe.txt
def labyrinthe_charger_depuis_fichier(labyrinthe_donnees, nom_fichier="labyrinthe.txt"):
    with open(nom_fichier, "r") as mon_fichier:
        mon_labyrinthe = mon_fichier.readlines()
    charger(mon_labyrinthe, labyrinthe_donnees)
    # depart_et_arrivee_du_joueur()
    return labyrinthe_donnees
        
def charger(mon_labyrinthe, labyrinthe_donnees):      
    print("Lecture du fichier labyrinthe.txt ligne par ligne:\n")
    print(mon_labyrinthe)

    print("Determination de la position des chemins et des murs: ")
    for i, ligne in enumerate(mon_labyrinthe):
        for j, caractere in enumerate(ligne.strip()):
            if caractere == '.':
                labyrinthe_donnees['chemins'].append((i, j))
                
            elif caractere == '#':
                labyrinthe_donnees['murs'].append((i, j))

            elif caractere == 'D':
                labyrinthe_donnees['depart'] = (i, j)
                labyrinthe_donnees['chemins'].append((i, j))

            elif caractere == 'A':
                labyrinthe_donnees['arrivee'] = (i, j)
                labyrinthe_donnees['chemins'].append((i, j))
                

        print("Les chemins ", labyrinthe_donnees['chemins'])
        print("Les murs", labyrinthe_donnees['murs'])

    print("Détermination de la largeur et la hauteur du labyrinthe:")
    labyrinthe_donnees['hauteur'] = len(mon_labyrinthe)
    labyrinthe_donnees['largeur'] = len(mon_labyrinthe[0].strip())

    print("La largeur vaut: ", labyrinthe_donnees['hauteur'])
    print("La hauteur vaut: ", labyrinthe_donnees['largeur'])

        
        
# Détermination de la position de départ et d'arrivée du joueur
# def depart_et_arrivee_du_joueur():
#     chaine = " ".join(mon_labyrinthe)
#     #depart
#     depart = chaine.replace("...#######", "D..#######").strip()


#     f = open("labyrinthe.txt", "w")
#     ecriture_1 = f.write(depart)

#     # arrivee
#     arrivee = depart.replace("########.#", "########A#").strip()

#     f = open("labyrinthe.txt", "w")
#     ecriture_1 = f.write(arrivee)

# Chargement du fichier labyrinthe.txt et execution des methodes main(), depart_et_arrivee_du_joueur()


def main():
    laby = Labyrinthe("labyrinthe.txt")
    laby.charger()
    laby.afficher()

main()