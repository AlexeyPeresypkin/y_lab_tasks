from antagonistfinder import AntagonistFinder
from hw_3.not_solid_code.mixins import UltimateAttackMixin, GunAttackMixin


class TV:

    def create_news(self: 'SuperHero', place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')

    def create_news_for_planets(self: 'SuperHero', place):
        coordinate_list = getattr(place, 'coordinates', ['unknown'])
        if coordinate_list:
            for coordinate in coordinate_list:
                print(f'Planet with coordinates {coordinate} was saved by {self.name}')


class SuperHero(TV, GunAttackMixin):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        print(f'{self.name} does not have an ultimate')


class Superman(UltimateAttackMixin, SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        super().attack()
        return 'Kick'

    def ultimate(self):
        self.incinerate_with_lasers()
