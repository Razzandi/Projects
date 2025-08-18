from default_character import Character
from Joe_Github.Projects.Games.In_Progress.Character_Tracker.Character.character_class import CharacterClass

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

    # Member variable properties
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
    def trap_list(self):
        return self._trap_list
    @trap_list.setter
    def trap_list(self, value):
        self._trap_list = value

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
    def hunting_technique_list(self):
        return self._hunting_technique_list
    @hunting_technique_list.setter
    def hunting_technique_list(self, value):
        self._hunting_technique_list = value

    @property
    def survival_gear_list(self):
        return self._survival_gear_list
    @survival_gear_list.setter
    def survival_gear_list(self, value):
        self._survival_gear_list = value

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