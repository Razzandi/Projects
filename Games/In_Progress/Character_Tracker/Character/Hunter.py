import Default_Character

class Hunter(Default_Character.Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Hunter", _level)
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
    def set_trap(self, trap_type):
        if trap_type in self._traps:
            print(f"{self._name} sets a {trap_type} trap.")
        else:
            print(f"{self._name} does not have a {trap_type} trap.")
    def track_prey(self, prey):
        print(f"{self._name} is tracking a {prey}.")
    def use_hunting_technique(self, technique):
        if technique in self._hunting_techniques:
            print(f"{self._name} uses {technique} technique.")
        else:
            print(f"{self._name} does not know the {technique} technique.")
    def equip_survival_gear(self, gear):
        if gear in self._survival_gear:
            print(f"{self._name} equips {gear}.")
        else:
            print(f"{self._name} does not have {gear}.")
    def shoot_arrow(self):
        if self._quiver_capacity > 0:
            self._quiver_capacity -= 1
            print(f"{self._name} shoots an arrow. Arrows left: {self._quiver_capacity}")
        else:
            print(f"{self._name} has no arrows left to shoot.")
    def command_pet(self, command):
        if self._pet:
            print(f"{self._name} commands {self._pet} to {command}.")
        else:
            print(f"{self._name} has no pet to command.")
    def rest(self):
        self._stamina = 100
        print(f"{self._name} rests and restores stamina to {self._stamina}.")
    def hunt(self, prey):
        print(f"{self._name} is hunting a {prey} in the {self._preferred_hunting_ground}.")
    def tame_pet(self, pet_name):
        self._pet = pet_name
        print(f"{self._name} has tamed a pet named {pet_name}.")
    def upgrade_bow(self, new_bow_type):
        self._bow_type = new_bow_type
        print(f"{self._name} has upgraded their bow to a {new_bow_type}.")
    def add_trap(self, trap_type):
        if trap_type not in self._traps:
            self._traps.append(trap_type)
            print(f"{self._name} has added a {trap_type} trap to their inventory.")
        else:
            print(f"{self._name} already has a {trap_type} trap.")

    def add_hunting_technique(self, technique): 
        if technique not in self._hunting_techniques:
            self._hunting_techniques.append(technique)
            print(f"{self._name} has learned a new hunting technique: {technique}.")
        else:
            print(f"{self._name} already knows the {technique} technique.")

    def add_survival_gear(self, gear):
        if gear not in self._survival_gear:
            self._survival_gear.append(gear)
            print(f"{self._name} has acquired new survival gear: {gear}.")
        else:
            print(f"{self._name} already has {gear}.")
    def display_status(self):
        print(f"Hunter: {self._name}, Level: {self._level}, Stamina: {self._stamina}, Pet: {self._pet}, Traps: {self._traps}, Bow Type: {self._bow_type}, Quiver Capacity: {self._quiver_capacity}, Preferred Hunting Ground: {self._preferred_hunting_ground}, Hunting Techniques: {self._hunting_techniques}, Survival Gear: {self._survival_gear}")