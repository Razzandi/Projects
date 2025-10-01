from default_character import Character
from character_class import CharacterClass

class Hunter(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.HUNTER, level)
        self._stamina = 100
        self._pet = None
        self._trap_list = []
        self._bow_type = "Longbow"
        self._quiver_capacity = 20
        self._preferred_hunting_ground = "Forest"
        self._hunting_technique_list = ["Stealth", "Tracking"]
        self._survival_gear_list = ["Knife", "Rope"]

    
    def get_stamina(self):
        """
        Returns the current stamina of the hunter.
        
        Args: 
            None
        
        Returns:
            int: Current stamina value.
        """
        return self._stamina
    
    def set_stamina(self, value):
        """
        Sets the stamina of the hunter.
        
        Args:
            value (int): New stamina value.
            
        Returns:
            int: Updated stamina value.
        """
        self._stamina = value
        return value
    
    def get_pet(self):
        """
        Returns the hunter's pet.
        
        Args: 
            None
        
        Returns:
            str or None: The name of the pet, or None if no pet is assigned.
        """
        return self._pet
    
    def set_pet(self, value):
        """
        Sets the hunter's pet.
        
        Args:
            value (str): The name of the pet.
            
        Returns:
            str: The name of the assigned pet.
        """
        self._pet = value
        return value
    
    def get_trap_list(self):
        """
        Returns the list of traps the hunter has.
        
        Args: 
            None
        
        Returns:
            list: List of trap types.
        """
        return self._trap_list
    
    def set_trap_list(self, value):
        """
        Sets the list of traps the hunter has.
        
        Args:
            value (list): List of trap types.
            
        Returns:
            list: Updated list of traps.
        """
        self._trap_list = value
        return value

    def get_bow_type(self):
        """
        Returns the type of bow the hunter uses.
        
        Args: 
            None
        
        Returns:
            str: Type of bow.
        """
        return self._bow_type
    
    def set_bow_type(self, value):
        """
        Sets the type of bow the hunter uses.
        
        Args:
            value (str): Type of bow.
            
        Returns:
            str: Updated type of bow.
        """
        self._bow_type = value
        return value

    def get_quiver_capacity(self):
        """
        Returns the quiver capacity of the hunter.

        Args: 
            None

        Returns:
            int: Quiver capacity.
        """
        return self._quiver_capacity

    def set_quiver_capacity(self, value):
        """
        Sets the quiver capacity of the hunter.

        Args:
            value (int): Quiver capacity.

        Returns:
            int: Updated quiver capacity.
        """
        self._quiver_capacity = value
        return value

    def get_preferred_hunting_ground(self):
        """
        Returns the preferred hunting ground of the hunter.

        Args: 
            None

        Returns:
            str: Preferred hunting ground.
        """
        return self._preferred_hunting_ground
    
    def set_preferred_hunting_ground(self, value):
        """
        Sets the preferred hunting ground of the hunter.

        Args:
            value (str): Preferred hunting ground.

        Returns:
            str: Updated preferred hunting ground.
        """
        self._preferred_hunting_ground = value
        return value

    def get_hunting_technique_list(self):
        """
        Returns the list of hunting techniques known by the hunter.

        Args: 
            None

        Returns:
            list: List of hunting techniques.
        """
        return self._hunting_technique_list

    def set_hunting_technique_list(self, value):
        """
        Sets the list of hunting techniques known by the hunter.

        Args:
            value (list): List of hunting techniques.

        Returns:
            list: Updated list of hunting techniques.
        """
        self._hunting_technique_list = value
        return value

    def get_survival_gear_list(self):
        """
        Returns the list of survival gear the hunter has.

        Args: 
            None

        Returns:
            list: List of survival gear.
        """
        return self._survival_gear_list
    
    def set_survival_gear_list(self, value):
        """
        Sets the list of survival gear the hunter has.

        Args:
            value (list): List of survival gear.

        Returns:
            list: Updated list of survival gear.
        """
        self._survival_gear_list = value
        return value

    # Member functions (actions/verbs)
    def set_trap(self, trap_type):
        """
        Sets a trap if the hunter has it in their inventory.
        """
        if trap_type in self._trap_list:
            print(f"{self._name} sets a {trap_type} trap.")
        else:
            print(f"{self._name} does not have a {trap_type} trap.")

    def track_prey(self, prey):
        """
        Tracks the specified prey.
        """
        print(f"{self._name} is tracking a {prey}.")

    def use_hunting_technique(self, technique):
        """
        Uses a hunting technique if known.
        """
        if technique in self._hunting_technique_list:
            print(f"{self._name} uses {technique} technique.")
        else:
            print(f"{self._name} does not know the {technique} technique.")

    def equip_survival_gear(self, gear):
        """
        Equips survival gear if available.
        """
        if gear in self._survival_gear_list:
            print(f"{self._name} equips {gear}.")
        else:
            print(f"{self._name} does not have {gear}.")

    def shoot_arrow(self):
        """
        Shoots an arrow if any are left in the quiver.
        """
        if self._quiver_capacity > 0:
            self._quiver_capacity -= 1
            print(f"{self._name} shoots an arrow. Arrows left: {self._quiver_capacity}")
        else:
            print(f"{self._name} has no arrows left to shoot.")

    def command_pet(self, command):
        """
        Commands the hunter's pet to perform an action.
        """
        if self._pet:
            print(f"{self._name} commands {self._pet} to {command}.")
        else:
            print(f"{self._name} has no pet to command.")

    def rest(self):
        """
        Restores the hunter's stamina to full.
        """
        self._stamina = 100
        print(f"{self._name} rests and restores stamina to {self._stamina}.")

    def hunt(self, prey):
        """
        Hunts a specified prey in the preferred hunting ground.
        """
        print(f"{self._name} is hunting a {prey} in the {self._preferred_hunting_ground}.")

    def tame_pet(self, pet_name):
        """
        Tames a pet and assigns it to the hunter.
        """
        self._pet = pet_name
        print(f"{self._name} has tamed a pet named {pet_name}.")

    def upgrade_bow(self, new_bow_type):
        """
        Upgrades the hunter's bow to a new type.
        """
        self._bow_type = new_bow_type
        print(f"{self._name} has upgraded their bow to a {new_bow_type}.")

    def add_trap(self, trap_type):
        """
        Adds a trap to the hunter's inventory if not already present.
        """
        if trap_type not in self._trap_list:
            self._trap_list.append(trap_type)
            print(f"{self._name} has added a {trap_type} trap to their inventory.")
        else:
            print(f"{self._name} already has a {trap_type} trap.")

    def add_hunting_technique(self, technique):
        """
        Adds a hunting technique to the hunter's repertoire if not already known.
        """
        if technique not in self._hunting_technique_list:
            self._hunting_technique_list.append(technique)
            print(f"{self._name} has learned a new hunting technique: {technique}.")
        else:
            print(f"{self._name} already knows the {technique} technique.")

    def add_survival_gear(self, gear):
        """
        Adds survival gear to the hunter's inventory if not already present.
        """
        if gear not in self._survival_gear_list:
            self._survival_gear_list.append(gear)
            print(f"{self._name} has acquired new survival gear: {gear}.")
        else:
            print(f"{self._name} already has {gear}.")

    def display_status(self):
        """
        Displays the current status of the hunter.
        """
        print(
            f"Hunter: {self._name}, Level: {self._level}, Stamina: {self._stamina}, Pet: {self._pet}, "
            f"Traps: {self._trap_list}, Bow Type: {self._bow_type}, Quiver Capacity: {self._quiver_capacity}, "
            f"Preferred Hunting Ground: {self._preferred_hunting_ground}, "
            f"Hunting Techniques: {self._hunting_technique_list}, Survival Gear: {self._survival_gear_list}"
        )