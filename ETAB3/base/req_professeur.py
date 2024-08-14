import mysql.connector  # Assurez-vous que ce module est installé

def ajouter_professeur(curseur, date_naissance, ville, prenom, nom, telephone, matiere_enseignee, vacant, prochain_cours, sujet_reunion):
    """Ajoute un professeur à la base de données."""
    query = ("INSERT INTO professeurs (date_naissance, ville, prenom, nom, telephone, matiere_enseignee, vacant, prochain_cours, sujet_reunion) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    curseur.execute(query, (date_naissance, ville, prenom, nom, telephone, matiere_enseignee, vacant, prochain_cours, sujet_reunion))

def modifier_professeur(curseur, id_professeur, nouveau_telephone, nouvelle_matiere, vacant, prochain_cours, sujet_reunion):
    """Modifie les informations d'un professeur dans la base de données."""
    query = ("UPDATE professeurs SET telephone = %s, matiere_enseignee = %s, vacant = %s, prochain_cours = %s, sujet_reunion = %s "
             "WHERE id = %s")
    curseur.execute(query, (nouveau_telephone, nouvelle_matiere, vacant, prochain_cours, sujet_reunion, id_professeur))

def supprimer_professeur(curseur, id_professeur):
    """Supprime un professeur de la base de données."""
    query = "DELETE FROM professeurs WHERE id = %s"
    curseur.execute(query, (id_professeur,))

def lister_professeurs(curseur):
    """Liste tous les professeurs de la base de données."""
    query = "SELECT * FROM professeurs"
    curseur.execute(query)
    return curseur.fetchall()

def recuperer_professeur(curseur, id_professeur):
    """Récupère un professeur par son identifiant."""
    query = "SELECT * FROM professeurs WHERE id = %s"
    curseur.execute(query, (id_professeur,))
    return curseur.fetchone()