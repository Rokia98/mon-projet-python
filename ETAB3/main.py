import time
import bcrypt
from base import bd
from menus import afficher_menu, accueil, quitter
from services import gestion_eleves, gestion_professeurs, gestion_utilisateurs

# Fonction pour récupérer un utilisateur depuis la base de données
def recuperer_utilisateur(identifiant):
    connection = bd.create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT pseudo, mot_de_passe FROM utilisateurs WHERE pseudo = %s", (identifiant,))
        utilisateur = cursor.fetchone()
        cursor.close()
        connection.close()
        return utilisateur
    return None

debut = time.time() 

accueil("BIENVENUE DANS L'APPLICATION ETAB v1.3")
while True:
    identifiant = input("\033[0;37mEntrez votre identifiant : \033[0m")
    mot_de_passe = input("\033[0;37mEntrez votre mot de passe : \033[0m")
    
    utilisateur_data = recuperer_utilisateur(identifiant)
    
    if utilisateur_data and bcrypt.checkpw(mot_de_passe.encode('utf-8'), utilisateur_data[1].encode('utf-8')):  # Vérifiez le mot de passe
        print("\033[0;92mAuthentification réussie !!\033[0m")
        time.sleep(0.6)
        accueil("BIENVENUE DANS L'APPLICATION ETAB v1.3")
        while True:
            afficher_menu()
            try:
                choix = int(input("\033[0;37mChoisissez une option dans le menu : \033[0m"))
            except ValueError:
                print('\033[0;93mVous devez entrer un chiffre du menu !!\033[0m')
                time.sleep(0.5)
                continue

            match choix:
                case 1:
                    time.sleep(0.4)
                    gestion_eleves.gestionEleves()
                case 2:
                    time.sleep(0.4)
                    gestion_professeurs.gestionProfesseurs()
                case 3:
                    gestion_utilisateurs.gestionUtilisateurs()
                case 0:
                    quitter(debut)     
                    break               
                case _:
                    print("\033[0;93mOption invalide, veuillez réessayer !!\033[0m")
                    time.sleep(0.5)
                    continue
    else:
        print("\033[0;91mÉchec de l'authentification, veuillez vérifier les informations saisies !\033[0m")
        time.sleep(0.4)
        continue
    break