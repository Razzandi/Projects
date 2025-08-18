from default_character import Character
from Joe_Github.Projects.Games.In_Progress.Character_Tracker.Character.character_class import CharacterClass

class Paladin(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.PALADIN, level)
        self._faith = 100
        self._holy_symbol = "Cross"
        self._divine_spell_list = []
        self._mount = "Warhorse"
        self._armor_type = "Plate"
        self._sacred_oath = "Oath of Devotion"
        self._healing_ability_list = ["Lay on Hands", "Cure Wounds"]

    # Member variable properties
    @property
    def faith(self):
        return self._faith
    @faith.setter
    def faith(self, value):
        self._faith = value

    @property
    def holy_symbol(self):
        return self._holy_symbol
    @holy_symbol.setter
    def holy_symbol(self, value):
        self._holy_symbol = value

    @property
    def divine_spell_list(self):
        return self._divine_spell_list
    @divine_spell_list.setter
    def divine_spell_list(self, value):
        self._divine_spell_list = value

    @property
    def mount(self):
        return self._mount
    @mount.setter
    def mount(self, value):
        self._mount = value

    @property
    def armor_type(self):
        return self._armor_type
    @armor_type.setter
    def armor_type(self, value):
        self._armor_type = value

    @property
    def sacred_oath(self):
        return self._sacred_oath
    @sacred_oath.setter
    def sacred_oath(self, value):
        self._sacred_oath = value

    @property
    def healing_ability_list(self):
        return self._healing_ability_list
    @healing_ability_list.setter
    def healing_ability_list(self, value):
        self._healing_ability_list = value

    # Member functions (actions/verbs)
    def smite(self, target):
        """
        Uses faith to smite a target with holy power.
        """
        if self._faith >= 20:
            self._faith -= 20
            print(f"{self._name} smites {target} with holy power!")
        else:
            print(f"{self._name} does not have enough faith to smite.")

    def heal(self, target):
        """
        Heals a target using Lay on Hands if available.
        """
        if "Lay on Hands" in self._healing_ability_list:
            print(f"{self._name} heals {target} using Lay on Hands.")
        else:
            print(f"{self._name} does not have healing abilities.")

    def mount_horse(self):
        """
        Mounts the paladin's horse.
        """
        print(f"{self._name} mounts their {self._mount}.")

    def dismount_horse(self):
        """
        Dismounts from the paladin's horse.
        """
        print(f"{self._name} dismounts from their {self._mount}.")