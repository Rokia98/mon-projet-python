from abc import ABC, abstractmethod

class ICRUDProfesseur(ABC):
    """
        Interface pour les opérations CRUD sur les professeurs.
    """

    # Ajouter un professeur 
    @abstractmethod
    def ajouter(self, professeur):
        pass
    
    # Modifier un professeur 
    @abstractmethod
    def modifier(self, professeur):
        pass
    
    # Supprimer un professeur  par son identifiant
    @abstractmethod
    def supprimer(self, identifiant):
        pass

    # Obtient un professeur 
    @abstractmethod
    def obtenir_professeurs(self):
        pass

    # Obtient un professeur par son identifiant
    @abstractmethod
    def obtenir(self, identifiant):
        pass
