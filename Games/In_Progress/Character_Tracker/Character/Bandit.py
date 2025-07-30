from Default_Character import Character

class Bandit(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Bandit", _level)
        self._stealth = 80
        self._notoriety = 50
        self._preferred_weapon = "Dagger"
        self._loot = []
        self._hideout_location = "Abandoned Warehouse"
        self._gang_size = 5
        self._escape_routes = ["Sewer", "Forest Path"]
        self._ransom_skills = ["Negotiation", "Intimidation"]
        

    # Unique member variables
    @property
    def stealth(self):
        return self._stealth
    @stealth.setter
    def stealth(self, value):
        self._stealth = value
    @property
    def notoriety(self):
        return self._notoriety
    @notoriety.setter
    def notoriety(self, value):
        self._notoriety = value
    @property
    def preferred_weapon(self):
        return self._preferred_weapon
    @preferred_weapon.setter
    def preferred_weapon(self, value):
        self._preferred_weapon = value
    @property
    def loot(self):
        return self._loot
    @loot.setter
    def loot(self, value):
        self._loot = value
    @property
    def hideout_location(self):
        return self._hideout_location
    @hideout_location.setter
    def hideout_location(self, value):
        self._hideout_location = value
    @property
    def gang_size(self):
        return self._gang_size
    @gang_size.setter
    def gang_size(self, value):
        self._gang_size = value
    @property
    def escape_routes(self):
        return self._escape_routes
    @escape_routes.setter
    def escape_routes(self, value):
        self._escape_routes = value
    @property
    def ransom_skills(self):
        return self._ransom_skills
    @ransom_skills.setter
    def ransom_skills(self, value):
        self._ransom_skills = value