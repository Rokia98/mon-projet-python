import mysql.connector
from mysql.connector import Error
from models.personne import Personne
from Eleve.ICrudEleve import ICRUDEleve

class Eleve(Personne, ICRUDEleve):
    """
    Classe représentant un élève, héritant de la classe Personne et de la classe ICRUDEleve.
    """

    def __init__(self, date_naissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(date_naissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule

    # Méthode pour obtenir la connexion à la base de données
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='etab_db'
            )
            return connection
        except Error as e:
            print(f"Erreur de connexion à la base de données : {e}")
            return None

    # Modifier un élève
    # @staticmethod
    @staticmethod
    def modifier(eleve):
        connection = Eleve.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Modifier d'abord les informations dans la table personnes
                query_personne = """
                    UPDATE personnes
                    SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s
                    WHERE id = (SELECT id_personne FROM eleves WHERE matricule = %s)
                """
                values_personne = (
                    eleve.date_naissance,
                    eleve.ville,
                    eleve.prenom,
                    eleve.nom,
                    eleve.telephone,
                    eleve.matricule
                )
                cursor.execute(query_personne, values_personne)

            # Ensuite, modifier les informations dans la table eleves
                query_eleve = """
                    UPDATE eleves
                    SET classe = %s
                    WHERE matricule = %s
                """
                values_eleve = (
                    eleve.classe,
                    eleve.matricule
                )
                cursor.execute(query_eleve, values_eleve)
                connection.commit()

                print(f"Élève {eleve.prenom} {eleve.nom} modifié avec succès.")
            except Error as e:
                print(f"Erreur lors de la modification de l'élève : {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()

    # Ajouter un élève

    @staticmethod
    def ajouter(eleve):
        connection = Eleve.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Insérer d'abord les informations dans la table personnes
                query_personne = """
                    INSERT INTO personnes (date_naissance, ville, prenom, nom, telephone)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values_personne = (
                    eleve.date_naissance,
                    eleve.ville,
                    eleve.prenom,
                    eleve.nom,
                    eleve.telephone
                )
                cursor.execute(query_personne, values_personne)
                id_personne = cursor.lastrowid  # Récupérer l'ID de la personne insérée

                # Ensuite, insérer les informations dans la table eleves
                query_eleve = """
                    INSERT INTO eleves (id_personne, classe, matricule)
                    VALUES (%s, %s, %s)
                """
                values_eleve = (
                    id_personne,
                    eleve.classe,
                    eleve.matricule
               )
                cursor.execute(query_eleve, values_eleve)
                connection.commit()

                print(f"Élève {eleve.prenom} {eleve.nom} ajouté avec succès.")
            except Error as e:
                print(f"Erreur lors de l'ajout de l'élève : {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()

      # Supprimer un élève
    @staticmethod
    def supprimer(identifiant):
        connection = Eleve.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM eleves WHERE matricule = %s"
                cursor.execute(query, (identifiant,))
                connection.commit()
                print(f"Élève avec matricule {identifiant} supprimé avec succès.")
            except Error as e:
                print(f"Erreur lors de la suppression de l'élève : {e}")
            finally:
                cursor.close()
                connection.close()

    # Obtenir les élèves
    @staticmethod
    @staticmethod
    def obtenir_eleve():
        connection = Eleve.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL qui joint la table `eleves` avec la table `personnes`
                query = """
                    SELECT e.id, p.prenom, p.nom, p.date_naissance, p.ville, p.telephone, e.classe, e.matricule
                    FROM eleves e
                    JOIN personnes p ON e.id_personne = p.id
                """
                cursor.execute(query)
                result = cursor.fetchall()

                # Vérifier que le résultat contient bien 8 colonnes
                if result:
                    return [
                        f"Élève n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, classe: {row[6]}, matricule: {row[7]}, téléphone: {row[5]}"
                        for row in result
                    ]
                else:
                    return []

            except Error as e:
                print(f"Erreur lors de l'obtention des élèves : {e}")
                return []
            finally:
                cursor.close()
                connection.close()

    # Obtenir un élève par son matricule
    @staticmethod
    def obtenir(identifiant):
        connection = Eleve.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Requête SQL qui joint la table `eleves` avec la table `personnes`
                query = """
                    SELECT e.id, p.prenom, p.nom, p.date_naissance, p.ville, p.telephone, e.classe, e.matricule
                    FROM eleves e
                    JOIN personnes p ON e.id_personne = p.id
                    WHERE e.matricule = %s
                """
                cursor.execute(query, (identifiant,))
                row = cursor.fetchone()

                # Vérifier que le tuple a bien 8 colonnes
                if row and len(row) == 8:
                    return f"Élève n° {row[0]} : {row[1]} {row[2]}, née le {row[3]} à {row[4]}, classe: {row[6]}, matricule: {row[7]}, téléphone: {row[5]}"
                else:
                    print(f"Erreur : Le nombre de colonnes récupérées est insuffisant ou l'élève avec le matricule {identifiant} n'existe pas.")
                    return None

            except Error as e:
                print(f"Erreur lors de l'obtention de l'élève : {e}")
                return None
            finally:
                cursor.close()
                connection.close()

    # Propriétés
    @property
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, classe):
        self.__classe = classe

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, matricule):
        self.__matricule = matricule

