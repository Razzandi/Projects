from default_character import Character
from character_class import CharacterClass

class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, CharacterClass.WARRIOR, level)
        self._strength = 100
        self._endurance = 90
        self._weapon_skill = 85
        self._armor_type = "Heavy"
        self._battle_cry = "For Glory!"
        self._combat_stance = "Aggressive"
        self._special_move_list = ["Power Strike", "Shield Bash"]
        self._war_horn = "Dragon's Roar"

    # Member variable properties

    def get_strength(self):
        """
        Gets the strength of the warrior.

        Args:
            None
        
        Returns:
            int: The strength value."""
        return self._strength
    
    def set_strength(self, value):
        """
        Sets the strength of the warrior.
        
        Args:
            value (int): The new strength value.
            
        Returns:
            None"""
        self._strength = value

    def get_endurance(self):
        """
        Gets the endurance of the warrior.
        
        Args:
            None
            
        Returns:
            int: The endurance value."""
        return self._endurance
    
    def set_endurance(self, value):
        """
        Sets the endurance of the warrior.
        
        Args:
            value (int): The new endurance value.
            
        Returns:
            None"""
        self._endurance = value

    def get_weapon_skill(self):
        """
        Gets the weapon skill of the warrior.
        
        Args:
            None
            
        Returns:
            int: The weapon skill value."""
        return self._weapon_skill
    
    def set_weapon_skill(self, value):
        """
        Sets the weapon skill of the warrior.
        
        Args:
            value (int): The new weapon skill value.
            
        Returns:
            None"""
        self._weapon_skill = value

    def get_armor_type(self):
        """
        Gets the armor type of the warrior.
        
        Args:
            None
            
        Returns:
            str: The armor type."""
        return self._armor_type
    
    def set_armor_type(self, value):
        """
        Sets the armor type of the warrior.
        
        Args:
            value (str): The new armor type.
            
        Returns:
            None"""
        self._armor_type = value

    def get_battle_cry(self):
        """
        Gets the battle cry of the warrior.
        
        Args:
            None
            
        Returns:
            str: The battle cry."""
        return self._battle_cry
    
    def set_battle_cry(self, value):
        """
        Sets the battle cry of the warrior.
        
        Args:
            value (str): The new battle cry.
            
        Returns:
            None"""
        self._battle_cry = value

    def get_combat_stance(self):
        """
        Gets the combat stance of the warrior.
        
        Args:
            None
            
        Returns:
            str: The combat stance."""
        return self._combat_stance
    
    def set_combat_stance(self, value):
        """
        Sets the combat stance of the warrior.
        
        Args:
            value (str): The new combat stance.
            
        Returns:
            None"""
        self._combat_stance = value

    def get_special_move_list(self):
        """
        Gets the list of special moves of the warrior.
        
        Args:
            None
            
        Returns:
            list: The list of special moves."""
        return self._special_move_list
    
    def set_special_move_list(self, value):
        """
        Sets the list of special moves of the warrior.
        
        Args:
            value (list): The new list of special moves.
        
        Returns:
            None"""
        self._special_move_list = value

    def get_war_horn(self):
        """
        Gets the war horn of the warrior.
    
        Args:
            None
        
        Returns:
            str: The war horn."""
        return self._war_horn
    
    def set_war_horn(self, value):
        """
        Sets the war horn of the warrior.
        
        Args:
            value (str): The new war horn.
            
        Returns:
            None"""
        self._war_horn = value

    # Member functions (actions/verbs)
    def go_berserk(self):
        """
        Increases strength and decreases endurance if enough endurance is available.

        Args:
            None

        Returns:
            str: Message about the berserk action and updated stats.
        """
        if self._endurance >= 20:
            self._strength += 20
            self._endurance -= 20
            return f"{self.name} goes berserk! Strength increased to {self._strength}, endurance decreased to {self._endurance}."
        else:
            return f"{self.name} does not have enough endurance to go berserk."
    
    def defend(self):
        """
        Switches the warrior's combat stance to defensive.

        Args:
            None

        Returns:
            str: Message about the new combat stance.
        """
        self._combat_stance = "Defensive"
        return f"{self.name} switches to a defensive stance."
    
    def use_special_move(self, move):
        """
        Uses a special move if known.

        Args:
            move (str): The name of the special move.

        Returns:
            str: Message about using the special move or not knowing it.
        """
        if move in self._special_move_list:
            return f"{self.name} uses {move}!"
        else:
            return f"{move} is not a known special move."
        
    def blow_war_horn(self):
        """
        Blows the warrior's war horn.

        Args:
            None

        Returns:
            str: Message about blowing the war horn.
        """
        return f"{self.name} blows the war horn: {self._war_horn}!"

    def train(self, hours):
        """
        Trains to increase strength and endurance.

        Args:
            hours (int): Number of hours spent training.

        Returns:
            str: Message about training and updated stats.
        """
        self._strength += hours * 2
        self._endurance += hours * 2
        return f"{self.name} trains for {hours} hours. Strength is now {self._strength}, Endurance is now {self._endurance}."
    
    def rest(self, hours):
        """
        Rests to recover endurance.

        Args:
            hours (int): Number of hours spent resting.

        Returns:
            str: Message about resting and updated endurance.
        """
        self._endurance += hours * 3
        return f"{self.name} rests for {hours} hours. Endurance is now {self._endurance}."
    
    def shout_battle_cry(self):
        """
        Shouts the warrior's battle cry.

        Args:
            None

        Returns:
            str: Message with the battle cry.
        """
        return f"{self.name} shouts: {self._battle_cry}!"
    
    def change_combat_stance(self, stance):
        """
        Changes the warrior's combat stance.

        Args:
            stance (str): The new combat stance.

        Returns:
            str: Message about the new combat stance.
        """
        self._combat_stance = stance
        return f"{self.name} changes combat stance to {self._combat_stance}."
    
    def equip_armor(self, armor):
        """
        Equips a new type of armor.

        Args:
            armor (str): The type of armor to equip.

        Returns:
            str: Message about equipping armor.
        """
        self._armor_type = armor
        return f"{self.name} equips {self._armor_type} armor."
    
    def wield_weapon(self, weapon):
        """
        Wields a weapon with the warrior's skill level.

        Args:
            weapon (str): The weapon to wield.

        Returns:
            str: Message about wielding the weapon.
        """
        return f"{self.name} wields a {weapon} with skill level {self._weapon_skill}."
    
    def show_status(self):
        """
        Shows the current status of the warrior.

        Args:
            None

        Returns:
            str: Message with the warrior's status.
        """
        return f"Warrior: {self._name}, Level: {self._level}, Strength: {self._strength}, Endurance: {self._endurance}, Weapon Skill: {self._weapon_skill}, Armor Type: {self._armor_type}, Combat Stance: {self._combat_stance}"
    
    def attack(self, target):
        """
        Attacks a target and calculates damage.

        Args:
            target (str): The target to attack.

        Returns:
            str: Message about the attack and damage dealt.
        """
        damage = self._strength * 0.5 + self._weapon_skill * 0.3
        return f"{self._name} attacks {target} dealing {damage} damage!"
    
    def defend_against(self, attacker):
        """
        Defends against an attacker and calculates block chance.

        Args:
            attacker (str): The attacker to defend against.

        Returns:
            str: Message about defending and block chance.
        """
        block_chance = self._endurance * 0.4 + self._weapon_skill * 0.2
        return f"{self._name} defends against {attacker} with a block chance of {block_chance}%."
    
    def rally_allies(self, allies):
        """
        Rallies allies to fight with renewed vigor.

        Args:
            allies (list): List of allies to rally.

        Returns:
            str: Message about rallying allies.
        """
        return f"{self._name} rallies the allies: {', '.join(allies)} to fight with renewed vigor!"
    
    def intimidate_enemy(self, enemy):
        """
        Intimidates an enemy to lower their morale.

        Args:
            enemy (str): The enemy to intimidate.

        Returns:
            str: Message about intimidating the enemy.
        """
        return f"{self._name} intimidates {enemy}, lowering their morale!"
    
    def forge_weapon(self, weapon_type):
        """
        Forges a new weapon for battle.

        Args:
            weapon_type (str): The type of weapon to forge.

        Returns:
            str: Message about forging the weapon.
        """
        return f"{self._name} forges a mighty {weapon_type} to use in battle!"
    
    def participate_in_tournament(self, tournament_name):
        """
        Participates in a combat tournament.

        Args:
            tournament_name (str): The name of the tournament.

        Returns:
            str: Message about participating in the tournament.
        """
        return f"{self._name} participates in the {tournament_name} tournament, showcasing their combat skills!"
    
    def lead_charge(self):
        """
        Leads a charge into battle.

        Args:
            None

        Returns:
            str: Message about leading the charge.
        """
        return f"{self._name} leads a charge into battle, inspiring allies to follow!"
    
    def train_with_mentor(self, mentor_name, hours):
        """
        Trains with a mentor to increase strength and weapon skill.

        Args:
            mentor_name (str): The mentor's name.
            hours (int): Number of hours spent training.

        Returns:
            str: Message about training and updated stats.
        """
        self._strength += hours * 3
        self._weapon_skill += hours * 2
        return f"{self._name} trains with mentor {mentor_name} for {hours} hours. Strength is now {self._strength}, Weapon Skill is now {self._weapon_skill}."
    
    def participate_in_battle(self, battle_name):
        """
        Participates in a battle.

        Args:
            battle_name (str): The name of the battle.

        Returns:
            str: Message about participating in the battle.
        """
        return f"{self._name} fights valiantly in the battle of {battle_name}!"
    
    def conquer_enemy(self, enemy_name):
        """
        Conquers an enemy.

        Args:
            enemy_name (str): The name of the enemy.

        Returns:
            str: Message about conquering the enemy.
        """
        return f"{self._name} conquers the enemy: {enemy_name}, bringing glory to their name!"
    
    def defend_territory(self, territory_name):
        """
        Defends a territory against threats.

        Args:
            territory_name (str): The name of the territory.

        Returns:
            str: Message about defending the territory.
        """
        return f"{self._name} defends the territory of {territory_name} against all threats!"
    
    def lead_siege(self, fortress_name):
        """
        Leads a siege on a fortress.

        Args:
            fortress_name (str): The name of the fortress.

        Returns:
            str: Message about leading the siege.
        """
        return f"{self._name} leads the siege on {fortress_name}, demonstrating strategic prowess!"
    
    def learn_special_move(self, move_name):
        """
        Learns a new special move if not already known.

        Args:
            move_name (str): The name of the special move.

        Returns:
            str: Message about learning the special move or already knowing it.
        """
        if move_name not in self._special_move_list:
            self._special_move_list.append(move_name)
            return f"{self._name} has learned a new special move: {move_name}!"
        else:
            return f"{self._name} already knows the special move: {move_name}."
