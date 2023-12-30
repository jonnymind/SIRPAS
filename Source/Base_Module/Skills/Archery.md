## Archery

@(dd archery)
{ 
  "*Name": "Archery",
  "*Brief": "Combat skill for using bows and similar weapons",
  "Base": "mD",
  "Category": "Skill/combat",
  "Dominance": "4",
  "Cost": "1 TT/Hard"
}

This is the base style (and skill) needed to use bows, crossbows and similar projectile
weapons.

Unless differently specified, all attacks from *archery* deal __cut__ damage,
and the range depends on the used weapon.

### Advanced Combat 

This is the number of maneuvers granted by archery in advanced combat system.

@(dt ac_archery_levels)
[
   ["Level", "Maneuvers"],
   ["1-9", 1],
   ["10-16", 2],
   ["17+", 3]
]

@(include Archery/*.md)
