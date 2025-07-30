from Default_Character import Character

class Rogue(Character):
    def __init__(self, _name, _level=1):
        super().__init__(_name, "Rogue", _level)
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
        damage = self.backstab_damage
        print(f"{self._name} performs a sneak attack on {target}, dealing {damage} damage!")
    
    def pick_lock(self, lock_difficulty):
        if self.lockpicking_skill >= lock_difficulty:
            print(f"{self._name} successfully picks the lock!")
        else:
            print(f"{self._name} fails to pick the lock.")
    
    def disarm_trap(self, trap_difficulty):
        if self.lockpicking_skill >= trap_difficulty:
            self.traps_disarmed += 1
            print(f"{self._name} successfully disarms the trap! Total traps disarmed: {self.traps_disarmed}")
        else:
            print(f"{self._name} fails to disarm the trap.")

    def evade(self):
        success_chance = self.evasion_ability
        print(f"{self._name} attempts to evade an attack with a success chance of {success_chance}%.")

    def join_thieves_guild(self, rank):
        self.thieves_guild_rank = rank
        print(f"{self._name} has joined the Thieves Guild with the rank of {rank}.")
    
    def use_stealth(self, duration):
        print(f"{self._name} uses stealth for {duration} minutes, remaining undetected.")
    
    def attack_with_preferred_weapon(self, target):
        print(f"{self._name} attacks {target} with their preferred weapon: {self.preferred_weapon}.")
    
    def increase_agility(self, amount):
        self.agility += amount
        print(f"{self._name}'s agility increases by {amount} to {self.agility}.")
    
    def show_status(self):
        print(f"Rogue: {self._name}, Level: {self._level}, Stealth: {self._stealth}, Agility: {self._agility}, Lockpicking Skill: {self._lockpicking_skill}, Backstab Damage: {self._backstab_damage}, Preferred Weapon: {self._preferred_weapon}, Thieves Guild Rank: {self._thieves_guild_rank}, Traps Disarmed: {self._traps_disarmed}, Evasion Ability: {self._evasion_ability}")
    
    def flee(self):
        print(f"{self._name} uses their agility and stealth to flee from danger!")
    
    def steal(self, target):
        print(f"{self._name} attempts to steal from {target} using their stealth skills.")
    
    def scout_area(self, area):
        print(f"{self._name} scouts the area: {area}, gathering information without being seen.")
    
    def create_distraction(self):
        print(f"{self._name} creates a distraction to divert attention away from their actions.")
    
    def hide_in_shadows(self, duration):
        print(f"{self._name} hides in the shadows for {duration} minutes, avoiding detection.")
    
    def train_lockpicking(self, hours):
        self.lockpicking_skill += hours * 2
        print(f"{self._name} trains lockpicking for {hours} hours, increasing skill to {self.lockpicking_skill}.")
    
    def upgrade_backstab(self, amount):
        self.backstab_damage += amount
        print(f"{self._name}'s backstab damage increases by {amount} to {self.backstab_damage}.")
    
    def improve_evasion(self, amount):
        self.evasion_ability += amount
        print(f"{self._name}'s evasion ability increases by {amount} to {self.evasion_ability}.")
    
    def complete_thieves_guild_mission(self, mission_name):
        print(f"{self._name} completes the Thieves Guild mission: {mission_name}, earning respect and rewards.")
    
    def bribe_guard(self, amount):
        print(f"{self._name} bribes a guard with {amount} gold to avoid trouble.")
    
    def find_treasure(self, treasure_name):
        print(f"{self._name} finds a hidden treasure: {treasure_name}, adding it to their loot.")
    
    def set_trap(self, trap_type):
        print(f"{self._name} sets a {trap_type} trap to protect their hideout or ambush enemies.")
    
    def lockpick_chest(self, chest_difficulty):
        if self.lockpicking_skill >= chest_difficulty:
            print(f"{self._name} successfully lockpicks the chest and finds valuable items inside!")
        else:
            print(f"{self._name} fails to lockpick the chest.")
        
    def backflip_escape(self):
        print(f"{self._name} performs a daring backflip to escape from a tight situation!")
    
    def shadow_step(self, target):
        print(f"{self._name} uses Shadow Step to teleport behind {target} for a surprise attack!")
    
    def silent_kill(self, target):
        print(f"{self._name} silently eliminates {target} without making a sound.")
    
    def disguise(self, new_identity):
        print(f"{self._name} disguises themselves as {new_identity} to infiltrate enemy lines.")
    
    def forge_document(self, document_type):
        print(f"{self._name} forges a {document_type} to aid in their clandestine activities.")
    
    def eavesdrop(self, conversation):
        print(f"{self._name} eavesdrops on a conversation: {conversation}, gathering valuable intel.")
    
    def pickpocket(self, target):
        print(f"{self._name} attempts to pickpocket {target} without being noticed.")
    
    def escape_artist(self):
        print(f"{self._name} uses their skills as an escape artist to get out of restraints or confinement.")
    
    def create_smoke_bomb(self):
        print(f"{self._name} creates a smoke bomb to obscure vision and make a quick getaway.")
    
    def lockpicking_mastery(self):
        self.lockpicking_skill = 100
        print(f"{self._name} has achieved mastery in lockpicking, skill is now {self.lockpicking_skill}.")
    
    def stealth_mastery(self):
        self.stealth = 100
        print(f"{self._name} has achieved mastery in stealth, skill is now {self.stealth}.")
    
    def agility_mastery(self):
        self.agility = 100
        print(f"{self._name} has achieved mastery in agility, skill is now {self.agility}.")
    
    def evasion_mastery(self):
        self.evasion_ability = 100
        print(f"{self._name} has achieved mastery in evasion, skill is now {self.evasion_ability}.")
    
    def train_stealth(self, hours):
        self.stealth += hours * 2
        print(f"{self._name} trains stealth for {hours} hours, increasing skill to {self.stealth}.")
    
    def train_agility(self, hours):
        self.agility += hours * 2
        print(f"{self._name} trains agility for {hours} hours, increasing skill to {self.agility}.")
    
    def train_evasion(self, hours):
        self.evasion_ability += hours * 2
        print(f"{self._name} trains evasion for {hours} hours, increasing skill to {self.evasion_ability}.")
    
    def upgrade_preferred_weapon(self, new_weapon):
        self.preferred_weapon = new_weapon
        print(f"{self._name} upgrades their preferred weapon to {new_weapon}.")
    
    def show_detailed_status(self):
        print(f"Rogue Detailed Status:\nName: {self._name}\nLevel: {self._level}\nStealth: {self._stealth}\nAgility: {self._agility}\nLockpicking Skill: {self._lockpicking_skill}\nBackstab Damage: {self._backstab_damage}\nPreferred Weapon: {self._preferred_weapon}\nThieves Guild Rank: {self._thieves_guild_rank}\nTraps Disarmed: {self._traps_disarmed}\nEvasion Ability: {self._evasion_ability}")
    
    