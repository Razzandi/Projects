import random

r = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling', 'Arakocra', 'Aasimar', 'Air Genasi', 'Bugbear', 'Centaur', 'Changeling', 'Deep Gnome', 'Duergar', 'Earth Genasi', 'Eladrin', 'Fairy', 'Firbolg', 'Fire Genasi', 'Githyanki', 'Githzerai', 'Goblin', 'Goliath', 'Harengon', 'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Minotaur', 'Orc', 'Satyr', 'Sea Elf', 'Shadar-kai', 'Shifter', 'Tabaxi', 'Tortle', 'Triton', 'Water Genasi', 'Yuan-ti', 'Kender', 'Astral Elf', 'Autognome', 'Giff', 'Hadozee', 'Plasmoid', 'Thri-kreen', 'Owlin', 'Dhampir', 'Hexblood', 'Reborn', 'Leonin', 'Satyr', 'Kalashtar', 'Shifter', 'Warforged', 'Verdan', 'Centaur', 'Loxodon', 'Simic Hybrid', 'Vedalken', 'Feral Tiefling', 'Locathah', 'Grung', 'Gith', ]
scartificer = ['Alchemist Artificer', 'Armorer Artificer', 'Artillerist Artificer', 'Battle Smith Articer']
scbarbarian = ['Path of the Wild Magic Barbarian', 'Path of the Ancestral Guardian Barbarian', 'Path of the Beast Barbarian', 'Path of the Berserker Barbarian', 'Path of the Storm Herald Barbarian', 'Path of the Totem Warrior Barbarian', 'Path of the Zealot Barbarian']
scbard = ['College of Creation Bard', 'College of Glamour Bard', 'College of Lore Bard', 'College of Spirits Bard', 'College of Swords Bard', 'College of Valor Bard', 'College of Whispers Bard', 'College of Eloquence Bard']
sccleric = ['Cleric of the Death Domain', 'Cleric of the Forge Domain', 'Cleric of the Order Domain', 'Cleric of the Grave Domain', 'Cleric of the Knowledge Domain', 'Cleric of the Life Domain', 'Cleric of the Light Domain', 'Cleric of the Nature Domain', 'Cleric of the Peace Domain', 'Cleric of the Tempest Domain', 'Cleric of the Trickery Domain', 'Cleric of the Twilight Domain', 'Cleric of the War Domain']
scdruid = ['Circle of Dreams Druid', 'Circle of Stars Druid', 'Circle of Wildfire', 'Circle of the Land(Arctic)', 'Circle of the Land(Coast)', 'Circle of the Land(Desert)', 'Circle of the Land(Forest)', 'Circle of the Land(Grassland)', 'Circle of the Land(Mountain)', 'Circle of the Land(Swamp)', 'Circle of the Land(Underdark)', 'Circle of the Moon', 'Circle of the Shepard', 'Circle of Spores']
scfighter = ['Arcane Archer Fighter', 'Battle Master Fighter', 'Cavalier Fighter', 'Champion Fighter', 'Eldritch Knight Fighter', 'Psi Warrior Fighter', 'Rune Knight Fighter', 'Samurai Fighter']
scmonk = ['Way of Mercy Monk', 'Way of Shadow Monk', 'Way of the Astral Self Monk', 'Way of the Drunken Master Monk', 'Way of the Four Elements Monk', 'Way of the Kensei Monk', 'Way of the Open Hand Monk', 'Way of the Sun Soul Monk']
scpaladin = ['Oath of Glory Paladin', 'Oath of Conquest Paladin', 'Oath of Devotion Paladin', 'Oath of Redemption Paladin', 'Oath of Vengeance Paladin', 'Oath of Ancients Paladin', 'Oath of Watchers Paladin', 'Oathbreaker Paladin']
scranger = ['Beast Master Ranger', 'Fey Wanderer Ranger', 'Gloom Stalker Ranger', 'Horizon Walker Ranger', 'Hunter Ranger', 'Monster Slayer Ranger', 'Swarmkeeper Ranger']
scrogue = ['Arcane Trickster Rogue', 'Assassin Rogue', 'Inquisitive Rogue', 'Mastermind Rogue', 'Phantom Rogue', 'Scout Rogue', 'Soulknife Rogue', 'Swashbuckler Rogue', 'Thief Rogue']
scsorcerer = ['Sorcerer']
scwarlock = ['Patron Archfey Warlock', 'Patron Celestial Warlock', 'Patron Fathomless Warlock', 'Patron Fiend Warlock', 'Patron Genie Warlock', 'Patron Great Old One Warlock', 'Patron Hexblade Warlock', 'Patron Undead Warlock']
scwizard = ['School of Bladesinging Wizard', 'School of Scribes Wizard', 'School of Abjuration Wizard', 'School of Conjuration Wizard', 'School of Divination Wizard', 'School of Enchantment Wizard', 'School of Evocation Wizard', 'School of Illusion Wizard', 'School of Necromancy Wizard', 'School of Transmutation Wizard', 'School of War Wizard']


scart = random.sample(scartificer, k=1)
scbarb = random.sample(scbarbarian, k=1)
scbar = random.sample(scbard, k=1)
sccle = random.sample(sccleric, k=1)
scdru = random.sample(scdruid, k=1)
scfig = random.sample(scfighter, k=1)
scmon = random.sample(scmonk, k=1)
scpal = random.sample(scpaladin, k=1)
scran = random.sample(scranger, k=1)
scrog = random.sample(scrogue, k=1)
scsor = random.sample(scsorcerer, k=1)
scwar = random.sample(scwarlock, k=1)
scwiz = random.sample(scwizard, k=1)
c = [scart, scbarb, scbar, sccle, scdru, scfig, scmon, scpal, scran, scrog, scsor, scwar, scwiz]

while True:
    user_input = input("Type 'run' to randomize a character, or 'q' to quit!").lower()
    ra = random.sample(r, k=1)
    cl = random.sample(c, k=1)

    if user_input == "q":
        break
    if user_input == 'run':
        print("You are a ",ra,cl)

        