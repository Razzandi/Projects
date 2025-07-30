from Default_Character import Character

class Mage(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Mage", _level)
        self._mana = 100
        self._spellbook = []
        self._familiar = None
        self._elemental_affinity = "Fire"
        self._rituals = []

    # Unique member variables
    @property
    def spellbook(self):
        return self._spellbook
    @spellbook.setter
    def spellbook(self, value):
        self._spellbook = value

    @property
    def familiar(self):
        return self._familiar
    @familiar.setter
    def familiar(self, value):
        self._familiar = value

    @property
    def elemental_affinity(self):
        return self._elemental_affinity
    @elemental_affinity.setter
    def elemental_affinity(self, value):
        self._elemental_affinity = value

    @property
    def rituals(self):
        return self._rituals

    @rituals.setter
    def rituals(self, value):
        self._rituals = value

    # Unique functions
    def cast_spell(self, spell):
        if spell in self._spellbook and self._mana >= 10:
            self._mana -= 10
            print(f"{self._name} casts {spell}!")
        else:
            print(f"{self._name} cannot cast {spell}.")

    def summon_familiar(self, familiar_name):
        self._familiar = familiar_name
        print(f"{self._name} has summoned {familiar_name} as their familiar.")
