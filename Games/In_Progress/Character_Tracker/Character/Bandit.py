from default_character import Character
from Joe_Github.Projects.Games.In_Progress.Character_Tracker.Character.character_class import CharacterClass

class Bandit(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.BANDIT, level)

        self._stealth_level = 80
        self._notoriety_level = 50
        self._weapon_preference = "Dagger"
        self._loot_list = []
        self._hideout_location = "Abandoned Warehouse"
        self._gang_member_count = 5
        self._escape_route_list = ["Sewer", "Forest Path"]
        self._ransom_skill_list = ["Negotiation", "Intimidation"]

    # Member variable properties
    @property
    def stealth_level(self):
        return self._stealth_level
    @stealth_level.setter
    def stealth_level(self, value):
        self._stealth_level = value

    @property
    def notoriety_level(self):
        return self._notoriety_level
    @notoriety_level.setter
    def notoriety_level(self, value):
        self._notoriety_level = value

    @property
    def weapon_preference(self):
        return self._weapon_preference
    @weapon_preference.setter
    def weapon_preference(self, value):
        self._weapon_preference = value

    @property
    def loot_list(self):
        return self._loot_list
    @loot_list.setter
    def loot_list(self, value):
        self._loot_list = value

    @property
    def hideout_location(self):
        return self._hideout_location
    @hideout_location.setter
    def hideout_location(self, value):
        self._hideout_location = value

    @property
    def gang_member_count(self):
        return self._gang_member_count
    @gang_member_count.setter
    def gang_member_count(self, value):
        self._gang_member_count = value

    @property
    def escape_route_list(self):
        return self._escape_route_list
    @escape_route_list.setter
    def escape_route_list(self, value):
        self._escape_route_list = value

    @property
    def ransom_skill_list(self):
        return self._ransom_skill_list
    @ransom_skill_list.setter
    def ransom_skill_list(self, value):
        self._ransom_skill_list = value

    # Member functions (actions/verbs)
    def steal_from(self, target):
        """
        Attempts to steal loot from a target.

        Parameters:
            target (str): The target to steal from.

        Returns:
            None
        """
        print(f"{self._name} attempts to steal from {target} using stealth level {self._stealth_level}.")

    def bribe_guard(self, amount):
        """
        Bribes a guard with a specified amount of loot.

        Parameters:
            amount (int): The amount of loot to use for bribery.

        Returns:
            None
        """
        if len(self._loot_list) >= amount:
            print(f"{self._name} bribes a guard with {amount} loot items.")
            self._loot_list = self._loot_list[amount:]
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
        if route in self._escape_route_list:
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
        if skill in self._ransom_skill_list:
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
        self._gang_member_count += number
        print(f"{self._name} expands the gang by {number} members. Total gang size: {self._gang_member_count}.")

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