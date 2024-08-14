from abc import ABC, abstractmethod
# from .eleve import Eleve

class ICRUDEleve(ABC):
    """
        Interface pour les opérations CRUD sur les élèves
    """

    # Ajoute un élève
    @abstractmethod
    def ajouter(self,  eleve): 
        pass
    
    # Modifie un élève
    @abstractmethod
    def modifier(self, eleve):
        pass

    # Supprime un élève par son identifiant
    @abstractmethod
    def supprimer(self, identifiant):
        pass
    
    # Obtient les élèves
    @abstractmethod
    def obtenirEleve(self) -> list:
        pass
    
    # Obtient un élève par son identifiant
    @abstractmethod
    def obtenir(self, identifiant) :
        pass