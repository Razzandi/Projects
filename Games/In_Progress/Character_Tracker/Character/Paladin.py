from default_character import Character
from character_class import CharacterClass

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
    def get_faith(self):
        """
        Gets the paladin's current faith.
        
        Args: 
            None
        
        Returns the current faith of the paladin."""
        return self._faith
    
    def set_faith(self, value):
        """
        Sets the paladin's faith.
        
        Args:
            value (int): New faith value.
        
        Returns:
            int: Updated faith value."""
        self._faith = value

    def get_holy_symbol(self):
        """
        Gets the paladin's holy symbol.
        
        Args: 
            None
            
        Returns:
            str: The paladin's holy symbol."""
        return self._holy_symbol
    
    def set_holy_symbol(self, value):
        """
        Sets the paladin's holy symbol.
        
        Args:
            value (str): New holy symbol.
            
        Returns:
            str: Updated holy symbol."""
        self._holy_symbol = value

    def get_divine_spell_list(self):
        """
        Gets the paladin's divine spell list.
        
        Args:
            None
        
        Returns:
            list: The list of divine spells known by the paladin."""
        return self._divine_spell_list
    
    def set_divine_spell_list(self, value):
        """
        Sets the paladin's divine spell list.
        
        Args:
            value (list): New list of divine spells.
        
        Returns:
            list: Updated list of divine spells."""
        self._divine_spell_list = value

    def get_mount(self):
        """
        Gets the paladin's mount.
        
        Args: 
            None
        
        Returns:
            str: The type of mount the paladin rides."""
        return self._mount
    
    def set_mount(self, value):
        """
        Sets the paladin's mount.
        
        Args:
            value (str): New mount type.
        
        Returns:
            str: Updated mount type."""
        self._mount = value

    def get_armor_type(self):
        """
        Gets the paladin's armor type.
        
        Args: 
            None
        
        Returns:
            str: The type of armor the paladin wears."""
        return self._armor_type
    
    def set_armor_type(self, value):
        """
        Sets the paladin's armor type.
        
        Args:
            value (str): New armor type.
        
        Returns:
            str: Updated armor type."""
        self._armor_type = value

    def get_sacred_oath(self):
        """
        Gets the paladin's sacred oath.
        
        Args: 
            None
        
        Returns:
            str: The paladin's sacred oath."""
        return self._sacred_oath
    
    def set_sacred_oath(self, value):
        """
        Sets the paladin's sacred oath.
        
        Args:
            value (str): New sacred oath.
            
        Returns:
            str: Updated sacred oath."""
        self._sacred_oath = value

    def get_healing_ability_list(self):
        """
        Gets the paladin's healing ability list.
        
        Args: 
            None
            
        Returns:
            list: The list of healing abilities known by the paladin."""
        return self._healing_ability_list
    
    def healing_ability_list(self, value):
        """
        Sets the paladin's healing ability list.
        
        Args:
            value (list): New list of healing abilities.
        
        Returns:
            list: Updated list of healing abilities."""
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
        print(f"{self._name} dismounts from their {self._mount}.")"""