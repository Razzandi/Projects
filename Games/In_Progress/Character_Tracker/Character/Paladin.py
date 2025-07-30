from Default_Character import Character

class Paladin(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Paladin", _level)
        self._faith = 100
        self._holy_symbol = "Cross"
        self._divine_spells = []
        self._mount = "Warhorse"
        self._armor_type = "Plate"
        self._sacred_oath = "Oath of Devotion"
        self._healing_abilities = ["Lay on Hands", "Cure Wounds"]
        
    # Unique member variables
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
    def divine_spells(self):
        return self._divine_spells
    @divine_spells.setter
    def divine_spells(self, value):
        self._divine_spells = value
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
    def healing_abilities(self):
        return self._healing_abilities
    @healing_abilities.setter
    def healing_abilities(self, value):
        self._healing_abilities = value

    # Unique functions
    def smite(self, target):
        if self._faith >= 20:
            self._faith -= 20
            print(f"{self._name} smites {target} with holy power!")
        else:
            print(f"{self._name} does not have enough faith to smite.")
    
    def heal(self, target):
        if "Lay on Hands" in self._healing_abilities:
            print(f"{self._name} heals {target} using Lay on Hands.")
        else:
            print(f"{self._name} does not have healing abilities.")
    
    def mount_horse(self):
        print(f"{self._name} mounts their {self._mount}.")  

    def dismount_horse(self):
        print(f"{self._name} dismounts from their {self._mount}.")