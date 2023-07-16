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
|------|---|
| Base | 3 |
| Category | Main |

The Body (**B**) is a value that describes your overall physical prowess in terms of
bodily strength, resilience to prolonged efforts, recovery speed, resistance to
illness and so on. For humans, it is measured in the range between 3 and 18 (the
possible outcomes of 3d6). Most adult characters score in the range between 10
and 12, with 18 representing a person with the best possible body (rarely if
ever ill, strong as the strongest wrestler or weight lifter, moving as swift as
a record runner and able to run as long as a marathon champion — all at the same
time), and 3 representing the weakest possible fully formed and barely
functional body.

## Mind

| <!-- --> | <!-- --> |
|------|---|
| Base | 3 |
| Category | Main |

The Mind (**M**) is the overall score of mental abilities in terms of intelligence, 
creativity, will power, mental sanity, depth of knowledge and so on. 
A mind level 3 represents a character that is barely functional as an autonomous person (or
creature) in the reference setting, while a 18 represents a character maximally intelligent, 
penetrating, knowledgable, sane and wise. The vast majority of characters (or heroes)
in the reference setting will have a mind between 10 and 12.

## Strength

| <!-- --> | <!-- --> |
|------|---|
| Base | B |
| Category | Primary |

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
|------|---|
| Base | B |
| Category | Primary |

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
|------|---|
| Base | B |
| Category | Primary |

Health (**H**) represents the resistance to fatigue, illness and polluted 
environment (including allergenic agents). It's used to determine how many
injuries can be withstood before being incapacitated,
and gives the base for all physical resistance skills.

## Will

| <!-- --> | <!-- --> |
|------|---|
| Base | M |
| Category | Primary |

Will (**W**) is the power of the mind to focus on a certain task, 
perform prolonged mental activity, keep determination in 
adverse situations and so on. It can be roughly thought as the 
equivalent of the strength (**S**) in the mind realm.

## Intelligence

| <!-- --> | <!-- --> |
|------|---|
| Base | M |
| Category | Primary |

Intelligence (**I**) is the ability to understand and solve complex problems, 
comprehend difficult study subjects, see through schemes and machinations 
etc. As it measure the flexibility of the mind processes, it can be thought 
as the dexterity (**D**) of the mind.

## Equilibrium

| <!-- --> | <!-- --> |
|------|---|
| Base | M |
| Category | Primary |

Equilibrium (**E**) is the stability of the mind, 
or basically the equivalent of its health (**H**). It indicates 
how much mental strain a person can take before being debilitated; 
of course, it is important in those settings where attacks are delivered 
to the mind instead of the body: fantasy, sci-fi and horror settings 
can present as many dangers for the mind as for the body, or more.

Hence, it forms the base of all the mental resistance skills.

# Advantages

Advantages special conditions that apply to the character in general 
or to a specific skill in particular, and that have a direct effect 
on some game mechanics.

Advantages can be bought for a certain number of **training tokens**
of a certain type; the more powerful the advantage, the more high
level the training tokens needed to train a point.

While most advantages are simply possessed by a character or not,
some can have different levels. In that case, the cost of
each ulterior point will be the cost of the base previous level plus one
token of the same type.

For example, **Survival Instinct** can have a level between 1 and 4, 
each granting a higher modifier. The first level costs 3 **TT**/*Normal*;
this means that level 2 costs 4 **TT**/Normal, level 3 costs 5 **TT**/*Normal*
and level 4 costs 6 **TT**/*Normal*.

Some advantage could have a pre-requisite that must be fulfilled in order to be acquired. 
For example, they could require having already acquired another advantage, 
or having a certain attribute at a minimum set score.

## List of advantages


- [Battleproof](#battleproof)
- [Born in a Mourning Hall](#born-in-a-mourning-hall)
- [By the skin of one's teeth](#by-the-skin-of-one's-teeth)
- [Combative spirit](#combative-spirit)
- [Deep Mind](#deep-mind)
- [Defense Expert](#defense-expert)
- [Easygoing](#easygoing)
- [Elemental Resistance](#elemental-resistance)
- [Expertise](#expertise)
- [Fast Paced](#fast-paced)
- [Hard Skin](#hard-skin)
- [Hard to Die](#hard-to-die)
- [Keen Eye](#keen-eye)
- [Mastery](#mastery)
- [Natural](#natural)
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
being incapacitated. The first physical wound is received during a fight will
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

## Defense Expert

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Combat style |
| Cost | 2 TT/Normal |

The character can perform one additional defense with the selected 
style per combat turn in one specific combat style. It's possible
to get this advantage for multiple styles.

## Easygoing

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 2 TT/Normal |

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
| Specialization | Skill |
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

Combat styles and other combat skills can be targeted by
mastery.

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

| <!-- --> | <!-- --> |
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

## Blind {#BaM-a-blind}

*Cost*: -40 CP

The character is blind. A character can minimize the effect
of this drag through different means, but cannot use any functional
substitute of normal vision unless it refunds the cost.

For example,
having a dog companion that guides the character through every
possible obstacle is still blindness, but having the ability to
communicate telepathically with demonic minions and use their
sight, or using a cyber plant that provides visual sensor stimuli
directly to the brain is not allowed.

## Criminal {#BaM-a-criminal}

*Cost*: 10 CP

The character is an active criminal. It is in hiding and
actively searched by the local law enforcement, and is in
contact with other criminals and criminal organisations.

The character has an initial wealth of 25,000$.

Add 5 CP if the character is also member of an active criminal
organisation. In this case, the character will have an initial
wealth of 50,000$ and a monthly wage of 3,000$, but it must abide
to the rules of the criminal organisation it is part of.

This perk grants a modifier of +2 to Intimidate.

Law Enforcer, Criminal Background, Criminal Boss and Criminal
are mutually exclusive: the character can chose only one of
them.

## Criminal Background {#BaM-a-criminal-background}

*Cost*: 10 CP

The character was a member of a criminal organization, and has
retained contacts with the ambient.

Characters with this perk have a +2 modifier to Persuade and +1 to
Intimidate.
Law Enforcer, Criminal Background, Criminal Boss and Criminal are
mutually exclusive: the character can chose only one of them.

## Criminal Boss {#BaM-a-criminal-boss}

Cost: variable.
The character is the leader of a criminal organization. It has a
relatively large network of criminals that follow his orders, a
consistent wealth and a flux of incoming money. On the other side,
it’s known to relevant police forces, constantly at risk of being
arrested and not always welcome in high social circles.

The size of the organization determines the cost in terms of points:

| Size               | Wealth             | Monthly Income     | CP                 |
|:------------------:|-------------------:|-------------------:|-------------------:|
| \< 10              | 100,000\$          | 5000\$             | 20                 |
| 10-20              | 250,000\$          | 7000\$             | 30                 |
| 20-50              | 1M\$               | 20,000\$           | 50                 |
| \>50               | 5M\$               | 100,000\$          | 75                 |

This perk grants a modifier of +4 on Intimidate checks and comparisons
against anyone, excluding other characters with the Criminal Boss perk.

Law Enforcer, Criminal Background, Criminal Boss and Criminal are
mutually exclusive: the character can chose only one of them.

## Crippled {#BaM-a-crippled}

*Cost*: -15 or -20 CP

The character has one arm (-15 CP) or one leg (-20 CP) non
functional or missing.

## Deaf {#BaM-a-deaf}

*Cost*: -30 CP

The character is deaf. A character can still use this drag even if it has a 
substitute for normal hearing, provided the substitute is just minimizing
the disadvantage. For example, having a laptop/tablet/phone that provides
the character with speech-to-text recognition is still being deaf, but
having the ability to communicate telepathically with demonic minions and
use their hearing would invalidate this drag.

## Famous {#BaM-a-famous}

| <!-- --> | <!-- --> |
|------|--|
| Spec |  |
| Cost | 10/15/20 CP |
| Prereq | - |
| Max | - |

The character is famous and easily identified by its peers.
Also, whoever wants to know about the character, or searching
for it because of any specific reason (i.e. to hire it for
a job, or to hunt it down), can easily find information
about it and its general whereabouts, unless the character
actively disguises and hides.

The cost depends on how famous the character is:

* 10CP: Known by 1/20th-1/10th of the population; people
occasionally identify it when walking by, or tells it
they heard about it.
* 15CP: Known by 1/5th of the population. During a day out,
or a long walk, the character is sure to be recognized,
and possibly stopped by admirers (or haters).
* 20CP: Known by more than half the population. Wherever the
character goes, it is recognized, and when that happens,
people flocks to see it.

## Field Expert {#BaM-a-field-expert}

*Cost*: 10 CP

The character is an expert in some relevant field of study: physics, psychology,
economics, information technology, regional lore, world lore, history etc.
This perk can be bought once per specialization field, and can be upgraded
(immediately or later on) to Renown Field Expert.

## Law Enforcer {#BaM-a-law-enforcer}

*Cost*: 15 CP or 20 CP

The character is a member of Police or equivalent Law Enforcement agency. This
includes also roles of Acting Inspectors and Prosecuting Judges.

The character has an initial wealth of 20,000$ and a monthly wage of 1,000$. 
Add 5 CP to be in higher ranks of Law Enforcement (Tenant in a police
station, Prosecution Judge). In this case, the initial wealth will be
40,000$ and the monthly wage will be 2,000$.

However, the character needs to respect the rules of Law Enforcement
(or face the consequences), and fulfill direct orders from the upper
ranks.

The perk gives a modifier of +2 to Persuade and -1 to Intimidate.

## Medical Knowledge {#BaM-a-medical-knowledge}

*Cost*: 12CP

The character knows relatively advanced medical treatment techniques.
It can be either a medic, a surgeon or a researcher. Its knowledge is
also correct, regardless of the technological level of the setting. For
example, even if set in a medieval period, the character knows how to
actually cure most illnesses, and the correct prophylactic procedure to
minimize the spread of diseases as the plague.

A character with this perk gains First Aid, and has a modifier of +6 on
all medical skills.

## Renown Field Expert {#BaM-a-renown-field-expert}

*Cost*: 10 CP
__*Prerequisite*__: *Field Expert*

The character is a renown authority in some relevant field of study: physics,
psychology, economics, information technology, regional lore, world lore,
history etc.

It has the same effect of the perk Famous, limited to the other people expert in
the same field.

This perk can be bought only if the character has also bought the Field Expert
perk on the same field.

## Wheelchair {#BaM-a-wheelchair}

*Cost*: -25 CP

The character legs are non functional, and it needs assistance or mechanical
devices to walk. This is not a drag in settings where the technology to
fully substitute body parts is readily available.

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

## Active Mitigation (-; H) {#BaM-s-active-mitigation}

The character can mitigate a damage equal to the success margin once per
turn.

## Charisma (M) {#BaM-s-charisma}

Used to influence positively other characters. Not to be confused with
*Persuade*. This skill is specifically meant for characters trying to
make a good impression, obtain favours, special treatments, or a
generic good attitude. Persuade is the skill to deliver one specific
talk with persuasive power.

## Chemistry (-; H) {#BaM-s-chemistry}

Technical knowledge of modern chemistry.

## Climbing (D; E) {#BaM-s-climbing}

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

## Deceit (I) {#BaM-s-deceit}

It’s the ability to say a credible lie.

## Endurance (H) {#BaM-s-endurance}

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

## Engineering (-; H) {#BaM-s-engineering}

Technical skill in modern engineering.

## First Aid {#BaM-s-first-aid}

| <!-- --> | <!-- --> |
|------|---|
| Base | - |
| Type | N |
| Prereq | - |
| Spec |  |

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

## Hacking/System (-; H) {#BaM-s-hacking}

When a character wants to hack a device or a system, it can roll on this to
check if it has the necessary knowledge to hack the system.

Each action requires a different check. A critical failure implies the hacking
has been neutralised and the source identified. A critical success implies that
the character has gained privileged access, and further actions on the same
system will not require a separate check.

The specifics of the system depend on the setting. For some settings, the
hacking skill could be general, while in other settings specific systems will be
identified, and they might require a separate hacking skill.

## Healing/Race {#BaM-s-healing}

| <!-- --> | <!-- --> |
|------|---|
| Base | - |
| Type | H |
| Prereq | First-aid 3 |
| Spec | Race |

The character has advanced practical medical knowledge for the setting
where the adventure takes place, and is able to heal illnesses, poisoning
and equivalent conditions for the target settings.

For instance, in a magic world where curses can cause illnesses, this
skill can also be used to treat the effect of the curses.

In a virtual words where AIs can be infected with viruses, this skill
can be used to run an anti-virus.

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
the *success margin* can be used by the *GM* to decide how fast the recovery is.

Ilnesses that are *difficult* or *hard* to cure will be transformed in *easy*
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

## Hiding (I; E) {#BaM-s-hiding}

The character knows how to hide so to look like inconspicuous material
(i.e. a sack of potatoes, a part of a load of straw on a cart, a roll
of cloth and so on). The difficulty of the check is determined by the GM.

## Hiding in Shadows (mD) {#BaM-s-hiding-in-shadows}

The character knows how to hide in dark places, or pass unobserved in a
crowded place.

## Initiative (D/W; H) {#BaM-s-initiative}

This skill represents the reaction times and determination under pressure of
the character. It is typically used in contests or rankings, to decide who
acts first during a stalemate, but it can be also used in checks. The order
in which a combat turn develops is decided by a ranking on the initiative
of all the involved characters.

The base is either Dexterity or Will, the best of the two.

## Intimidate (W) {#BaM-s-intimidate}

Intimidate is the action of menacing someone that some negative outcome will
follow, unless they don’t comply with some desired course of actions. For
intimidation to be effective, the menace must be credible, and the target
must actually wish for that not to happen.

## Investigation (I; H) {#BaM-s-investigation}

The ability to find hidden clue or draw correct conclusions with a limited
amount of clue. Particularly useful when visiting the scene of a crime.

## Lie Detection (mI; H) {#BaM-s-lie-detection}

This skill represents the ability of the character to detect lies, given
small hints on the voice, facial expressions and behaviour of the target.

A skilled lier can oppose its deception. Otherwise, the character can try
a check on this skill, with a difficulty that depends on the amount of
information the character has about the truth.

## Lock Picking (-) {#BaM-s-lock-picking}

Used to try opening normal locks. The lock must be within the reach of the technological knowledge of the character. The character must have also proper tools at its disposal to try the action.

## Lore Knowledge/field (-; E) {#BaM-s-lore-knowledge}

This skill represents the knowledge of the character about lore and stories in
the setting where the adventure takes place. The skill is specific for lore
types; for example, it can be targeted at norse mythology, egyptology, local
lores etc.

To check wether a character knows a specific lore it gets in contact with, check
against a difficulty which depends on how widespread the knowledge is,
considered the specific setting where the adventure takes place.

A lore everyone knows is checked as “trivial”, one that is particularly obscure
an known only to experts or initiates is “very hard”.

## Perception (W; H) {#BaM-s-perception}

Determines whether the character is able to detect an element in the surrounding
that is hard to spot, as a secret door, a potential danger, a follower and so
on.

It is used when there aren’t more specific skills to be applied in the specific
situation. For example, trying to find traps is done by rolling on traps.

## Persuade (I) {#BaM-s-persuade}

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

## Pickpocket (hD) {#BaM-s-pickpocket}

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

## Poisons (-) {#BaM-s-poisons}

Technical knowledge for recognizing (_normal_) and producing (_hard_) poisons.

## Resistance/source {#BaM-s-resistance-source}

| <!-- --> | <!-- --> |
|------|-------|
| Base | H/E/- |
| Type | H |
| Prereq | - |
| Spec | **DP** source type |

The character has aqcuired a specific resistance against
a determined damage source. The base of the resistance
depends on the macro-category of the danage source,
as specified in the following table:

| Damage type | Base        |
|-------------|-------------|
| Physical    | Health      |
| Mental      | Equilibrium |
| Elemental   | Elem. Res.  |

The advantage [Elemental Resistance](BaM-a-elemental-resitance) gives
the base against elemental damage.

## Riding/mount (mD) {#BaM-s-riding}

This skill is used to perform particularly difficult actions while riding a
specific animal. For example, jumping a fence with a horse, jumping across
acrobatic platforms with a motor bike, running through a busy skyline with a
flying car and so on.

The skill is specific for each device (or animal) that the character might ride.
Some riding specialisation can be baseless, if learning them requires a specific
preparation (for example, helicopter pilot).

## Running (D) {#BaM-s-running}

Running is the skill used when deciding which character wins a run race.
It can also be used to check if a character is able to run for a long time.

## Silent Movement (D) {#BaM-s-silent-movement}

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

## Stabilize {#BaM-s-stabilize}

| <!-- --> | <!-- --> |
|------|---|
| Base | I |
| Type | E |
| Prereq | - |
| Spec |  |

The character can perform a *hard* simple check in order to save the life
of disable companions. 

Using a first-aid kit changes the difficulty of the check from *hard* to *easy*.

A critical success means that the character also heals its lightest wound. A 
critical failure causes the character to die immediately.

## Treating wounds/Race Type {#BaM-s-treating-wounds}

| <!-- --> | <!-- --> |
|------|---|
| Base | - |
| Type | H |
| Prereq | First-aid 6 |
| Spec | Race Type |

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
* Large animals (elefant, dragons, etc.)

## Traps (I; H) {#BaM-s-traps}

This skill represents the knowledge of the character about traps, and is used
to either detect, build or try and disarm traps, with the following modifiers:

| Height                           | Modifier                         |
|--------------------------------------|--------------------------------------|
| Build                                | Trivial                              |
| Detect                               | Normal                               |
| Disarm                               | Hard                                 |

Each tarp might come with a separate specific modifier in order to be
detected and disarmed. Once a trap is discovered, the character might
attempt a separate check on Traps at normal difficulty to determine
its modifier prior attempting to remove it.

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

| <!-- --> | <!-- --> |
|------|------|
| Cost | 4 CP |
| Type | Defense |
| Modifier | mD |

Disengage is a defense allowing to move half the normal movement speed in the current turn. It automatically succeeds if the opponents are not trying to attack the character using it.
On failure, the disengagement fails and the character cannot move.
If the contest succeeds, the character can move even if other subsequent attacks succeed.

### Instincitve Defense {#BaM-s-generic-combat-instinctive-defense}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 3 CP |
| Type | Defense |
| Modifier | mD |

The instinctive defense is used against physical attacks whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available maneuvers for this turn.

It’s ineffective against mind attacks.

### Shoot {#BaM-s-generic-combat-shoot}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 6 CP |
| Type | Attack |
| Modifier | -1 |
| Range | 30 ft |
| Damage Type | Piercing |
| Damage | __SM__+4 |

Shoot with a projectile weapon while not being skilled to do so.
Weapons requiring skill in being loaded (i.e. bows, special military
rifles etc.) cannot be used with this skill, but loaded weapons (i.e.
crossbows) can.

### Slash {#BaM-s-generic-combat-slash}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 5 CP |
| Type | Attack |
| Modifier | mS |
| DR | -1 |
| Damage | __SM__ |
| Condition | __(Stun 2)__ |

A generic combat maneuver that can be used with any weapon, including improvised ones. Clubs made out of table legs, guns without ammunitions used as maces, and in general anything you swing at an opponent without knowing exactly what you’re doing is covered under this maneuver.
The damage type depends on the nature of the weapon. It can be either cut or blunt.
On critical success, it applies stun for 2 turns.

### Throw {#BaM-s-generic-combat-throw}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 5 CP |
| Type | Attack |
| Modifier | mS |
| DR | -1 |
| Range | 15 ft |
| Damage Type | blunt/cut |
| Damage | __SM__ |
| Condition | __(Stun 2)__ |

This attack consists in throwing a heavy object to an enemy in range.
Anything goes; even weapons, as long as the weight of the object is
between two and eight pounds weight.

The damage dealt is normally of __blunt__ type, unless the thrown object
is sharp; then it becomes of __cut__ type.

A critical success applies also the stun condition for 2 turns.

### Thrust {#BaM-s-generic-combat-thrust}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 5 CP |
| Type | Attack |
| Modifier | mD |
| DR | -1 |
| Damage Type | cut |
| Damage | __SM__ |

A generic maneuver performed with any pointed or cutting weapon,
(always causing __cut__ damage),
including improvised ones. The character thrusts the weapon forward.
On success, it causes a piercing damage for half the success margin
plus the dexterity.

### Willpower Defense {#BaM-s-generic-combat-willpower-defense}

| <!-- --> | <!-- --> |
|------|------|
| Cost | 3 CP |
| Type | Defense |
| Modifier | mW |

The willpower defense is used against mental attacks, whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available maneuvers for
this turn.

## Archery {#BaM-s-archery}

| <!-- --> | <!-- --> |
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

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Archery 3 |

Take a maneuver to improve the next attack, giving it a modifier of +1.
It can be repeated any number of times within a single turn, but the
modifier is applied only to the very next Shoot.

### Localized Shot {#BaM-s-localized-shot}

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

### Overextend {#BaM-s-overextend}

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

### Overload {#BaM-s-archery-overload}

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

### Shoot {#BaM-s-archery-shoot}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Archery 1 |
| Damage | __SM__+4 |

Loads and shoot an arrow or a bolt.

### Brawl {#BaM-s-brawl}

| <!-- --> | <!-- --> |
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

### Evade {#BaM-s-brawl-evade}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Brawl 1 |
| DR | -1 |

Try and evade an attack moving the body out of the way of the incoming hit.

### Grapple {#BaM-s-brawl-grapple}

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

### Kick {#BaM-s-brawl-kick}

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

### Punch {#BaM-s-brawl-punch}

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

### Smash {#BaM-s-brawl-smash}

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

## Concentration {#BaM-s-concentration}

| <!-- --> | <!-- --> |
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

### Block  {#BaM-s-concentration-block}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mW |
| Prereq | Concentration 1 |
| DR | -1 |

The character raises a mental barrier in order to block an incoming attack.

### Dig into you  {#BaM-s-concentration-dig-into-you}

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

### Divert {#BaM-s-concentration-divert}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mI |
| Prereq | Concentration 1 |
| DR | -1 |

The defendant diverts the attention of the attacker on an irrelevant
thought or memory, causing the attack to miss.

### Mind Grasp  {#BaM-s-concentration-mind-grasp}

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

### Sensations {#BaM-s-concentration-sensations}

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

### Yes, but you... {#BaM-s-concentration-yes-but-you}

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

## Firearms {#BaM-s-firearms}

| <!-- --> | <!-- --> |
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

### Aimed Shot {#BaM-s-firearms-aimed-shot}

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

### Duck {#BaM-s-firearms-duck}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Firearms 2 |

Duck or evade while holding the firearm to avoid incoming fire.

### Fast Reload {#BaM-s-firearms-fast-reload}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Actions |
| Prereq | Firearms 4 |

Ability to reload the weapon in the heat of the combat, using a
maneuver.

### Localized Shot {#BaM-s-firearms-localized-shot}

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

### Point Blank {#BaM-s-firearms-point-blank}

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

### Rapid Fire {#BaM-s-firearms-rapid-fire}

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

### Shoot {#BaM-s-firearms-shoot}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Prereq | Firearms 1 |
| Damage | __SM__+7 |

Normal base attack with firearms.

### Take Cover {#BaM-s-firearms-take-cover}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | +3 |
| Prereq | Firearms 3 |
| DR | -2 |

If a cover is within movement range for the turn, the character can use this defense to run towards a covered position, with a fixed +3 modifier.

## Full Contact {#BaM-s-full-contcat}

| <!-- --> | <!-- --> |
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

### Counter kick {#BaM-s-full-contact-counter-kick}

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

### Crouch {#BaM-s-full-contact-crouch}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Full Contact 3 |

The character loads the next attack, receiving a **DP** modifier equal
to the success margin to be used in the very next attack in Brawl
or Full Contact styles.

If the next maneuver used is not an attack, or if the attack fails, 
the modifier is lost.

### Elbow Blow {#BaM-s-full-contact-elbow-blow}

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

### Knee Blow {#BaM-s-full-contact-knee-blow}

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

## Knife Fight {#BaM-s-knife-fight}

| <!-- --> | <!-- --> |
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

### Backstep {#BaM-s-knife-combat-backstep}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |

Skip back, trying to get out of the range of a melee attack.

### Belly Opener {#BaM-s-knife-combat-belly-opener}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -1 |
| Prereq | Knife Fight 3 |
| DR | -2 |
| Damage | __SM__+5 |

Swing the blade in an upward strike, aiming at the lower part of the opponent
body.

### Change Hands {#BaM-s-knife-combat-change-hands}

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

### Downstab {#BaM-s-knife-combat-downstab}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 2 |
| DR | -2 |
| Damage | __SM__+4 |

Swing the blade in a downward strike, aiming at the upper part of the
opponent body.

### Evade {#BaM-s-knife-combat-evade}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |

Try and evade an attack.

### Feint {#BaM-s-knife-combat-feint}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | +3 |
| Prereq | Knife Fight 3 |
| DR | -2 |

Fake an attack, without actually completing it. On success it doesn’t
deal damage, but gives a **DP** modifier on the next move equal to
the success margin.

### Hand Cutting {#BaM-s-knife-combat-hand-cutting}

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

### Spring Up {#BaM-s-knife-combat-spring-up}

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

### Throw {#BaM-s-knife-combat-throw}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |
| Damage | __SM__+1 |
| Condition | (__Cripple__) |

Throws the knife at an opponent within 15 feet. On success, it deals a limited damage.

### Thrust {#BaM-s-knife-combat-thrust}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| DR | -1 |
| Damage | __SM__+4 |
| Condition | (__Cripple__) |

Attacks the target thrusting the knife forward, in a straight line.

### Wrap and Stab {#BaM-s-knife-combat-wrap-and-stab}

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

## Swordfight {#BaM-s-swordfight}

| <!-- --> | <!-- --> |
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

### Deviate {#BaM-s-swordfight-deviate}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Swordfight 1 |
| DR | -1 |

A basic defense; the character intercept the opponent’s blow with its own
weapon, using its own dexterity.

### Feint {#BaM-s-swordfight-feint}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Swordfight 6 |
| DR | -2 |

Uses an attack that will not deliver damage on success,
to get a **DP** modifier equal to the success margin on the
damage of very next attack.

### Parry {#BaM-s-swordfight-parry}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |

A basic defense; the character intercept the opponent’s blow with
its own weapon, using its own strength to resist it.

### Parry Projectiles {#BaM-s-swordfight-parry-projectiles}

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

### Shield Bash {#BaM-s-swordfight-shield-bash}

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

### Shield Parry {#BaM-s-swordfight-shield-parry}

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS+3 |
| Prereq | Swordfight 2 |
| DR | -1 |
| Limitation | Shield |

Can be used only if the character is wearing a shield. The defender blocks
the opponent’s blow with its shield.

### Slash {#BaM-s-swordfight-slash}

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| DR | -1 |
| Damage | __SM__+6 |

A simple lateral stroke.

### Thrust {#BaM-s-swordfight-thrust}

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

## Weapons

Weapons are either used unskillfully, using any one of the Generic Combat Skills, or through the appropriate combat style. The default damage (and often, damage type) caused by the weapon is already accounted for in the combat style; for example, Firearms/shoot causes a higher damage than Brawl/punch because guns are more lethal than bare hands.
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
rather than recompute the power of the characters each time it's needed
looking at the value of all of their attributes
