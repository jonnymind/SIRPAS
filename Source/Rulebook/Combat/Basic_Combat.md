## Basic Combat

Sirpas _basic combat_ is a sub-system employed when two or more parties are
fighting each other.

### Combat Turns

Combat is divided in turns. Normally, characters can perform just one action
per turn, but certain skills and advantages grant the ability to perform more
maneuvers.

The length of the turn depends on the settings: it might be one second in a Wild
West setting where gunslingers are fighting, ten seconds when considering melee
fights in medieval settings, one nanosecond in fights between AIs, one minute in
fights between giant robots or starships and so on.

For most situations, you’ll want to consider the length of a combat turn being
10 seconds.

### Combat order

Each turn, a ranking throw called **combat order** is performed to determine the order in which
every participant takes action. The attribute used for the ranking is decided
by the **GM**, or it can be specified by the modules or adventure settings. 

Once the **combat order** is established, each character takes action in turn,
choosing what action they want to perform:

* Attack
* Wait for a better moment
* Move
* Switch Weapon
* Use an item
* Use a non-combat skill

A character can use only a single combat skill during a turn, but some combat skills
provide multiple _actions_, which means they can be used multiple times per turn to
defend or attack.

A character can use the combat skill for defending against an attack also if it not
its turn; however, when its turn comes, it will be able to attack only if it has some
actions left unused.

A character might also decide not perform any action when its turn comes; if it does so,
it can interrupt any other action performed later on by characters down the initiative
ranking, or eventually use a defense to respond to a later attack.

### Instinctive Defense

In some situations, the defender is aware of the incoming attack (i.e. has seen
the attacker and is ready to receive the blow) but can’t use any skill as a defense. 

Typical reasons are:
* The character already used all the actions at their disposal in a combat
  turn and can’t react any more
* The defender doesn't have a proficiency in the skill used by the attacker,
  and is just reacting instinctively.
* The rules explicitly prohibit the use of other defenses (i.e. when disengaging
  from the combat).

In those cases, provided the defender is at least aware of the attacks, it can use
an appropriate **generic combat skill** as a defense. Some **GCS** are meant specifically
to be used as instinctive defense, and may have a better base than more specific ones.
For example, a module may have both **dodge** and **slash** as **GCS**, with **dodge**
being a skill specific for defense only, and with a better base value than **slash**.

### Mixing different skill ranges

In some cases, it is necessary to mix differently ranged skills as attack
and defenses. For example, an archer may be attacked in melee range by
someone swinging a sword; similarly, a martial artist may need to dodge
an arrow. 

The situation is resolved as follows:

* When the opponents are in *close quarters*,
  **ranged** skills have a -2 modifier when defending against **melee** attacks. 

* When opponents are are not in *close quarters*,
  **melee** skills have a -1 modifier when defending 
  against **ranged** attacks per every two times of the *close quarter* distance.

The *close quarter* it's the distance that an average fighter can jump and perform
a melee attack in one swoop. This is normally 6 feet, but may be different in settings
where the characters have superpowers that allow for faster movement (i.e. in an
adventure about vampires), or different sizes (i.e. in battles between giant robots).

>For example, a martial artist using defending against a
sharp shooter standing between 6 and 12 feet away would have a penalty of -1;
at a distance of 60 feet, the penalty would be -5 (60/6/2 = 5). This can seem
a lot, but ranged skills have penalties for long range shot and range limits
already: no one can hope to perform a valid melee defense against a sniper
hidden on the next hill.

**Metaphysical** skills cannot be use to defend against **melee** or **ranged** skills, and
the other away around, **melee** and **ranged** skills cannot be used to defend
against a **metaphysical** attack.

### Ranged attacks falloff

Attack with ranged weapons receive the following modifier, which depends on the
distance to the target:

$(include /tables/ranged_falloff.md)

### Cover

Cover provides a modifier to the defense against ranged attacks.

$(include /tables/cover.md)

If a character has _full coverage_ and doesn't attack, nor moves, nor doesn't
perform any action that exposes it, it cannot be attacked with a ranged weapon.
The defense is required only if the character is actually performing an action
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

$(include /tables/tactical_situation.md)

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
* __Tiredness__: The characters are particularly tired, i.e. because they
couldn't rest after previous fight, or because being forced to fight after a
long march, or for having run because of a chasing.
* __Demoralized__: The characters are demoralized because of having lost
an important target already, their leader, the location they were meant to
defend, etc.

### Automatic Attack

In some case, the target of an attack is unsuspecting or unable to react:
for example, the target of a hidden sniper, or a sleeping victim.

In those situations, the combat is not resolved through a contest; the attacker
rolls on the attack skill, with the following difficulty table:

$(include /tables/automatic_attack.md)


### Attack and Defense

When an attack is declared, the target (or targets) can use a defense, either
by using a specific combat skill or a _generic defense_.

The attacker and all the affected targets perform a Contest using their
chosen skill as a base.

The attacker rolls and adds the value of the skill, as for any contest.

Determined the value for the attack roll, each defender performs its defense,
rolling on the chosen defense skill.

A draw means that neither the attack, nor the defense have been successful.
A successful attack delivers a damage to the target. A successful defense
might have an effect that depends on the used skill (it might also deliver
a damage to the attacker).

### Moving during combat

It is possible to move during combat at a speed that can be reasonably covered
in a combat turn. Modules can define the speed depending on module-specific attributes.

Opponents targeting the character (either because they are nearby in melee,
or because they have aimed at them previously) can use an attack against
them to prevent them from moving, provided they still have actions 
available in the combat round, and are in range of any part of the path 
of their target. In that case, the moving character must successfully 
defend using **disengage** as the only possible defense. 

The **disengage** defense is either a viable defense of choice with -4 penalty,
or a specific check/attribute defined by the modules.

If it fails, other than receiving normal damage, it also stays unmoved, and
the action is nevertheless consumed.

> If a character plans to move and there isn't any urgency to do that, it's
better to wait for any opponent that might target them to use up all their
attacks, so to be able to move freely.

### Damage

Damage is measured in *damage points* (**DP**), and is accounted as the established by the
__injury__ rule.

The damage delivered by a successful attack (or defense) is specified in the
skill description under the _base damage_ voice; usually, it's computed
adding the success margin of the contest to some attribute based modifier.

The _dominance_ of the skill, and eventually of the used weapon, is
added to the _base damage_; other modifiers (i.e. temporary magic
incantation) might further be applied. The final total damage delivered
is called _active damage_ (__AD__).

The character receiving the damage computes its _damage mitigation_ (__DM__)
by adding _passive defenses_ that can affect the damage source (i.e. armours),
and eventually _active defenses_ they might use.

Finally, the target character receives a number of __DP__ = __AD__ - __DM__.
This damage is accounted as specified by the [injury and damage](#injury-and-damage) rule.

### Critical Rolls

A critical success doubles the value of the _success margin_ when computing
the _active damage_. When the damage roll doesn't involve the **SM** in the
computation of the **AD**, a critical result adds 4 **DP**.

> Notice that some defenses might generate a damage too.

A critical failure indicates a failure even when the roll itself would
indicate a success. For example, suppose an attacker with __brawl__ 16 against
a defender with __archery__ 5. If the attacker rolls 3, which is a critical
failure, the attack fails even if 16+3 would be above the archer's roll.

If both the attacker and defender roll a critical failure, the roll result
(with the respective modifiers) is considered: critical failures on both sides
elide each other.
