from abc import ABC, abstractmethod

class IEducation(ABC):
    """
        Interface pour les méthodes liées à l'éducation.
    """

    # Enseigne une matière
    @abstractmethod
    def enseigner(self, matiere):
        pass

    # Prépare le contenu d'un cours
    @abstractmethod
    def preparerCours(self, cours):
        pass
    
    # Assiste à une réunion sur un sujet donné
    @abstractmethod
    def assisterReunion(self, sujet):
        pass
