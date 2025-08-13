from default_character import Character
from Joe_Github.Projects.Games.In_Progress.Character_Tracker.Character.character_class import CharacterClass

class Paladin(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, CharacterClass.PALADIN, _level)
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
        """
        Gets the paladin's faith value.

        Returns:
            int: The current faith value.
        """
        return self._faith

    @faith.setter
    def faith(self, value):
        """
        Sets the paladin's faith value.

        Parameters:
            value (int): The new faith value.

        Returns:
            None
        """
        self._faith = value

    @property
    def holy_symbol(self):
        """
        Gets the paladin's holy symbol.

        Returns:
            str: The holy symbol.
        """
        return self._holy_symbol

    @holy_symbol.setter
    def holy_symbol(self, value):
        """
        Sets the paladin's holy symbol.

        Parameters:
            value (str): The new holy symbol.

        Returns:
            None
        """
        self._holy_symbol = value

    @property
    def divine_spells(self):
        """
        Gets the paladin's list of divine spells.

        Returns:
            list: The list of divine spells.
        """
        return self._divine_spells

    @divine_spells.setter
    def divine_spells(self, value):
        """
        Sets the paladin's list of divine spells.

        Parameters:
            value (list): The new list of divine spells.

        Returns:
            None
        """
        self._divine_spells = value

    @property
    def mount(self):
        """
        Gets the paladin's mount.

        Returns:
            str: The name of the mount.
        """
        return self._mount

    @mount.setter
    def mount(self, value):
        """
        Sets the paladin's mount.

        Parameters:
            value (str): The new mount name.

        Returns:
            None
        """
        self._mount = value

    @property
    def armor_type(self):
        """
        Gets the paladin's armor type.

        Returns:
            str: The armor type.
        """
        return self._armor_type

    @armor_type.setter
    def armor_type(self, value):
        """
        Sets the paladin's armor type.

        Parameters:
            value (str): The new armor type.

        Returns:
            None
        """
        self._armor_type = value

    @property
    def sacred_oath(self):
        """
        Gets the paladin's sacred oath.

        Returns:
            str: The sacred oath.
        """
        return self._sacred_oath

    @sacred_oath.setter
    def sacred_oath(self, value):
        """
        Sets the paladin's sacred oath.

        Parameters:
            value (str): The new sacred oath.

        Returns:
            None
        """
        self._sacred_oath = value

    @property
    def healing_abilities(self):
        """
        Gets the paladin's healing abilities.

        Returns:
            list: The list of healing abilities.
        """
        return self._healing_abilities

    @healing_abilities.setter
    def healing_abilities(self, value):
        """
        Sets the paladin's healing abilities.

        Parameters:
            value (list): The new list of healing abilities.

        Returns:
            None
        """
        self._healing_abilities = value

    # Unique functions
    def smite(self, target):
        """
        Uses faith to smite a target with holy power.

        Parameters:
            target (str): The target to smite.

        Returns:
            None
        """
        if self._faith >= 20:
            self._faith -= 20
            print(f"{self._name} smites {target} with holy power!")
        else:
            print(f"{self._name} does not have enough faith to smite.")

    def heal(self, target):
        """
        Heals a target using Lay on Hands if available.

        Parameters:
            target (str): The target to heal.

        Returns:
            None
        """
        if "Lay on Hands" in self._healing_abilities:
            print(f"{self._name} heals {target} using Lay on Hands.")
        else:
            print(f"{self._name} does not have healing abilities.")

    def mount_horse(self):
        """
        Mounts the paladin's horse.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} mounts their {self._mount}.")

    def dismount_horse(self):
        """
        Dismounts from the paladin's horse.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} dismounts from their {self._mount}.")