import mysql.connector  # Ou tout autre module de connexion à votre base de données

def ajouter_utilisateur(curseur, pseudo, motDePasse):
    """Ajoute un utilisateur à la base de données."""
    query = "INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, NOW())"
    curseur.execute(query, (pseudo, motDePasse))

def modifier_mot_de_passe(curseur, pseudo, nouveauMotDePasse):
    """Modifie le mot de passe d'un utilisateur dans la base de données."""
    query = "UPDATE utilisateurs SET mot_de_passe = %s WHERE pseudo = %s"
    curseur.execute(query, (nouveauMotDePasse, pseudo))

def supprimer_utilisateur(curseur, pseudo):
    """Supprime un utilisateur de la base de données."""
    query = "DELETE FROM utilisateurs WHERE pseudo = %s"
    curseur.execute(query, (pseudo,))

def lister_utilisateurs(curseur):
    """Liste tous les utilisateurs de la base de données."""
    query = "SELECT id, pseudo, date_creation FROM utilisateurs"
    curseur.execute(query)
    return curseur.fetchall()

def recuperer_utilisateur(curseur, pseudo):
    """Récupère un utilisateur par son pseudo."""
    query = "SELECT id, pseudo, date_creation FROM utilisateurs WHERE pseudo = %s"
    curseur.execute(query, (pseudo,))
    return curseur.fetchone()

