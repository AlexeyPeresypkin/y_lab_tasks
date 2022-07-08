from places import Kostroma, Tokyo
from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_antagonist(self, place):
        ...


class AntagonistFinder(Place):

    def get_antagonist(self, place):
        if isinstance(place, Kostroma):
            place.get_orcs()
        elif isinstance(place, Tokyo):
            place.get_godzilla()
