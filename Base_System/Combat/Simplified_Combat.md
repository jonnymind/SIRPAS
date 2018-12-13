## Simplified Combat

TODO

The effect of the damage is computed as described by the
[_injury and damage_](#injury-and-damage) rules.


### Combat Turns

Combat is divided in turns. Normally, characters can perform just one action
per turn, but certain skills and advantages grant the ability to perform more
manoeuvres.

The length of the turn depends on the settings: it might be one second in a Wild
West setting where gunslingers are fighting, ten seconds when considering melee
fights in medieval settings, one nanosecond in fights between AIs, one minute in
fights between giant robots or starships and so on.

For most situations, you’ll want to consider the length of a combat turn being
10 seconds.

### Initiative

Each turn, all the participants roll a ranking on
[__initiative__](#Initiative).

Character decide the action they want to perform proceeding in ranking order:

* Attack
* Wait for a better moment
* Move
* Switch Weapon
* Use an item

A character can use only a single combat skill during a turn, but some skill
provides multiple _actions_, which means it can be used multiple times per turn.
Any character must decide if it wants to use its skill actions for attack, defence
or both.

When its turn in ranking come, provided a character has still some actions to use
with the chosen skill, they can perform an attack.

It is always possible to use one of the _generic defences_ from
[Generic Manoeuvres](#Generic_Manoeuvres) to resist an attack, no matter how
many actions have been performed with other skills.

### Instinctive Defence

In some situations, the defender is aware of the incoming attack (i.e. has seen
the attacker and is ready to receive the blow) but can’t use any defence. One
reason might be that it already used all the defence at its disposal in a combat
turn and can’t react any more, or it might be that it has no proficiency in that
kind of combat — this often happens with metaphysical attacks directed at
targets that don’t have a specific skill to use in response — or in case it’s
explicitly dictated by the rules — for example, defending against any attack
after using disengage.

In those cases, provided the defender is at least aware of the attacks, it can
use either an [instinctive defence](#Instinctie Defence)
(against physical attacks) or a [willpower defence](#Willpower Defence)
(against mind attacks).

### Moving during combat

It is possible to move during combat at the speed indicated in the
[__dexterity__](#Dexterity) table.

Opponents targeting the character (either because they are nearby in melee,
or because they have aimed at them previously) can use an attack against
them to prevent them from moving.

The moving character must successfully defend with the
(__disengage__)[#Disengage] generic manoeuvre. If they fail, other than
receiving normal damage, they will also fail to move.

> If a character plans to move and there isn't any urgency to do that, it's
better to wait for any opponent that might target them to use up all their
attacks, so to be able to move freely.

### Ranged weapons falloff

Attack with ranged weapons receive the following modifier, which depends on the
distance to the target:

$(include /Base_System/tables/ranged_falloff.md)

### Cover

Cover provides a modifier to the defence against ranged attacks.

$(include /Base_System/tables/cover.md)

If a character has _full coverage_ and doesn't attack, nor moves, nor doesn't
perform any action that exposes it, it cannot be attacked with a ranged weapon.
The defence is required only if the character is actually performing an action
that would expose part of it out of the cover.

A _partial cover_ is a high wall, large tree or column, three feet rock, and
anything that could cover part of the body from the aim of the opponent.

A character _on the ground_ is completely squashed, and can only use weapons
and skill that might be used from this position (i.e. firearms).

A _precarious_ cover is something providing just visual obfuscation, like a
bush, or very partial cover, as a think tree trunk.

### Tactical situation

Some tactical situations during combat provide modifiers to the attack
rolls.

$(include /Base_System/tables/tactical_situation.md)

* __Surprise__: one group surprises the other, which wasn't ready to fight.
The surprise advantage lasts the first combat turn only.
* __High Ground__: One group is fighting from uphill, or in an otherwise
greatly advantageous position.
* __High Morale__: The party has a high morale because of a specific fact;
for example, because there is an important target in sight (the exit of a
dungeon, the treasure or person they were searching for etc), or because of
a stretch of boasting victories.
* __Desperate__: The party is in a desperate situation, and had the time
to contemplate defeat and come with terms to that before the fight. It might
depend of a perceived superiority of the opponents, or because all food was
depleted and a breakthrough is necessary for survival, etc.
* __Tiredness__: The characters are particularly tired, I.e. because they
couldn't rest after previous fight, or because being forced to fight after a
long march, or for having run because of a chasing.
* __Demoralised__: The characters are demoralised because of having lost
an important target already, their leader, the location they were meant to
defend, etc.

## Automatic Attack

In some case, the target of an attack is unsuspecting or incapacitated to react:
for example, the target of a hidden sniper, or a sleeping victim.

In those situations, the combat is not resolved through a contest; the attacker
can simply roll on the attack skill, with the following difficulty table:

$(include /Base_System/tables/automatic_attack.md)





### Attack and Defence

When an attack is declared, the target (or targets) can use a defence, either
by using a specific combat skill or a _generic defence_.

The attacker and the defender perform a Contest using their chosen skill as a
base. The attacker will add the modifier from the _dominance_ of its combat skill,
and if any, of its weapon; similarly, the defender will add the _dominance_
of the selected skill, and eventually, of its armour, to the defence roll.

> Note: you can ignore the skill _dominance_ if attacker and defender use
the same skill (or if the _dominance_ is the same).

### Damage

If the attacker succeeds, it wounds the target. The seriousness of the wound
depends on the success margin.

$(include /Base_System/tables/base_injuries.md)

### Resist Damage

The defender can degrade one injury per turn to the lower level (or avoiding
completely light wounds) by performing a check on [__health__](#health), for
physical attacks, or [__equilibrium__](#equilibrium) for mental attacks,
with the following modifiers:

$(include /Base_System/tables/base_resist_injuries.md)

### Damage computation

The damage caused by a successful attack is determined by the _success margin_
of the attack, plus some factor specified in the combat skill description.

If the attack was a was a _critical success_, or the defence was a
_critical failure_, the damage portion caused by the _success margin_ is
doubled.

This amount is then reduced by the passive defence offered by the defender,
which involves its armour and other means, as described by the _injury_ rules.
