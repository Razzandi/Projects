import Default_Character

class Priest(Default_Character.Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Priest", _level)
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
        self._faith += duration * 2
        print(f"{self._name} prays for {duration} minutes and increases faith to {self._faith}.")
    
    def heal(self, target):
        if self._faith >= 10:
            self._faith -= 10
            print(f"{self._name} heals {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to heal.")

    def bless(self, target):
        if self._faith >= 5:
            self._faith -= 5
            print(f"{self._name} blesses {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to bless.")
    
    def perform_ritual(self, ritual_name):
        if ritual_name in self._rituals:
            print(f"{self._name} performs the ritual: {ritual_name}.")
        else:
            print(f"{self._name} does not know the ritual: {ritual_name}.")
    
    def read_sacred_text(self):
        print(f"{self._name} reads from the {self._sacred_text}, gaining wisdom and insight.")
    
    def cast_divine_spell(self, spell_name, target):
        if spell_name in self._divine_spells:
            if self._faith >= 15:
                self._faith -= 15
                print(f"{self._name} casts {spell_name} on {target}, faith is now {self._faith}.")
            else:
                print(f"{self._name} does not have enough faith to cast {spell_name}.")
        else:
            print(f"{self._name} does not know the divine spell: {spell_name}.")
    
    def convert(self, target):
        print(f"{self._name} attempts to convert {target} to their faith.")
    
    def meditate(self, duration):
        self._faith += duration
        print(f"{self._name} meditates for {duration} minutes and increases faith to {self._faith}.")
    
    def perform_exorcism(self, target):
        if self._faith >= 25:
            self._faith -= 25
            print(f"{self._name} performs an exorcism on {target}, faith is now {self._faith}.")
        else:
            print(f"{self._name} does not have enough faith to perform an exorcism.")
    
    def lead_service(self):
        print(f"{self._name} leads a religious service, inspiring the congregation.")
    
    def offer_guidance(self, target):
        print(f"{self._name} offers spiritual guidance to {target}.")