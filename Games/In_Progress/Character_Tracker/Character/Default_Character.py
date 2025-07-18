# Create Base Character class

class Character:
        _name = "Name"
        _char_class = "Villager" #Turn this into an enum later
        _level = 1
        _inventory = []
        _abilities = {}
        _stats = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
        _health = 100
        _sanity = 100
        _mana = 50
        _experience = 0
        _quests = []
        _location = "Starting Village"
        _status_effects = []
        _allies = []
        _enemies = []
        _notes = []

        def __init__(self, _name, _char_class, _level=1):
            self._name = _name
            self._char_class = _char_class
            self._level = _level
            self._inventory = []
            self._abilities = {}
            self._stats = {
                'strength': 10,
                'dexterity': 10,
                'constitution': 10,
                'intelligence': 10,
                'wisdom': 10,
                'charisma': 10
            }
            self._health = 100
            self._sanity = 100
            self._mana = 50
            self._experience = 0
            self._quests = []
            self._location = "Starting Village"
            self._status_effects = []
            self._allies = []
            self._enemies = []
            self._notes = []

        def level_up(self):
            self._level += 1
            self._health += 10
            self._mana += 5
            self._stats['strength'] += 1
            self._stats['dexterity'] += 1
            self._stats['constitution'] += 1
            self._stats['intelligence'] += 1
            self._stats['wisdom'] += 1
            self._stats['charisma'] += 1
            print(f"{self._name} has leveled up to _level {self._level}!")

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def char_class(self):
            return self._char_class

        @char_class.setter
        def char_class(self, value):
            self._char_class = value

        @property
        def level(self):
            return self._level

        @level.setter
        def level(self, value):
            self._level = value

        @property
        def inventory(self):
            return self._inventory

        @inventory.setter
        def inventory(self, value):
            self._inventory = value

        @property
        def abilities(self):
            return self._abilities

        @abilities.setter
        def abilities(self, value):
            self._abilities = value

        @property
        def stats(self):
            return self._stats

        @stats.setter
        def stats(self, value):
            self._stats = value

        @property
        def health(self):
            return self._health

        @health.setter
        def health(self, value):
            self._health = value

        @property
        def sanity(self):
            return self._sanity

        @sanity.setter
        def sanity(self, value):
            self._sanity = value

        @property
        def mana(self):
            return self._mana

        @mana.setter
        def mana(self, value):
            self._mana = value

        @property
        def experience(self):
            return self._experience

        @experience.setter
        def experience(self, value):
            self._experience = value

        @property
        def quests(self):
            return self._quests

        @quests.setter
        def quests(self, value):
            self._quests = value

        @property
        def location(self):
            return self._location

        @location.setter
        def location(self, value):
            self._location = value

        @property
        def status_effects(self):
            return self._status_effects

        @status_effects.setter
        def status_effects(self, value):
            self._status_effects = value

        @property
        def allies(self):
            return self._allies

        @allies.setter
        def allies(self, value):
            self._allies = value

        @property
        def enemies(self):
            return self._enemies

        @enemies.setter
        def enemies(self, value):
            self._enemies = value

        @property
        def notes(self):
            return self._notes

        @notes.setter
        def notes(self, value):
            self._notes = value