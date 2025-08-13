from Default_Character import Character
from CharacterClass import CharacterClass

class Rogue(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, CharacterClass.ROGUE, _level)

        self._stealth = 90
        self._agility = 85
        self._lockpicking_skill = 75
        self._backstab_damage = 150
        self._preferred_weapon = "Dagger"
        self._thieves_guild_rank = "Novice"
        self._traps_disarmed = 10
        self._evasion_ability = 80
        
    # Unique member variables
    @property
    def stealth(self):
        return self._stealth
    @stealth.setter
    def stealth(self, value):
        self._stealth = value
    @property
    def agility(self):
        return self._agility
    @agility.setter
    def agility(self, value):
        self._agility = value
    @property
    def lockpicking_skill(self):
        return self._lockpicking_skill
    @lockpicking_skill.setter
    def lockpicking_skill(self, value):
        self._lockpicking_skill = value
    @property
    def backstab_damage(self):
        return self._backstab_damage
    @backstab_damage.setter
    def backstab_damage(self, value):
        self._backstab_damage = value
    @property
    def preferred_weapon(self):
        return self._preferred_weapon
    @preferred_weapon.setter
    def preferred_weapon(self, value):
        self._preferred_weapon = value
    @property
    def thieves_guild_rank(self):
        return self._thieves_guild_rank
    @thieves_guild_rank.setter
    def thieves_guild_rank(self, value):
        self._thieves_guild_rank = value
    @property
    def traps_disarmed(self):
        return self._traps_disarmed
    @traps_disarmed.setter
    def traps_disarmed(self, value):
        self._traps_disarmed = value
    @property
    def evasion_ability(self):
        return self._evasion_ability
    @evasion_ability.setter
    def evasion_ability(self, value):
        self._evasion_ability = value

    # Unique functions
    def sneak_attack(self, target):
        """
        Performs a sneak attack on the target, dealing backstab damage.

        Parameters:
            target (str): The target to attack.

        Returns:
            None
        """
        damage = self.backstab_damage
        print(f"{self._name} performs a sneak attack on {target}, dealing {damage} damage!")

    def pick_lock(self, lock_difficulty):
        """
        Attempts to pick a lock based on the lock's difficulty.

        Parameters:
            lock_difficulty (int): The difficulty level of the lock.

        Returns:
            None
        """
        if self.lockpicking_skill >= lock_difficulty:
            print(f"{self._name} successfully picks the lock!")
        else:
            print(f"{self._name} fails to pick the lock.")

    def disarm_trap(self, trap_difficulty):
        """
        Attempts to disarm a trap based on its difficulty.

        Parameters:
            trap_difficulty (int): The difficulty level of the trap.

        Returns:
            None
        """
        if self.lockpicking_skill >= trap_difficulty:
            self.traps_disarmed += 1
            print(f"{self._name} successfully disarms the trap! Total traps disarmed: {self.traps_disarmed}")
        else:
            print(f"{self._name} fails to disarm the trap.")

    def evade(self):
        """
        Attempts to evade an attack using evasion ability.

        Parameters:
            None

        Returns:
            None
        """
        success_chance = self.evasion_ability
        print(f"{self._name} attempts to evade an attack with a success chance of {success_chance}%.")

    def join_thieves_guild(self, rank):
        """
        Joins the Thieves Guild with a specified rank.

        Parameters:
            rank (str): The rank to join with.

        Returns:
            None
        """
        self.thieves_guild_rank = rank
        print(f"{self._name} has joined the Thieves Guild with the rank of {rank}.")

    def use_stealth(self, duration):
        """
        Uses stealth for a specified duration.

        Parameters:
            duration (int): The number of minutes to remain undetected.

        Returns:
            None
        """
        print(f"{self._name} uses stealth for {duration} minutes, remaining undetected.")

    def attack_with_preferred_weapon(self, target):
        """
        Attacks a target with the rogue's preferred weapon.

        Parameters:
            target (str): The target to attack.

        Returns:
            None
        """
        print(f"{self._name} attacks {target} with their preferred weapon: {self.preferred_weapon}.")

    def increase_agility(self, amount):
        """
        Increases the rogue's agility by a specified amount.

        Parameters:
            amount (int): The amount to increase agility by.

        Returns:
            None
        """
        self.agility += amount
        print(f"{self._name}'s agility increases by {amount} to {self.agility}.")

    def show_status(self):
        """
        Displays the current status of the rogue.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Rogue: {self._name}, Level: {self._level}, Stealth: {self._stealth}, Agility: {self._agility}, Lockpicking Skill: {self._lockpicking_skill}, Backstab Damage: {self._backstab_damage}, Preferred Weapon: {self._preferred_weapon}, Thieves Guild Rank: {self._thieves_guild_rank}, Traps Disarmed: {self._traps_disarmed}, Evasion Ability: {self._evasion_ability}")

    def flee(self):
        """
        Uses agility and stealth to flee from danger.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} uses their agility and stealth to flee from danger!")

    def steal(self, target):
        """
        Attempts to steal from a target using stealth skills.

        Parameters:
            target (str): The target to steal from.

        Returns:
            None
        """
        print(f"{self._name} attempts to steal from {target} using their stealth skills.")

    def scout_area(self, area):
        """
        Scouts an area to gather information without being seen.

        Parameters:
            area (str): The area to scout.

        Returns:
            None
        """
        print(f"{self._name} scouts the area: {area}, gathering information without being seen.")

    def create_distraction(self):
        """
        Creates a distraction to divert attention.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} creates a distraction to divert attention away from their actions.")

    def hide_in_shadows(self, duration):
        """
        Hides in the shadows for a specified duration.

        Parameters:
            duration (int): The number of minutes to hide.

        Returns:
            None
        """
        print(f"{self._name} hides in the shadows for {duration} minutes, avoiding detection.")

    def train_lockpicking(self, hours):
        """
        Trains lockpicking for a specified number of hours.

        Parameters:
            hours (int): The number of hours to train.

        Returns:
            None
        """
        self.lockpicking_skill += hours * 2
        print(f"{self._name} trains lockpicking for {hours} hours, increasing skill to {self.lockpicking_skill}.")

    def upgrade_backstab(self, amount):
        """
        Upgrades backstab damage by a specified amount.

        Parameters:
            amount (int): The amount to increase backstab damage by.

        Returns:
            None
        """
        self.backstab_damage += amount
        print(f"{self._name}'s backstab damage increases by {amount} to {self.backstab_damage}.")

    def improve_evasion(self, amount):
        """
        Improves evasion ability by a specified amount.

        Parameters:
            amount (int): The amount to increase evasion ability by.

        Returns:
            None
        """
        self.evasion_ability += amount
        print(f"{self._name}'s evasion ability increases by {amount} to {self.evasion_ability}.")

    def complete_thieves_guild_mission(self, mission_name):
        """
        Completes a Thieves Guild mission.

        Parameters:
            mission_name (str): The name of the mission.

        Returns:
            None
        """
        print(f"{self._name} completes the Thieves Guild mission: {mission_name}, earning respect and rewards.")

    def bribe_guard(self, amount):
        """
        Bribes a guard with a specified amount of gold.

        Parameters:
            amount (int): The amount of gold to bribe with.

        Returns:
            None
        """
        print(f"{self._name} bribes a guard with {amount} gold to avoid trouble.")

    def find_treasure(self, treasure_name):
        """
        Finds a hidden treasure and adds it to the rogue's loot.

        Parameters:
            treasure_name (str): The name of the treasure.

        Returns:
            None
        """
        print(f"{self._name} finds a hidden treasure: {treasure_name}, adding it to their loot.")

    def set_trap(self, trap_type):
        """
        Sets a trap to protect the hideout or ambush enemies.

        Parameters:
            trap_type (str): The type of trap to set.

        Returns:
            None
        """
        print(f"{self._name} sets a {trap_type} trap to protect their hideout or ambush enemies.")

    def lockpick_chest(self, chest_difficulty):
        """
        Attempts to lockpick a chest based on its difficulty.

        Parameters:
            chest_difficulty (int): The difficulty level of the chest.

        Returns:
            None
        """
        if self.lockpicking_skill >= chest_difficulty:
            print(f"{self._name} successfully lockpicks the chest and finds valuable items inside!")
        else:
            print(f"{self._name} fails to lockpick the chest.")


    def backflip_escape(self):
        """
        Performs a daring backflip to escape from a tight situation.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self._name} performs a daring backflip to escape from a tight situation!")

    def shadow_step(self, target):
        """
        Uses Shadow Step to teleport behind a target for a surprise attack.

        Parameters:
            target (str): The target to teleport behind.

        Returns:
            None
        """
        print(f"{self._name} uses Shadow Step to teleport behind {target} for a surprise attack!")

    def silent_kill(self, target):
        """
        Silently eliminates a target without making a sound.

        Parameters:
            target (str): The target to eliminate.

        Returns:
            None
        """
        print(f"{self._name} silently eliminates {target} without making a sound.")