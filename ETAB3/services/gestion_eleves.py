import time
from menus import afficherSousMenuElev, accueil
from Eleve.eleve import Eleve

def ajouterEleve():
    dateNaissance = input("Entrez la date de naissance (YYYY-MM-DD) : ")
    ville = input("Entrez la ville : ")
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    telephone = input("Entrez le numéro de téléphone : ")
    classe = input("Entrez la classe : ")
    matricule = input("Entrez le matricule : ")

    eleve = Eleve(dateNaissance, ville, prenom, nom, telephone, classe, matricule)
    Eleve.ajouter(eleve)
    print(f"Élève {prenom} {nom} ajouté avec succès.")

def listerEleves():
    eleves = Eleve.obtenirEleve()
    if eleves:
        print("Liste des élèves :")
        for eleve in eleves:
            print(eleve)
    else:
        print("Aucun élève enregistré.")

def modifierEleve():
    matricule = input("Entrez le matricule de l'élève à modifier : ")
    eleve = Eleve.obtenir(matricule)
    if eleve:
        print(f"Modification de l'élève : {eleve}")
        # Demande des nouvelles informations
        eleve.set_date_naissance  = input("Nouvelle date de naissance (YYYY-MM-DD) : ") or eleve.date_naissance 
        eleve.set_ville = input("Nouvelle ville : ") or eleve.ville
        eleve.set_prenom = input("Nouveau prénom : ") or eleve.prenom
        eleve.set_nom = input("Nouveau nom : ") or eleve.nom
        eleve.set_telephone = input("Nouveau téléphone : ") or eleve.telephone
        eleve.set_classe = input("Nouvelle classe : ") or eleve.classe
        print(f"Élève {eleve.prenom} {eleve.nom} modifié avec succès.")
    else:
        print(f"Aucun élève trouvé avec le matricule {matricule}.")

def supprimerEleve():
    matricule = input("Entrez le matricule de l'élève à supprimer : ")
    if Eleve.supprimer(matricule):
        print(f"Élève avec matricule {matricule} supprimé avec succès.")
    else:
        print(f"Aucun élève trouvé avec le matricule {matricule}.")

def gestionEleves():
    accueil("GESTION DES ÉLÈVES")
    while True:
        afficherSousMenuElev()
        try:
            choix = int(input("\033[0;37mChoisissez une option dans le menu : \033[0m"))
        except ValueError:
            print('\033[0;93mVous devez entrer un chiffre du menu !!\033[0m')
            time.sleep(0.5)
            continue

        match choix:
            case 1:
                ajouterEleve()
            case 2:
                supprimerEleve()
            case 3:
                modifierEleve()
            case 4:
                listerEleves()               
            case 5:
                break             
            case 0:
                return                   
            case _:
                print("\033[0;93mOption invalide, veuillez réessayer !!\033[0m")
                time.sleep(0.5)
                continue