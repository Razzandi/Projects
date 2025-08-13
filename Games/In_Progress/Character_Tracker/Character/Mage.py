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
        """
        Gets the mage's spellbook.

        Returns:
            list: The list of spells known by the mage.
        """
        return self._spellbook

    @spellbook.setter
    def spellbook(self, value):
        """
        Sets the mage's spellbook.

        Parameters:
            value (list): The new list of spells for the mage.
        
        Returns:
            None
        """
        self._spellbook = value

    @property
    def familiar(self):
        """
        Gets the mage's familiar.

        Returns:
            str or None: The name of the mage's familiar, or None if not set.
        """
        return self._familiar

    @familiar.setter
    def familiar(self, value):
        """
        Sets the mage's familiar.

        Parameters:
            value (str): The name of the familiar.
        
        Returns:
            None
        """
        self._familiar = value

    @property
    def elemental_affinity(self):
        """
        Gets the mage's elemental affinity.

        Returns:
            str: The mage's elemental affinity.
        """
        return self._elemental_affinity

    @elemental_affinity.setter
    def elemental_affinity(self, value):
        """
        Sets the mage's elemental affinity.

        Parameters:
            value (str): The new elemental affinity.
        
        Returns:
            None
        """
        self._elemental_affinity = value

    @property
    def rituals(self):
        """
        Gets the mage's rituals.

        Returns:
            list: The list of rituals known by the mage.
        """
        return self._rituals

    @rituals.setter
    def rituals(self, value):
        """
        Sets the mage's rituals.

        Parameters:
            value (list): The new list of rituals for the mage.
        
        Returns:
            None
        """
        self._rituals = value

    # Unique functions
    def cast_spell(self, spell):
        """
        Casts a spell from the mage's spellbook if enough mana is available.

        Parameters:
            spell (str): The name of the spell to cast.

        Returns:
            None
        """
        if spell in self._spellbook and self._mana >= 10:
            self._mana -= 10
            print(f"{self._name} casts {spell}!")
        else:
            print(f"{self._name} cannot cast {spell}.")

    def summon_familiar(self, familiar_name):
        """
        Summons a familiar for the mage.

        Parameters:
            familiar_name (str): The name of the familiar to summon.

        Returns:
            None
        """
        self._familiar = familiar_name
        print(f"{self._name} has summoned {familiar_name} as their familiar.")