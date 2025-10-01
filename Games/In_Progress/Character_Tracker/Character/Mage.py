from default_character import Character
from character_class import CharacterClass

class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.MAGE, level)
        self._mana = 100
        self._spellbook = []
        self._familiar = None
        self._elemental_affinity = "Fire"
        self._ritual_list = []

    # Member variable properties
    
    def get_mana(self):
        """
        Gets the mage's current mana.

        Args: 
            None

        Returns the current mana of the mage."""
        return self._mana

    def set_mana(self, value):
        """
        Sets the mage's mana.
        
        Args:
            value (int): New mana value.
            
        Returns:
            int: Updated mana value.
        """
        self._mana = value

    def get_spellbook(self):
        """
        Gets the mage's spellbook.

        Args: 
            None

        Returns:
            list: The list of spells known by the mage.
        """
        return self._spellbook
    
    def set_spellbook(self, value):
        """
        Sets the mage's spellbook.

        Args: 
            value (list): The new list of spells for the mage.

        Returns:
            None
        """
        self._spellbook = value

    def get_familiar(self):
        """
        Gets the mage's familiar.

        Args: 
            None

        Returns:
            str or None: The name of the mage's familiar, or None if not set.
        """
        return self._familiar
    
    def set_familiar(self, value):
        """
        Sets the mage's familiar.

        Args: 
            value (str): The name of the familiar.

        Returns:
            None
        """
        self._familiar = value

    def get_elemental_affinity(self):
        """
        Gets the mage's elemental affinity.

        Args:
            None

        Returns:
            str: The mage's elemental affinity.
        """
        return self._elemental_affinity
    
    def set_elemental_affinity(self, value):
        """
        Sets the mage's elemental affinity.

        Args:
            value (str): The new elemental affinity.

        Returns:
            None
        """
        self._elemental_affinity = value

    def get_ritual_list(self):
        """
        Gets the mage's rituals.

        Args:
            None

        Returns:
            list: The list of rituals known by the mage.
        """
        return self._ritual_list
    
    def set_ritual_list(self, value):
        """
        Sets the mage's rituals.

        Parameters:
            value (list): The new list of rituals for the mage.

        Returns:
            None
        """
        self._ritual_list = value

    # Member functions (actions/verbs)
    def cast_spell(self, spell):
        """
        Casts a spell from the mage's spellbook if enough mana is available.

        Args:
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

        Args:
            familiar_name (str): The name of the familiar to summon.

        Returns:
            None
        """
        self._familiar = familiar_name
        print(f"{self._name} has summoned {familiar_name} as their familiar.")