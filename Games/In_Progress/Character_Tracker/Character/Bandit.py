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

    # Unique functions
    def steal(self, target):
        """
        Attempts to steal loot from a target.

        Parameters:
            target (str): The target to steal from.

        Returns:
            None
        """
        print(f"{self._name} attempts to steal from {target} using stealth skill {self._stealth}.")

    def bribe_guard(self, amount):
        """
        Bribes a guard with a specified amount of loot.

        Parameters:
            amount (int): The amount of loot to use for bribery.

        Returns:
            None
        """
        if len(self._loot) >= amount:
            print(f"{self._name} bribes a guard with {amount} loot items.")
            self._loot = self._loot[amount:]
        else:
            print(f"{self._name} does not have enough loot to bribe the guard.")

    def plan_escape(self, route):
        """
        Plans an escape using a specified route.

        Parameters:
            route (str): The escape route to use.

        Returns:
            None
        """
        if route in self._escape_routes:
            print(f"{self._name} plans an escape through the {route}.")
        else:
            print(f"{self._name} does not know the escape route: {route}.")

    def ransom_hostage(self, hostage, skill):
        """
        Attempts to ransom a hostage using a specified skill.

        Parameters:
            hostage (str): The name of the hostage.
            skill (str): The ransom skill to use.

        Returns:
            None
        """
        if skill in self._ransom_skills:
            print(f"{self._name} uses {skill} to ransom {hostage}.")
        else:
            print(f"{self._name} does not possess the ransom skill: {skill}.")

    def expand_gang(self, number):
        """
        Expands the gang by a specified number of members.

        Parameters:
            number (int): The number of new members to add.

        Returns:
            None
        """
        self._gang_size += number
        print(f"{self._name} expands the gang by {number} members. Total gang size: {self._gang_size}.")

    def relocate_hideout(self, new_location):
        """
        Relocates the bandit's hideout to a new location.

        Parameters:
            new_location (str): The new hideout location.

        Returns:
            None
        """
        self._hideout_location = new_location
        print(f"{self._name} relocates the hideout to {new_location}.")