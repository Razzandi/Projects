from typing import Any
from default_character import Character
from character_class import CharacterClass

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
    def get_stealth_level(self):
        """
        Returns the current stealth level of the bandit.
        
        Args: 
            None
        
        Returns:
            int: Current stealth level value.
        """
        return self._stealth_level
    
    def set_stealth_level(self, value):
        """
        Sets the stealth level of the bandit.
        
        Args:
            value (int): New stealth level value.
            
        Returns:
            int: Updated stealth level value.
        """
        self._stealth_level = value
        return value
    
    def get_notoriety_level(self):
        """
        Returns the current notoriety level of the bandit.
        
        Args: 
            None
        
        Returns:
            int: Current notoriety level value.
        """
        return self._notoriety_level
    
    def set_notoriety_level(self, value):
        """
        Sets the notoriety level of the bandit.
        
        Args:
            value (int): New notoriety level value.
            
        Returns:
            int: Updated notoriety level value.
        """
        self._notoriety_level = value
        return value
    
    def get_weapon_preference(self):
        """
        Returns the bandit's weapon preference.
        
        Args: 
            None
        
        Returns:
            str: The name of the preferred weapon.
        """
        return self._weapon_preference
    
    def set_weapon_preference(self, value):
        """
        Sets the bandit's weapon preference.
        
        Args:
            value (str): The name of the preferred weapon.
            
        Returns:
            str: The name of the assigned weapon preference.
        """
        self._weapon_preference = value
        return value
   
    def get_loot_list(self):
        """
        Returns the list of loot the bandit has.
        
        Args: 
            None
        
        Returns:
            list: List of loot items.
        """
        return self._loot_list
    
    def set_loot_list(self, value):
        """
        Sets the list of loot the bandit has.
        
        Args:
            value (list): List of loot items.
            
        Returns:
            list: Updated list of loot items.
        """
        self._loot_list = value
        return value
    
    def get_hideout_location(self):
        """
        Returns the bandit's hideout location.
        
        Args: 
            None
        
        Returns:
            str: The name of the hideout location.
        """
        return self._hideout_location
    
    def set_hideout_location(self, value):
        """
        Sets the bandit's hideout location.
        
        Args:
            value (str): The name of the hideout location.
            
        Returns:
            str: The name of the assigned hideout location.
        """
        self._hideout_location = value
        return value
    
    def get_gang_member_count(self):
        """
        Returns the number of gang members the bandit has.
        
        Args: 
            None
        
        Returns:
            int: Number of gang members.
        """
        return self._gang_member_count
    
    def set_gang_member_count(self, value):
        """
        Sets the number of gang members the bandit has.
        
        Args:
            value (int): Number of gang members.
            
        Returns:
            int: Updated number of gang members.
        """
        self._gang_member_count = value
        return value
  
    def get_escape_route_list(self):
        """
        Returns the list of escape routes the bandit knows.
        
        Args: 
            None
        
        Returns:
            list: List of escape route names.
        """
        return self._escape_route_list
    
    def set_escape_route_list(self, value):
        """
        Sets the list of escape routes the bandit knows.
        
        Args:
            value (list): List of escape route names.
            
        Returns:
            list: Updated list of escape routes.
        """
        self._escape_route_list = value
        return value
   
    def get_ransom_skill_list(self):
        """
        Returns the list of ransom skills the bandit possesses.
        
        Args: 
            None
        
        Returns:
            list: List of ransom skill names.
        """
        return self._ransom_skill_list
    
    def set_ransom_skill_list(self, value):
        """
        Sets the list of ransom skills the bandit possesses.
        
        Args:
            value (list): List of ransom skill names.
            
        Returns:
            list: Updated list of ransom skills.
        """
        self._ransom_skill_list = value
        return value

    # Member functions (actions/verbs)
    def steal_from(self, target):
        """
        Attempts to steal loot from a target.

        Args:
            target (str): The target to steal from.

        Returns:
            None
        """
        print(f"{self._name} attempts to steal from {target} using stealth level {self._stealth_level}.")

    def bribe_guard(self, amount):
        """
        Bribes a guard with a specified amount of loot.

        Args:
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

        Args:
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

        Args:
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

        Args:
            number (int): The number of new members to add.

        Returns:
            None
        """
        self._gang_member_count += number
        print(f"{self._name} expands the gang by {number} members. Total gang size: {self._gang_member_count}.")

    def relocate_hideout(self, new_location):
        """
        Relocates the bandit's hideout to a new location.

        Args:
            new_location (str): The new hideout location.

        Returns:
            None
        """
        self._hideout_location = new_location
        print(f"{self._name} relocates the hideout to {new_location}.")