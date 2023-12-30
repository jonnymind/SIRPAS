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
[advantage system in the rulebook](https://jonnymind.github.io/SIRPAS/Rulebook.html/#advantages-and-disadvantages), 

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
