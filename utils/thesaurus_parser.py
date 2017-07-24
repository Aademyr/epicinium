'''
Utility to turn thesaurus.com input into usable lists of strings
and stripping trash text.
'''

# Paste input block here
s = '''
Bar of Air Ball
Bar of Ancestral Bronze
Caretaker's Bar
Clear Orb
Cone of Muck Touches
Cone of the Perfect Rite of Climbing
Crazed Cleric's Cube
Crazed Conjurer's Sphere
Cursed Messiahs' Bar of the Snake
Evil Thundering Bar
Great Pyramid of Dwarven Sadism Lance
Haunted Sinner's Cone
Innocent Ghosts' Cube of Curing Conjuration
Insane Wanderer's Sphere of Archers
Lost Cone
Lost Orb of Platinum Field
Orb of Time Arrow
Perfected Orb
Sphere of Sound Breath
Villainous Openers' Bar
Adamantine Bar
Bar of Ice Spans
Bar of the Glorious Evocation of Control
Bar of the Walkers' Ceremony of Perfection
Benevolent Krakens' Pyramid of the Barbaric Wyrm
Blasphemous Fiery Cone
Cube of the Kingly Breaker
Cursed Bar of Metal Rings
Doomed Instant Cube of Closing Transformation
Doomed Serpent's Orb of the Priests' Incatation of Lava
Drakes' Cone
Electrical Bar of Nothing Alteration
Envenomed Cone
Fiery Bar of the Exceptional Evocation of Become Drake
Generous Slayers' Cone of the Feline
Haunted Arch-angels' Sphere of Clairaudience Control
Orb of the Titans
Sphere of the Good Queen
Unknowable Burning Sphere of Fletchers
Wizards' Pyramid
Bar of the Holy Casting of Control Dragon
Corrupt Human's Cube of Alter Invisibility
Cowardly Elves' Sphere
Crusaders' Cube
Cube of Deflect Sound
Eagles' Pyramid
Endless Bar of the Beast
Ethereal Orb of the Thinkers' Working of Insanity
Fortuitous Soldier's Pyramid of Stranglers
Generous Monk's Cube of the Hearers' Charm of Lava
Hellish Yellow Orb of Bronze Hail
Holy Sphere
Jagged Cube of Silver Touches
Keen Cone
Orb of Fine Sea Serpents
Red Sphere of Doomed Infamy
Sylvan Speaker's Cone
Unjust Divinity's Cube of Crystal Ring
Unjust Monk's Orb
Wonderful Animate Cube
Black Gauntlet of the Defender
Chain Mail of Imperial Lineage
Dire Fiery Hauberk of Platinum Blasts
Ethereal Envenomed Quilted Armor
Evil Joiners' Tower Shield of Dexterity
Green Shield of Distant Cleverness
Haunted Spectres' Buckler
Intelligent Traveller's Shield
Lady's Buckler of the Charismatic Beater
Leather Armor of Platinum Cloud
Lost Banded Mail of Influence Conjuration
Mystic Tower Shield
Prismatic Banded Mail
Ring Mail of Bone Barriers
Serene Annihilator's Hauberk
Shield of Intoxication
Shooting Breast Plate of Mana Clouds
Studious Traitor's Shield
Sylvan Jagged Quilted Armor of Perfect Slime
Tower Shield of Copper and Assailing
Abyssimal Gauntlet of Diamond Lance
Ancient Knights' Tower Shield of Kill Fish
Armguard of Diamond Lances
Banded Mail of the Elemental Messiah
Blessed Immovable Gauntlet of the Humanoid
Buckler of Diamond Zones
Buckler of Ice Spans
Corrupt Vipers' Tower Shield
Demonic Snakes' Tower Shield of the Unspeakable Evocation of Blending
Gauntlet of the Clever King
God's Hauberk
Illuminated Ring Mail of Villainous Lightning
Mystical Gauntlet of Intoxication
Mystical Gods' Quilted Armor
Perfected Serpents' Buckler
Perfected Shooting Ring Mail
Plate Mail of the Speaker
Tower Shield of the Unknowable Illusion of Invisibility
Unknowable Adamantine Armguard
Unspeakable Yellow Banded Mail
Armguard of Compassion
Blue Greaves of Transform Nondetection
Bracer of Conjure Sneaking
Breast Plate of Greater Mana Shield
Breast Plate of the Lawful Witchery of the Hateful Caretakers
Chain Mail of Dwarven Flesh Barriers
Chain Mail of Mystical Bone Chains
Deadly Spined Breast Plate of Lust Circle
Glorious Undead's Tower Shield
Gods' Armguard
Hauberk of the Ancestral Ritual of Kill Consumer
Hauberk of the Hex of Carnage
Hellish Undead's Buckler of the Glamour of Earth
Insane Saint's Banded Mail
Leather Armor of Spirit Clouds
Meteoric Shield of Ghost Slaying
Otherworldly Envenomed Chain Mail
Perfected Amazon's Armguard of Monsters
Tower Shield of the Screaming Archmagi
Worldly Icy Shield of Acid Beams
'''

s = s.replace('\'', "\\'").replace('star', '').replace('\n\n', '\n').replace('\n', '\', 1.0),\n(\'')[2:-1]
s = s[6:-1]
s = '(' + s + '),'
print s
