import mysql.connector  # Assurez-vous que ce module est installé

def ajouter_eleve(curseur, date_naissance, ville, prenom, nom, telephone, classe, matricule):
    """Ajoute un élève à la base de données."""
    query = ("INSERT INTO eleves (date_naissance, ville, prenom, nom, telephone, classe, matricule) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    curseur.execute(query, (date_naissance, ville, prenom, nom, telephone, classe, matricule))

def modifier_eleve(curseur, matricule, nouveau_telephone, nouvelle_classe):
    """Modifie les informations d'un élève dans la base de données."""
    query = ("UPDATE eleves SET telephone = %s, classe = %s WHERE matricule = %s")
    curseur.execute(query, (nouveau_telephone, nouvelle_classe, matricule))

def supprimer_eleve(curseur, matricule):
    """Supprime un élève de la base de données."""
    query = "DELETE FROM eleves WHERE matricule = %s"
    curseur.execute(query, (matricule,))

def lister_eleves(curseur):
    """Liste tous les élèves de la base de données."""
    query = "SELECT * FROM eleves"
    curseur.execute(query)
    return curseur.fetchall()

def recuperer_eleve(curseur, matricule):
    """Récupère un élève par son matricule."""
    query = "SELECT * FROM eleves WHERE matricule = %s"
    curseur.execute(query, (matricule,))
    return curseur.fetchone()