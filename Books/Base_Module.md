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

## Main and primary attributes

Every character has the following **Main** attributes:

* Body (**B**): The physical aspect of the character. Body **primary** attributes are:
  * Strength (**S**): raw physical power;
  * Dexterity (**D**): speed, precision and control over actions performed with the body;
  * Health (**H**): Resilience against fatigue, injury and illness.
* Mind (**M**): describes the mental prowess of a character. Mind **primary** attributes are:
  * Will (**W**): strength of conviction and assertiveness.  
  * Intelligence (**I**): ability to understand and solve complex problems; mental flexibility.
  * Equilibrium (**E**): resilience to mental strain, stress and madness.

The [**body**](#body) primary provides also the **base value** of 
[**strength**](#strength), [**dexterity**](#dexterity) and (**health**)[#health]. This means that
the value of **body** is also the *default* value for the these dependent primaries; you can
then train each of them separately using *primary tokens*, and improve them over their base
value, but if you train the main trait **body**, all its dependent attributes will grow with it.

Similarly, [**mind**](#mind) provides the base value for [**will**](#will), [**intelligence**](#intelligence) and [**equilibrium**](#equilibrium).

In turn, the primaries are themselves base for other attributes and skills.

There is more to be known on each of those attributes, but you can [jump into action](advantages) 
from here.

## Body

| <!-- --> | <!-- --> |
|----------|------|
| Category | Main |
| Base | 3 |

The Body (**B**) is a value that describes your overall physical prowess in terms of
bodily strength, resilience to prolonged efforts, recovery speed, resistance to
illness and so on. For humans, it is measured in the range between 3 and 18 (the
possible outcomes of 3d6). Most adult characters score in the range between 9
and 12, with 18 representing a person with the best possible body (rarely if
ever ill, strong as the strongest wrestler or weight lifter, moving as swift as
a record runner and able to run as long as a marathon champion — all at the same
time), and 3 representing the weakest possible fully formed and barely
functional body.

## Mind

| <!-- --> | <!-- --> |
|----------|------|
| Category | Main |
| Base | 3 |

The Mind (**M**) is the overall score of mental abilities in terms of intelligence, 
creativity, will power, mental sanity, depth of knowledge and so on. 
A mind level 3 represents a character that is barely functional as an autonomous person (or
creature) in the reference setting, while a 18 represents a character maximally intelligent, 
penetrating, knowledgable, sane and wise. The vast majority of characters (or heroes)
in the reference setting will have a mind between 9 and 12.

## Strength

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | B |

Strength (**S**) is the attribute measuring a character physical strength. 
In the default setting, it also indicates how much weight the character 
can transport without being fatigued, or the amount of weight it can 
carry without being slowed down, or that it can lift. There are different
tiers  used in various occasion, all multiple of the value of Strength in 
pounds:

| Weight             | Transport          | Lift               | Movement           |
|:------------------:|--------------------|--------------------|--------------------|
| <= *S* x 1         | Trivial            | Normal             | Normal             |
| <= *S* x 2         | Easy               | Difficult          | Normal             |
| <= *S* x 3         | Normal             | Hard               | 3/4                |
| <= *S* x 4         | Difficult          | Very Hard          | 2/3                |
| <= *S* x 5         | Hard               | Very Hard          | 1/2                |
|  > *S* x 5         | Very Hard          | Very Hard          | 1/3                |

The name of the tiers match the names of the skill difficulty levels, 
as they are directly applied as a difficulty level in various checks.
However, they also define other effects that are not directly related with skills; 
for example, the transport weight tier is applied directly to the combat movement: 
a character transporting  a "very hard" weight has its movement cut to one third 
of it normal movement

## Dexterity

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | B |

Dexterity (**D**) expresses the ability to control one’s own body.
Eye-hand coordination, agility, reaction times and rapidity are all 
components of dexterity. A dexterity of 3 indicates sluggish reaction times, 
18 indicates a martial-art or olympic gymnast level of dexterity, 
with the vast majority of common people stacking around 10-12.

The *dexterity* indicates also the base movement speed of a character.
The actual speed depends on what a character actually is; a cyborg with
**D**12 will probably be faster than any human with **D**18. 

The following table is for humans; you can adapt it to other races
by using the *speed coefficient* of that race (for humans, it's 1).

| Dexterity | Sprint: Ft. x sec | Run: Ft. x sec | Ft. x turn |
|----------:|------------------:|---------------:|-----------:|
|         3 |                 3 |              1 |         10 |
|         4 |                 7 |              2 |         11 |
|         5 |                10 |              3 |         13 |
|         6 |                13 |              4 |         15 |
|         7 |                15 |              5 |         18 |
|         8 |                17 |              7 |         22 |
|         9 |                19 |              9 |         26 |
|        10 |                20 |             11 |         28 |
|        11 |                21 |             12 |         30 |
|        12 |                23 |             13 |         33 |
|        13 |                25 |             14 |         36 |
|        14 |                28 |             16 |         40 |
|        15 |                31 |             18 |         45 |
|        16 |                33 |             20 |         52 |
|        17 |                37 |             23 |         57 |
|        18 |                42 |             27 |         63 |

Notice that the speed for combat turn is not necessarily the sprint speed,
as movement during combat is limited by other factors. Also, the combat
turn here is the standard 10 seconds combat turn of the the base system;
other systems might redefine the duration of a combat turn (and how *dexterity*
works in those contexts).

## Health

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | B |

Health (**H**) represents the resistance to fatigue, illness and polluted 
environment (including allergenic agents). It's used to determine how many
injuries can be withstood before being incapacitated,
and gives the base for all physical resistance skills.

## Will

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | M |

Will (**W**) is the power of the mind to focus on a certain task, 
perform prolonged mental activity, keep determination in 
adverse situations and so on. It can be roughly thought as the 
equivalent of the strength (**S**) in the mind realm.

## Intelligence

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | M |

Intelligence (**I**) is the ability to understand and solve complex problems, 
comprehend difficult study subjects, see through schemes and machinations 
etc. As it measure the flexibility of the mind processes, it can be thought 
as the dexterity (**D**) of the mind.

## Equilibrium

| <!-- --> | <!-- --> |
|----------|---------|
| Category | Primary |
| Base | M |

Equilibrium (**E**) is the stability of the mind, 
or basically the equivalent of its health (**H**). It indicates 
how much mental strain a person can take before being debilitated; 
of course, it is important in those settings where attacks are delivered 
to the mind instead of the body: fantasy, sci-fi and horror settings 
can present as many dangers for the mind as for the body, or more.

Hence, it forms the base of all the mental resistance skills.

## Checks

> For the full description refer to the Rulebook **[checks]($RulebookAddress/#checks)** section.

Attempting any non-trivial action requires performing a *check* on a given attribute
related to the attempt to perform. For example, trying to push a cart stuck in the mud
may require a *check* on **strength**. 

Checks (abbreviated as **CHK**) are resolved by adding the value of a throw of three 
6-faced die (3d6) to the value of the attribute under check, and achieving total result 
of **21** or more, called **Success Level** (**SL**). The **SL** may be different when
the actions to perform are  easier or harder than normal. Other modifier can be
applied as the situation requires; for example, being wound makes every action harder,
applying a fixed penalty of -1 to -10 points depending on the severity of the wounds.

Each check has a **Success Margin** (**SM**), that is the difference between the
total value of the dice throw and the **SL**. On success, the **SM** is zero or
greater; on failure, the **SM** is negative.

When two characters attempt to perform the same action at the same time,
or try to stop an opponent from performing an action using another skill, 
a **Contest** happens. In this case, the success margin is the difference 
between the highest score and the other.

Finally, when there are multiple characters trying to best each other at a specific
skill (e.g. running up a hill), a **Ranking** (**RNK**) is performed. In rankings,
the winner has a success margin of zero, while all the others have a negative **SM**,
that is the distance from the first. When whole parties try to best each other,
a **Multiranking** (**MRNK**) takes place; each party performs a ranking, then
the scores of the same ranks in each party is compared (first against first,
second against second and so on); the winner party is the one with the most 
winning ranks.

# Advantages

Advantages special conditions that apply to the character in general 
or to a specific skill in particular, and that have a direct effect 
on some game mechanics.

Advantages can be bought for a certain number of **training tokens**
of a certain type; the more powerful the advantage, the more high
level the training tokens needed to train a point.

While most advantages are simply possessed by a character or not, 
some can have different levels. In that case, the cost of
each ulterior point is the base cost plus one token of the same type
per level. For example, **Survival Instinct** can have a level between 1 and 4, 
each granting a higher modifier. The first level costs 3 **TT**/*Normal*; 
this means that level 2 costs 3 + 2 = 5, level 3 costs 3 + 3 = 6
and level 4 costs 3 + 4 = 7 **TT**/*Normal*.

Some advantage could have a pre-requisite that must be fulfilled in order to be acquired. 
For example, they could require having already acquired another advantage, 
or having a certain attribute at a minimum set score.

It is also possible to acquire advantages for free, as a special reward for
a particularly brilliant deed; also, if an advantage is not needed anymore, 
it can be removed, and half its total cost will be refunded (rounded up).

For more details on the advantage system, consult the 
[advantage system in the rulebook](https://jonnymind.github.io/SIRPAS/Rulebook.html#advantages-and-disadvantages), 

## Foudnational advantages


- [Battleproof](#battleproof)
- [Born in a Mourning Hall](#born-in-a-mourning-hall)
- [By the skin of one's teeth](#by-the-skin-of-one's-teeth)
- [Combative spirit](#combative-spirit)
- [Deep Mind](#deep-mind)
- [Easygoing](#easygoing)
- [Elemental Resistance](#elemental-resistance)
- [Expertise](#expertise)
- [Fast Paced](#fast-paced)
- [Hard Skin](#hard-skin)
- [Hard to Die](#hard-to-die)
- [Keen Eye](#keen-eye)
- [Lucky](#lucky)
- [Mastery](#mastery)
- [Medical knowledge](#medical-knowledge)
- [Natural](#natural)
- [Nimble crowder](#nimble-crowder)
- [Offensive flow](#offensive-flow)
- [Survival instinct](#survival-instinct)
- [Total Mitigation](#total-mitigation)

## Battleproof

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Hard |
| Prerequisite | Hard to die |

The character can withstand an additional heavy wound (or the equivalent **IP** from
lighter wounds) from physical sources before
being incapacitated. 

The first physical wound is received during a fight will
automatically heal in 4 hours, even if not treated.

## Born in a Mourning Hall 

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Hard |
| Prerequisite | Hard to die |

The character can withstand an additional heavy wound from mental sources 
(or the equivalent amount of **IP** from lighter wounds) before being
incapacitated, and will not die in case the last wound received was from a
mental source if not treated for 1 hour, regardless of the Injury Points
sustained.

The last mental wound received during a fight will automatically heal in 4
hours, even if not treated.

## By the skin of one's teeth

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Primary |

This advantage allows to resist automatically a single
deadly wound from any source once per day.

The "boundary" of the day is selected by the GM (on player's suggestion),
to be of some significance for the character. It could be the midnight
in a specific place, the sunset, the sunrise, or performing a 
daily ritual specific of the character's creed or habit.

## Combative spirit

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Hard |
| Levels | 3 |

Ignore the negative modifier caused by wounds up to the level of this advantage
(maximum 3).

For example, if a character with **combative spirit** 1 receives a serious wound,
it would normally have a penalty of -1 to any check, but with this advantages
the penalty can be ignored. If another serious wound is received, instead of
the normal -2 penalty, the character will only receive a -1 penalty.

## Deep Mind

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Prerequisite | Mind 9 |
| Cost | 2 TT/Hard |
| Levels | 6 |

The character acquires a passive mitigation against *despair*
and *maddening* damage equal to the level of this advantage.

## Easygoing

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 2 TT/Normal |
| Conflict | Self taught |

Easy checks on the specialized skill get an additional modifier 
of +1, and trivial checks have an additional modifier of +2.

This extends to any kind of checks and skills, including
contests and combat skills.

## Elemental Resistance

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Element type |
| Cost | 2 TT/Hard |
| Levels | 6 |

The character has an innate resistance to elemental attacks of the
specified type. All checks against the element type receive the
level of this advantage as a positive modifier. This includes
defense checks in combat and resistance checks.

This advantage should be granted only in settings where it
makes sense, i.e. as a racial characteristic of a fantasy
race, or for characters genetically engineered, or for
synthetic life forms as androids etc.

## Expertise

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 3 TT/Hard |
| Prerequisite | Easygoing |

This advantage allows to throw 4 die instead of 3 in any check
involving the specified skill, and select the three best rolls out
of them.

This includes combat styles and other combat skills.

The prerequisite for Expertise is to have [Easygoing](#easygoing) on the
same skill.

When targeted with this advantage, some skills also improve their
quality. For example, [first-aid](#BaM-s-first-aid) can normally
cure light wounds only, but if the character has the advantage
*Expertise/First-Aid*, it can also cure serious wounds.

Skills having a special effect when associated with Expertise will describe
it explicitly in their description.

## Fast Paced

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Normal |
| Prerequisite | Dexterity 9 |
| Levels | 3 |

During combat, the character can move for 6 extra feet per turn for 
each level of this skill.

## Hard Skin

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Hard |
| Prerequisite | Body 9 |
| Levels | 6 |

The character gains a passive defense against blunt
and cut damage equal to the level acquired.

## Hard to Die 

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Hard |

When receiving a deadly wound, resistance checks are lowered
by one difficulty level (normal checks become easy, 
easy checks become trivial etc.).

## Keen Eye

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Hard |
| Prerequisite | Dexterity 9 |
| Levels | 4 |

Falloff in ranged combat is increased of 6 ft. per point of this advantage.

## Lucky

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Main |
| Conflict | Unlucky |

The character can re-roll one dice having scored 1 on any check. This is applied 
before any other advantage is considered.

For example: a character with **expert**/*lockpicking* attempts opening a lock.
As they have the advantage [expert](#expert) on lock-picking, they will roll 4d6 
and select the best 3 rolls. 

Suppose the rolls result in 1, 1, 3 and 4. The character can now re-roll one
of the die having rolled 1, scoring a 6 instead, so the rolls are now
1, 3, 4 and 6. **Expert** is applied next, which allows to chose 3, 4 and 6,
for a total of 13.

If the re-rolled dice scores a 1 again, that result must be accepted
as final, unless other rules allows re-rolling a 1 roll for any other
reason.

> For example, this happens in many **resistance checks** against a sudden
death, or when covered by temporary effects that allow to re-roll any
dice scoring 1 indefinitely.

**Notice** that this advantage is opposed to **Unlucky**.

## Mastery

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 1 TT/Primary |
| Prerequisite | Expertise |

Skill Mastery is an advantage that is 
applied on a specific skill. As a pre-requisite,
the character must have already Expertise on the same skill.

Mastery changes all the checks using that skill from a 3d6 
throw to a 2d6+6 (as if one dice is always automatically 
rolling a 6).

Combat styles and other combat skills **can** be targeted by
**mastery**.

## Medical knowledge

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 3 TT/Hard |
| Level | 3 |

The character knows relatively advanced medical treatment techniques.
It can be either a medic, a surgeon or a researcher. Its knowledge is
also correct, regardless of the technological level of the setting. For
example, even if set in a medieval period, the character knows how to
actually cure most illnesses, and the correct prophylactic procedure to
minimize the spread of diseases as the plague.

All checks involving medicines and cures receive a modifier equal to
the level of this advantage

## Natural

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 2 TT/Hard |
| Prerequisite | Easygoing |

The character is a "natural" in a certain discipline: tasks that would
be normally hard for anyone else come much easier to them. 

Difficult checks on the target skill get an additional modifier of +1, 
hard checks have an additional modifier of +2, and Very Hard 
checks have a +3 modifier. Without any other situational modifiers,
the effective modifiers for difficult, hard and very hard checks 
become -2, -4 and -5.

This advantage can target also combat styles and other combat skills.

Before becoming "natural" in a certain discipline, the character must
have acquired the advantage [easygoing](#easygoing) on the same discipline.

## Nimble crowder

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 1 TT/Hard |
| Conflict | Latecomer |

This advantage allows to exchange the place in a [ranking]($RulebookAddress#ranking) or
[multiranking]($RulebookAddress#multiranking) with any character from their party that scored
in a lower position in those rankings where being placed high
is advantageous, or raise in the ranking where higher places
are disadvantageous.

For example, supposed a [simplified combat]($RulebookAddress#simplified-combat)
is taking place, and these are the results:

| Place | Party A | Party B | Winner |
|------:|---------|---------|--------|
| 1     | 18      |  22     | B      |
| 2     | 16      |  18     | B      |
| 3     | 12      |  15     | B      |
| 4     | 9       |  8      | A      |

Party A scores 1 and party B scores 3 points, as party B wins the first three places, while 
party A wins the 4th.

If the character in second place uses the **nimble crowder** advantage to move down at the 3d rank,
now party A and B are in a draw: 18-22 (point B), 12-18 (point B), 16-14 (point A), 9-8 (point A).
With this move, the character that was previously in the second place can improve the tactical
outcome of the battle.

Another usage of this advantage may be during a [basic combat]($RulebookAddress#basic-combat) 
**combat order** ranking, which, in this *foundation*, is performed on the [initiative](#initiative) 
skill. Suppose the outcome of the ranking is as follows.

| Place | Roll    | Party   | Member |
|------:|---------|---------|--------|
| 1     | 18      |  A      | Warrior|
| 2     | 16      |  B      | Goblin |
| 3     | 12      |  A      | Wizard |
| 4     | 9       |  B      | Gnoll  |

If the warrior uses the placement to just wait for a better moment, the goblin
will go first; but they use this advantage to move to the third spot in place
of the wizard, that character can go first, and cast a debilitating spell on
the opposing party.

This advantage conflicts with the [latecomer](#latecomer) disadvantage.

## Offensive flow

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Combat style |
| Cost | 2 TT/Hard |

The character can perform one additional offense with the selected 
style per combat turn in one specific combat style. It's possible
to get this advantage for multiple styles.

## Survival instinct

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 3 TT/Normal |
| Levels | 4 |

All instinctive defense checks get a +1 modifier per level of this advantage.

## Total Mitigation

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Normal |

When the character receives an effective damage for 0 **DP** it still sustain a _scratch_.
This advantage prevents that.

However, other negative effects will still be applied. For example, if the character is
hit by a poisonous dart but the effective damage after all the mitigations are applied is 0,
while it won't receive a scratch, even with this advantage the poison will still be
applied.

# Disadvantages

Disadvantages are permanent penalties afflict the character.

A player can decide to apply some disadvantage to their character
before beginning an adventure, as doing so grants **training tokens** that
can be employed to make the character stronger in other aspects.

While most disadvantages are simply afflicting a character or not,
some can have different In this case, the player receives the base
value indicated in the description, plus the same amount of points
as the level of the disadvantage.

For example, **Nervous** can have a level between 1 and 3, 
each inflicting a more negative modifier. The description indicates that the
"cost" (to be intended as tokens refunded to the player) is 3 **TT**/*Hard*.
So getting level 1 grants the player 3 + 1 = 4 **TT**/*Hard*; level 2 grants
3 + 2 = 5 and level 3 grants 3 + 3 = 6 **TT**/*Hard*. This means that
players can get a total of 4 + 5 + 6 = 15 **TT**/*Hard* if they give
**Nervous**/3 to their characters.

Curses and other negative effects can temporarily or permanently inflict
disadvantages against the will of the players; in that case, they won't
receive any bonus tokens. It is also possible to get rid of a disadvantage
that the players don't want anymore, provided it was given to their
character on their own will, by spending an amount of tokens double the
ones received when it was applied (rounded down).

For more details on the advantage system, consult the 
[advantage system in the rulebook](https://jonnymind.github.io/SIRPAS/Rulebook.html/#advantages-and-disadvantages),

## Foudnational disadvantages


- [Fainting](#fainting)
- [Fumbling](#fumbling)
- [Latecomer](#latecomer)
- [Nervous](#nervous)
- [Self Taught](#self-taught)
- [Situational Unawareness](#situational-unawareness)
- [Soft Skin](#soft-skin)
- [Unlucky](#unlucky)
- [Vulnerable](#vulnerable)
- [Weak Mind](#weak-mind)

## Fainting

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 1 TT/main |

A character with this disadvantage is subject to fainting when receiving
a serious or heavy wound.

The character must perform a **resistance check** against the source
of damage causing the wound. On failure, it receives the 
**fainting** status: the character is unable to perform any action for
about half a minute.

In combat, this translates in losing any action left in this turn
and skipping the next one; in this situation, instinctive defense
checks get a -3 modifier. Further wounds while affected by the
**fainting** status do not re-apply it.

## Fumbling

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Primary |

This disadvantage makes considerably easier to score a critical failure
in every check.

Each entry in the [critical failure]($RulebookAddress#critical-results) 
table is increased of three points. The success margin for scoring
a critical failure becomes:

* Trivial: -3
* Easy: -4
* Normal: -5
* Hard: -6
* Very hard: -7

Also, in *normal*, *hard* and *very hard* checks a natural roll of 3 **or** 4 leads to 
an automatic critical failure, regardless of the negative success margin.

## Latecomer

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Primary |
| Conflict | Nimble crowder |

Whenever a [ranking]($RulebookAddress#ranking) is performed, the character 
gets one place lower than their scored rank. This is not applied to
[multirankings]($RulebookAddress#multiranking)

If two or more characters with this disadvantage are stacked in consecutive places,
the first character without this disadvantage ranks on top of them.

For example, suppose this is the outcome of an **initiative** ranking to establish
a **combat order**:

| Place | Roll    | Party   | Member |
|------:|---------|---------|--------|
| 1     | 18      |  A      | Warrior|
| 2     | 16      |  A      | Wizard |
| 3     | 12      |  B      | Goblin |
| 4     | 9       |  B      | Gnoll  |

If both the warrior and the wizards have this disadvantage and the goblin hasn't,
the ranking will be modified as:

| Place | Roll    | Party   | Member |
|------:|---------|---------|--------|
| 1     | 12      |  B      | Goblin |
| 2     | 18      |  A      | Warrior|
| 3     | 16      |  A      | Wizard |
| 4     | 9       |  B      | Gnoll  |

This disadvantage conflicts with [nimble crowder](#nimble-crowder), even if that
advantage have a similar effect, that is, being able to reduce the character
position in any ranking at will.

## Nervous

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Hard |
| Levels | 3 |

The character receives a penalty equal to the level of this disadvantage
whenever they must "move first" in a game situation. This includes, but is
not limited to:

* When they are the first in a **combat order** ranking, i.e. when they
move first in a combat round.
* When they are on the top spot of a **multiranking**.
* On the first check after winning a **ranking**, e.g. on the first action
once entering a house after they won the ranking to rush inside.

If it's possible to renounce being the first acting in a given context,
the character can chose if move first and face the penalty of this disadvantage,
or wait and move without penalty.

For example, even when having won a **combat order** ranking, characters are not
forced to move first. They can wait for any other moment in the round to act; if they
let someone else (enemy or allied) to perform an action first, they can then
act without any penalty.

Similarly, even after winning a ranking that would allow them to move first,
i.e. after being the first rushing in a house, they can forfeit the 
privilege of being the first to act, and let someone else (e.g. the second
in the ranking) to act first.

However, it's not possible to arbitrarily change spot in a multiranking. So,
if the character is first in their team in a multiranking, he or she will have
to score against the other teams top-scorer applying the penalty of this
disadvantage.

## Self Taught

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Specialization | Skill |
| Cost | 2 TT/Normal |
| Conflict | Easygoing |

Easy checks on the specialized skill get a penalty modifier 
of -1, and trivial checks have a modifier of -2.

This extends to any kind of checks and skills, including
contests and combat skills.

## Situational Unawareness

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 1 TT/Hard |
| Levels | 3 |

All instinctive defense checks and contests get a -1
modifier per level of this disadvantage. 

## Soft Skin

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Hard |
| Levels | 3 |

The character receives a passive penalty against blunt
and cut damage equal to the level acquired.

## Unlucky

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Main |
| Conflict | Lucky |

The character performs every check (except direct **resistance checks**) 
rolling an additional, separate six-face dice (suggest using a 
differently colored one, if possible).

If the separate roll scores 1, the *worst* roll of the other die in the check
(*after* applying other advantages) is substituted with 1.

For example: a character with **expert**/*lockpicking* attempts opening a lock.
As they have the advantage [expert](#expert) on lock-picking, they will roll 4d6 
and select the best 3 rolls. However,
they also must roll for **unlucky**. Suppose the roll for the check gives
2, 3, 3 and 4, and the **expert** advantage allows to discard the lower roll (2),
resulting in 3, 3 and 4. However, the unlucky dice rolls 1: 
the lowest roll after applying **expert** (3) must be discarded
and changed into 1, so the check result will now be 1 + 3 + 4 = 8 instead of
3 + 3 + 4 = 10.

If the special dice roll scores 1, but one of the other rolls was already
a natural 1, nothing happens.

This penalty is **not** applied on any **resistance check**. Also, any
temporary effect improving the natural rolls will temporarily disable
this disadvantage as a side-effect.

**Notice** that this disadvantage is opposed to **Lucky**.

## Vulnerable

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Specialization | Damage source |
| Cost | 1 TT/Hard |
| Levels | 3 |

The character receives 1 additional **damage point** from the 
target source, once at least 1 damage point is already received.

This is before the application of direct damage reduction; this
means that armors, force fields, energy shields, magic and so on
can absorb part of the additional damage.

If the damage source deals 0 **DP** before applying any mitigation
for any reason, this disadvantage is not applied.

This disadvantage is specialized by damage source. It is to 
considered conflicting with any advantage that provides damage
reduction from that specific damage source (e.g. [hard skin](#hard-skin)
providing resistance against some types of physical damages).

On the other hand, a character may have resistance against some
specific damage and vulnerabilities against others. For example,
it may be resistant to cold but vulnerable to heat, both being
elemental damage sources.

## Weak Mind

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Hard |
| Levels | 3 |

The character acquires a passive vulnerability against *despair*
and *maddening* damage equal to the level of this advantage.

# Backgrounds

Backgrounds are generic advantages and disadvantages giving 
deeper customization to characters in the game world. 

Whatever in makes the character stand out with respect to the vast
population is considered a *background*.

There isn't a net distinction between positive
and negative backgrounds: they all have a positive cost in 
**training tokens** to be spent at character creation. It is also
possible to receive the backgrounds as a consequence of adventuring;
for example, one can certainly become an outlaw during the course 
of an adventure.

For more details about backgrounds, 
[read the background section in the Rulebook]($RulebookAddress#backgrounds)


- [Aristocrat](#aristocrat)
- [Corporative](#corporative)
- [Criminal Boss](#criminal-boss)
- [Cult member](#cult-member)
- [Fallen Aristocrat](#fallen-aristocrat)
- [Famous](#famous)
- [Field expert](#field-expert)
- [Gang member](#gang-member)
- [Law Enforcer](#law-enforcer)
- [Military](#military)
- [Outlaw](#outlaw)
- [Sectarian](#sectarian)
- [Wealthy](#wealthy)

## Aristocrat 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Primary |

The character is an aristocrat in the target setting. In settings
that don’t consider birth rights as traditional aristocracy, the
the character belongs to a similar oligarchy or high-order political
elite.

The cost, and the effect of the background on the game, depends on the
level of aristocracy:

* Baron, career politician, oligarch: 1 TT/Primary
* Count, party leader, organization leader: 2 TT/Primary
* Duke, minister, CEO: 3 TT/Primary
* King, prince, prime minister, president: 4 TT/Primary

The background is applied also if the character is a close family member
(child, parent, souse) of a person in the given position. For example,
if a player wants to play the son of a baron, they will have to spend
1 TT/Primary too.

This background is not applied if the character is prevented from using the
social position for any reason: check the background "Fallen aristocracy"
for that.

## Corporative

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1 TT/Hard |

A corporative is an employee of a company or governmental
institution large enough to define a vast part of their 
character and behavior.

For example, university professor, researcher, manager in a
multinational, engineer in a governmental space program are all
covered by this background.

Of course, the position must leave the character the possibility
to participate in the adventure. That may be justified as paid absence,
sabbatical, research project, special assignment, special operation
etc.

However, fort his background to be active, the character must always
retain the connection with the organization, and suffer the consequences
in case it breaks they break its rules.

While covering governmental agencies, this background doesn't cover law 
enforcement and military organizations, which are separately defined by
the [law enforcer](#law-enforcer) and [military](#military) backgrounds.

## Criminal Boss

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1 TT/main |

The character is the leader of a criminal organization. It has a
relatively large network of criminals that follow his orders, a
consistent wealth and a flux of incoming money. On the other side,
it’s known to relevant police forces, constantly at risk of being
arrested and not always welcome in high social circles.

## Cult member 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1 TT/Hard |

The character is an active follower of a cult.
That includes any kind of cult, from major religions 
to minor local cults, but not secret sects or outlawed
cults; that is covered by the [Sectarian](#sectarian) background.

Being an active follower means to uphold the principles and
the practice of the rules with as little deviation as possible.

## Fallen Aristocrat 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Hard |

The character was part of an aristocratic family in the target setting, 
but either:

* they are prevented from accessing the benefits of that position; or
* they lost permanently or semi-permanently that position.

Some possible examples:

* an out-of-wedlock child of a baron, who is known by their
  father but not officially recognized as a heir; 
* the only child survivor of a usurped and exterminated royal family;
* a former party leader that has been excised out of the ruling structures
  during some power struggle.
* A noble rebelling against their king.

A character like Robin Hood would fit this background.

The cost, and the effect of the background on the game, depends on the
level of former / unrecognized aristocracy:

* Baron, career politician, oligarch: 1 TT/Hard 
* Count, party leader, organization leader: 2 TT/Hard
* Duke, minister, CEO: 3 TT/Hard
* King, prince, prime minister, president: 4 TT/Hard

## Famous 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Primary |

The character is famous and easily identified by its peers.
Also, whoever wants to know about the character, or searching
for it because of any specific reason (i.e. to hire it for
a job, or to hunt it down), can easily find information
about it and its general whereabouts, unless the character
actively disguises and hides.

Characters with other backgrounds may be famous as well;
an aristocrat probably is, and so is a boss criminal. This
background covers being famous directly for
some deed or action, besides the ones specifically covered by
other backgrounds.

The cost depends on how famous the character is:

* 1 **TT**/*Primary*: Known by 1/20th-1/10th of the population; people
  occasionally identify them when walking by, and have
  heard of he character.
* 2 **TT**/*Primary*: Known by 1/5th of the population. During a day out,
  or a long walk, the character is sure to be recognized,
  and possibly stopped by admirers (or haters).
* 3 **TT**/*Primary*: Known by more than half the population. Wherever the
  character goes, they are recognized, and when that happens,
  people flock to see them, or flee if they have a negative fame.

## Field expert

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Primary |

The character is an expert in some relevant field of study: physics, psychology,
economics, information technology, regional lore, world lore, history etc.

## Gang member

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 2 TT/Hard |

While not currently outlaw, the character is part of an active
criminal organization.

Gang members have a higher initial pool of money to use.

## Law Enforcer

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Hard |

The character is a member of the Police, city guard, castle guard, 
or equivalent Law Enforcement agency. This includes also commanding
roles

* Simple Member: 1/TT Primary
* Sergeant, squad leader, garrison leader: 2/TT Primary
* Inspector, Inquirer, Inqusitor: 3/TT Primary
* Prosecutor, Judge: 4/TT Primary

## Military

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1+ TT/Primary |

The character is part of a military organization, or organized
militia. This includes modern armies, knight orders, semi-regular
militia, legions and so on.

The cost of this background depends on the level occupied in the
military:

* Soldier: 1 TT/primary
* Sergeant, legionary: 2 TT/primary
* Captain, centurion: 3 TT/primary
* Colonel, general: 4 TT/primary

Of course, the character needs to have a reason to join the adventure.
This will usually be a special assignment, a long term espionage or
survey mission, or even a temporary license.

## Outlaw

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 2 TT/Hard |

The character is a fugitive in the eye of the law, whether
they have actually committed any crime or not.

In some game worlds, political or religious organizations
may be outlawed. In some others, characters with special
birthmarks, uncommon powers or attributes may be outlaw.

In some game worlds a person could become outlaw
because of ostracism towards their family member; that would
be the case of a king declaring the whole family of a
treasonous baron to be outlaw.

However, this applies also to real criminals, as a typical
outlaw in a western movie.

## Sectarian 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 1 TT/Hard |

The character is a member of a secret, non-governmental organization.

This includes but is not limited to:

* Secret criminal organizations. While all criminal organization
  require an amount of secrecy, to the organizations we're talking here
  are more in the line of the historical *hashashin*, super-villain 
  mysterious sects that have their primary activity into crime.
* Occult and exoteric organizations.
* Underground cults.
* Underground anti-governmental organizations.

And in general, any organization that:

* has a strict code of conduct; and
* has a proclaimed target objective that the members must actively pursue; and
* requires exclusive and perpetual affiliation; and
* requires secrecy and forbids members to let their affiliation known to any non authorized person.

## Wealthy 

| <!-- --> | <!-- --> |
|----------|------------|
| Category | Background |
| Cost | 2 TT/hard |

The character has personal wealth in excess with respect
to the population average, enough to be considered in the richest 1%.

This background doesn't cover the source of the wealth; it's to be
employed only when no other background that would usually result
in the character being wealthy cannot be applied. 

Reasons for this background to apply could be:

* While the family of the character is not part of the world
  aristocracy, it has accumulated wealth through trade and/or hard work.
* The character has received their wealth as an inheritance, a lottery win,
  a gamble, or any other random reason.
* The character found their wealth as a lucky consequence of a previous
  adventure, i.e. they stumbled on a treasure that wasn't supposed to be there.
* The character has a very lucrative activity in the game world which is not
  covered by any other background.

This background is not applied when the wealth of the character may be related
or explained by any other background (i.e. being a high ranking member of the
[military](#military)).

# Skills

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


- [Acrobatics](#acrobatics)
- [Active Mitigation](#active-mitigation)
- [Archery](#archery)
- [Block](#block)
- [Brawl](#brawl)
- [Charisma](#charisma)
- [Chemistry](#chemistry)
- [Climbing](#climbing)
- [Concentration](#concentration)
- [Deceit](#deceit)
- [Disengage](#disengage)
- [Endurance](#endurance)
- [Engineering](#engineering)
- [Firearms](#firearms)
- [First Aid](#first-aid)
- [Full Contact](#full-contact)
- [Hacking](#hacking)
- [Healing](#healing)
- [Hiding](#hiding)
- [Hiding in Shadows](#hiding-in-shadows)
- [Initiative](#initiative)
- [Instinctive Defense](#instinctive-defense)
- [Intimidate](#intimidate)
- [Investigation](#investigation)
- [Knife Fight](#knife-fight)
- [Lie Detection](#lie-detection)
- [Lock Picking](#lock-picking)
- [Lore Knowledge](#lore-knowledge)
- [Perception](#perception)
- [Persuade](#persuade)
- [Pickpocket](#pickpocket)
- [Poisons](#poisons)
- [Repair](#repair)
- [Resistance](#resistance)
- [Riding](#riding)
- [Running](#running)
- [Shoot](#shoot)
- [Silent Movement](#silent-movement)
- [Slash](#slash)
- [Stabilize](#stabilize)
- [Swordfight](#swordfight)
- [Throw](#throw)
- [Thrust](#thrust)
- [Treating Wounds](#treating-wounds)
- [Willpower Defense](#willpower-defense)
- [Break Free](#break-free)
- [Traps](#traps)

## Acrobatics

| <!-- --> | <!-- --> |
|------|---|
| Base | D |
| Category | Skill |
| Cost | 1 TT/Normal |

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

## Active Mitigation 

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | AM |
| Category | Skill/combat |
| Specialization | combat style |
| Cascade | Yes |
| Cost | 1 TT/Hard |

Once per combat turn, the character can mitigate incoming damage
by an amount equal (or less) than the **Success Margin** on a **Simple Check** on
this skill.

For example, a warrior has **AM/Swordfight** 6, and the advantage **Expert/AM/Swordfight** 
It receives damage for 5 **DP** after passive mitigation.

The Success Level for this simple check is 16 (being an Expert rolling **AM** a 16 after various
modifier, the check results 6+16 = 22, which has **SM** 22 - 21 = 1.

In the end, the fighter receives 5-1 = 4 **DP**.

This is a [cascade skill]($RulebookAddress#cascade-attributes); this means
it's possible to acquire this attribute multiple times to perform multiple
active mitigations per turn.

## Archery

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 4 |
| Cost | 1 TT/Hard |

This is the base style (and skill) needed to use bows, crossbows and similar projectile
weapons.

Unless differently specified, all attacks from *archery* deal __cut__ damage,
and the range depends on the used weapon.

### Advanced Combat 

This is the number of maneuvers granted by archery in advanced combat system.

| Level | Maneuvers |
|-----|---|
| 1-9 | 1 |
| 10-16 | 2 |
| 17+ | 3 |

#### Aim 

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Archery 3 |

Take a maneuver to improve the next attack, giving it a modifier of +1.
It can be repeated any number of times within a single turn, but the
modifier is applied only to the very next Shoot.

#### Localized Shot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | Variable |
| Prereq | Archery 5 |
| DR | -1 |
| Damage | __SM__+1 |
| Condition | (__Cripple__) |

Loads and shoot an arrow or a bolt aiming to a specific part of the body.

A _critical success_ will cause automatically
a _localized heavy wound_, crippling that part of the body,
if the damage caused would be otherwise enough to cause at least
a _light wound_.

> Localized heavy wounds can have further negative effects with respect to
normal heavy wounds, as disarming, reducing the movement speed, blinding
and so on.

If the localized shot was aimed at the head, a _critical success_ will cause
a _deadly wound_.

The modifier to be applied depends on the target part of the body:

| Body Part | Modifier |
|:---------:|---------:|
| Arm       | -2       |
| Leg       | -3       |
| Head      | -4       |

#### Overextend

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Modifier | mS-2 |
| Prereq | Archery 6 |
| DR | -1 |
| Limitation | Bows |

Take a maneuver to bend the bow more than normal in order to improve
the next attack, giving it a damage modifier equal to the success
margin of this check.

#### Overload

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Archery 9 |

Loads two arrows or two bolts in the weapon. The very next attack will have a
fixed modifier of -3, but the character gains an extra attack
to be used in the current or the next turn.

> This maneuver gains an extra attack only. Defense and action count
is not affected.

This is useful when it’s not currently possible or ideal to attack a target, but
you don’t want to lose the attack.

#### Shoot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Archery 1 |
| Damage | __SM__+4 |

Loads and shoot an arrow or a bolt.

## Block 

| <!-- --> | <!-- --> |
|------|-----|
| Base | D/2 |
| Callsign | Blk |
| Category | Skill/combat |
| Cost | 1 TT/Normal |

This skill is used to try and block an opponent in *close quarters*. 

If the opponent is unaware, the attempt will succeed with a **CHK** 
at *easy* level.

In combat, the opponent can use any melee defense. In that case,
a **CFR** between **Blk** and the defense is attempted.

Normally, the block lasts one turn; then the opponent can try 
to [break free](#break-free) or any 
relevant melee defense to exit the block.

A critical success indicates that the blocker has completely
subdued the opponent, that will be unable to break free unless
the blocker is forced to remove the block.

Multiple characters can attempt to block the same opponent; in that
case, a **RNK** is attempted. All the characters scoring higher than
the defendant will be actively engaged in the block.

## Brawl

| <!-- --> | <!-- --> |
|------|----|
| Base | mS |
| Category | Skill/combat |
| Dominance | 1 |
| Cost | 1 TT/Normal |

Brawl is the style of fight with bare hand and feet, without a specific
preparation. It’s often used in tavern and bar fights, and can also be
useful in other combat situations.

Every human or humanoid character has access to brawl.

Unless differently specified, all attacks from **brawl** deal _blunt_
damage, and all the maneuvers are melee.

### Advanced Combat

The number of maneuvers the character can use per round depends on
the level of brawl:

| Level | Maneuvers |
|-----|---|
| 1-5 | 1 |
| 5-10 | 2 |
| 11-15 | 3 |
| 16+ | 4 |

#### Block

| <!-- --> | <!-- --> |
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

#### Evade

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Brawl 1 |
| DR | -1 |

Try and evade an attack moving the body out of the way of the incoming hit.

#### Grapple

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Prereq | Brawl 8 |
| DR | -1 |
| Condition | __Block__ |

The character tries to grab and control the opponent. Effective only against
targets with a strength less than the double of the attacker’s, and with a body
less than double the size.

The attacker and the defender are both blocked, until the attacker fails the
attack with a +3 modifier in the subsequent turns, or performs another
action.When used against the blocked target, diminishing return is not applied
on either side.

#### Kick

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Brawl 1 |
| DR | -1 |
| Damage | __SM__+mD |
| Condition | __(Stun 2)__ |

The character attacks with a kick, causing a damage equal its dexterity plus the success margin.
Gets a +2 modifier on small creatures (less half the size of the attacker) and grounded  targets.
On critical success, it stuns the target for 2 turns.

#### Punch

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Brawl 1 |
| DR | -1 |
| Damage | __SM__+mS |
| Condition | __(Stun 2)__ |

Attacks with a direct punch. A critical success stuns the target for 2 turns.
Receives a -2 modifier against targets larger than the attacker.

#### Smash

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Brawl 6 |
| DR | -1 |
| Damage | __SM__-2 |
| Condition | __Grounded__ |

The attacker throws its own body against the target. On success, the target is
grounded for a turn.

Receives a +2 modifier on smaller targets and -2 on larger targets. Brawl/Evade
and other evasions receive a +2 modifier to defend against this action.

Can’t be used against grounded targets.

## Charisma

| <!-- --> | <!-- --> |
|------|---|
| Base | M |
| Category | Skill |
| Cost | 1 TT/Normal |

Used to influence positively other characters. Not to be confused with
*Persuade*. This skill is specifically meant for characters trying to
make a good impression, obtain favours, special treatments, or a
generic good attitude. Persuade is the skill to deliver one specific
talk with persuasive power.

## Chemistry

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical knowledge of chemistry or equivalent science in the world setting
(e.g. alchemy in a magic world).

## Climbing

| <!-- --> | <!-- --> |
|------|---|
| Base | D |
| Category | Skill |
| Cost | 1 TT/Easy |

Used to check when the character climbs a section of wall 6 feet high. Use the
following table to determine the difficulty of the action:

| Surface                          | Modifier                         |
|--------------------------------------|--------------------------------------|
| Ivy riddled wall                     | Trivial                              |
| Old bricks                           | Easy                                 |
| Stone Wall                           | Normal                               |
| Rock Wall                            | Difficult                            |
| Castle Wall                          | Hard                                 |
| Polished Wall                        | Very Hard                            |

If the character fails, it stays at its current spot, and it can try again
with the repeated attempt modifiers.

A critical failure implies that the character fell from the current spot.
A critical success indicates it climbed for 12 feet instead of 6.

## Concentration

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill/combat |
| Dominance | 1 |
| Cost | 1 TT/Hard |

Concentration is a simple mind-oriented fighting style, which can be seamlessly
integrated in a traditional melee fight. It covers the role of the default
combat style for mental combat, analogous to brawl for physical combat. In a
world where mental fight is a thing, everyone should be able to mind meld, like
everyone is able to brawl in physical worlds.

While other fighting styles in the manual are realistic, this requires a setting
specifically supporting mind powers. However, the style is suitable for sci-fi
settings to handle fights between AIs, robots, hackers and so on, with
low-resolution.

### Advanced Combat

The number of maneuvers the character can use per round depends on the level
of Concentration:

| Level | Maneuvers |
|-----|---|
| 1-7 | 1 |
| 8-13 | 2 |
| 14+ | 3 |

#### Alien Thoughts

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mI |
| Prereq | Concentration 1 |
| DR | -1 |
| Damage Type | Maddening |
| Damage | __SM__+mI |

The attacker projects alien, irrational thoughts in the defendant’s,
in order to cause maddening.

#### Block

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mW |
| Prereq | Concentration 1 |
| DR | -1 |

The character raises a mental barrier in order to block an incoming attack.

#### Dig into you

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mW |
| Prereq | Concentration 1 |
| DR | -1 |
| Damage Type | Despair |
| Damage | __SM__+mW |
| Condition | __(Stun 2)__ |

The character attacks by searching for painful memories and thoughts, in order to cause despair in the target.

#### Divert

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mI |
| Prereq | Concentration 1 |
| DR | -1 |

The defendant diverts the attention of the attacker on an irrelevant
thought or memory, causing the attack to miss.

#### Mind Grasp
#
| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mI |
| Prereq | Concentration 6 |
| DR | -1 |
| Condition | __Blocked__ |

The character tries to acquire the control of the defendant mind. On success,
the defendant is unable to act (blocked). To keep holding the target, the attacker
must continue to use this attack with + 3 modifier against it at each turn. When
this maneuver is used against a blocked target, diminishing return is not
applied on either side.

The attacker must keep using this attack once per turn and can’t move or perform
any other action.

If the attacker receives any damage, the concentration is broken.

#### Sensations

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -1 |
| Prereq | Concentration 4 |
| DR | -1 |
| Damage Type | Confusion |
| Damage | __SM__+*mW* |
| Condition | __(Stun 2)__ |

The attacker tries to hijack the sensory system of the target mind, 
causing it to hallucinate and fail to coordinate with the body. 
On critical success, the target is stunned for 2 turn.

#### Yes, but you...

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mI |
| Prereq | Concentration 6 |
| DR | -1 |
| Damage Type | Despair |
| Damage | __SM__-2 |

The defendant turns the mental attack against the attacker.
If the defense is successful, the attacker is hit back for a
number of despair points equal to the success margin
of the defense minus two (minimum 1 dp).

## Deceit

| <!-- --> | <!-- --> |
|------|---|
| Base | I |
| Category | Skill |
| Cost | 1 TT/Normal |

It’s the ability to say a credible lie.

A critical failure indicates that the target hasn't just understood it was being
deceived, but they also understood the truth that the character was trying to hide.

A critical success indicates that the target will still believe the deceit after
being shown proof of the contrary.

## Disengage 

| <!-- --> | <!-- --> |
|------|---|
| Base | D |
| Callsign | Dis |
| Category | Skill/combat |
| Cost | 1 TT/Easy |

Disengage allows to break off from a melee engagement, and to move half the normal movement 
speed in the current turn. 

It automatically succeeds if there isn't any opponent currently able or willing to attack
the character using it. 

This skill can also be used against an incoming attack; in that case, it works as a
standard defense, and a combat **CNT** is performed between the attack skill of the attacker
and the **Dis** of the defender. 

If one or more opponents try to stop the disengaging character with something else
than a direct attack (i.e. grabbing or blocking them), a **RNK** is performed, 
and the disengagement succeeds only if the defendant is the top ranked.

On failure, the disengagement fails and the character cannot move; when used as a defense,
this also means that the attack has been successful.

## Endurance

| <!-- --> | <!-- --> |
|------|------|
| Base | Body |
| Callsign | End |
| Category | Skill |
| Cost | 1 TT/Hard |

Endurance is the ability to resist long lasting physical strain. A long march,
swimming, carrying weights for a long time etc. requires an endurance check.
Subsequent endurance checks against the same condition are treated as repeated
check (each of them gets a -1 modifier), even if other skills are used
meanwhile.

For example, if a group is taking a forced march and has already passed a check,
is forced to a fight and then resumes the march without any rest, the next
endurance check will have a modifier of -1.

A success indicates that the character is able to continue the effort. In case
of failure, the character needs to try again with the ever increasing repeated
check, until success becomes impossible.

A critical success causes the next repeated check to be won automatically, and
the current repeated modifier is also reduced by 1.

A critical failure indicates that the character is exhausted, and needs to rest.
If it is in a precarious situation, i.e. swimming, walking along a dangerous
mountain trail, it might be forced to roll against a deadly wound or die.

## Engineering

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical skill in world-relevant engineering. For example,
in a steampunk world, it would be the ability to put together
mechanical devices. 

## Firearms

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 5 |
| Cost | 1 TT/Hard |

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

| Level | Maneuvers |
|-----|---|
| 1-5 | 1 |
| 5-10 | 2 |
| 11-15 | 3 |
| 16+ | 4 |

#### Aim

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Firearms 3 |

Take a maneuver to improve the next attack, giving it a
modifier of +1. It can be repeated any number of times within a 
single turn, but the modifier is applied only to the very next 
Shoot or Aimed Shoot, either within the same turn or in the very next one. 

No other action can be performed while aiming, and performing another
action will discard the modifiers achieved.

#### Aimed Shot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Firearms 6 |
| DR | -2 |
| Damage | __SM__+9 |
| Condition | __Injury__ |

Inflicts a -3 modifier on the attack, but it generates an injury one level
more severe than normal. Light wounds becomes severe, severe wounds become
heavy and heavy wounds becomes deadly.

#### Duck

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Firearms 2 |

Duck or evade while holding the firearm to avoid incoming fire.

#### Fast Reload

| <!-- --> | <!-- --> |
|------|---------|
| Type | Actions |
| Prereq | Firearms 4 |

Ability to reload the weapon in the heat of the combat, using a
maneuver.

#### Localized Shot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | Variable |
| Prereq | Firearms 4 |
| DR | -2 |
| Damage | __SM__+4 |
| Condition | __(Cripple)__ |

Shoot aiming a part of the body.

A _critical success_ will cause automatically
a _localized heavy wound_, crippling that part of the body,
if the damage caused would be otherwise enough to cause at least
a _light wound_.

> Localized heavy wounds can have further negative effects with respect to
normal heavy wounds, as disarming, reducing the movement speed, blinding
and so on.

If the localized shot was aimed at the head, a _critical success_ will cause
a _deadly wound_.

The modifier to be applied depends on the target part of the body:

| Body Part  | Modifier |
|:----------:|---------:|
| Arm        | -2       |
| Leg        | -3       |
| Head       | -4       |

#### Point Blank

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | +2 |
| Prereq | Firearms 6 |
| DR | -1 |
| Range | Melee |
| Damage | __SM__+10 |
| Condition | __(Deadly)__ |

Fires at point blank on targets in melee range.
On critical success it causes a deadly wound.

#### Rapid Fire

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Firearms 9 |
| DR | -3 |
| Range | 15 ft |
| Damage | __SM__+3 |

Fires twice in a single maneuver, each time with reduced attack and
damage. Can be used with pistols only.

#### Shoot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Prereq | Firearms 1 |
| Damage | __SM__+7 |

Normal base attack with firearms.

#### Take Cover

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | +3 |
| Prereq | Firearms 3 |
| DR | -2 |

If a cover is within movement range for the turn, the character can use this defense to run towards a covered position, with a fixed +3 modifier.

## First Aid

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Normal |

This skill can be used to perform the following actions:
* cure a *light wound* with a successful *normal* check;
* reduce a *serious wound* into a *light wound* with a *difficult* check;
* reduce a *heavy wound* into a *serious wound* with a *hard* check.

Using a standard first-aid kit gives a modifier of +6 (some special first-aid kits
have higher modifiers). 

>Notice that no matter the modifier received with a first-aid kit, for what
concerns *critical results*, checks on 
*serious wounds* and *heavy wounds* are still *hard* and *very hard*.

The user can also cure more wounds on the same character; each further cured
wound requires adding the penalty of a *repeated check*, even if the previous
check is successful.

This skill can also be used to stabilize a disabled target with a successful *normal* check. 
Using a first-aid kit makes the check become *trivial* (no further modifier given by
the first-aid kit is applied).

A *critical success* (whether the skill is used to stabilize or cure a wound) heals another 
*light wound*, if the character has any.

A *critical failure* causes a light wound. If the skill is used to stabilize a dying 
character, a critical failure will kill it immediately.

If the skill is target of an [expertise](#Bam-a-expertise-skill) advantage, it can
also cure *serious wounds* instead of reducing them, and critical success will cure
up to an extra *serious wound*, if the target character has no more *light wounds* 
to cure.

## Full Contact

| <!-- --> | <!-- --> |
|------|---------|
| Base | Brawl/2 |
| Category | Skill/combat |
| Prerequisite | Brawl 4 |
| Dominance | 3 |
| Cost | 1 TT/Hard |

An advanced version and extension of Brawl. While still not being a full-fledged
martial art, it’s a style of combat that requires dedication, and if
professionally trained, can be quite effective even against more famous martial
arts.

A character using Full Contact can use all the maneuvers from *Brawl* under
*Full Contact* instead (whichever has the higher level).

All damage from *full contact* is of __blunt__ type, unless differently
specified.

### Advanced Combat

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

#### Counter Punch

| <!-- --> | <!-- --> |
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

#### Counter kick

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD-2 |
| Prereq | Full Contact 3 |
| DR | -2 |
| Damage | __SM__-1 |
| Condition | __(Stun 2)__ |

A counter-attack performed on melee attacks. Tries to evade
the incoming blow and use the opening to strike with a punch
on the higher part of the body. Has modifier +2 against
smaller creatures.

Ineffective against non-melee and animal attacks.

#### Crouch

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Full Contact 3 |

The character loads the next attack, receiving a **DP** modifier equal
to the success margin to be used in the very next attack in Brawl
or Full Contact styles.

If the next maneuver used is not an attack, or if the attack fails, 
the modifier is lost.

#### Elbow Blow

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Full Contact 1 |
| DR | -2 |
| Damage | __SM__+2 |
| Condition | __(Stun 2)__ |

The character attacks with the elbow, causing a damage equal to its strength
plus its success margin, and a modifier of +2.

#### Knee Blow

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Full Contact 1 |
| DR | -2 |
| Damage | __SM__+3 |

The character attacks with its knee, causing a damage equal to its dexterity,
plus the success margin and a fixed modifier of 2.

Gets a +2 modifier on small creatures (less half the size of the attacker)
and grounded targets.

## Hacking

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Callsign | Hk |
| Category | Skill |
| Specialization | system |
| Cost | 1 TT/Hard |

When a character wants to hack a device or a system, it can roll on this to
check if it has the necessary knowledge to hack the system.

Each action requires a different check. A critical failure implies the hacking
has been neutralised and the source identified. A critical success implies that
the character has gained privileged access, and further actions on the same
system will not require a separate check.

The specifics of the system depend on the setting. For some settings, the
hacking skill could be general, while in other settings specific systems will be
identified, and they might require a separate hacking skill.

## Healing

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | Hl |
| Category | Skill |
| Prerequisite | First Aid 6 |
| Cost | 1 TT/Hard |

The character has advanced practical medical knowledge for the setting
where the adventure takes place, and is able to heal illnesses, poisoning
and equivalent conditions for the target settings, that may affect
biological living beings.

For instance, in a magic world where curses can cause illnesses, this
skill can also be used to treat the effect of the curses.

The type of illness determine the difficulty of the check. The following table 
gives a basic reference frame for deciding the difficulty of a check.

| Illness Type                     | Severity                         |
|----------------------------------|----------------------------------|
| Common Cold                      | Trivial                          |
| Light Fever                      | Easy                             |
| Intestinal Fever                 | Normal                           |
| Malaria/Pneumonia                | Difficult                        |
| Plague/Yellow Fever              | Hard                             |

Specific information about the setting will be used by the GM or directly
given in the descriptioin of the illnesses in order to determine the 
check difficulty.

The time required for the cure to take effect is in the order of hours to days;
the **Success Margin** can be used by the *GM* to decide how fast the recovery is.

Illnesses that are *difficult* or *hard* to cure will be transformed in *easy*
or *trivial* ilnesses before being cured. For instance, a successful cure of
*plague* will initially turn the illness into a *light feever*, which can then
be cured again to heal it completely.

Particular setting-specific devices can give determined bonuses in curing generic
or particular illnesses. Specific medicines or magic potions can give very high
bonuses (+12 or more) almost granting a success, even if the characters using them
have no healing skill at all.

A *critical success* will cure the illness completely and in record time.
A *critical failure* will cause another illness to appear (i.e. intoxication
from the medicinal active principle, appearance of secondary side-effects etc.).

## Hiding

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Category | Skill |
| Cost | 1 TT/Easy |

The character knows how to hide so to look like inconspicuous material
(i.e. a sack of potatoes, a part of a load of straw on a cart, a roll
of cloth and so on). The difficulty of the check is determined by the GM.

This skill is used only when trying to hide into a spot or a location
that offer a high chance not to be seen at all. To try and hide in 
places or behind covers that would offer little screening from sight,
use [Hiding in Shadows](#hiding-in-shadows) instead.

## Hiding in Shadows

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Callsign | HiS |
| Category | Skill |
| Cost | 1 TT/Normal |

The character knows how to hide in dark places, or pass unobserved in a
crowded place.

This skill can also be used to hide in behind furnitures, tapestries, and in
general, in environments that would offer little chance for hiding
effectively otherwise.

## Initiative

| <!-- --> | <!-- --> |
|------|--------|
| Base | D or W |
| Callsign | In |
| Category | Skill/combat |
| Cost | 1 TT/Hard |

This skill represents the reaction times and determination under pressure of
the character. It is typically used in contests or rankings, to decide who
acts first during a stalemate, but it can be also used in checks. The order
in which a combat turn develops is decided by a ranking on the initiative
of all the involved characters.

Initiative is a combat skill, and is typically used in the base and 
advanced combat systems; it can also be used in any out-of-combat
situation that requires readiness of wit and/or sudden mobility.

The base is either Dexterity or Will, the best of the two.

## Instinctive Defense 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill |
| Cost | 1 TT/Hard |

The instinctive defense is used against physical attacks whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available maneuvers for this turn.

It’s ineffective against mind attacks.

## Intimidate

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill |
| Cost | 1 TT/Normal |

Intimidate is the action of menacing someone that some negative outcome will
follow, unless they don’t comply with some desired course of actions. For
intimidation to be effective, the menace must be credible, and the target
must actually wish for that not to happen.

## Investigation

| <!-- --> | <!-- --> |
|------|---|
| Base | I |
| Callsign | Inv |
| Category | Skill |
| Cost | 1 TT/Hard |

The ability to find hidden clue or draw correct conclusions with a limited
amount of clue. Particularly useful when visiting the scene of a crime.

## Knife Fight

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 3 |
| Cost | 1 TT/Hard |

Fighting with knives and very short swords has different mechanics than the ones used when wielding a longer blade. Basically, it’s like having a fist armed with a single fang.
While the weapon themselves could be less effective than longer ones, the style itself can be extremely effective in every scenario.
Knife fighting is particularly adequate for characters with a high dexterity.

### Advanced Combat

The number of maneuvers the character can use per round depends on the level of Kinfe Fight:

(dt ac_knife_fight_levels)
[
   ["Level", "Maneuvers"],
   ["1-5", 1],
   ["6-10", 2],
   ["11-15", 3],
   ["16+", 4]
]

#### Backstab

| <!-- --> | <!-- --> |
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

#### Backstep

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |

Skip back, trying to get out of the range of a melee attack.

#### Belly Opener

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -1 |
| Prereq | Knife Fight 3 |
| DR | -2 |
| Damage | __SM__+5 |

Swing the blade in an upward strike, aiming at the lower part of the opponent
body.

#### Change Hands

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 2 |
| DR | -2 |

Use a maneuver to confuse the opponent and gain a +4 modifier on the next
attack.

The move is considered an attack, so the opponent must win a defense or
suffer the standard penalty.

#### Downstab

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 2 |
| DR | -2 |
| Damage | __SM__+4 |

Swing the blade in a downward strike, aiming at the upper part of the
opponent body.

#### Evade

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |

Try and evade an attack.

#### Feint

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | +3 |
| Prereq | Knife Fight 3 |
| DR | -2 |

Fake an attack, without actually completing it. On success it doesn’t
deal damage, but gives a **DP** modifier on the next move equal to
the success margin.

#### Hand Cutting

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD-2 |
| Prereq | Knife Fight 4 |
| DR | -2 |
| Damage | __SM__-2 |
| Condition | (__Disarm__) |

Aims at an incoming blow from dealt through an anatomic part (punch, kick,
animal attack and so on). Effective also against most melee weapon users,
when the attack moves the arm holding the weapon in range.

If the counter-attack causes a serious wound or worse, the target loses the
weapon.

#### Spring Up

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Knife Fight 6 |
| DR | -2 |
| Damage | __SM__+8 |

The character bend on its legs and springs forward, thrusting the blade towards
the opponent. It has a -3 modifier, but on success it deals a devastating
damage.

#### Throw

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |
| Damage | __SM__+1 |
| Condition | (__Cripple__) |

Throws the knife at an opponent within 15 feet. On success, it deals a limited damage.

#### Thrust

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |
| Damage | __SM__+4 |
| Condition | (__Cripple__) |

Attacks the target thrusting the knife forward, in a straight line.

#### Wrap and Stab

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD-3 |
| Prereq | Knife Fight 4 |
| DR | -2 |
| Damage | __SM__+6 |
| Condition | (__Injury__) |

Try to grab the opponent while fighting, to deliver deeper wounds. On success, this maneuver delivers an injury one level higher than normal.
_Light wounds_ become severe,_ severe wounds_ become heavy, and
_heavy wounds_ become deadly.

## Lie Detection

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Callsign | LD |
| Category | Skill |
| Cost | 1 TT/Hard |

This skill represents the ability of the character to detect lies, given
small hints on the voice, facial expressions and behavior of the target.

A skilled lier can oppose its deception; in this case, there will be a
simple contest (**CNT**) between the [persuade](#persuade) skill of the target
against the **LD** of the character. 

If the target isn't an able deceiver, the character can try
a check on this skill, with a difficulty that depends on the amount of
information the character has about the truth.

## Lock Picking

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | lp |
| Category | Skill |
| Cost | 1 TT/Normal |

Used to try opening normal locks. The lock must be within the 
reach of the technological knowledge of the character. 
The character must have also proper tools at its disposal
to try the action.

## Lore Knowledge

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | lk |
| Category | Skill |
| Specialization | field |
| Cost | 1 TT/Easy |

This skill represents the knowledge of the character about lore and stories in
the setting where the adventure takes place. The skill is specific for lore
types; for example, it can be targeted at norse mythology, egyptology, local
lores etc.

To check wether a character knows a specific lore it gets in contact with, check
against a difficulty which depends on how widespread the knowledge is,
considered the specific setting where the adventure takes place.

A lore everyone knows is checked as “trivial”, one that is particularly obscure
an known only to experts or initiates is “very hard”.

## Perception

| <!-- --> | <!-- --> |
|------|---|
| Base | W |
| Callsign | Prc |
| Category | Skill |
| Cost | 1 TT/Normal |

Determines whether the character is able to detect an element in the surrounding
that is hard to spot, as a secret door, a potential danger, a follower and so
on.

It is used when there aren’t more specific skills to be applied in the specific
situation. For example, trying to find traps is done by rolling on traps.

## Persuade

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill |
| Cost | 1 TT/Normal |

With this skill, the character can persuade others. Persuading means leading
others to believe the truth of some idea, fact or point of view (regardless of
them being actually true or not). Persuasion works on characters that don’t have
strong evidence or didn’t made up their mind already on said idea, fact or point
of view.

Persuasion can also be used to convince someone into performing some action, or
abstaining to perform some action they should do, provided the consequences for
doing so are not particularly harsh. For example, you can persuade some security
guards to let you in a restricted party, provided they don’t have categorical
orders, or provided that they think they can get away with a transgression.

## Pickpocket

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Callsign | Pp |
| Category | Skill |
| Cost | 1 TT/Normal |

Tires to remove objects from another characters. The objects must not be
secured to its body for the action to be successful. Use the following
table to determine the difficulty of the action:

| Target awareness                 | Modifier                         |
|----------------------------------|----------------------------------|
| Sleeping/tied/helpless           | Trivial                          |
| Busy (attention diverted)        | Easy                             |
| Unsuspecting                     | Normal                           |
| Attentive                        | Difficult                        |
| Suspicious                       | Hard to very hard                |

The action cannot reasonably be tried if the target is actually aware of
the fact that the character is actively trying to pickpocket it.

## Poisons

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical knowledge for recognizing or producing poisons.

To recognize a poison, the character must win a simple check at *normal* difficulty.

To produce one successfully, they must pass a *hard* check.

## Repair

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Callsign | Rep |
| Category | Skill |
| Specialization | machinery type |
| Cost | 1 TT/Normal |

This skill is used to fix machineries, magic constructs, AI, and in general
any non-living entity that doesn't have a *health*. 

The skill must be specialize for machinery category, which must be relevant
in the game world. 

Special repair kit, software tools, magic devices etc. may provide a bouns
on the simple check roll.

## Resistance

| <!-- --> | <!-- --> |
|------|---------|
| Base | Varying |
| Callsign | Res |
| Category | Skill |
| Specialization | Damage source |
| Cost | 1 TT/Hard |

The character has acquired a specific resistance against
a determined damage source. The base of the resistance
depends on the macro-category of the damage source,
as specified in the following table:

| Damage type | Base        |
|-------------|-------------|
| Physical    | Health      |
| Mental      | Equilibrium |
| Elemental   | Elem. Res.  |

The advantage [Elemental Resistance](#elemental-resitance) gives
the base against elemental damage.

This skill is used in **Resistance Checks** (**RC**) to avoid negative
effects from various deadly or potentially incapacitating sources.
Poisons, illness, certain magic spells, overwhelming mental attacks
and so on.

This is not a combat skill, but it may be used in specific situation
also in combat; for example, it's used to avert complete incapacitation
after receiving a deadly wound.

## Riding

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Specialization | mount |
| Cost | 1 TT/Easy |

This skill is used to perform particularly difficult actions while riding a
specific animal or vehicle. For example, jumping a fence with a horse, 
jumping across acrobatic platforms with a motor bike, running through a 
busy skyline with a flying car and so on.

The skill is specific for each device (or animal) that the character might ride.

## Running

| <!-- --> | <!-- --> |
|------|---|
| Base | D |
| Category | Skill |
| Cost | 1 TT/Easy |

Running is the skill used when deciding which character wins a run race.
It can also be used to check if a character is able to run for a long time.

## Shoot 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Cost | 1 TT/Normal |

Shoot with a projectile weapon while not being specifically skilled to do so.
Weapons requiring skill in being loaded (i.e. bows, special military
rifles etc.) cannot be used with this skill, but loaded weapons (i.e.
crossbows) can.

## Silent Movement

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Callsign | Sil |
| Category | Skill |
| Cost | 1 TT/Easy |

This skill is used when the character wants to try and move silently. The
following table describes possible modifiers:

| Terrain                              | Modifier                             |
|--------------------------------------|--------------------------------------|
| Stone                                | Trivial                              |
| Compact soil                         | Easy                                 |
| House wooden floor                   | Normal                               |
| Old wooden floor                     | Difficult                            |
| Dead Leaves                          | Hard                                 |
| Squeaky Floor.                       | Very Hard                            |

## Slash 

| <!-- --> | <!-- --> |
|------|----|
| Base | mS |
| Callsign |  |
| Category | Skill/combat |
| Cost | 1 TT/Easy |

A generic combat maneuver that can be used with any weapon, 
including improvised ones. Clubs made out of table legs, 
guns without ammunitions used as maces, and in general anything you 
swing at an opponent without knowing exactly what you’re doing is 
covered under this maneuver.

If the opponent is unaware, the skill requires a **CHK** at *easy* level.

In combat, the opponent can use any defense, and a normal combat **CFR** is performed.

The damage type depends on the nature of the weapon. It can be either cut or blunt.
On critical success, it applies stun for 1 turns.

## Stabilize

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Skill/combat |
| Cost | 1 TT/Easy |

The character can perform a *hard* simple check in order to save the life
of disable companions. 

Using a first-aid kit changes the difficulty of the check from *hard* to *easy*.

A critical success means that the character also heals its lightest wound. A 
critical failure causes the character to die immediately.

## Swordfight

| <!-- --> | <!-- --> |
|------|----------|
| Base | mS or mD |
| Category | Skill/combat |
| Dominance | 4 |
| Cost | 1 TT/Hard |

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

| Level | Maneuvers |
|-----|---|
| 1-6 | 1 |
| 7-11 | 2 |
| 12-15 | 3 |
| 17+ | 4 |

#### Cleave

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |
| Damage | __SM__+6 |
| Condition | (__Stun 2__) |

A vertical stroke, leveraging on the strength of the weapon welder.
A critical success stuns the opponent for 2 turns.

#### Deviate

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Swordfight 1 |
| DR | -1 |

A basic defense; the character intercept the opponent’s blow with its own
weapon, using its own dexterity.

#### Feint

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Swordfight 6 |
| DR | -2 |

Uses an attack that will not deliver damage on success,
to get a **DP** modifier equal to the success margin on the
damage of very next attack.

#### Parry

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |

A basic defense; the character intercept the opponent’s blow with
its own weapon, using its own strength to resist it.

#### Parry Projectiles

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Swordfight 6 |
| DR | -1 |
| Range | 30 ft |
| Limitation | Shield |

Can be used only if the character is wearing a shield. The defender
can block a projectile incoming from a maximum range of 30 feet.

#### Shield Bash

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -2 |
| Prereq | Swordfight 4 |
| DR | -2 |
| Damage Type | Blunt |
| Damage | __SM__-2 |
| Condition | (__Grounded__) |

Can be used only if the character is wearing a shield. The attacker
charges the opponent with its shield, trying to make it fall on the
ground. On success, the opponent is grounded for the rest of the turn.

#### Shield Parry

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS+3 |
| Prereq | Swordfight 2 |
| DR | -1 |
| Limitation | Shield |

Can be used only if the character is wearing a shield. The defender blocks
the opponent’s blow with its shield.

#### Slash

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |
| Damage | __SM__+6 |

A simple lateral stroke.

#### Thrust

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Swordfight 2 |
| DR | -1 |
| Limitation | Swords |
| Damage | __SM__+6 |

Thrusts a cutting weapon towards the opponent. Cannot be used with blunt or
two handed weapons (including swords).

## Throw 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Cost | 1 TT/Hard |

This attack consists in throwing a heavy object to an enemy in range.
Anything goes; even weapons, as long as the weight of the object is
between two and eight pounds weight.

The damage dealt is normally of __blunt__ type, unless the thrown object
is sharp; then it becomes of __cut__ type.

If the opponent is unaware, the skill requires a **CHK** at *normal* 
difficulty to succeed. In combat, a normal combat **CFR** against 
the opponent's defense is attempted.

A critical success applies also the stun condition for 1 turn.

## Thrust

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Cost | 1 TT/Normal |

A generic maneuver performed with any pointed or cutting weapon,
(always causing __cut__ damage),
including improvised ones. The character thrusts the weapon forward.

If the opponent is unaware, the skill requires a successful **CHK**
against *easy* difficulty.

In combat, a normal **CFR** is attempted against the opponent's defense.

## Treating Wounds

| <!-- --> | <!-- --> |
|----------|-----|
| Callsign | TrW |
| Category | Skill |
| Specialization | race type |
| Prerequisite | Healing 3 |
| Cost | 1 TT/Hard |

The character has advanced practical medical knowledge for the setting
where the adventure takes place, and is able to heal wounds of the target
creature race. 

The following table is applied when checking for the character success:

| Severity                         | Severity                         |
|----------------------------------|----------------------------------|
| Light                            | Easy                             |
| Severe                           | Normal                           |
| Heavy                            | Difficult                        |

Standard First-aid kits give a +6 modifier to heal *light wounds* only. 
Specific healing aids in the target setting can provide other modifiers.

The time required for the healing to be performed depends on the setting
and on the device used. A SF cellular replicator or a magic balm could
allow healing heavy wounds in one day, in a few hours or in minutes,
while in other settings, an herbal healing remedy might require a week.

The *race type* specifier is to be considered in large categories. For
example:
* Humanoids (Humans, elves, orcs etc.)
* Human-sized animals (dogs to deers)
* Small animals (birds, cats, etc.)
* Large animals (elephant, dragons, etc.)

## Willpower Defense 

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill/combat |
| Cost | 1 TT/Hard |

The willpower defense is used against mental attacks, whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available actions for
this turn.

## Break Free 

| <!-- --> | <!-- --> |
|------|-----|
| Base | D/2 |
| Callsign | Bfr |
| Category | Skill/combat |
| Cost | 1 TT/Normal |

This skill is used to try and break free out of an engaged block.
Unless the character is completely subdue, they can attempt a **Bfr**
each successive turn.

To successfully break free, a character must win a **RNK** against 
all the opponents that have achieved a successful lock in the previous turn.

## Traps

| <!-- --> | <!-- --> |
|------|---|
| Base | I |
| Category | Skill |
| Cost | 1 TT/Hard |

This skill represents the knowledge of the character about traps, and is used
to either detect, build or try and disarm traps, with the following modifiers:

| Height                           | Modifier                         |
|--------------------------------------|--------------------------------------|
| Build                                | Trivial                              |
| Detect                               | Normal                               |
| Disarm                               | Hard                                 |

Each tarp might come with a separate specific modifier in order to be
detected and disarmed. Once a trap is discovered (either through
this skill or by other means), the character might
attempt a separate check on Traps at easy difficulty to determine
its modifier prior attempting to disarm it.

# Combat

Combat is an advanced form of contest. In a normal contest, characters
try to win one over another on specific skills, while in combat,
contests are finalized to deal damage or other negative effects on
an unwilling target.

The Rule Book provides several sub-systems to resolve conflicts, increasingly
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

# Game Setup

With all the rules down, how to organize, prepare and run a game session?

(TODO)

## Character power

At times it's useful to have a rough estimate of the approximate power of a character. That
can be useful to determine at a glance if a certain adventure is too hard or too easy for
the players, or to decide how many enemies of a certain type it's fair to face in a fight.

How strong is a character is a matter of how the various skills have been trained. For this
reason, the **power** of a character is determined as the number of **main** training tokens
needed train all its skills, rounded up. 

To determine this value sum all the points spent on every skill and attribute, dividing them
accordingly with their relative hierarchy value.

- Mains: 1
- Primary: 1/2
- Secondary & Hard skills: 1/4
- Normal Skills: 1/8
- Easy Skills: 1/16

For example, a character has the following **mains** (notice that the base of all mains is 3):

- Body (3): 3 + 7 = 10  
- Mind (3): 3 + 6 = 9

These are the character primaries (again, we count the additional tokens spent on each attribute):

- Strength (**B**): 10 + 1 = 11
- Dexterity (**B**): 10 + 6 = 16
- Health (**B**): 10: 10 + 0 = 10
- Will (**M**): 9 + 3 = 12
- Intelligence (**M**): 9 + 5 = 14
- Equilibrium (**M**): 9 + 1 = 10

Then, the character has the following hard skills (baseless):

- Endurance: 5
- Engineering: 2

And the following normal skills:

- Deceit(**I**): 14 + 3 = 17
- Acrobatics(**D**): 16 + 1 = 17

The power is then:

* Points from the mains: 7 + 6 = 13
* Points from the primaries: (1 + 6 + 3 + 5 + 1 = 16) / 2 = 8
* Points from the hard skills: (5 + 2 = 7) / 4 = 1.75
* Points from the normal skills: (3 + 1 = 4) / 8 = 0.5

For a grand total of 13 + 8 + 1.75 + 0.5 = 23.25, rounded up to 24.

> It may be useful to note down the number of tokens actually spent
rather than recompute the power of the characters each time it's needed,
keeping track of the character power as it grows.
