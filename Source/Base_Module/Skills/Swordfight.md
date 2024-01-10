## Swordfight

@(dd swordfight)
{ 
  "*Name": "Swordfight",
  "*Brief": "Skill for handling swords and hand-weapons in combat",
  "Base": "mS or mD",
  "Category": "Skill/combat",
  "Dominance": "4",
  "EC": "Swords, Maces",
  "Cost": "1 TT/Hard"
}

Swordfight is the simplest discipline for handling traditional melee weapons.
Despite the name, it’s not limited to swords, as it can be used also with maces,
flails, shields and so on.

The style doesn’t differentiate between different kind of weapons as far as
special effect and damage is concerned. To take advantage of the specificities
of each weapon, a character can learn the specific style.

###  Two-handed weapons

This style can be used with large two-handed swords, maces and hammers as well;
they prevent the usage of a shield (and any maneuver related requiring it),
but give a **DP** modifier of +3.

### Advanced Combat

The number of maneuvers the character can use per round depends on the level
of Sword Fight:

@(dt ac_swordfight_levels)
[["Level", "Maneuvers"],
["1-6", 1],
["7-11", 2],
["12-15", 3],
["17+", 4]
]

@(include Swordfight/*.md)
