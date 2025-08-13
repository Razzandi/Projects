from default_character import Character
from Joe_Github.Projects.Games.In_Progress.Character_Tracker.Character.character_class import CharacterClass

class Hunter(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, CharacterClass.HUNTER, _level)
        self._stamina = 100
        self._pet = None
        self._traps = []
        self._bow_type = "Longbow"
        self._quiver_capacity = 20
        self._preferred_hunting_ground = "Forest"
        self._hunting_techniques = ["Stealth", "Tracking"]
        self._survival_gear = ["Knife", "Rope"]

    # Unique member variables
    @property
    def stamina(self):
        return self._stamina
    @stamina.setter
    def stamina(self, value):
        self._stamina = value
    @property
    def pet(self):
        return self._pet
    @pet.setter
    def pet(self, value):
        self._pet = value
    @property
    def traps(self):
        return self._traps
    @traps.setter
    def traps(self, value):
        self._traps = value
    @property
    def bow_type(self):
        return self._bow_type
    @bow_type.setter
    def bow_type(self, value):
        self._bow_type = value
    @property
    def quiver_capacity(self):
        return self._quiver_capacity
    @quiver_capacity.setter
    def quiver_capacity(self, value):
        self._quiver_capacity = value
    @property
    def preferred_hunting_ground(self):
        return self._preferred_hunting_ground
    @preferred_hunting_ground.setter
    def preferred_hunting_ground(self, value):
        self._preferred_hunting_ground = value
    @property
    def hunting_techniques(self):
        return self._hunting_techniques
    @hunting_techniques.setter
    def hunting_techniques(self, value):
        self._hunting_techniques = value
    @property
    def survival_gear(self):
        return self._survival_gear
    @survival_gear.setter
    def survival_gear(self, value):
        self._survival_gear = value

    # Unique functions
        # Unique functions
    def set_trap(self, trap_type):
        """
        Sets a trap if the hunter has it in their inventory.

        Parameters:
            trap_type (str): The type of trap to set.

        Returns:
            None
        """
        if trap_type in self._traps:
            print(f"{self._name} sets a {trap_type} trap.")
        else:
            print(f"{self._name} does not have a {trap_type} trap.")

    def track_prey(self, prey):
        """
        Tracks the specified prey.

        Parameters:
            prey (str): The type of prey to track.

        Returns:
            None
        """
        print(f"{self._name} is tracking a {prey}.")

    def use_hunting_technique(self, technique):
        """
        Uses a hunting technique if known.

        Parameters:
            technique (str): The hunting technique to use.

        Returns:
            None
        """
        if technique in self._hunting_techniques:
            print(f"{self._name} uses {technique} technique.")
        else:
            print(f"{self._name} does not know the {technique} technique.")

    def equip_survival_gear(self, gear):
        """
        Equips survival gear if available.

        Parameters:
            gear (str): The survival gear to equip.

        Returns:
            None
        """
        if gear in self._survival_gear:
            print(f"{self._name} equips {gear}.")
        else:
            print(f"{self._name} does not have {gear}.")

    def shoot_arrow(self):
        """
        Shoots an arrow if any are left in the quiver.

        Parameters:
            None

        Returns:
            None
        """
        if self._quiver_capacity > 0:
            self._quiver_capacity -= 1
            print(f"{self._name} shoots an arrow. Arrows left: {self._quiver_capacity}")
        else:
            print(f"{self._name} has no arrows left to shoot.")

    def command_pet(self, command):
        """
        Commands the hunter's pet to perform an action.

        Parameters:
            command (str): The command to give to the pet.

        Returns:
            None
        """
        if self._pet:
            print(f"{self._name} commands {self._pet} to {command}.")
        else:
            print(f"{self._name} has no pet to command.")

    def rest(self):
        """
        Restores the hunter's stamina to full.

        Parameters:
            None

        Returns:
            None
        """
        self._stamina = 100
        print(f"{self._name} rests and restores stamina to {self._stamina}.")

    def hunt(self, prey):
        """
        Hunts a specified prey in the preferred hunting ground.

        Parameters:
            prey (str): The prey to hunt.

        Returns:
            None
        """
        print(f"{self._name} is hunting a {prey} in the {self._preferred_hunting_ground}.")

    def tame_pet(self, pet_name):
        """
        Tames a pet and assigns it to the hunter.

        Parameters:
            pet_name (str): The name of the pet to tame.

        Returns:
            None
        """
        self._pet = pet_name
        print(f"{self._name} has tamed a pet named {pet_name}.")

    def upgrade_bow(self, new_bow_type):
        """
        Upgrades the hunter's bow to a new type.

        Parameters:
            new_bow_type (str): The new bow type.

        Returns:
            None
        """
        self._bow_type = new_bow_type
        print(f"{self._name} has upgraded their bow to a {new_bow_type}.")

    def add_trap(self, trap_type):
        """
        Adds a trap to the hunter's inventory if not already present.

        Parameters:
            trap_type (str): The type of trap to add.

        Returns:
            None
        """
        if trap_type not in self._traps:
            self._traps.append(trap_type)
            print(f"{self._name} has added a {trap_type} trap to their inventory.")
        else:
            print(f"{self._name} already has a {trap_type} trap.")

    def add_hunting_technique(self, technique):
        """
        Adds a hunting technique to the hunter's repertoire if not already known.

        Parameters:
            technique (str): The hunting technique to add.

        Returns:
            None
        """
        if technique not in self._hunting_techniques:
            self._hunting_techniques.append(technique)
            print(f"{self._name} has learned a new hunting technique: {technique}.")
        else:
            print(f"{self._name} already knows the {technique} technique.")

    def add_survival_gear(self, gear):
        """
        Adds survival gear to the hunter's inventory if not already present.

        Parameters:
            gear (str): The survival gear to add.

        Returns:
            None
        """
        if gear not in self._survival_gear:
            self._survival_gear.append(gear)
            print(f"{self._name} has acquired new survival gear: {gear}.")
        else:
            print(f"{self._name} already has {gear}.")

    def display_status(self):
        """
        Displays the current status of the hunter.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Hunter: {self._name}, Level: {self._level}, Stamina: {self._stamina}, Pet: {self._pet}, Traps: {self._traps}, Bow Type: {self._bow_type}, Quiver Capacity: {self._quiver_capacity}, Preferred Hunting Ground: {self._preferred_hunting_ground}, Hunting Techniques: {self._hunting_techniques}, Survival Gear: {self._survival_gear}")