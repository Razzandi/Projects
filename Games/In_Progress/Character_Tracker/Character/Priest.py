from Default_Character import Character
from CharacterClass import CharacterClass

class Priest(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, CharacterClass.PRIEST, _level)

        self._faith = 100
        self._holy_symbol = "Ankh"
        self._divine_spells = []
        self._cleric_domain = "Life"
        self._sacred_text = "Book of Light"
        self._healing_abilities = ["Heal", "Bless"]
        self._rituals = ["Sanctify", "Consecrate"]
        
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
    def cleric_domain(self):
        return self._cleric_domain
    @cleric_domain.setter
    def cleric_domain(self, value):
        self._cleric_domain = value
    @property
    def sacred_text(self):
        return self._sacred_text
    @sacred_text.setter
    def sacred_text(self, value):
        self._sacred_text = value
    @property
    def healing_abilities(self):
        return self._healing_abilities
    @healing_abilities.setter
    def healing_abilities(self, value):
        self._healing_abilities = value
    @property
    def rituals(self):
        return self._rituals
    @rituals.setter
    def rituals(self, value):
        self._rituals = value

    # Unique functions
    def pray(self, duration):
        """
        Prays for a specified duration to increase faith.

        Parameters:
            duration (int): The number of minutes spent praying.

        Returns:
            None
        """
        self._faith += duration * 2
        print(f"{self._name} prays for {duration} minutes and increases faith to {self._faith}.")

    def heal(self, target):
        """
        Heals a target if enough faith is available.

        Parameters:
            target (str): The target to heal.

        Returns:
            None
        """
        if self._faith >= 10:
            self._faith -= 10
            print(f"{self._name} heals {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to heal.")

    def bless(self, target):
        """
        Blesses a target if enough faith is available.

        Parameters:
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

        Parameters:
            ritual_name (str): The name of the ritual to perform.

        Returns:
            None
        """
        if ritual_name in self._rituals:
            print(f"{self._name} performs the ritual: {ritual_name}.")
        else:
            print(f"{self._name} does not know the ritual: {ritual_name}.")

    def read_sacred_text(self):
        """
        Reads from the sacred text to gain wisdom and insight.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} reads from the {self._sacred_text}, gaining wisdom and insight.")

    def cast_divine_spell(self, spell_name, target):
        """
        Casts a divine spell on a target if known and enough faith is available.

        Parameters:
            spell_name (str): The name of the divine spell.
            target (str): The target of the spell.

        Returns:
            None
        """
        if spell_name in self._divine_spells:
            if self._faith >= 15:
                self._faith -= 15
                print(f"{self._name} casts {spell_name} on {target}, faith is now {self._faith}.")
            else:
                print(f"{self._name} does not have enough faith to cast {spell_name}.")
        else:
            print(f"{self._name} does not know the divine spell: {spell_name}.")

    def convert(self, target):
        """
        Attempts to convert a target to the priest's faith.

        Parameters:
            target (str): The target to convert.

        Returns:
            None
        """
        print(f"{self._name} attempts to convert {target} to their faith.")

    def meditate(self, duration):
        """
        Meditates for a specified duration to increase faith.

        Parameters:
            duration (int): The number of minutes spent meditating.

        Returns:
            None
        """
        self._faith += duration
        print(f"{self._name} meditates for {duration} minutes and increases faith to {self._faith}.")

    def perform_exorcism(self, target):
        """
        Performs an exorcism on a target if enough faith is available.

        Parameters:
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

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} leads a religious service, inspiring the congregation.")

    def offer_guidance(self, target):
        """
        Offers spiritual guidance to a target.

        Parameters:
            target (str): The target to offer guidance to.

        Returns:
            None
        """
        print(f"{self._name} offers spiritual guidance to {target}, helping them find clarity and purpose.")