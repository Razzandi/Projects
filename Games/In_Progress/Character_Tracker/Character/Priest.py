from default_character import Character
from character_class import CharacterClass

class Priest(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.PRIEST, level)
        self._faith = 100
        self._holy_symbol = "Ankh"
        self._divine_spell_list = []
        self._cleric_domain = "Life"
        self._sacred_text = "Book of Light"
        self._healing_ability_list = ["Heal", "Bless"]
        self._ritual_list = ["Sanctify", "Consecrate"]

    # Member variable properties
    
    def get_faith(self):
        """
        Gets the priest's current faith.
        
        Args: 
            None
            
        Returns:
            int: The current faith of the priest."""
        return self._faith
    
    def set_faith(self, value):
        """
        Sets the priest's faith.

        Args:
            value (int): New faith value.
        
        Returns:
            int: Updated faith value."""
        self._faith = value

    def get_holy_symbol(self):
        """
        Gets the priest's holy symbol.
        
        Args: 
            None
            
        Returns:
            str: The priest's holy symbol."""
        return self._holy_symbol
    
    def set_holy_symbol(self, value):
        """
        Sets the priest's holy symbol.

        Args:
            value (str): New holy symbol.
        
        Returns:
            str: Updated holy symbol."""
        self._holy_symbol = value

    def get_divine_spell_list(self):
        """
        Gets the priest's divine spell list.
        
        Args:
            None
        
        Returns:
            list: The list of divine spells known by the priest."""
        return self._divine_spell_list
    
    def set_divine_spell_list(self, value):
        """
        Sets the priest's divine spell list.
        
        Args:
            value (list): New list of divine spells.
            
        Returns:
            list: Updated list of divine spells."""
        self._divine_spell_list = value

    def get_cleric_domain(self):
        """
        Gets the priest's cleric domain.
        
        Args:
            None
            
        Returns:
            str: The priest's cleric domain."""
        return self._cleric_domain
    
    def set_cleric_domain(self, value):
        """
        Sets the priest's cleric domain.
        
        Args:
            value (str): New cleric domain.
            
        Returns:
            str: Updated cleric domain."""
        self._cleric_domain = value

    def get_sacred_text(self):
        """
        Gets the priest's sacred text.
        
        Args:
            None
            
        Returns:
            str: The priest's sacred text."""
        return self._sacred_text
    
    def set_sacred_text(self, value):
        """
        Sets the priest's sacred text.
        
        Args:
            value (str): New sacred text.
            
        Returns:
            str: Updated sacred text."""
        self._sacred_text = value

    def get_healing_ability_list(self):
        """
        Gets the priest's healing ability list.
        
        Args:
            None
            
        Returns:
            list: The list of healing abilities known by the priest."""
        return self._healing_ability_list
    
    def set_healing_ability_list(self, value):
        """
        Sets the priest's healing ability list.
        
        Args:
            value (list): New list of healing abilities.
            
        Returns:
            list: Updated list of healing abilities."""
        self._healing_ability_list = value

    def get_ritual_list(self):
        """
        Gets the priest's ritual list.
        
        Args:
            None
            
        Returns:
            list: The list of rituals known by the priest."""
        return self._ritual_list
    
    def set_ritual_list(self, value):
        """
        Sets the priest's ritual list.
        
        Args:
            value (list): New list of rituals.
            
        Returns:
            list: Updated list of rituals."""
        self._ritual_list = value

    # Member functions (actions/verbs)
    def pray(self, duration):
        """
        Prays for a specified duration to increase faith.

        Args:
            duration (int): The number of minutes spent praying.

        Returns:
            None
        """
        self._faith += duration * 2
        print(f"{self._name} prays for {duration} minutes and increases faith to {self._faith}.")

    def heal_target(self, target):
        """
        Heals a target if enough faith is available.

        Args:
            target (str): The target to heal.

        Returns:
            None
        """
        if self._faith >= 10:
            self._faith -= 10
            print(f"{self._name} heals {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to heal.")

    def bless_target(self, target):
        """
        Blesses a target if enough faith is available.

        Args:
            target (str): The target to bless.

        Returns:
            None
        """
        if self._faith >= 5:
            self._faith -= 5
            print(f"{self._name} blesses {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to bless.")

    def perform_ritual(self, ritual_name):
        """
        Performs a ritual if known.

        Args:
            ritual_name (str): The name of the ritual to perform.

        Returns:
            None
        """
        if ritual_name in self._ritual_list:
            print(f"{self._name} performs the ritual: {ritual_name}.")
        else:
            print(f"{self._name} does not know the ritual: {ritual_name}.")

    def read_sacred_text(self):
        """
        Reads from the sacred text to gain wisdom and insight.

        Args:
            None

        Returns:
            None
        """
        print(f"{self._name} reads from the {self._sacred_text}, gaining wisdom and insight.")

    def cast_divine_spell(self, spell_name, target):
        """
        Casts a divine spell on a target if known and enough faith is available.

        Args:
            spell_name (str): The name of the divine spell.
            target (str): The target of the spell.

        Returns:
            None
        """
        if spell_name in self._divine_spell_list:
            if self._faith >= 15:
                self._faith -= 15
                print(f"{self._name} casts {spell_name} on {target}, faith is now {self._faith}.")
            else:
                print(f"{self._name} does not have enough faith to cast {spell_name}.")
        else:
            print(f"{self._name} does not know the divine spell: {spell_name}.")

    def convert_target(self, target):
        """
        Attempts to convert a target to the priest's faith.

        Args:
            target (str): The target to convert.

        Returns:
            None
        """
        print(f"{self._name} attempts to convert {target} to their faith.")

    def meditate(self, duration):
        """
        Meditates for a specified duration to increase faith.

        Args:
            duration (int): The number of minutes spent meditating.

        Returns:
            None
        """
        self._faith += duration
        print(f"{self._name} meditates for {duration} minutes and increases faith to {self._faith}.")

    def perform_exorcism(self, target):
        """
        Performs an exorcism on a target if enough faith is available.

        Args:
            target (str): The target of the exorcism.

        Returns:
            None
        """
        if self._faith >= 25:
            self._faith -= 25
            print(f"{self._name} performs an exorcism on {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to perform an exorcism.")

    def lead_service(self):
        """
        Leads a religious service to inspire the congregation.

        Args:
            None

        Returns:
            None
        """
        print(f"{self._name} leads a religious service, inspiring the congregation.")

    def offer_guidance(self, target):
        """
        Offers spiritual guidance to a target.

        Args:
            target (str): The target to offer guidance to.

        Returns:
            None
        """
        print(f"{self._name} offers spiritual guidance to {target}, helping them find clarity and purpose.")