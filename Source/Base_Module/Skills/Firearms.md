## Firearms

@(dd Firearms)
{ 
  "*Name": "Firearms",
  "*Brief": "Basic skill for using firearms",
  "Base": "mD",
  "Category": "Skill/combat",
  "Dominance": "5",
  "Cost": "1 TT/Hard"
}

This combat style is the bases for using firearms. In general, the weapon gives
the modifier for the attack roll and determines the range, but the damage
generated is usually the same. Firing with a pistol six feet away from the
target or with a precision gun from 90 feet afar yields mostly the same results,
provided you can hit the mark.

All the damage type caused by **firearms** is of _piercing_ type, unless differently
specified.

Everyone can shoot with a firearm; as such, the firearms style is available to
anyone, but most maneuvers have a relatively high pre-requisite.

### Advanced Combat

The number of maneuvers the character can use per round depends on the level of
Firearms:

@(dt ac_firearms)
[
   ["Level", "Maneuvers"],
   ["1-5", 1],
   ["5-10", 2],
   ["11-15", 3],
   ["16+", 4]
]

@(include Firearms/*.md)
