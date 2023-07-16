# Introduction

This is the SIRPAS Base Module, also known as the *Foundation*. 

SIRPAS stands for "Simple Role Playing Adventure System". It's a modular RPG
system that separates the rules from the definition of the various statistics
used by the characters to move through the game.

The Base Module presents a set of generic statistics (attributes, skills, advantages and
perks) that should cover most adventure styles, game worlds and settings.

Further modules, describing specific settings and worlds, can use the whole
of the base module and add on top of it, or redefine and eventually discard whatever
element they want.

> The rest of this book refers itself as the *Foundation*.

## Jump into the action

This manual is organized so that you can skim through the main
paragraph of every chapter to start getting into the game. If you
prefer, you can read it front to back, but it's not necessary.

When you need more details, you can go back to the relevant chapter
and read the paragraph you're interested into.

Even more details about the rules are in the [Rulebook](https://jonnymind.github.io/SIRPAS/Rulebook.html),
where every fine mechanics is treated in depth; the paragraphs in this
*Foundation* points directly at the relevant sections in the Rulebook.

At the end of every paragraph, there will be a link to the next one
so that joining the action is even easier. 

So, let's get into the adventure... and [jump into the action](#foundational-attributes).

## Somewhat standalone

The *Foundation* is designed so that reading the Rulebook in advance is not
necessary. You can read this manual and start playing right away.

As the various statistics are introduced, the underlying rules are briefly
explained, and the relevant section of the Rulebook is indicated, so that
it can be used as a reference as you go through this manual.

# Foundational Attributes

The *Foundation* has a hierarchy of attributes, from the least specific to the
more detailed. Attributes meant to express the proficiency of a character in
a particular ability are called *skills*, but are otherwise identical to other
attributes.

The hierarchy is so defined:

```
Mains -> Primary -> Secondary & Hard Skills -> Normal Skills -> Easy Skills
```

**Mains** and **Primaries** have a value between 3 and 18. 

For those, 3 means the attribute is minimally
functional, as that of a young child, and 18 is the peak achievement of a character
in the adventure setting. The vast majority of the population would stack
around 9-11.

Secondary attributes and skills have different value range: 0-20, with 0 being
*untrained* and 20 being the peak training possible.

# Skills {#BaM-m-skills}

Skills are abilities that a character can exercise at a certain moment, and 
They are usually based on a single attribute; this means that, if the character
didn’t invent any CP in them, they assume the same value of he attribute they
are based on.

Some are based on multiple attributes: their base value can be a mean of two or 
more attributes, or can be the best out of alternative attributes.

Some skills don’t have a base: they represent abilities that must be learned
from scratch; for example lock picking must be learned before being used.

Last, some skills have a base that depends on a base modifier; this is indicated
with a lowercase letter 'm' in front of the attribute.

## Acrobatics (D) {#BaM-s-acrobatics}

The character is able to perform acrobatic feats, including falling from a
height that would normally damage a less skilled character.

If used to check if the character is hurt when falling from a height, the
following table indicates the modifier applied:

| Height                               | Modifier                             |
|--------------------------------------|--------------------------------------|
| 6 feet                               | Trivial                              |
| 9 feet                               | Easy                                 |
| 12 feet                              | Normal                               |
| 18 feet                              | Difficult                            |
| 24 feet                              | Hard                                 |
| 30 feet                              | Very Hard                            |

Above 30 feet, the check fails automatically. 

When the check fails the character takes 1 damage point per feet.

# Advantages {#BaM-gen-advantages}

Advantages special conditions that apply to the character in general or to a specific skill in particular, 
and that have a direct effect on some game mechanics.

While most advantages are simply possessed by a character or not, some can have different levels. 
For example, Survival Instinct can have a level between 1 and 3, each granting a higher modifier. 

In that case, the description of the advantage indicates the initial cost and the cost per additional level. 
The cost of a further level is given by the base cost, plus the additional level cost times the current level. 
For example, if the description indicates the cost in **CP** being 5+2, it means that the first level costs 5, 
the second 5+2*1 = 7, the third 5+2*2 = 9 and so on.

Some advantage could have a pre-requisite that must be fulfilled in order to be acquired. 
For example, they could require having already acquired another advantage, or having a certain 
statistic at a minimum set score.

## Battleproof (10CP) {#BaM-a-battleproof}

The character can withstand an additional wound from physical sources before
being incapacitated. The first physical wound is received during a fight will
automatically heal in 6 hours, even if not treated.

# Disadvantages {#BaM-gen-disadvantages}

Advantages can also be negative (disadvantages). A character might be given
disadvantages temporarily or permanently, because of what happened during
previous adventures, or as a background flavour, or in order to gain CP to be
spent elsewhere, in other statistics.

## Lack of Instinct 1-4 (6/3CP) {#BaM-a-lack-of-instinct}

All instinctive defense checks and contests get a -1
modifier per level bought. 

Cannot be countered by buying Survival Instinct.

# Perks and Drags {#BaM-gen-perks-and-drags}

Perks and drags are generic advantages and disadvantages that don’t 
impact the game system directly. They usually give more flavour  in 
terms of roleplaying, and better define a character in its settings.

>Being famous, of noble origins, being able to play a certain instrument, 
knowing a certain literature or scientific topic, being rich, and the 
inverse of those are considered perks (or drags). 

They can and usually will have an influence in how the adventure plays, 
and some of them has also some indirect effect on the rules. For example, 
Medical Knowledge is mainly meant for your character to be able to speak 
competently about illnesses and cures, but it also influences the rolls on 
First Aid; Criminal Boss is meant to direct your adventure in a certain 
direction, but it also influences the skill Intimidate.

## Aristocrat {#BaM-a-aristocrat}

|   |   |
|------|--|
| Spec |  |
| Cost | 20/30/40 CP |
| Prereq | - |
| Max | - |

The character is an aristocrat in the target setting. In settings
that don’t comprise a birth right, traditional aristocracy, the
perk grants belonging to a similar oligarchy or high-order political
elite.

The cost, and the effect of the perk on the game, depend on the
level of aristocracy:

* Baron, career politician, oligarch: 20 CP
* Count, party leader, organization leader: 30 CP
* Duke, minister, CEO: 40 CP

# Combat

Combat is an advanced form of contest. In a normal contest, characters
try to win one over another on specific skills, while in combat,
contests are finalized to deal damage or other negative effects on
an unwilling target.

The Base Module provides several sub-systems to resolve conflicts, increasingly
detailed (and complex):

* *Simplified Combat*: It's a simple way to resolve small combats.
	It consists in a specialized form of [multi-contest](#multi-contest) applied to combat
	skills, which takes into account the relative ranking in the contests to
	determine winners, losers, and other possible outcomes.
* *Basic Combat*: It's a sub-system dedicated specifically to combat, using
	the combat skills with specific rules, and takes into account positioning,
	tactical advantages and other combat-specific elements.
* *Advanced Combat*: This is the full fledged combat system, extending the
	_basic combat_ and using special sub-skills called _maneuvers_.

You can mix and match these sub-systems in the same adventure, without
limitation. You can either choose one or another depending on the experience
of the players, or their inclinations, or you can base the choice on the
relevance of the combat in the adventure. For example, you could resolve
a brawl erupted in a tavern as a *simplified combat*, to turn to the
*advanced combat* when things get nasty while fighting the guards to escape
a dungeon.

## Generic Combat Skills {#BaM-s-generic-combat-skills}

The skills in this sections are combat skills not related with any
_combat style_.

They differ from normal maneuvers in the fact that they don’t belong to any
style, and as proper skills, they can be learned independently, and targeted by
advantages and perks.

### Disengage {#BaM-s-generic-combat-disengage}

|   |   |
|------|------|
| Cost | 4 CP |
| Type | Defense |
| Modifier | mD |

Disengage is a defense allowing to move half the normal movement speed in the current turn. It automatically succeeds if the opponents are not trying to attack the character using it.
On failure, the disengagement fails and the character cannot move.
If the contest succeeds, the character can move even if other subsequent attacks succeed.

## Archery {#BaM-s-archery}

|   |   |
|------|------|
| Cost | 6 CP |
| Modifier | mD |
| Dominance | 4 |

This is the base style (and skill) needed to use bows, crossbows and similar projectile
weapons.

Unless differently specified, all attacks from *archery* deal __cut__ damage,
and the range depends on the used weapon.

The number of maneuvers the character can use per round depends on the level of Archery:

| Level | Maneuvers |
|-----|---|
| 1-9 | 1 |
| 10-16 | 2 |
| 17+ | 3 |

### Aim {#BaM-s-aim}

|   |   |
|------|--------|
| Type | Action |
| Prereq | Archery 3 |

Take a maneuver to improve the next attack, giving it a modifier of +1.
It can be repeated any number of times within a single turn, but the
modifier is applied only to the very next Shoot.

### Brawl {#BaM-s-brawl}

|   |   |
|------|------|
| Cost | 2 CP |
| Modifier | mS |
| Dominance | 1 |

Brawl is the style of fight with bare hand and feet, without a specific
preparation. It’s often used in tavern and bar fights, and can also be
useful in other combat situations.

Every human or humanoid character has access to brawl.

Unless differently specified, all attacks from *brawl* deal __blunt__
damage, and all the maneuvers are melee.

The number of maneuvers the character can use per round depends on
the level of brawl:

| Level | Maneuvers |
|-----|---|
| 1-5 | 1 |
| 5-10 | 2 |
| 11-15 | 3 |
| 16+ | 4 |

### Block {#BaM-s-brawl-block}

|   |   |
|------|---------|
| Type | Defense |
| Modifier | mS |
| Prereq | Brawl 1 |
| DR | -1 |

Block an incoming blow with the lower part of the arms (similar to the guard
in a boxe match).

Can't be used against any weapon, unless the arms are given an amrour
capable to completely block the attack; for example, a character arm might be
stuck to an iron rod; in this case, the character can use __block__ against i.e.
a sword or a mace.

## Concentration {#BaM-s-concentration}

|   |   |
|------|------|
| Cost | 2 CP |
| Modifier | mW |
| Dominance | 1 |

Concentration is a simple mind-oriented fighting style, which can be seamlessly
integrated in a traditional melee fight. It covers the role of the default
combat style for mental combat, analogous to brawl for physical combat. In a
world where mental fight is a thing, everyone should be able to mind meld, like
everyone is able to brawl in physical worlds.

While other fighting styles in the manual are realistic, this requires a setting
specifically supporting mind powers. However, the style is suitable for sci-fi
settings to handle fights between AIs, robots, hackers and so on, with
low-resolution.

The number of maneuvers the character can use per round depends on the level
of Concentration:

| Level | Maneuvers |
|-----|---|
| 1-7 | 1 |
| 8-13 | 2 |
| 14+ | 3 |

### Alien Thoughts {#BaM-s-concentration-alien-thoughts}

|   |   |
|------|--------|
| Type | Attack |
| Modifier | mI |
| Prereq | Concentration 1 |
| DR | -1 |
| Damage Type | Maddening |
| Damage | __SM__+mI |

The attacker projects alien, irrational thoughts in the defendant’s,
in order to cause maddening.

## Firearms {#BaM-s-firearms}

|   |   |
|------|------|
| Cost | 6 CP |
| Modifier | mD |
| Dominance | 7 |

This combat style is the bases for using firearms. In general, the weapon gives
the modifier for the attack roll and determines the range, but the damage
generated is usually the same. Firing with a pistol six feet away from the
target or with a precision gun from 90 feet afar yields mostly the same results,
provided you can hit the mark.

All the damage type caused by *firearms* is of __piercing__ type, unless differently
specified.

Everyone can shoot with a firearm; as such, the firearms style is available to
anyone, but most maneuvers have a relatively high pre-requisite.
The number of maneuvers the character can use per round depends on the level of
Firearms:

| Level | Maneuvers |
|-----|---|
| 1-5 | 1 |
| 5-10 | 2 |
| 11-15 | 3 |
| 16+ | 4 |

### Aim {#BaM-s-firearms-aim}

|   |   |
|------|--------|
| Type | Action |
| Prereq | Firearms 3 |

Take a maneuver to improve the next attack, giving it a
modifier of +1. It can be repeated any number of times within a 
single turn, but the modifier is applied only to the very next 
Shoot or Aimed Shoot, either within the same turn or in the very next one. 

No other action can be performed while aiming, and performing another
action will discard the modifiers achieved.

## Full Contact {#BaM-s-full-contcat}

|   |   |
|------|------|
| Cost | 3 CP |
| Prerequisite | **Brawl** 4 |
| Modifier | mS |
| Dominance | 3 |

An advanced version and extension of Brawl. While still not being a full-fledged
martial art, it’s a style of combat that requires dedication, and if
professionally trained, can be quite effective even against more famous martial
arts.

A character using Full Contact can use all the maneuvers from *Brawl* under
*Full Contact* instead (whichever has the higher level).

All damage from *full contact* is of __blunt__ type, unless differently
specified.

A well trained full-contact fighter is as dangerous as an armed opponent.
A character using Full Contact can use an extra maneuver from this style each
turn.

For example, a character with Full Contact 10 has two maneuvers it can
chose from either Full Contact or Brawl, plus one from Full Contact only.

| Level | Maneuvers |
|-----|---|
| 1-5 | 1 |
| 5-10 | 2 |
| 11-15 | 3 |
| 16+ | 4 |

### Counter Punch {#BaM-s-full-contact-counter-punch}

|   |   |
|------|---------|
| Type | Defense |
| Modifier | mS-2 |
| Prereq | Full Contact 3 |
| DR | -2 |
| Damage | __SM__-1 |
| Condition | __(Stun 2)__ |

A counter-attack performed on melee attacks. Tries
to evade the incoming blow and use the opening to strike
with a punch on the higher part of the body. Has modifier -2 against
smaller creatures (it’s harder to find a spot to counter-attack
them with a punch).

Ineffective against non-melee and animal attacks.

## Knife Fight {#BaM-s-knife-fight}

|   |   |
|------|------|
| Cost | 5 CP |
| Modifier | mD |
| Dominance | 4 |

Fighting with knives and very short swords has different mechanics than the ones used when wielding a longer blade. Basically, it’s like having a fist armed with a single fang.
While the weapon themselves could be less effective than longer ones, the style itself can be extremely effective in every scenario.
Knife fighting is particularly adequate for characters with a high dexterity.
The number of maneuvers the character can use per round depends on the level of Kinfe Fight:

(dt ac_knife_fight_levels)
[["Level", "Maneuvers"],
["1-5", 1],
["6-10", 2],
["11-15", 3],
["16+", 4]
])

### Backstab {#BaM-s-knife-combat-backstab}

|   |   |
|------|--------|
| Type | Attack |
| Modifier | mD-2 |
| Prereq | Knife Fight 6 |
| DR | -2 |
| Damage | __SM__+6 |
| Condition | (__Deadly__) |

Assail an opponent from behind and deliver a potentially deadly blow.
The character must be positioned behind a target to be able to
perform this move. On a critical success, the target receives a _deadly
wound_.

## Swordfight {#BaM-s-swordfight}

|   |   |
|------|------|
| Cost | 6 CP |
| Modifier | mS |
| Dominance | 6 |

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

The number of maneuvers the character can use per round depends on the level
of Sword Fight:

| Level | Maneuvers |
|-----|---|
| 1-6 | 1 |
| 7-11 | 2 |
| 12-15 | 3 |
| 17+ | 4 |

### Cleave {#BaM-s-swordfight-cleave}

|   |   |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |
| Damage | __SM__+6 |
| Condition | (__Stun 2__) |

A vertical stroke, leveraging on the strength of the weapon welder.
A critical success stuns the opponent for 2 turns.

# Equipment {#BaM-gen-equipment}

## Adventuring Equipment {#BaM-gen-adventuring-equipment}

TODO

## Armours {#BaM-gen-armours}

Armours provide damage mitigation against some specific damage types. Naturally, the damage mitigation applies to the part of the body where the armour is applied.
The following table is a generic guide that indicates the type of material of which armours are built, their approximate weight  in pounds, the cut, blunt and piercing damage mitigation and an approximate cost. The weight refer to the material applied to a body armour; to get the weight of arm and leg armour divide by half, and for an helmet divide by four.

| Material Type      | Weight       | Dominance    | Cut          | Blunt        | Piercing     | Cost        |
|:-------------------|-------------:|-------------:|-------------:|-------------:|-------------:|------------:|
| Heavy Garment (1)  | 2            | 0            | 1            | 0            | 1            | 200$        |
| Kevlar             | 2            | 5            | 5            | 3            | 6            | 800$        |
| Bullet-proof Armor | 12           | 5            | 6            | 4            | 7            | 500$        |
| Meta-material (2)  | 6            | 6            | 4            | 6            | 3            | 1200$       |
| Energy Shielding (3) | 0          | 7            | 6            | 7            | 5            | 4000$       |
| Leather            | 8            | 1            | 3            | 1            | 2            | 40$         |
| Ring Mail          | 10           | 2            | 3            | 2            | 1            | 80$         |
| Chain Mail         | 14           | 2            | 3            | 1            | 2            | 150$        |
| Scale Mail         | 15           | 3            | 4            | 2            | 3            | 400$        |
| Thin Plate (4)     | 18           | 4            | 5            | 3            | 4            | 600$        |
| Heavy Plate        | 24           | 5            | 6            | 4            | 5            | 800$        |

(1) Normal clothing doesn’t provide any mitigation, but heavy, multi-layer garment (i.e. overcoat, jacket, gilet, shirt and underwear) do.
(2) Gel-like material reactive to sudden shock.
(3) Just indicative; can be anything, depending on the technology. 
(4) Includes military metal helmets.

## Weapons {#BaM-gen-weapons}

Weapons are either used unskilfully, using any one of the Generic Combat Skills, or through the appropriate combat style. The default damage (and often, damage type) caused by the weapon is already accounted for in the combat style; for example, Firearms/shoot causes a higher damage than Brawl/punch because guns are more lethal than bare hands.
However, some special weapon (i.e. magic swords, experimental rifles etc.) might give their wielder a modifier either to the attack or defense rolls, or solely to the damage caused once a hit is scored.
In the following table, the weight is the typical weight of for the given type of weapon, the range either the throwing distance or the range of the projectiles, in feet, and the cost is an indicative cost for a normal weapon of that kind.

| Weapon Type        | Weight             | Range              | Cost              |
|--------------------|--------------------|--------------------|-------------------|
| Knife              | 1                  | 10                 | 20$               |
| Sword              | 3                  | -                  | 400$              |
| Mace               | 6                  | -                  | 100$              |
| Throwing Knife     | 0.2                | 18                 | 5$                |
| War Hammer (*)     | 12                 | -                  | 300$              |
| Two Handed Sword (*) | 8                | -                  | 600$              |
| Shield             | 6                  | -                  | 80$               |
| Pistol (revolver)  | 1                  | 60                 | 600$              |
| Pistol (Semi-auto) | 1                  | 60                 | 800$              |
| Rifle              | 4                  | 90                 | 1200$             |
| Sniper’s rifle     | 6                  | 120                | 1800$             |
| Short Bow          | 1                  | 30                 | 40$               |
| Bow                | 1                  | 45                 | 80$               |
| Long Bow           | 2                  | 60                 | 120$              |
| Crossbow           | 2                  | 40                 | 150$              |
| Heavy Crossbow     | 4                  | 60                 | 200$              |

(*) Two handed weapons.