## Basic Combat

Sirpas _basic combat_ is a sub-system employed when two or more parties are
fighting each other.

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

Each turn, all the participants roll a ranking on the skill called
[__initiative__](#Initiative).

Characters decide the action they want to perform proceeding in ranking order:

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
[Generic Combat Skills](#Generic_Manoeuvres) to resist an attack, no matter how
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

### Skill Range

Combat skills are divided into _melee_, _ranged_ and _metaphysical_.

* _Melee_ skills work when the combatants are in close range, and can
   physically harm each other without any projection.
* _Ranged_ skills use a weapon, a projectile or any mean to physically
   project a harmful device or source of energy towards a target. Skills of
   magical nature might be ranged if they magically create a projectile, ray
   of energy or any physical mean to harm a target.
* _Metaphysical_ skills require their user to know where a target is in order
   to direct the attack, but they have no physical range. The target could be
   on another planet, as long as the user has a mean to see, feel or simply
   know _instantly_ about it.

### Mixing different skill ranges

In some cases, it is necessary to mix differently ranged skills as attack
and defences.

For example, an archer could be overcome by a
soldier armed with a sword. It might then be be forced, or simply prefer,
to use its _archery_ skill as its defence.

Similarly, a martial artist could spot a shooter, and decide to use its
_full contact_ skill to try and avoid to be hit.

When defending against _ranged skills_, a _melee_ skill receives a modifier of
+1 when defending in _melee_ range (i.e. if they are in close quarters with
the attaccker); if not, -1 for each 18 feet of distance from the source.

>For example, a martial artist using _full contact_ against a
shooter 40 feet away would have a penalty of -2. If the attacker were
in melee range, the modifier would be +1, and six feet away there wouldn't
be any modifier.

When defending against _melee_ skills, a _ranged_ skill gets a penalty of -3.

_Metaphysical_ skills cannot be use to defend against physical skills, and
the other away around, _melee_ and _ranged_ skills cannot be used to defend
against a _metaphysical_ attack.

### Ranged attacks falloff

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

The attacker and all the affected targets perform a Contest using their
chosen skill as a base.

The attacker rolls and adds the value of the skill, as for any contest.

Determined the value for the attack roll, each defender performs its defence,
rolling on the chosen defence skill.

A draw means that neither the attack nor the defence have been successful.
A successful attack delivers a damage to the target. A successful defence
might have an effect that depends on the used skill (it might also deliver
a damage to the attacker).

### Damage

Damage is measured in **DP**, and is accounted as the established by the
__injury__ rule.

The damage delivered by a successful attack (or defence) is specified in the
skill description under the _base damage_ voice; usually, it's computed
adding the success margin of the contest to some attribute based modifier.

The _dominance_ of the skill, and eventually, of the used weapon is then
added to the _base damage_; other modifiers (i.e. temporary magic
incantation) might further be applied. The final total damage delivered
is called _active damage_ (__AD__).

The character receiving the damage computes its _damage mitigation_ (__DM__)
by adding _passive defences_ that can affect the damage source (i.e. armours),
and eventually _active defences_ they might use.

Finally, the target character receives a number of __DP__ = __AD__ - __DM__.
This damage is accounted as specified by the [_injury and damage_](injury-and-damage) rule.

### Critical Rolls

A critical success doubles the value of the _success margin_ when computing
the _active damage_. When the damage roll doesn't involve the **SM** in the
computation of the **AD**, a critical result adds 4 **DP**.

> Notice that some defences might generate a damage too.

A critical failure indicates a failure even when the roll itself would
indicate a success. For example, suppose an attacker with __brawl__ 16 against
a defender with __archery__ 5. If the attacker rolls 3, which is a critical
failure, the attack fails even if 16+3 would be above the archer's roll.

If both the attacker and defender roll a critical failure, the roll result
(with the respective modifiers) is considered: critical failures on both sides
elide each other.
