import Default_Character

class Warrior(Default_Character.Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Warrior", _level)
        self._strength = 100
        self._endurance = 90
        self._weapon_skill = 85
        self._armor_type = "Heavy"
        self._battle_cry = "For Glory!"
        self._combat_stance = "Aggressive"
        self._special_moves = ["Power Strike", "Shield Bash"]
        self._war_horn = "Dragon's Roar"
        

    # Unique member variables
    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, value):
        self._strength = value
    @property
    def endurance(self):
        return self._endurance
    @endurance.setter
    def endurance(self, value):
        self._endurance = value
    @property
    def weapon_skill(self):
        return self._weapon_skill
    @weapon_skill.setter
    def weapon_skill(self, value):
        self._weapon_skill = value
    @property
    def armor_type(self):
        return self._armor_type
    @armor_type.setter
    def armor_type(self, value):
        self._armor_type = value
    @property
    def battle_cry(self):
        return self._battle_cry
    @battle_cry.setter
    def battle_cry(self, value):
        self._battle_cry = value
    @property
    def combat_stance(self):
        return self._combat_stance
    @combat_stance.setter
    def combat_stance(self, value):
        self._combat_stance = value
    @property
    def special_moves(self):
        return self._special_moves
    @special_moves.setter
    def special_moves(self, value):
        self._special_moves = value
    @property
    def war_horn(self):
        return self._war_horn
    @war_horn.setter
    def war_horn(self, value):
        self._war_horn = value

    # Unique functions
    def berserk(self):
        if self._endurance >= 20:
            self._strength += 20
            self._endurance -= 20
            return f"{self.name} goes berserk! Strength increased to {self._strength}, endurance decreased to {self._endurance}."
        else:
            return f"{self.name} does not have enough endurance to go berserk."
    
    def defend(self):
        self._combat_stance = "Defensive"
        return f"{self.name} switches to a defensive stance."
    
    def use_special_move(self, move):
        if move in self._special_moves:
            return f"{self.name} uses {move}!"
        else:
            return f"{move} is not a known special move."
        
    def blow_war_horn(self):
        return f"{self.name} blows the war horn: {self._war_horn}!"

    def train(self, hours):
        self._strength += hours * 2
        self._endurance += hours * 2
        return f"{self.name} trains for {hours} hours. Strength is now {self._strength}, Endurance is now {self._endurance}."
    
    def rest(self, hours):
        self._endurance += hours * 3
        return f"{self.name} rests for {hours} hours. Endurance is now {self._endurance}."
    
    def shout_battle_cry(self):
        return f"{self.name} shouts: {self._battle_cry}!"
    
    def change_combat_stance(self, stance):
        self._combat_stance = stance
        return f"{self.name} changes combat stance to {self._combat_stance}."
    
    def equip_armor(self, armor):
        self._armor_type = armor
        return f"{self.name} equips {self._armor_type} armor."
    
    def wield_weapon(self, weapon):
        return f"{self.name} wields a {weapon} with skill level {self._weapon_skill}."
    
    def level_up(self):
        super().level_up()
        self._strength += 5
        self._endurance += 5
        self._weapon_skill += 3
        return f"{self.name} has leveled up! Strength: {self._strength}, Endurance: {self._endurance}, Weapon Skill: {self._weapon_skill}."
        
    def show_status(self):
        return f"Warrior: {self._name}, Level: {self._level}, Strength: {self._strength}, Endurance: {self._endurance}, Weapon Skill: {self._weapon_skill}, Armor Type: {self._armor_type}, Combat Stance: {self._combat_stance}"
    
    def attack(self, target):
        damage = self._strength * 0.5 + self._weapon_skill * 0.3
        return f"{self._name} attacks {target} dealing {damage} damage!"
    
    def defend_against(self, attacker):
        block_chance = self._endurance * 0.4 + self._weapon_skill * 0.2
        return f"{self._name} defends against {attacker} with a block chance of {block_chance}%."
    
    def rally(self, allies):
        return f"{self._name} rallies the allies: {', '.join(allies)} to fight with renewed vigor!"
    
    def intimidate(self, enemy):
        return f"{self._name} intimidates {enemy}, lowering their morale!"
    
    def forge_weapon(self, weapon_type):
        return f"{self._name} forges a mighty {weapon_type} to use in battle!"
    
    def participate_in_tournament(self, tournament_name):
        return f"{self._name} participates in the {tournament_name} tournament, showcasing their combat skills!"
    
    def lead_charge(self):
        return f"{self._name} leads a charge into battle, inspiring allies to follow!"
    
    def train_with_mentor(self, mentor_name, hours):
        self._strength += hours * 3
        self._weapon_skill += hours * 2
        return f"{self._name} trains with mentor {mentor_name} for {hours} hours. Strength is now {self._strength}, Weapon Skill is now {self._weapon_skill}."
    
    def participate_in_battle(self, battle_name):
        return f"{self._name} fights valiantly in the battle of {battle_name}!"
    
    def conquer_enemy(self, enemy_name):
        return f"{self._name} conquers the enemy: {enemy_name}, bringing glory to their name!"
    
    def defend_territory(self, territory_name):
        return f"{self._name} defends the territory of {territory_name} against all threats!"
    
    def lead_siege(self, fortress_name):
        return f"{self._name} leads the siege on {fortress_name}, demonstrating strategic prowess!"
    
    def train_special_move(self, move_name):
        if move_name not in self._special_moves:
            self._special_moves.append(move_name)
            return f"{self._name} has learned a new special move: {move_name}!"
        else:
            return f"{self._name} already knows the special move: {move_name}."
        