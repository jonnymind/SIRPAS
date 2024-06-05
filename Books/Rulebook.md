# SIRPAS Ruleset Manual

# Introduction

SIRPAS stands for "SImple Role Playing Adventure System". It's a generic, modular
and extensible table-top RPG system, that aims to be as simple as needed and
become as complex as you wish.

## A system for everyone

Sirpas is for everyone: beginners, intermediate and veteran players.

However, this manual takes the basic concepts of RPGs for granted; 
it doesn't explain how to prepare, organize, manage, or behave during a 
game session. This rulebook presents the game as succinctly as possible;
all the concepts commonly known in RPG can be easily found in the larger
Internet, and may be introduced in a different manual.

## Play Any World

Sirpas is a generic role playing system, that doesn’t presume anything on the
setting of your adventures. The system applies whatever your players might want
to play; as normal people struggling to survive in a post-apocalyptic world, as
wizards and knights in a high fantasy setting, as cyborgs in a SF plot, or even
as AIs in a virtual reality.

## Combatless Adventures

In most RPG settings, combat is a central part of the game action, if not the
absolute protagonist. This leads to RPG systems being usually structured around
the combat mechanics, and gaming sessions being mainly occupied by detailing
combat actions.

SIRPAS works the other way around: the combat system is simply the
specialization of the general system. As such, is possible to run adventures or
entire campaign devoid of "combat", and focusing either on other kind of contest
(as i.e. skill battles in virtual worlds), or in other aspects of the role
playing altogether.

Consider, for example, a police drama as a RPG setting. While gunfights might
play an important part in the campaign, the very nature of a gunfight doesn’t
translate into interesting RPG mechanics, while more interesting actions as
sword fights or martial art fights might not fit the setting.

As such, SIRPAS focuses on a more differentiated gameplay, which can be as
combat-intensive or combat-devoid as needed.

## Ruleset and Skillset

SIRPAS is based on a *ruleset* and one or more *skillsets*. Together, they 
describe how to use the *roleplaying mechanics*: they explain how to perform 
certain action, attack or defend in combat, cast a magic spell and so on,
perform an athletic feat and so on.

A *skillset* is a set of numerical and qualitative attributes that describe
the abilities of a character. *Strength*, *dexterity*, *ancient knowledge*, 
*piloting vehicles* and so on would be some of the attributes defined by a
*skillset*.

The *ruleset* describes how any skillset in the SIRPAS system works.

This manual contains the *ruleset* and the *generic skillset*, which 
can be used in most scenarios and game worlds directly any modification.

To make this manual simpler to use, the **generic skillset** is presented together
with the parts of the *rulset* it refers to, in sections separated by the heading
"Generic Skillset". Despite being in the same manual, the *generic skillset* should
not be considered a mandatory part of the SIRPAS system: it's just a basic 
implementation, ready for use to start playing right away.

**Example**: the *ruleset* indicates that
characters participating in a fight need to perform a *ranking check* to determine
the order in which they can perform their action, but doesn't indicate which skill
is to be used for the ranking. The *generic skillset* defines an **Initiative** skill,
which is based on either **Dexterity** or **Will** attributes, that is used to perform 
the ranking. Another *skillset* may:

* redefine the **Initiative** skill to be based on different
characteristics: for example, it may be baseless or based on **Computational Speed** for AIs; or
* set up a different skill for the purpose; for example, in a western epic setting it
  may be **Gunslinging**.

### Limits of the Generic Skillset

The *generic skillset* should be directly applicable to 
many different scenarios; from realistic historical settings to high-fantasy 
realms, from space operas to cyberpunk future cities. However, it assumes that the
playing characters are either humans, and that their feat are somewhat grounded in common human 
experiences. It may be not adequate to describe worlds where characters are completely different;
for example, body-less AIs, Chinese opera Wu-xia semi-gods, giant robots, starships etc. 
could require a completely different skillset.

Some settings could leverage the *generic skillset* by just adding or altering some
aspects, while others may use a completely different set of skills. 
For example, a setting about a war between lycanthropes and vampires may be based
on the the generic skillset and:

* Add a primary attribute besides **Body** and **Mind**, i.e. **Darkness**.
* add some skills that only lycanthropes or vampires can have.
* tweak the maximum values beyond 18 to reflect super-human abilities.

On the other hand, a Cthulhu-eqsue adventure setting may ditch the concept of 
**Body** and **Mind** entirely, and just define a **Sanity** primary attribute.

# Statistics

In SIRPAS, the statistics are all the numeric or quality values that define a characters. 
They are divided in the following categories:

- [Attributes](#attributes): important aspect of the character on which many other mechanics depend. 
  For example *body*, *strength*, or *spirit* could be attributes in many game worlds.
  **Skills** are special **attributes** used to perform specific actions, 
  as *hacking*, *lock picking*, *running*, *climbing* etc.
- [Statuses](#statuses): values that vary fluidly during an adventure; for example,
  to keep track of the current health of a character you can look at its **injury points**.
- [Vantages](#vantages): **advantages** or **disadvantages** targeting either the
  rules as a whole or improving a specific attribute in some way. For example, some advantages
  allows you to throw more die in some situation, others may reduce the difficulty
  of actions performed with a certain skill.
- [Backgrounds](#backgrounds): distinctive traits setting the character apart from the 
  background people in the setting; for example, being "famous" or "outlaw". 
  They have an impact in the adventure at large, and might also affect indirectly 
  some checks, providing bonuses and penalties at discretion of the game master.

## Attributes and Skills

Attributes describe a character as succinctly as possible.

Main attributes, describe the overall build of a character, indicating their
characteristics in broad categories as physical and mental, spiritual, magical, technological etc.

Skills are specialized attributes that are used to perform specific actions.

1. *Primary attributes* (or *primaries*) describe the overall build of your character.
2. *Secondary attributes* (or *secondaries*) are specializations of *primaries*
   to better describe the overall character capabilities.
3. *Hard Skills* require special training on top of the natural prowess granted by the attributes.
4. *Normal skills* just require a basic training on top of the natural abilities of a character.
5. *Easy skills* can be performed by anyone, although a special training may grant a character
    better results.

Attributes are normally expressed as a value between 3 and 18, 
which is the range of value that can be expressed by summing the 
result of a 3d6 dice throw. A value of 3 represents the minimum skill 
level, or characteristic, that a character could have to be still 
considered minimally functional in the game world — a value below 3 
would indicate a sub-normal characteristic. A value of 18 would represent 
the apex for the game environment, and the values between 10 and 12 would be 
the most common across the reference population.

The scaling would be relative to the game setting. For example, if playing 
a campaign where the characters are Greek or Norse gods, a value of 3 on any 
statistic would probably express a level of proficiency far superior to that of
any human.

Notice that the scaling is not linear: it follows the probability distribution
of the 3d6 dice throw. For example, a character with strength 12 is just marginally 
stronger than one with strength 11, but one with strength 18 is in a totally 
different league than one with strength 17. Similarly, characters with health 
10 and 11 have a very similar constitution, but one with health 3 will 
be much weaker than one with health 4.

### Most specific attribute

As attributes are ordered in a hierarchy, the base of each of them indicating their parent,
when a character needs to perform an action for which a specific attribute is not provided
by the game module in use, the Game Master will chose the best approximation possible.

Example: Suppose the game module provides the attributes **charisma**, base for **elegance**,
which is base for **etiquette**. If the character needs to perform a correct ballroom 
introduction, **etiquette** will be chosen; to determine how well they dance (provided 
there isn't a **dance** skill available), **elegance** will be next in the line, and
to determine the impression left with some chit-chat after the dance, **charisma** will be
used.

### Base value

In general, it's common for higher level attributes to 
form the **base** of the lower level ones, which are said to be their **dependent** 
attributes. Every dependent attribute has a **base value**,
a default value that depends on the current value of its base.

Whenever a base attribute improves for any reason, all the dependents improve as well. 
Of course, improving attributes that form the base of many others is typically more 
difficult than improving the dependents.

For example, suppose that in a game world the attribute **Arm Wrestling (AW)** based on
for **Strength (S)**. A character that has never learned any specific arm wrestling trick
has the same value in **AW** and **S**. If **S** is 10, **AW** is 10 as well.
If the character trains
on **AW**, it may get an extra point and have **S**=10, **AW**= **S**+1 =11. 
If the character then trains on general **S** (which is harder than specialize in **AW**),
so that its **S**=11, its **AW** grows too, as now **AW** = **S**+1 = 12.

> Not all the attributes have bases; those at the top of the hierarchy, even some skill
that cannot be classified or inherit any base value are called **baseless**, and their
default value is 0 unless differently specified.

### Base Modifiers

In some situation, instead of using an attribute as a direct base, 
the system requires to use a *modifier* that depends on the value
of the base. Those are called **base modifiers**.

This happens when some attributes are hard to train, and so
they need to be learned almost from scratch, but some other
attribute may give a minor advantage. For example learning
**lores** requires studying them; there is no way around actually
opening the books (or any equivalent media). However, a high
**intelligence** may help both to memorize and grasp some aspect or
detail that would pass unnoticed by most. In such cases, the
**intelligence** cannot be a direct base for **lores**, but could
well provide a base modifier.

The following table indicates the **base modifier** associated with
the value of the base attribute. 

| Attribute | Modifier |
|:---------:|---------:|
|    3-5    |       -3 |
|    6-7    |       -2 |
|    8-9    |       -1 |
|   10-11   |        0 |
|   12-13   |       +1 |
| 14-15     |       +2 |
| 16-18     |       +3 |
To indicate that the modifier of an attribute is base for another, the
attribute is prefixed with a lower case "**m**". For example, 
Suppose a skill like **swimming** is based on the modifier of an
attribute called **Dex**. The base of **swimming** will be then
expressed not as **Dex**, but as m**Dex**.

### Type or base values

While attributes are organized in a hierarchy, the hierarchy is not necessarily
top-to-bottom. Some attributes may have multiple bases, or more complex way to
determine their default value.

For example, consider a magic system where the **mana pool** (amount of magic power
that can be spent before resting) depends on the **affinity** to a certain element.
The system has **affinity**/*element* attributes for *earth*, *air*, *water* and *fire*, which
play different roles at different times, but the **mana pool** is based on the 
*highest of them*. Or, it may have their average, or their sum as a base. In this
case, **mana pool** is *dependent* of all of the **affinity** attributes, which are
all its base, but the actual **base value** may be a formula.

There are different type of bases, expressed as a formula in parenthesis after the
dependent attribute name in their formal definition:

* Baseless: the attribute has no base. This is expressed by not having any value
in parenthesis after the name.
* Fixed base: (N) where N is a number. N is the **base value** for that attribute.
* Direct Base: expressed as (**X**) where **X** is the official abbreviation of the base.
the attribute has the value of **X** as its **base value**.
* Modifier Base: (m**X**). The **base value** is the *modifier* of the attribute X.
* Base Portion: (**X**/N). The **base value** is a portion N of the base attribute.
Typically N is 2, 3 or 4 (the **base value** being half, a third or a fourth of that of the
base attribute). Rounding is always down.
* Average Base: (avg **A**, **B**,...). The **base value** is the average of the listed
values.
* Choice Base: (**A** or **B**). The **base value** is the best between the options listed.

### Training attributes

Any permanent alteration to an attribute is known as "training". Generally, that
means increasing its value, but a training can be negative (i.e. because of
an accident producing a permanent disadvantage or a long-lasting curse).

The most common way to improve an attribute is spending a resource
generated by going through various in-games experiences, called 
**training tokens** (**TT**).

As attributes are hierarchical, and training base attributes is harder than
derived ones, **TT**s can only be applied to the attribute of a specific level,
or they can be exchanged with 2 **TT**s of the lower level.

So, **TT/Primary** can be exchanged for 2 **TT/Secondary**, 4 **TT/Hard Skill**,
8 **TT/Normal Skill** and 16 **TT/Easy Skill**.

It is not possible to exchange multiple lower level tokens for a higher level one:
**TT**s represent formative experiences the characters have gone through during
a game session, and to change something at the very base if their essence,
they must have faced impressive events; a large number of small experiences
won't cut it.

> Notice that, usually, base skills will have more than 2 dependents;
this means that exchanging a higher level token for 2 lower ones is
usually not worth, unless the character really need some
differently based lower level attribute to be improved as soon as possible.

#### Training pre-requisites

Some attributes may have pre-requisites for training. They can be either:

* not accessible until one or more other attributes have reached a certain level, or
* be capped to the current level of another attribute.

For example, in a Sci-fi campaign with psionic powers, the skill **natural mentalism** may be
capped to the current value of **mental power**, and **mind melding** could be inaccessible
until **mental power** reaches at least level 10.

Eventual prerequisites are declared in the attribute description.

### In-world training (optional)

The Game Master or the modules may require additional conditions to be able to train attributes,
other than having the necessary **TT**. Some examples:

* Having an adequate trainer available for teaching;
* Undertake a specific ritual at a specific time/location;
* Having the necessary cyber implants available;
* Spending a sensible time in training;

It's totally plausible for the character to just improve as a matter of spending
the **TT**, as the tokens represent an amount of experience that *per se*, for the mere
fact of being acquired, in the general case should grant an improvement of their abilities.

But in some scenarios, the **TT** may represent a lived experience that needs to be formalized,
a token of *being ready* to take the step of the formal training.

### Cascade Skills

*Cascade skills* are skills that require a check on a different subversion of the
skill each time a check is repeatedly attempted. 

For example, some combat skills can be used only once per combat turn. To use them
multiple times in a turn, a second version of the same skill must be trained.

In the player sheet, they will be indicated as "Cascade skill / 1", "Cascade Skill / 2"
and so on. If the composite skill is specialized, it will be indicated as 
"Cascade Skill/specialization / 1", "Cascade Skill/specialization / 2" and so on.

Composite attributes are still targeted as a single one by attribute-targeting advantages
and disadvantages.

For example, if "Active Mitigation" is a combat cascade and specialized skill,
and **Swordfight** is a combat style,
the advantage **Expert / Active Mitigation / Swordfight** will cover all the versions
of **Active Mitigation / Swordfight**.

### Temporary attribute variations

Normally, the value of dependent attributes is computed only when the base attribute changes
definitively, through a means that improves (or reduces it) permanently. In practice,
this happens every few hours of uninterrupted game.

However, it's possible that an attribute is temporarily altered by various means;
for example by magic, drugs or boosts to cyber implants.

If the attribute is a base for many others, it may be difficult to keep track of the
temporary changes to its dependents. To avoid excessive burden to the game play,
temporary attribute variations are applied to its dependents only if the attribute
is their **direct base**.

Every other case, that is, every case in which a dependent has a complex formula
to determine its base value, is considered as if the value of its base (or bases)
cannot be immediately applied.

For example, an arm wrestler can feel a temporary boost or loss of
strength right away. This will be expressed as the attribute **arm wrestling** 
having the direct base value of *strength*, expressed as "(**S**)".
Conversely, if **lore** has a base value expressed as
"(m**I**)" where **I** stands for **intelligence**, and m**I** is the 
**intelligence** modifier, this means that it takes some effort to learn lores
even for a very intelligent character, and as such, a temporary improvement
of **intelligence** won't be transferred to **lore**.

## Generic Attributes

The *Generic Skillset* provides a set of primary and secondary 
attributes that can be used in most settings, together with some
generic skills that cover most common situations.

Every character has the following *primary* and *secondary* attributes:

* Body (**B**): The physical aspect of the character. Body *secondary* attributes are:
  * Strength (**S**): raw physical power;
  * Dexterity (**D**): speed, precision and control over actions performed with the body;
  * Health (**H**): Resilience against fatigue, injury and illness.
* Mind (**M**): describes the mental prowess of a character. Mind *secondary* attributes are:
  * Will (**W**): strength of conviction and assertiveness.  
  * Intelligence (**I**): ability to understand and solve complex problems; mental flexibility.
  * Equilibrium (**E**): resilience to mental strain, stress and madness.

The [**body**](#body) primary provides also the **base value** of 
[**strength**](#strength), [**dexterity**](#dexterity) and (**health**)[#health]. This means that
the value of **body** is also the *default* value for the these dependent primaries; you can
then train each of them separately using *scondary tokens*, and improve them over their base
value, but if you train the main trait **body**, all its dependent attributes will grow with it.

Similarly, [**mind**](#mind) provides the base value for [**will**](#will), [**intelligence**](#intelligence) and [**equilibrium**](#equilibrium).

In turn, the secondary attributes are themselves base for other attributes and skills.

### Body

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | B |
| Category | Primary |
| Base | 3 |
| Cost | 1 TT/Primary |

The Body (**B**) is a value that describes your overall physical prowess in terms of
bodily strength, resilience to prolonged efforts, recovery speed, resistance to
illness and so on. For humans, it is measured in the range between 3 and 18 (the
possible outcomes of 3d6). Most adult characters score in the range between 9
and 12, with 18 representing a person with the best possible body (rarely if
ever ill, strong as the strongest wrestler or weight lifter, moving as swift as
a record runner and able to run as long as a marathon champion — all at the same
time), and 3 representing the weakest possible fully formed and barely
functional body.

### Mind

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | M |
| Category | Primary |
| Base | 3 |
| Cost | 1 TT/Primary |

The Mind (**M**) is the overall score of mental abilities in terms of intelligence, 
creativity, will power, mental sanity, depth of knowledge and so on. 
A mind level 3 represents a character that is barely functional as an autonomous person (or
creature) in the reference setting, while a 18 represents a character maximally intelligent, 
penetrating, knowledgable, sane and wise. The vast majority of characters (or heroes)
in the reference setting will have a mind between 9 and 12.

### Strength

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | S |
| Category | Secondary |
| Base | B |
| Cost | 1 TT/Secondary |

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

### Dexterity

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | D |
| Category | Secondary |
| Base | B |
| Cost | 1 TT/Secondary |

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

### Health

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | H |
| Base | B |
| Category | Secondary |
| Cost | 1 TT/Secondary |

Health (**H**) represents the resistance to fatigue, illness and polluted 
environment (including allergenic agents). It's used to determine how many
injuries can be withstood before being incapacitated, and gives the base for 
all physical resistance skills.

A normal character can sustain 10 + **H** **IP**s from physical sources before 
becoming *incapacitated* and risk dying without an active intervention (e.g.
having someone using the [stabilize](#stabilize) skill on them).

Also, characters can ignore the **IP** penalty up to **mH**. For example,
a character with *health* 17 (**mH** = 3) can ignore the first 3 penalties
(at **IP** 6). If the character receives 16 **IP**s, it will suffer 
(16-6)/2 = 5 points of penalty.

### Will

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | W |
| Category | Secondary |
| Base | M |
| Cost | 1 TT/Secondary |

Will (**W**) is the power of the mind to focus on a certain task, 
perform prolonged mental activity, keep determination in 
adverse situations and so on. It can be roughly thought as the 
equivalent of the strength (**S**) in the mind realm.

### Intelligence

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | I |
| Category | Secondary |
| Base | M |
| Cost | 1 TT/Secondary |

Intelligence (**I**) is the ability to understand and solve complex problems, 
comprehend difficult study subjects, see through schemes and machinations 
etc. As it measure the flexibility of the mind processes, it can be thought 
as the dexterity (**D**) of the mind.

### Equilibrium

| <!-- --> | <!-- --> |
|----------|---|
| Callsign | E |
| Category | Secondary |
| Base | M |
| Cost | 1 TT/Secondary |

Equilibrium (**E**) is the stability of the mind, 
or basically the equivalent of its health (**H**). It indicates 
how much mental strain a person can take before being debilitated; 
of course, it is important in those settings where attacks are delivered 
to the mind instead of the body: fantasy, sci-fi and horror settings 
can present as many dangers for the mind as for the body, or more.

Hence, it forms the base of all the mental resistance skills.

A normal character can sustain 10 + **E** **IP**s from psychic sources before 
becoming *incapacitated* and risk dying without an active intervention (e.g.
having someone using the [stabilize](#stabilize) skill on them).

Also, characters can ignore the **IP** penalty up to **mE**. For example,
a character with *euqilibrium* 17 (**mE** = 3) can ignore the first 3 penalties
(at **IP** 6). If the character receives 16 **IP**s, it will suffer 
(16-6)/2 = 5 points of penalty.

## Generic skillset: General skills
The *Generic Skillset* provides a set of skills that can be used in most settings.

Skills specifically used for combat that are still part of the generic
skillset are described separately, under the *combat system* section.


- [Acrobatics](#acrobatics)
- [Charisma](#charisma)
- [Chemistry](#chemistry)
- [Climbing](#climbing)
- [Deceit](#deceit)
- [Endurance](#endurance)
- [Engineering](#engineering)
- [First Aid](#first-aid)
- [Hacking](#hacking)
- [Healing](#healing)
- [Hiding](#hiding)
- [Hiding in Shadows](#hiding-in-shadows)
- [Intimidate](#intimidate)
- [Investigation](#investigation)
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
- [Silent Movement](#silent-movement)
- [Traps](#traps)
- [Treating Wounds](#treating-wounds)

### Acrobatics

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

### Charisma

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

### Chemistry

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical knowledge of chemistry or equivalent science in the world setting
(e.g. alchemy in a magic world).

### Climbing

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

### Deceit

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

### Endurance

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

### Engineering

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical skill in world-relevant engineering. For example,
in a steampunk world, it would be the ability to put together
mechanical devices. 

### First Aid

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| EC | First Aid Kit |
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

### Hacking

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Callsign | Hk |
| Category | Skill |
| Specialization | system |
| EC | Rootkit (opt) |
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

### Healing

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | Hl |
| Category | Skill |
| Prerequisite | First Aid 6 |
| EC | First Aid Kit, Healing Kit (opt) |
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

### Hiding

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

### Hiding in Shadows

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

### Intimidate

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill |
| Cost | 1 TT/Normal |

Intimidate is the action of menacing someone that some negative outcome will
follow, unless they don’t comply with some desired course of actions. For
intimidation to be effective, the menace must be credible, and the target
must actually wish for that not to happen.

### Investigation

| <!-- --> | <!-- --> |
|------|---|
| Base | I |
| Callsign | Inv |
| Category | Skill |
| Cost | 1 TT/Hard |

The ability to find hidden clue or draw correct conclusions with a limited
amount of clue. Particularly useful when visiting the scene of a crime.

### Lie Detection

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

### Lock Picking

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | lp |
| Category | Skill |
| EC | Lock Picks |
| Cost | 1 TT/Normal |

Used to try opening normal locks. The lock must be within the 
reach of the technological knowledge of the character. 
The character must have also proper tools at its disposal
to try the action.

### Lore Knowledge

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

### Perception

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

### Persuade

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

### Pickpocket

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

### Poisons

| <!-- --> | <!-- --> |
|----------|-------|
| Category | Skill |
| Cost | 1 TT/Hard |

Technical knowledge for recognizing or producing poisons.

To recognize a poison, the character must win a simple check at *normal* difficulty.

To produce one successfully, they must pass a *hard* check.

### Repair

| <!-- --> | <!-- --> |
|------|----|
| Base | mI |
| Callsign | Rep |
| Category | Skill |
| Specialization | machinery type |
| EC | Repair Kit |
| Cost | 1 TT/Normal |

This skill is used to fix machineries, magic constructs, AI, and in general
any non-living entity that doesn't have a *health*. 

The skill must be specialize for machinery category, which must be relevant
in the game world. 

Special repair kit, software tools, magic devices etc. may provide a bouns
on the simple check roll.

### Resistance

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

### Running

| <!-- --> | <!-- --> |
|------|---|
| Base | D |
| Category | Skill |
| Cost | 1 TT/Easy |

Running is the skill used when deciding which character wins a run race.
It can also be used to check if a character is able to run for a long time.

### Silent Movement

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

### Traps

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

### Treating Wounds

| <!-- --> | <!-- --> |
|----------|-----|
| Callsign | TrW |
| Category | Skill |
| Specialization | race type |
| Prerequisite | Healing 3 |
| EC | Healing Kit (opt) |
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

# Statuses and status points

Characters will sustain negative effects in pools called *statuses*. Most statuses are binary,
i.e. on or off. For example, a character may be *asleep* or *awake*: its "being awake" status may
be on/off.

Some statuses have numeric values, and the character will be negatively affected if the number
increases. For example, the number of [injury points](#wounds):
the higher, the worse.

Finally, there are statuses that start at a certain maximum level, and as the characters use 
their skills, they are used up. This statuses are called *pools*, and various modules and 
sub-systems can define different pools for specific usages. For example, a magic system may
define a *mana pool*, which determines how many spells a character can cast.

# Vantages

**Vantages** special conditions that apply to the character in general or to a specific attribute 
or set of attribute in particular, and that have a direct effect on some game mechanics.
They are called **advantages** if positive and **disadvantages** if negative. 

For example, some advantages may grant you the possibility to automatically win a draw once a day. 
Others may give you extra die to throw and use in some situation. Others may give you one extra
point to all the skills having a certain base attribute, i.e. improve all *easy skill checks* based on 
a certain attribute. Others may reduce the difficulty level of the attempts on a certain skill by one
level, so that i.e. a skill called **climbing** on *easy* targets becomes trivial, on *normal* targets it 
becomes *easy* and so on. 

**Disadvantages** are negative **vantages**. A character might be given
disadvantages temporarily or permanently, because of what happened during
previous adventures, or as a background flavor. As disadvantages have negative CP costs, 
a player can chose to get certain disadvantages in order to gain **training tokens** to be
spent elsewhere, in other statistics.

While most advantages are simply either active or not, some can have different levels. 
For example, an advantage called i.e. Survival Instinct, which, say, reduce the difficulty level
of all survival checks, may have a level between 1 and 3, each granting a one extra reduced difficulty level. 

In that case, the cost to be paid (or refund obtained) of each level is the base cost 
plus the level acquired.

For example, suppose an advantage called **graceful** can be acquired at levels 1 to 3, each level
making the advantage stronger. 
The cost indicated in the description is 2 **TT**/*Primary* (training tokens of type *primary*). 
To buy level 1, the players must spend 2 + 1 = 3 tokens; level 2 costs 2 + 2 = 4, and level 3
2 + 3 = 5 tokens. This means that if players wants to get **graceful**/3 from scratch, 
they must use 3 + 4 + 5 = 12 *primary* tokens.

The tokens refunded when acquiring (willfully) a disadvantage follow the same rule, granting
a number of tokens equal to the indicated base cost plus the level the players are willing
to take, cumulated. So, if a disadvantage called **clumsy** has base "cost" 2 **TT**/*Primary* and
can be acquired with level 1 to 3, players giving **clumsy**/3 to their character will receive
3 + 4 + 5 = 12 **TT**/*Primary* to be spent on something else.

### Advantage prerequisites

Some advantage could have a pre-requisite that must be fulfilled in order to be acquired. 
For example, they could require having already acquired another advantage, or having a certain 
statistic at a minimum set score.

### Other limitations (optional)

The GM may allow to get a certain number of advantages and/or disadvantages to be taken at character creation, 
or may allow to get some of them later on if that's fitting for the setting. For example, in a cyberpunk
setting, many advantages may be granted through body implants, which may be be bought under certain
conditions.

## Premium advantages

In some cases, a character can receive an advantage as a reward for completing
a certain task. Advantages can be gained by magic, e.g. blessings, or physical conditions, 
e.g. receiving a cybernetic implant by the government as a reward for being enlisted
in a special corp.

Whenever an advantage is a acquired as a reward, that require spending the front
cost in **TT**s

## Removing advantages

It is possible to remove advantages that have become obsolete. If the player so wishes, 
it can remove an advantage and recover half its nominal cost in **TT**s (rounded up). 
This doesn't include premium advantages, that is, advantages received as rewards for
in-game deeds.

## Penalty disadvantages

In some cases, a character can receive a disadvantage unwillingly. This may be
caused by magic, e.g. curses, or physical conditions, e.g. a necessary
cybernetic component of their body becoming unserviceable or being hijacked by
a malignant hacker.

Whenever a disadvantage is a acquired as a penalty, that doesn't give any
additional **TT**.

## Removing disadvantages

It is possible to remove disadvantages that the players have willfully 
applied on their character. This can be done by:

* paying back double the cost of the disadvantage in equivalent **Training Tokens**, or
* by performing particularly worthy tasks in game, aimed directly at reducing or
removing the disadvantage. For example, a player may save a famous cybernetic scientist
in exchange for his help removing a defective cyber implant. This can remove also
*penalty disadvantages*.

If the disadvantage has levels, each level needs to be removed separately: it's
necessary to pay double the tokens received by acquiring each level, one by one, 
before being able to remove the disadvantage completely. 

For example, if a **clumsy**/3 disadvantage, with base cost 2 **TT**/*Primary* granted
3 + 4 + 5 = 12 tokens, to remove it players must pay 24 **TT**/*Primary*.

## Conflicting vantages

Characters cannot acquire advantages having opposite effects to disadvantages they own, 
and the other way around, they cannot acquire disadvantages conflicting with advantages
they already own.

If a game situation applies a *premium advantage* or a *penalty disadvantage* to a character
already having a conflicting vantage, that one is removed instead.

For example, suppose that the advantage **graceful** has the opposite disadvantage
called **clumsy**:
it acts on the same skills and checks, but the first gives a bonus while the second
inflicts an opposite penalty. In this situation, if a character having **graceful** is
hit by **clumsy** because of the effect of a curse, **graceful** is removed instead.

If the conflicting advantages are leveled, the character is left with the larger 
of the two, reduced of the value of the other. For example, if a character with
**clumsy**/1 receives a blessing that would grant **graceful**/3, then
**graceful**/2 is applied instead.

This happens also if the to statistics are not exactly specular, but just
acting in opposite direction on the same skills or checks. For example, 
if **expert** reduces the natural penalty of *normal*, *hard* and *very hard* checks for
a certain skill while **novice** increases the penalty of *trivial* checks only, 
they are still considered conflicting under this rule. However, they would not
be considered conflicting if they affect different skills.

## Skill-specific disadvantages

Some disadvantage can target specific skills and checks, making them harder
or weaker for the character afflicted by it.

In general, the **GM** should allow players to acquire the disadvantage
in exchange for tokens only if it's actually relevant for them:

* On a skill that is very commonly used by everyone in-world, as a hacking
skill on a AI or cyberpunk setting, or a fist fighting skill in a fantasy world.
* On a skill that is relevant for the in-world occupation of the player, 
as for example thievery skills for thieves and spies, healing skills for
healers and so on.

The idea here is that of not giving "free upgrades" for the players to use
without consequences.

This doesn't *necessarily* apply to *penalty disadvantages*, 
that characters may be subject
to because of something happening during their adventure. For example, a
character may receive a light curse that afflicts a specific skill by design, which
may or may not be relevant for the character.

## Generic Skillset: Advantages


- [Battleproof](#battleproof)
- [Born in a Mourning Hall](#born-in-a-mourning-hall)
- [By the skin of one's teeth](#by-the-skin-of-one's-teeth)
- [Combat Flow](#combat-flow)
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
- [Survival instinct](#survival-instinct)
- [Total Mitigation](#total-mitigation)

### Battleproof

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Hard |
| Prerequisite | Hard to die |

The character can withstand an additional heavy wound (or the equivalent **IP** from
lighter wounds) from physical sources before being incapacitated. 

The first physical wound is received during a fight will
automatically heal in 4 hours, even if not treated.

### Born in a Mourning Hall 

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

### By the skin of one's teeth

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Secondary |

This advantage allows to resist automatically a single
deadly wound from any source once per day.

The "boundary" of the day is selected by the GM (on player's suggestion),
to be of some significance for the character. It could be the midnight
in a specific place, the sunset, the sunrise, or performing a 
daily ritual specific of the character's creed or habit.

### Combat Flow

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Primary |
| Levels | 6 |
| Cost | 1 TT/Normal |

The character receivers an additional point of the *Advanced Combat Resource*
generated by the target primary: **Stamina** for **Body** and **Focus** for **Mind**.

### Combative spirit

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

### Deep Mind

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Prerequisite | Mind 9 |
| Cost | 2 TT/Hard |
| Levels | 6 |

The character acquires a passive mitigation against *despair*
and *maddening* damage equal to the level of this advantage.

### Easygoing

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

### Elemental Resistance

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

### Expertise

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

### Fast Paced

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Normal |
| Prerequisite | Dexterity 9 |
| Levels | 3 |

During combat, the character can move for 6 extra feet per turn for 
each level of this skill.

### Hard Skin

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 2 TT/Hard |
| Prerequisite | Body 9 |
| Levels | 6 |

The character gains a passive defense against blunt
and cut damage equal to the level acquired.

### Hard to Die 

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Hard |

When receiving a deadly wound, resistance checks are lowered
by one difficulty level (normal checks become easy, 
easy checks become trivial etc.).

### Keen Eye

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Hard |
| Prerequisite | Dexterity 9 |
| Levels | 4 |

Falloff in ranged combat is increased of 6 ft. per point of this advantage.

### Lucky

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 1 TT/Primary |
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

### Mastery

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Specialization | Skill |
| Cost | 1 TT/Secondary |
| Prerequisite | Expertise |

Skill Mastery is an advantage that is 
applied on a specific skill. As a pre-requisite,
the character must have already Expertise on the same skill.

Mastery changes all the checks using that skill from a 3d6 
throw to a 2d6+6 (as if one dice is always automatically 
rolling a 6).

Combat styles and other combat skills **can** be targeted by
**mastery**.

### Medical knowledge

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

### Natural

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

### Nimble crowder

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

### Survival instinct

| <!-- --> | <!-- --> |
|----------|-----------|
| Category | Advantage |
| Cost | 3 TT/Normal |
| Levels | 4 |

All instinctive defense checks get a +1 modifier per level of this advantage.

### Total Mitigation

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

## Generic Skillset: Disadvantages


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
| Cost | 1 TT/Primary |

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

### Fumbling

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Secondary |

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

### Latecomer

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Secondary |
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

### Nervous

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

### Self Taught

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

### Situational Unawareness

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 1 TT/Hard |
| Levels | 3 |

All instinctive defense checks and contests get a -1
modifier per level of this disadvantage. 

### Soft Skin

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Hard |
| Levels | 3 |

The character receives a passive penalty against blunt
and cut damage equal to the level acquired.

### Unlucky

| <!-- --> | <!-- --> |
|----------|--------------|
| Category | Disadvantage |
| Cost | 2 TT/Primary |
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

### Vulnerable

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

### Weak Mind

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

Some backgrounds may be generally advantageous for the character,
while others might be generally detrimental. 

For example, being famous, of noble origins, 
having a career in a peculiar field as university professor,
being an outlaw, a member of an ostracized
religious sect or having an uncommon phobia are all *backgrounds*. 
While being famous seems more desirable than being an outlaw,
in some game situations it may be preferable to be the latter than
the former. 

For this reason, there isn't a net distinction between positive
and negative backgrounds, and they all have a positive cost in 
**training tokens** to be spent at character creation. It is also
possible to receive the backgrounds as a consequence of adventuring;
for example, one can certainly become an outlaw during the course 
of an adventure; nobles can lose their titles, university professors
can lose their positions and phobias can be cured, but differently from
*vantages*, *backgrounds* can only be removed as a consequence of
gameplay.

## Effect on the game

Backgrounds can and usually will have an influence in how the adventure plays,
but they don't have a direct effect on the rules; that what's
vantages are for. However, some of them may have
some indirect effect on the rules in some specific situation. 

For example, being a **criminal boss** doesn't give the character a direct upgrade
or downgrade in any skill check; it is meant to direct the character's adventure 
in a certain direction, and make clearer how they will react when facing
criminality or law enforcement, but in some cases the **GM** may apply a
discretional bonus or penalty on some check, i.e. when trying to
**intimidate** a gang member.

## Backgrounds are not physical

Physical characteristics are never to be considered backgrounds; this
because any physically apparent characteristic would either have an
effect on attributes or be severely limiting on the gameplay. For example,
the ability to **persuade** already takes into account the attractiveness
of a character. Conversely, a physical disability is difficult to translate
into gameplay, while a low attribute number can better represent it.

## Generic Skillset: Backgrounds


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
| Cost | 1+ TT/Secondary |

The character is an aristocrat in the target setting. In settings
that don’t consider birth rights as traditional aristocracy, the
the character belongs to a similar oligarchy or high-order political
elite.

The cost, and the effect of the background on the game, depends on the
level of aristocracy:

* Baron, career politician, oligarch: 1 TT/Secondary
* Count, party leader, organization leader: 2 TT/Secondary
* Duke, minister, CEO: 3 TT/Secondary
* King, prince, prime minister, president: 4 TT/Secondary

The background is applied also if the character is a close family member
(child, parent, souse) of a person in the given position. For example,
if a player wants to play the son of a baron, they will have to spend
1 TT/Secondary too.

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

# Checks

A check consists of throwing dices and verify if the result is successful.
Checks are the nuts and bolts of SIRPAS. Practically every action that 
might succeed or fail requires performing a successful check. There are different 
kind of checks that apply to different situations, but in general, a check 
consists in beating some high point score summing a 3d6 with the value of
the statistics on which the check is performed.

## Simple check

A *simple check* is a test for the character to be able to perform a certain
action, which requires a certain **skill** to be employed. For example, to verify 
if the character can land safely after jumping down from a height, it must pass 
a *simple check* on a skill having that purpose (for example *acrobatics*).

The skill descriptions indicate which actions are covered by each of them. When a character 
wants to perform an action not covered by a specific skill, one of its generic attributes are used instead; 
the Game Master decide which is the most adequate one. For example, if a character is trying to 
extract a sword stuck on a wooden beam, which is a situation not covered by any skill in the base manual, 
the Game Master might ask to pass a *simple check* on its *strength*.

To *perform* a **simple check** means to throw three dice (or a different number, where the
rules specify it) and sum the result of the rolled dice to the value of the employed skill or
attribute. The rules might specify other modifiers to be applied to specific checks; for example
being injured applies a penalty to any check.

The sole result of the dice rolls is called **natural result**, while the grand total of the **natural result**,
skill or attribute value and modifiers is called *check result* (**CR**). To win (or *pass*) a **simple check**, 
the **check result** must be above a score called *success level* (**SL**) that depends on the difficulty of 
the action, according with the following table:

| Difficulty           |  Success Level   |
|----------------------|-----------------:|
| Trivial              |  15              |
| Easy                 |  18              |
| Normal               |  21              |
| Difficult            |  24              |
| Hard                 |  27              |
| Very Hard            |  29              |

Skill descriptions will reference this table to specify which kind off attempt are to considered, easy,
normal, hard and so on. When the skill description doesn't specify it,
the Game Master can assign a difficulty modifier depending on the situation.

Some skills may be performed only against a **normal** success level, but assign an additional
bonus or penalty depending on the situation. For example, trying to perform an acrobatic action
while jumping from high may inflict a penalty that increases in proportion to the height of the jump.

### Success Margin

The difference between the **check result** and the **success level** is called **Success Margin** 
(**SM**). The **SM** is 0 or above on success, and less than 0 on failure.

### Automatic Results

In a **simple check**, When a *natural 18* is scored, and if the action is of *normal* difficulty 
or easier, the *simple check* is automatically passed, regardless the *check result* being actually 
above the required **SL** or not.

When a *natural 3* is scored, and if the action is of *normal* difficulty or harder, the *simple check*
automatically fails, regardless the *check result* being actually below the required **SL** or not.

**Optional:** *easy* actions have an *automatic success* with a *natural 17* or better and *very easy*
actions with a *natural 16* or better. *Hard* actions fail automatically with a *natural 4* or worse, and
*very hard* actions with a *natural 5* or worse.

An **automatic result** is considered also a **critical success** or **critical failure**.

## Repeated Attempts

In some situation, it is possible to repeat a failed attempt soon after the
first try, either by the same character or by another one in the same group.

For example, picking a lock (when no one is around and there aren’t
time constraints) can be repeated indefinitely by every member that could be 
able to open it, until a success is achieved, or unless the lock turns out
to be actually impossible to pick.

Normally, any check that can rationally be performed more than once in a row can
be repeated by increasing the **SL** by 2 points. For example, suppose you're retrying 
to break in an apartment; you have to perform a check on a lockpick skill
against a **SL** of 21 (a normal check). On failure, your character or another one in the group
might try again, but this time the **SL** will be 23.

The time required for an attempt is usually indicated in the description of the target
skill; if not, the Game Master decides how long any attempt should take, depending on 
the situation.

It is possible to attempt the action again with its natural **SL** letting a reasonable
amount of time to pass. For actions taking a few moments, it will be after a long rest
(equivalent of a good night of sleep). For actions requiring long preparation (i.e. 
studying the lore of a region), it might be a week or a month; if not specified in the
skill description, the Game Master will decide.

## Contest

Some actions are performed either in competition or against other characters.
When this happens, a *contest* (**CNT**) must be performed. Both characters (or the
Master in place of NPCs), must perform the equivalent of a *simple check* on
a *normal difficulty*, trying to beat the opponent's roll.

Some contest can be asymmetrical: for example, an attacker will roll on some
attack skill, while a defender will try and prevent the attacker success using
some defense skill. The skill and combat sections describe some possible
asymmetric skills, but players and masters (and other expansions) might come up
with new ones if the situation suggests so.

The character having scored the highest result wins the contest, and the **SM**
is computed for the winner only (and so, it is always positive).

Draws are normally allowed, and they might either mean that a new situation
has taken by both characters having achieved a success at the same time,
or nothing has changed as each character prevented the other from acting. 

For example, suppose that two characters struggle to reach for a weapon during a
brawl, with a contest on dexterity. If they roll a draw, it means both of them
reached for the weapon, and now the situation has changed. A different contest
may now take place: a contest on *strength* to determine who can pull the hardest.
This time, if they have a draw, it means that none of them is able to snitch the
weapon from the other, and they can try again. 

### Non-draw contests

Contests that don't allow draws are specifically indicated by the rules as
*Non-Draw Contests* (**ndCNT**). In this cases, when a draw is scored, it is
discarded as not performed, and another contest takes place.

## Rankings

Ranking rolls (**RNK**) are special contests between two or more characters, ranking them in a
order that doesn’t allow for draws. Also, in *rankings* the **SM** is not relevant.

For example, to establish the arrival order in a running relay, every participant rolls a ranking on 
a skill used for running.  The order of arrival is decided once and for all, 
and draws are not allowed.

Draws are resolved by re-rolling on the same skill. The re-roll is only relevant
for the relative order of the characters in draw. For example, suppose that, in
said race, four character score a total of 26, 22, 22 and 20 respectively. Now,
the second and third characters roll to decide their relative position; the winner
of the two will be the second in ranking, and the looser will be the third, regardless
of the score they draw now.

## Multi-contests

A multi-contest (**mCNT**) is a contest between two or more parties,
each comprising one or more characters. 

In a multi-contest, each party performs a *ranking* on the 
selected skill. Then, the best *check results* from each party
are compared against each other, and a point is assigned to the
party having the highest *check result* among the top scores
in each of them. 

The contest continues
comparing the second-best results, the third-best results and so on,
until all the parties have a score to oppose to the others. Draws
are discarded.

The party having scored the highest number of points is the winner. If
more than one party has totalized the same number of points, a multi-draw
happens; depending on the context (and on the rules), the multi-draw might either
lead to a new situation, or require the whole multi-contest to be repeated.

The characters that have scored points for the winning parties are called
**scorers**; those who have lost their roll (regardless of their party 
having won or not) are called **succumbers**. The ones who couldn't be
matched with a ranking from the other parties are **excluded**.

As there could be negative consequences for the losing parties, each
losing participant will receive the difference between their score
and the winner of their rank as a negative *success margin*, 

Notice that a multi-contest between two parties comprising just one 
character each is almost the same as a *direct contest*, with the 
difference that, instead of assigning a positive *SM* to the winner, 
a negative *SM* is assigned to the loser.

**Example**: Three parties, composed of 3, 4 and 5 members respectively,
try running up a hill before the others. They perform a *multi-contest*
on a skill or attribute used for running. The rankings in each party result in:

* Party A: 29-23-20
* Party B: 26-25-22-19
* Party C: 28-22-21-18-16

The points are assigned as follows:

* A = 29, B = 26, C = 28 - Point for A, **SM** of B = -3, **SM** of C = -1  
* A = 23, B = 25, C = 22 - Point for B, **SM** of A = -2, **SM** of C = -3
* A = 20, B = 22, C = 21 - Point for B, **SM** of A = -2, **SM** of C = -1

Group A has 1 point, while group B has 2: group B wins the multi-contest.

The the fourth ranked in B, and the fourth and fifth in C are **excluded** 
and will not contribute to winning.

Nevertheless, the most numerous group has an advantage in having more chances
to score high points than the others -- everything else equal.

The effect of the multi-contest in the adventure should reflect its outcome. In this
example, as team A had the highest score but ended up losing the race, the two 
characters with the highest scores in parties A and B might have fumbled on the hill, 
or grabbed each other in a brawl, while the two characters having scored points for the 
winning party would have reached the top, nearly followed by the losers, 
and at a distance, by the ones excluded from the contest.

## Ranking generation for the **GM**

In a multi-contest, each player rolls its own dice, and performs its own computation, communicating
the final result to the **GM**; the players may even sort their scores before
doing that, helping out the GM in its task.

However, the GM is alone in rolling the dice for the characters they control; repeating several 3d6 rolls
and adding various modifiers that can change during an action (i.e. because a GM controlled character
gets wounded) can be tiresome, and can slow down the pace of the game for the players as well.

To prepare the multi-contest, the GM should:
1. Write the characters he controls on a column of a notepad.
2. Besides each name, write the modifiers for that characters.
3. Unless each GM controlled character is special, the GM always assigns the best outcome 
   to the topmost character, so that it can read the ranking results go top to bottom. 

If the GM doesn't have a dice-throwing application handy, which can automate part of the process, it
can use the following procedure to generate multiple scores at once:
1. Roll 2d6 and write down the result.
2. Roll Nd6, where N is the count of character controlled by the *GM*.
3. If more than one 6 is rolled, count them as 7, 8 etc.
4. If more than one 1 is rolled, count them as 0, -1 etc.
5. Add each single rolled result to the previous 2d6 roll.

For example, the GM controls 5 characters.
1. It rolls 2d6 for a total of 7.
1. It now rolls 5d6, one per character; the results are 6, 6, 4, 1, 1.
1. The characters gets the following points, top to bottom: 7+7 = 14, 7+6 = 13, 7+4 = 11, 7+1 = 8 and 7+0 = 7.
1. Now the GM gets the result from the players, and communicates the winning party, 
   the scoring characters and, if relevant, the negative **SM** of the **succumber** characters.

## Critical Results

[Automatic results](#RB-automatic-results) in simple checks are considered
critical results, but a critical result can also be achieved when the
success margin of an action is extreme (in both directions).

Unless specified otherwise, a *success margin* particularly high is
called *critical success* (**CrS**), and one particularly low is called 
*critical failure* (**CrF**).

Critical successes and failures will
result in particularly good or bad outcomes; when not specified by 
the rules or the skill description, the Game Master will determine 
how the outcome exceeds a normal result. 

In a *contest* the **SM** can be only positive. For this reason,
a contest can't determine **critical failures**, only a 
**critical success** for the winner.

Conversely, **rankings** have only negative **SM**, so they can only result
in **critical failures**

The following table describes which **SM** are considered **critical results**,
depending on the complexity of the action. *Contests* are considered *normal actions*
on this regard, unless specified otherwise.

| Difficulty      | SM for CrS  | SM for CrF |
|-----------------|-------------|------------|
| Trivial         | >= +6       | <= -6      |
| Easy            | >= +7       | <= -7      |
| Normal          | >= +8       | <= -8      |
| Difficult       | >= +9       | <= -9      |
| Hard            | >= +10      | <= -10     |

# Damage and Injury

A critical aspect of any RPG is the set of rules that determine how characters
sustain damage and receive injuries.

SIRPAS has a modular injury system, which can be fitted in any setting and play styles.

It can be used to determine an overall result of a fight, or to determine precisely 
which part of a human body, mechanical robot, flying mount or AI virtual device 
has been damaged, and to what extent it has been incapacitated. 

It can be employed to keep the score of harmless intellectual challenges, 
as well as devastating psychic attack on the mental sanity of the characters.

## Damage Points

The *raw damage* a character receives is measured in *damage points* (**DP**).

Damage can come in the way of characters in various forms, and from various
sources; hence, **DP** have also a *quality*, which depends on which source
is generating them.

A source could be physical harm, fatigue, heat, cold, mental stress etc., as
your module requires. 

## Effective Damage

Incoming *raw damage* is modified through the application of *defenses*, 
that reduce it in various ways; they are mainly divided in the following categories:

- *Passive Defenses*: reducing the incoming **DP**s of a flat amount (like physical armors),
  or dividing the damage by a certain factor, i.e. 4/5 or 3/4 (like magic or sci-fi shields),
  or eventually by an hybrid formula (as in the case of specific resistances against some
  kind of damage).
- *Active Defenses*: the amount of reduced **DP**s depends on the use of a certain
  character ability. 

The way different kind of damages impact on the characters is fully considered by the way
defenses are applied to reduce the incoming **DP**s.

The count of **DP**s left after the defenses are applied is called 
*effective damage* (**ED**).

## Wounds

When sustaining a certain amount of damage, the character
receive a certain kind of wound, according with the following table:

|**ED** | Wound   | **IP** | 
|------:| -----   | ------:| 
| 0-1   | Scratch |      - | 
| 2-3   | Light   |      1 | 
| 4-6   | Serious |      2 |  
| 7-9   | Heavy   |      4 | 
| 10+   | Deadly  |      - | 

Wounds are of the same type of the damage received. For example,
physical damage generate a physical wound; mental damage causes
mental wounds and so on. 

The severity of the received wound and its type determine the amount and type 
of *injury points* (**IP**) currently sustained by a certain character;
once the **IP**s are above the maximum damage of a certain type 
a character can sustain, it becomes *incapacitated*, and it may 
eventually die, if the wounds are not treated.

### Wounds Penalty

A character receives a penalty to any check of half the sum total of
**IP**s across all types (rounded down). 

While the type of the wounds is relevant for the amount of damage that
can be sustained, that doesn't matter for how well the character is
performing. You are not going to find a new theorem with an untreated broken
arm, and your fighting style will be less than effective if your
mind is in shambles.

### Scratches

A character receiving an *effective damage* not less than 0, 
but below the amount necessary to generate a light wound receives 
a "scratch".

Scratches are extremely light wounds that, by themselves, don't impact
the character **IP** pool.

### Scratches to Wounds

Once received a certain number of scratches, they are considered
as one light wound (**Scratch To Wound**, or **StW**). By default, 
this value is 4, meaning that 4 scratches are considered a light wound, but
this can be overridden by modules depending on their setting.

### Side effect of non-scratches (optional)

When the **ED** is less than 0, that isn't accounted as a scratch. However, 
it may still generate negative side effects, for example apply any form of 
physical or magical poisoning, inject a virus in an AI or in a cyber brain
and so on.

## Direct Wounds

In some situation, a character can receive a wound of a certain kind directly,
(not just as a consequence of receiving a certain amount of **damage points**).

For instance,
certain magic spells could cause a heavy wound directly if the character fails
an attempt to resist them. A overwhelmingly powerful weapon, for example a starship
laser directed against a human, could have the same effect. Explicit actions 
performed on the character when it is unable to defend itself could deal
an arbitrary wound as the attacker seems fit, etc.

Direct wounds will immediately apply the relative **injury points** as if they were
received through damage application.

## Resistance check

In some situation, it's possible to avert the received damage partially
or completely using a **resistance check** (**RC**). 

The resistance check is a **simple check** with a difficulty modifier
determined by seriousness of the damage that is being averted.

|  Wound seriouness | Difficuylty          |
|-------------------|----------------------|
|  Non-scatch       | Trivial              |
|  Scratch          | Easy                 |
|  Light            | Normal               |
|  Serious          | Difficult            |
|  Heavy            | Hard                 |
|  Deadly           | Very Hard            |

For example, suppose a character is hit with a deadly poisonous dart.
To avert immediate death, they must perform a **RC** against poison
with *very hard* difficulty.

It's not normally possible to avert non-lethal damage during combat using
a **resistance check**, unless specific advantages or other
module-specific rules provide this ability.

The attribute used for **RC**s is the most detailed one that can be applied
in the situation. 

Suppose for example that a module defines hierarchy the attributes:

```
Body -> Metabolism
Spirit -> Willpower -> Fear Resistance.
```

In this situation, **Metabolism** would be used to resist poison, while
**Fear Resistance** would be used to avert damages and negative effects
caused by any **fear** based attack.

In general, the attribute description gives a generic indication on which
type of damage it can avert; so the fact that **Metabolism**
could be used to resist poison damage (and maybe some other negative
effects) would be indicated in its description. 

At any rate, the Game Master can pick any attribute that would be relevant,
and ultimately, the most basic attributes if a specific one can't be found.

> The base module defines **resistance** skills covering all the damage
sources it introduces.

## Incapacitation

The amount of **injury points** that incapacitate a character is defined
by the modules, and can be tweaked by the Game Master to better fit the
mood of its campaign.

A realistic setting may set the limit for humans to 4 or 5 heavy wounds,
or equivalent amount of lighter wounds (that would be 16 or 20 points),
but if characters are something different from humans (e.g. vampires,
werewolves, android etc.) they might have a greater resistance to pain
and/or damage.

Normally, a count of 20 **IP** would give a penalty of -10 to any check,
which may be severely limiting even for a powerful character; however,
the modules may provide means to reduce or ignore the penalty under certain
situations with advantages or special gear, as enchanted armors, stimulant shots,
magic spells, nanomachines etc.

## Deadly Wounds (optional)

When a character receives an amount of *ED* higher than the higher limit
for heavy wounds, it sustains a wound that is
potentially able to kill them immediately.

To avert an immediate death, the character must pass a _simple check_ on an
attribute related with the type of damage received.

If the check is successful, the character receives a _heavy wound_ instead.

> Remember that the _resistance check_ has a negative modifier of half the
received **IP**s, as any other action.

## Localized Wounds

By default, wounds are generally applied in the generality of the body,
but some abilities allow to aim a certain specific part.

### Wounds to limbs or periferical devices

When a wound is localized on a specific body part (an arm, a leg), 
any action involving that body part receives the double amount of
penalty from that wound type (that is; the same amount of penalty
as the number of injury points that part has received). 

For instance, a *heavy wound* localized on a leg will cause 4 *IP* as normal, 
resulting in a penalty of -2 points to any check, but the penalty will be
-4 or any skill involving jumping, running and using specifically the legs.

This extends to non human and even virtual body parts as well: and AI receiving
a heavy wound on a virtual device will have a double penalty if it tries to use
that device to perform any action.

### Wounds to the head or control unit (optional)

When a wound affects the head (or other target part that is particularly critical
to control the behavior of the character), it generates an additional **injury point**.

## Healing

The **IP** generated by wounds (and relative check penalties) affect the
characters until they are healed. Wounds are healed one-by-one, unless
a general healing procedure is applied (i.e. a magic spell that restores
the character health completely, a backup-restore procedure on an AI etc.)

As a wound is cured through any mean (medicine, magic, natural healing etc.), 
its **IP** cost and relative check penalty are removed.

Light and serious wounds heal naturally after a reasonable amount of time.
Common sense can be used by the Game Master and the players to determine
the adequate time; for humans, a light wound may heal completely in less
than a week (generally, after a day of full rest and basic treatment), 
while a serious wound would take about month (or a week of full rest and
basic treatment).

Heavy wounds require specific treatment to be cured.

### Healing Scratches

Scratches not turned into a light wound are removed after a reasonable amount of time
and minimal care adequate to the setting. For example, in a fantasy setting, that may
be spending a few minutes to tend the wounds after a combat. In a cyberpunk setting, 
it may be applying wound-reducing foams. 

### Day-rest healing

Unless differently specified by the modules a full day of rest and basic tending 
will:

* Heal all scratches not counted as light wounds;
* If there character hasn't got any scratches, heal 1 light wound.

# Combat

Combat is an advanced form of contest. In a normal contest, characters
try to win one over another on specific skills, while in combat,
contests are finalized to deal damage or other negative effects on
an unwilling target.

SIRPAS offer three set of rules for resolving combat situations, with 
increasing level of complexity:

- *Simplified Combat*: It's a simple way to resolve small combat situations.
	It consists in a specialized form of [multi-contest](#multi-contest) applied to combat
	skills, which takes into account the relative ranking in the contests to
	determine winners, losers, and other possible outcomes.
- *Basic Combat*: It's a sub-system dedicated specifically to combat, using
	the combat skills with specific rules, and takes into account positioning,
	tactical advantages and other combat-specific elements.
- *Advanced Combat*: This is the full fledged combat system, extending the
 	_basic combat_ and using special sub-skills called _maneuvers_.

You can chose to stick with one combat system or mix and match them the same adventure, 
without limitation, depending on how combat-centric is your adventure, or how
important is a specific combat in your story.

## Combat skills

Every form of combat is based on special attributes called **combat skills**.
They represent the proficiency of a character in fighting. 

Skills like (for example) **archery**, **gunslinging**, **kung-fu dragon style**, 
**battle hacking** or **punching**, or in general, any natural, codified or 
semi-codified way to perform a fight in the adventure setting are **combat skills**. 

**Combat skills** work similarly to any other skill in the system, with
the addition of the following characteristic:

* **Range type** (**Rt**): Can be **melee**, **ranged** or **transcendental**. 
* **Actions**: Some skills can be used multiple times in a combat turn. For example,
  a nimble skill having 3 **actions** would allow the character to attempt 3 attacks,
  or move, switch weapon and attack, all in the same turn.
* **Dominance** (**Dom**): a value roughly describing the effectiveness of the skill
  in a mixed combat, given opponents of the same skill level. 
* **Style**: A set of specific ways to use the combat skill, called **maneuvers** 
  causing special effects to take place during the combat 
  (used in the _advanced system_ only). 

### Generic combat skills

Trying to attack any target against their will should always involve 
a **combat skill**, even when not using a codified style of fighting. 

For example, a non-trained character may still just pick up a blunt
weapon and swing it, or pull a trigger of a loaded fire arm, or simply
try and punch someone, without a specific proficiency in a martial art or
any other experience about a specific way to fight.

The modules provide a set of "natural" **generic combat skills**, that
work as a default skill used when trying to attack someone without any specific
training. Of course, they are less effective than specific combat skills, but
they are also cheaper to train.

**Generic combat skills** always have a **dominance** of 0, **actions** of 1
and they  don't have an associated **style**, that is,
they cannot be used to execute any special **maneuver** in the advanced 
combat system.

### Skill Range

Combat skills are divided into _melee_, _ranged_ and _transcendental_.

* _Melee_ skills work when the combatants are in *close quarters*, and can
   physically harm each other without any projection.
* _Ranged_ skills use a weapon, a projectile or any mean to physically
   project a harmful device or source of energy towards a target. Skills of
   magical nature might be ranged if they magically create a projectile, ray
   of energy or any physical mean to harm a target.
* _Transcendental_ skills require their user to know where a target is in order
   to direct the attack, but they have no physical range. The target could be
   on another planet, as long as the user has a mean to see, feel or simply
   know _instantly_ about it.

### Close Quarters

The *close quarter* distance it's the distance at which a melee attack can 
be proficiently employed.

It corresponds to the distance an average fighter can jump and perform
a melee attack in one swoop. This is normally 6 feet, but may be different in settings
where the characters have superpowers that allow for faster movement (i.e. in an
adventure about vampires), or different sizes (i.e. in battles between giant robots).

### Dominance

The **dominance** (**Dom**) of a combat skill describes its effectiveness
in a mixed combat, given opponents of the same skill level. 

For example, in a certain setting **archery** skill may have **Dom** 3, 
while **gunslinging** has **Dom** 6; this means that a gunslinger would 
way more effective than a comparably competent archer on the battlefield.

Dominance is mostly used in the *advanced* combat system, but is also used
when mixing combat styles in the other systems. Whenever different combat
styles are employed, the **dominance** value of each skill is added to
every roll.

> For example, suppose a brawl fight
takes place in a tavern, and the town guards, armed with their crossbows, turn
in to stop the fight. As far as the combat skills go, the guards are using **archery**, 
while the brawlers are using **brawl**. While guards are less experienced in 
their **archery** than tavern goers are in their **brawl**, **archery** has an
innate advantage: its **Dom** may be somewhere around 3, while **brawl** **Dom** could
be 0 or 1. To resolve any fight, everyone will then add the value of the **dominance**
of they skill they want to (or can) use to every roll they take.

## Simplified Combat {#BaM-m-simplified-combat}

This combat system can be used to resolve fights between small group of opponents
are facing each other with _compatible_ fighting skills and weaponry.
For example, you can use this method when two small bands are shooting at
each other using using a **firearm** or similar skill, or involved in a fist fight and
using **brawl**, or taking part in a little **swordfight**_** skirmish. 

It is also possible for parties to use different, but somewhat compatible skills. 
For example, in a medieval tavern fight, guards may interrupt a brawl using armed
combat of some sort, or in a modern setting, someone may pull out a firearm during
a bar fight, of some participant may not be confident in brawling and use
a **generic combat skill** and swing pieces of broken furniture around.

In this cases, each participant will add the **dominance** value of the combat
skill they're using. 

### Fight Resolution

The simplified combat is a modified repeated multi-contest without draws.

The **GM** and/or the players decide how many rounds the fight will last in advance,
so that the best out of 1, 3, 5 (or more) rounds wins the fight.

Each turn, every participant uses the skill it prefers to use in this context 
(possibly, the best one). If the participants use different skills, 
they add their respective **dominance** to their throw.

On party draws (same number of points scored by each party), the throws are
repeated.

The effect of winning is determined by the circumstances. For example, 
a tavern brawl is hardly lethal, and a "friendly" swordfight (i.e. in order 
to subdue or dissuade an opponent) might simply end with the surrender of the
losing party. If that's not the case, both winner and losers may receive 
damage (with the losers generally receiving more).

## Injury Generation in Simplified Combat (optional)

In simplified combat, a losing character receives a number of **DP** equal to their
(negative) success margin. For example, if it loses with a **SM** of -6, 
it receives 6 **DP**. 

> Reminder: each success margin is computed with respect to the throw having the same ranking
in the other team. Highest throw in team A is compared with highest of team B, second highest
of A with second highest of B and so on.

The character can then use any sensible mitigation (armor or skills, if possible) to reduce
the raw **DP**.

A *critical failure* means that the character receives a *heavy wound* automatically.
Notice that, if one party is larger than the other, some of the characters in that party
(the ones with the lowest scores) will not be engaged directly in the fight; so, the lowest-scoring
characters will be mostly unharmed. However, they may still score a *critical failure* and
receive a wound because of that.

> As all the other rules about damage, **Injury Point** penalty applies to the simplified combat
as well. 

### Fight Continuation 

If the characters so desire, they can continue fighting until the losing party is
ultimately defeated (all of its characters are disabled) or decides to flee.

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

Each turn, a ranking throw called **combat order** is performed to determine the 
order in which every participant takes action. The attribute used for the ranking 
is decided by the **GM**, or it can be specified by the modules or adventure 
settings. 

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

A character can use the combat skill for defending against an attack also if it's not
their turn; however, when their turn comes, they will be able to attack only if they have
some actions left unused.

A character might also decide not perform any action when their turn comes; if so
they can interrupt any other action performed later on by others down the initiative
ranking, or eventually use a defense to respond to a later attack.

### Instinctive Defense

In some situations, the defender is aware of the incoming attack (i.e. has seen
the attacker and is ready to receive the blow) but can’t use any skill as a defense. 

Typical reasons are:
* The character already used all the actions at their disposal in a combat
  turn and can’t react any more;
* The defender doesn't have a proficiency in the skill used by the attacker,
  and is just reacting instinctively.
* The rules explicitly prohibit the use of other defenses (i.e. when disengaging
  from the combat).

In those cases, provided the defender is at least aware of the attacks, they can use
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

> For example, a martial artist using defending against a
sharp shooter standing between 6 and 12 feet away would have a penalty of -1;
at a distance of 60 feet, the penalty would be -5 (60/6/2 = 5). This can seem
a lot, but ranged skills have penalties for long range shot and range limits
already: no one can hope to perform a valid melee defense against a sniper
hidden on the next hill.

**Transcendental** skills cannot be use to defend against **melee** 
or **ranged** skills, and the other away around, **melee** and **ranged** 
skills cannot be used to defend against a **transcendental** attack.

### Ranged attacks falloff

Attack with ranged weapons receive the following modifier, which depends on the
distance to the target:

| Distance    | Modifier |
|:-----------:|---------:|
| < 1/4 range | 0        |
| < 2/4 range | -1       |
| < 3/4 range | -2       |
| <= range    | -4       |

### Cover

Cover provides a modifier to the defense against ranged attacks.

| Cover         | Modifier |
|:--------------|---------:|
| Full          | +4       |
| Partial       | +2       |
| On The Ground | +2       |
| Precarious    | +1       |

If a character has _full coverage_ and doesn't attack, nor moves, nor doesn't
perform any action exposing them, they cannot be attacked with a ranged weapon.
The defense is required only if the character is actually performing an action
that would expose part of them out of the cover.

A _partial cover_ is a high wall, large tree or column, a three feet tall rock, and
anything that could cover part of the body from the aim of the opponent.

A character _on the ground_ is completely squashed, and can only use weapons
and skill that might be used from this position (i.e. firearms).

A _precarious_ cover is something providing just visual obfuscation, like a
bush, or very partial cover, as a think tree trunk.

### Tactical situation

Some tactical situations during combat provide modifiers to the attack
rolls.

| Condition      | Modifier |
|:---------------|---------:|
| Surprise       | +2       |
| Higher Ground  | +1       |
| High Morale    | +1       |
| Desperate      | +1       |
| Tiredness      | -2       |
| Demoralized    | -1       |
| Bad Visibility | -1       |

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
depend of a perceived superiority of the opponents, or because all food is
depleted and a breakthrough is necessary for survival, etc.
* __Tiredness__: The characters are particularly tired, i.e. because they
couldn't rest after previous fights, or because being forced to fight after a
long march, or for having run because of a chasing.
* __Demoralized__: The characters are demoralized because of having lost
an important target already, their leader, the location they were meant to
defend, etc.

### Automatic Attack

In some case, the target of an attack is unsuspecting or unable to react:
for example, the target of a hidden sniper, or a sleeping victim.

In those situations, the combat is not resolved through a contest; the attacker
rolls on the attack skill, with the following difficulty table:

| Target Status                    | Modifier                         |
|----------------------------------|----------------------------------|
| Sleeping                         | Trivial                          |
| Distracted                       | Easy                             |
| Unaware                          | Normal                           |
| Suspicious                       | Difficult                        |
| Aware                            | Hard                             |
| In guard                         | Very Hard                        |

### Attack and Defense

When an attack is declared, the target (or targets) can use a defense, either
by using a specific combat skill or a _generic defense_.

The attacker and all the affected targets perform a Contest using their
chosen skill as a base.

The attacker rolls and adds the value of the skill, as for any contest.

Determined the value for the attack roll, each defender performs its defense,
rolling on the chosen defense skill.

A draw means that neither the attack nor the defense have been successful.
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
incantation) might further be applied. 

The character receiving the damage computes its _damage mitigation_ (__DM__)
by adding _passive defenses_ that can affect the damage source (i.e. armours),
and eventually _active defenses_ they might use.

Finally, the target character receives a number of __ED__ = __DP__ - __DM__.
This damage is accounted as specified by the [injury and damage](#injury-and-damage) rule.

### Critical Rolls

A critical success doubles the value of the _success margin_ when computing
the **DP** (for the attacker) or the **DM** (for the defender). 
When the damage roll doesn't involve the **SM**, the critical success adds
automatically 4 points to the final result.

> Notice that some defenses might generate a damage too.

A critical failure indicates a failure even when the roll itself would
indicate a success. For example, suppose an attacker with __brawl__ 16 against
a defender with __archery__ 5. If the attacker rolls 3, which is a critical
failure, the attack fails even if 16+3 would be above the archer's roll.

If both the attacker and defender roll a critical of the same type, the critical part is
discarded and only the roll result (with the respective modifiers) is considered: 
critical failures or successes on both sides elide each other.

## Advanced Combat

Advanced Combat is the most sophisticated combat sub-system; it expands the
basic combat system by adding a set of sub-skills for each combat skill,
called **maneuvers**. They represent special actions a character can take while using
the combat skill.

There are specific maneuvers to attack and defend in each style, and each of
them has different balances of difficulty of execution versus potential damage,
or different effects on the reset of the combat. Some maneuvers provide
modifiers to subsequent moves, while some other generate damage also
when defending.

### Maneuver types

Maneuvers are divided into _attacks_, _defenses_ and _actions_. Attacks and
defenses represent a mores specific usages of the base combat skill as
per the _base combat_ rules; _actions_ are other ways a combat skill can be employed.

### Maneuver Cost and Combat Resource

Each maneuver requires to spend a certain amount of **Advanced Combat Resources** (**ACR**) to be
successfully performed. The pool of ACR depends on the **Primary** attribute on which the combat type
relies on (physical, mental, magical etc.).

Once the pool is depleted, the character can perform only the basic maneuvers of the given combat style,
which has a cost of 0 **ACR**, and usually consists of the same basic action that could be performed in the
base combat.

Each primary attribute in the system determines a type and initial pool of combat
resources. For example, the **Generic Skillset** **Body** attribute determines an amount
of **Stamina**, which is used to perform physical advanced maneuvers based.

Advantages and temporary effect can provide a larger resource pool.

The pool is replenished at the end of the combat, after a period of rest that of one
minute for each point to be replenished, rounded up to the nearest ten minute slot.

## Generic Skillset: Combat Skills


- [Active Mitigation](#active-mitigation)
- [Archery](#archery)
- [Advanced Combat](#advanced-combat)
- [Block](#block)
- [Brawl](#brawl)
- [Advanced Combat](#advanced-combat)
- [Break Free](#break-free)
- [Concentration](#concentration)
- [Advanced Combat](#advanced-combat)
- [Disengage](#disengage)
- [Firearms](#firearms)
- [Advanced Combat](#advanced-combat)
- [Full Contact](#full-contact)
- [Advanced Combat](#advanced-combat)
- [Initiative](#initiative)
- [Instinctive Defense](#instinctive-defense)
- [Knife Fight](#knife-fight)
- [Advanced Combat](#advanced-combat)
- [Shoot](#shoot)
- [Slash](#slash)
- [Swordfight](#swordfight)
- [Two-handed weapons](#two-handed-weapons)
- [Advanced Combat](#advanced-combat)
- [Throw](#throw)
- [Thrust](#thrust)
- [Willpower Defense](#willpower-defense)

### Active Mitigation 

| <!-- --> | <!-- --> |
|----------|----|
| Callsign | AM |
| Category | Skill/combat |
| Specialization | combat style |
| Cascade | Yes |
| EC | Shields (opt) |
| Cost | 1 TT/Hard |

Once per combat turn, the character can mitigate incoming damage
by an amount equal (or less) than the **Success Margin** on a **Simple Check** on
this skill. 

This skill can be used also in simplified combat, after the full amount of damage
received by a character is computed.

For example, a warrior has **AM/Swordfight** 6, and the advantage **Expertise/AM/Swordfight** 
It receives damage for 5 **DP** after passive mitigation. Rolling on this skill
4 die (as an expert for **AM** in **Swordfight** style) it obtains 6, 5, 5, 1, for a total
of 6 + 5 + 5 for the roll and 6 for the skill level; the total is 22, so the **SM** is 
22 - 21 = 1.

In the end, the fighter receives 5-1 = 4 **DP**.

**Optional**: Dedicated equipment can change the difficulty of the check. Wearing a shield
or a defensive equivalent for the selected style will make the check *easy*.
In ranged styles, cover will be considered adequate shielding. More advanced technology or
magic may make the check *very easy*.

This is a [cascade skill]($RulebookAddress#cascade-skills); this means
it's possible to acquire this attribute multiple times to perform multiple
active mitigations per turn.

### Archery

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 4 |
| EC | Bows, Crossbows |
| Cost | 1 TT/Hard |

This is the base style (and skill) needed to use bows, crossbows and similar projectile
weapons.

Unless differently specified, all attacks from *archery* deal __pierce__ damage,
and the range depends on the used weapon.

### Advanced Combat 

*Archery* uses **Focus** as combat resources, which is determined by the **Mind**
primary attribute.

#### Aim 

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Archery 3 |
| ACR | 1 **Fcs** |

Take a maneuver to improve the next attack, giving it a modifier of +1.
It can be repeated any number of times within a single turn, but the
modifier is applied only to the very next Shoot.

#### Localized Shot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | Variable |
| Prereq | Archery 5 |
| ACR | 3 **Fcs** |
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
| ACR | 3 **Stm** |
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
| ACR | 0 |

Loads and shoot an arrow or a bolt.

### Block 

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

### Brawl

| <!-- --> | <!-- --> |
|------|----|
| Base | mS |
| Category | Skill/combat |
| Dominance | 0 |
| EC | Hand Fight (opt) |
| Cost | 1 TT/Normal |

Brawl is the style of fight with bare hand and feet, without a specific
preparation. It’s often used in tavern and bar fights, and can also be
useful in other combat situations.

Every human or humanoid character has access to brawl.

Unless differently specified, all attacks from **brawl** deal _blunt_
damage, and all the maneuvers are melee.

### Advanced Combat

*Brawl* uses **Stamina** as combat resources, which is determined by the **Body**
primary attribute.

#### Block

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS |
| Prereq | Brawl 1 |
| ACR | 1 |

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
| ACR | 0 |

Try and evade an attack moving the body out of the way of the incoming hit.

#### Grapple

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Prereq | Brawl 8 |
| ACR | 3 **Stm** |
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
| ACR | 1 **Stm** |
| Damage | __SM__+mD |
| Condition | __(Stun 2)__ |

The character attacks with a kick, causing a damage equal its dexterity plus the success margin.
Gets a +2 modifier on small creatures (less half the size of the attacker) and grounded targets.
On critical success, it stuns the target for 2 turns.

#### Punch

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Brawl 1 |
| ACR | 0 |
| Condition | __(Stun 2)__ |

Attacks with a direct punch. A critical success stuns the target for 2 turns.
Receives a -2 modifier against targets larger than the attacker.

#### Smash

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Brawl 6 |
| ACR | 3 **Stm** |
| Damage | __SM__-2 |
| Condition | __Grounded__ |

The attacker throws its own body against the target. On success, the target is
grounded for a turn.

Receives a +2 modifier on smaller targets and -2 on larger targets. Brawl/Evade
and other evasions receive a +2 modifier to defend against this action.

Can’t be used against grounded targets.

### Break Free 

| <!-- --> | <!-- --> |
|------|-----|
| Base | D/2 |
| Callsign | Bfr |
| Category | Skill/combat |
| Cost | 1 TT/Normal |

This skill is used to try and break free out of an engaged block.
Unless the character is completely subdued, they can attempt a **Bfr**
each successive turn.

To successfully break free, a character must win a **RNK** against 
all the opponents that have achieved a successful lock in the previous turn.

### Concentration

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

*Concentration* uses **Focus** as combat resources, which is determined by the **Mind**
primary attribute.

#### Alien Thoughts

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mI |
| Prereq | Concentration 1 |
| ACR | 0 |
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
| ACR | 0 |

The character raises a mental barrier in order to block an incoming attack.

#### Dig into you

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mW |
| Prereq | Concentration 1 |
| ACR | 2 **Fcs** |
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
| ACR | 1 **Fcs** |

The defendant diverts the attention of the attacker on an irrelevant
thought or memory, causing the attack to miss.

#### Mind Grasp
#
| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mI |
| Prereq | Concentration 6 |
| ACR | 3 **Fcs** |
| Condition | __Blocked__ |

The character tries to acquire the control of the defendant mind. On success,
the defendant is unable to act (blocked). To keep holding the target, the attacker
must continue to use this attack with + 3 modifier against it at each turn. 

The attacker must maintain its **concentration** to keep the target blocked. Only
one target can be blocked at a time.

#### Sensations

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -1 |
| Prereq | Concentration 4 |
| ACR | 2 **Fcs** |
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
| ACR | 2 **Fcs** |
| Damage Type | Despair |
| Damage | __SM__-2 |

The defendant turns the mental attack against the attacker.
If the defense is successful, the attacker is hit back for a
number of despair points equal to the success margin
of the defense minus two (minimum 1 dp).

### Disengage 

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

### Firearms

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 5 |
| EC | Firearms |
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

The Advanced Combat Cost of *Firearm* maneuvers is expressed in Focus (**Fcs**). 
A sharp mind is required to be a good sharpshooter.

#### Aim

| <!-- --> | <!-- --> |
|------|--------|
| Type | Action |
| Prereq | Firearms 3 |
| ACR | 1 **Fcs** |

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
| ACR | 4 **Fcs** |
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
| ACR | 0 |

Duck or evade while holding the firearm to avoid incoming fire.

#### Fast Reload

| <!-- --> | <!-- --> |
|------|---------|
| Type | Actions |
| Prereq | Firearms 4 |
| ACR | 1 **Fcs** |

Ability to reload the weapon in the heat of the combat, using a
maneuver.

#### Localized Shot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | Variable |
| Prereq | Firearms 4 |
| ACR | 1 **Fcs** |
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
| ACR | 3 **Fcs** |
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
| ACR | 2 **Fcs** |
| Range | 15 ft |
| Damage | __SM__+3 |

Fires twice in a single maneuver, each time with reduced attack and
damage. Can be used with pistols only.

#### Shoot

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Prereq | Firearms 1 |
| ACR | 0 |

Normal base attack with firearms.

#### Take Cover

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | +3 |
| Prereq | Firearms 3 |
| ACR | 2 **Fcs** |

If a cover is within movement range for the turn, the character can use this defense 
to run towards a covered position, with a fixed +3 modifier.

### Full Contact

| <!-- --> | <!-- --> |
|------|---------|
| Base | Brawl/2 |
| Category | Skill/combat |
| Prerequisite | Brawl 4 |
| Dominance | 3 |
| EC | Hand Fight (opt) |
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

*Full Contact* uses **Stamina** as combat resources, which is determined by the **Body**
primary attribute.

#### Counter Punch

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS-2 |
| Prereq | Full Contact 3 |
| ACR | 2 **Stm** |
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
| ACR | 2 **Stm** |
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
| ACR | 1 **Stm** |

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
| ACR | 2 **Stm** |
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
| ACR | 1 **Stm** |
| Damage | __SM__+3 |

The character attacks with its knee, causing a damage equal to its dexterity,
plus the success margin and a fixed modifier of 2.

Gets a +2 modifier on small creatures (less half the size of the attacker)
and grounded targets.

### Initiative

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

### Instinctive Defense 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill |
| Cost | 1 TT/Hard |

The instinctive defense is used against physical attacks whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available maneuvers for this turn.

It’s ineffective against mind attacks.

### Knife Fight

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| Dominance | 3 |
| EC | Knives |
| Cost | 1 TT/Hard |

Fighting with knives and very short swords has different mechanics than the ones used when wielding a longer blade. Basically, it’s like having a fist armed with a single fang.
While the weapon themselves could be less effective than longer ones, the style itself can be extremely effective in every scenario.
Knife fighting is particularly adequate for characters with a high dexterity.

### Advanced Combat

*Knife Fight* uses **Stamina** as combat resources, which is determined by the **Body**
primary attribute.

#### Backstab

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD-2 |
| Prereq | Knife Fight 6 |
| ACR | 2 **Stm** |
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
| ACR | 0 |

Skip back, trying to get out of the range of a melee attack.

#### Belly Opener

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -1 |
| Prereq | Knife Fight 3 |
| ACR | 4 **Stm** |
| Damage | +5 |

Swing the blade in an upward strike, aiming at the lower part of the opponent
body.

#### Change Hands

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 2 |
| ACR | 1 **Stm** |

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
| ACR | 3 **Stm** |
| Damage | +4 |

Swing the blade in a downward strike, aiming at the upper part of the
opponent body.

#### Evade

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| ACR | 3 **Stm** |

Try and evade an attack.

#### Feint

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | +3 |
| Prereq | Knife Fight 3 |
| ACR | 1 **Stm** |

Fake an attack, without actually completing it. On success it doesn’t
deal damage, but gives a **DP** modifier on the next move equal to
the success margin.

#### Hand Cutting

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD-2 |
| Prereq | Knife Fight 4 |
| ACR | 3 **Stm** |
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
| ACR | 4 **Stm** |
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
| ACR | 1 **Stm** |
| Damage | __SM__+1 |
| Condition | (__Cripple__) |

Throws the knife at an opponent within 15 feet. On success, it deals a limited damage.

#### Thrust

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Knife Fight 1 |
| ACR | 1 **Stm** |
| Damage | __SM__+4 |
| Condition | (__Cripple__) |

Attacks the target thrusting the knife forward, in a straight line.

#### Wrap and Stab

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD-3 |
| Prereq | Knife Fight 4 |
| ACR | 3 **Stm** |
| Damage | __SM__+6 |
| Condition | (__Injury__) |

Try to grab the opponent while fighting, to deliver deeper wounds. On success, this maneuver delivers an injury one level higher than normal.
_Light wounds_ become severe,_ severe wounds_ become heavy, and
_heavy wounds_ become deadly.

### Shoot 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| EC | Projectiles |
| Cost | 1 TT/Normal |

Shoot with a projectile weapon while not being specifically skilled to do so.
Weapons requiring skill in being loaded (i.e. bows, special military
rifles etc.) cannot be used with this skill, but loaded weapons (i.e.
crossbows) can.

### Slash 

| <!-- --> | <!-- --> |
|------|----|
| Base | mS |
| Callsign |  |
| Category | Skill/combat |
| EC | Blades, Maces |
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

### Swordfight

| <!-- --> | <!-- --> |
|------|----------|
| Base | mS or mD |
| Category | Skill/combat |
| Dominance | 4 |
| EC | Swords, Maces |
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

Brawl uses **Stamina** as combat resources, which is determined by the **Body**
primary attribute.

#### Cleave

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| ACR | 3 **Stm** |
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
| ACR | 1 **Stm** |

A basic defense; the character intercept the opponent’s blow with its own
weapon, using its own dexterity.

#### Feint

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | -3 |
| Prereq | Swordfight 6 |
| ACR | 2 **Stm** |

Uses an attack that will not deliver damage on success,
to get a **DP** modifier equal to the success margin on the
damage of very next attack.

#### Parry

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mS |
| Prereq | Swordfight 1 |
| ACR | 0 |

A basic defense; the character intercept the opponent’s blow with
its own weapon, using its own strength to resist it.

#### Parry Projectiles

| <!-- --> | <!-- --> |
|------|---------|
| Type | Defense |
| Modifier | mD |
| Prereq | Swordfight 6 |
| ACR | 0 |
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
| ACR | 1 **Stm** |
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
| ACR | 1 **Stm** |
| Limitation | Shield |

Can be used only if the character is wearing a shield. The defender blocks
the opponent’s blow with its shield.

#### Slash

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mS |
| Prereq | Swordfight 1 |
| ACR | 0 |
| Damage | __SM__+6 |

A simple lateral stroke.

#### Thrust

| <!-- --> | <!-- --> |
|------|--------|
| Type | Attack |
| Modifier | mD |
| Prereq | Swordfight 2 |
| ACR | 1 **Stm** |
| Limitation | Swords |
| Damage | __SM__+6 |

Thrusts a cutting weapon towards the opponent. Cannot be used with blunt or
two handed weapons (including swords).

### Throw 

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| EC | Throwable (opt) |
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

### Thrust

| <!-- --> | <!-- --> |
|------|----|
| Base | mD |
| Category | Skill/combat |
| EC | Blades |
| Cost | 1 TT/Normal |

A generic maneuver performed with any pointed or cutting weapon,
(always causing __cut__ damage),
including improvised ones. The character thrusts the weapon forward.

If the opponent is unaware, the skill requires a successful **CHK**
against *easy* difficulty.

In combat, a normal **CFR** is attempted against the opponent's defense.

### Willpower Defense 

| <!-- --> | <!-- --> |
|------|----|
| Base | mW |
| Category | Skill/combat |
| Cost | 1 TT/Hard |

The willpower defense is used against mental attacks, whenever
it’s not possible to use any other defense, for example, because
the character has used up all of the available actions for
this turn.

# Equipment

For *equipment* we intend whatever material is necessary for a skill to function.
For example, to use (lock picking)[#lock_picking] it is necessary for the characters to have a 
basic lock picking set available. Many combat skills require a specific type of weapons.

Advanced equipment may provide improvements of various nature:

* Provide a flat bonus to some dice roll involved in the skill.
* Reduce the difficulty level of checks.
* Improve the dominance of the combat skill used.
* Provide advantages as described in the manual (i.e. an automatic *mastery*).
* Provide additional side effects as:
  * reducing the noise caused by certain actions
  * introduce poison-like effects
  * produce a curse or a blessing when used
  * provide a passive or active damage reduction when receiving damage

Similarly, poor equipment may have reverse effect; for example, 
making simple actions more difficult, or providing a penalty to any dice roll.

Reasons why equipment may provide non-standard advantages are:

* Manufacture quality
* Magic
* Explicit upgrades
* Setting anachronism (coming from the future / a different place).

## Equipment Categories

Equipment is divided in *categories* (**EC**) which is the type of equipment that may be used
by a certain skill. 

A generic skill may actually use multiple **EC**s; for example, generic
**Shoot** skill may use anything that can be loaded with a projectile, so **EC** could include
firearms and crossbows.

Similarly, a single item may belong to multiple categories; a sniper rifle may be a *firearm* and
also a *precision weapon*.

## Optional Equipment

Some skills do not require to use any equipment, but may benefit from using one. For
example, in a fistfight is possible to fight with bare hands, but when using a device
as a metal gauntlet, the efficacy increases. 

## Generic Items

Not all objects the characters can use, wear or eat are considered "equipment". Anything that
isn't needed by a specific attribute is referred as a *generic item*. This includes:

* Clothing
* Food
* Magic Potions
* Single-use Healing Devices (e.g. stim-shot)
* etc.

In general, anything a character an use or carry but is not directly used by a specific skill or
attribute is a *generic item*.

## Charges and re-charges

Some equipment can be used a limited number of times, after which it either becomes unusable or
needs to be recharged. This is the case of magic scrolls in certain magic settings, that can be
used only once, or pistols that require recharging after their magazine is depleted.

## Generic skillset: Equipment

### Adventuring Equipment

Adventuring equipment is the equipment used in non-combat skills.

| Weapon Type          | Modifier   | Weight |     EC                 | Cost     |
|--------------------  |------------|-------:|:----------------------:|---------:|
| First Aid            | -          | 1      | First Aid Kit          | 20$      |
| Improved First Aid   | +1 PT      | 4      | First Aid Kit          | 400$     |
| Portable ER          | +2 PT      | 8      | First Aid, Healing Kit | 1000$    |
| Medikit              | Expertise  | 12     | First Aid, Healing Kit | 5000$    |
| Net Tools            | +1 PT      | -      | Rootkit                | 100$     |
| Penetration Kit      | Expertise  | -      | Rootkit                | 1000$    |
| Lock Picks           | -          | -      | Lock Picks             | 10$      |
| Improved Lock Picks  | +1 PT      | -      | Lock Picks             | 100$     |
| Prof. Lock Picks     | +2 PT      | -      | Lock Picks             | 400$     |
| Repair Set           | -          | -      | Repair Kit             | 80$      |
| Workshop Set         | +2 PT      | -      | Repair Kit             | 500$     |

### Armours

Armours provide damage mitigation against some specific damage types. Naturally, the damage mitigation applies to the part of the body where the armour is applied.
The following table is a generic guide that indicates the type of material of which armours are built, their approximate weight  in pounds, the cut, blunt and piercing damage mitigation and an approximate cost. The weight refer to the material applied to a body armour; to get the weight of arm and leg armour divide by half, and for an helmet divide by four.

| Material Type      | Weight       | Cut          | Blunt        | Piercing     | Cost        |
|:-------------------|-------------:|-------------:|-------------:|-------------:|------------:|
| Heavy Garment (1)  | 2            | 1            | 0            | 1            | 200$        |
| Kevlar             | 2            | 5            | 3            | 6            | 800$        |
| Bullet-proof Armor | 12           | 6            | 4            | 7            | 500$        |
| Meta-material (2)  | 6            | 4            | 6            | 3            | 1200$       |
| Energy Shielding (3) | 0          | 6            | 7            | 5            | 4000$       |
| Leather            | 8            | 3            | 1            | 2            | 40$         |
| Ring Mail          | 10           | 3            | 2            | 1            | 80$         |
| Chain Mail         | 14           | 3            | 1            | 2            | 150$        |
| Scale Mail         | 15           | 4            | 2            | 3            | 400$        |
| Thin Plate (4)     | 18           | 5            | 3            | 4            | 600$        |
| Heavy Plate        | 24           | 6            | 4            | 5            | 800$        | 

(1) Normal clothing doesn’t provide any mitigation, but heavy, multi-layer garment (i.e. overcoat, jacket, gilet, shirt and underwear) do.
(2) Gel-like material reactive to sudden shock.
(3) Just indicative; can be anything, depending on the technology. 
(4) Includes military metal helmets.

### Weapons

Weapons are either used unskillfully, using any one of the Generic Combat Skills, or through the appropriate combat style. The default damage (and often, damage type) caused by the weapon is already accounted for in the combat style; for example, Firearms/shoot causes a higher damage than Brawl/punch because guns are more lethal than bare hands.

However, some special weapon (i.e. magic swords, experimental rifles etc.) might give their wielder a modifier either to the attack or defense rolls, or solely to the damage caused once a hit is scored.
In the following table, the weight is the typical weight of for the given type of weapon, the range either the throwing distance or the range of the projectiles, in feet, and the cost is an indicative cost for a normal weapon of that kind.

| Weapon Type          | Modifier   | Weight | Range  |     EC                 | Cost     |
|--------------------  |------------|-------:|-------:|:----------------------:|---------:|
| Knife                | -          | 1      | 10     | Knives, Blades         | 20$      |
| Sword                | -          | 3      | -      | Swords, Blades         | 400$     |
| Mace                 | -          | 6      | -      | Maces                  | 100$     |
| Iron Fist            | +1 Dom     | 1      | -      | Hand Fight             | 20$      |
| Gauntlet             | +2 Dom     | 4      | -      | Hand Fight             | 200$     |
| Throwing Knife       | +1 Dom     | 0.2    | 18     | Throwing               | 5$       |
| War Hammer (*)       | +1 Dom     | 12     | -      | Maces                  | 300$     |
| Two Handed Sword (*) | -          | 8      | -      | Swords                 | 600$     |
| Shield               | +1 PT      | 6      | -      | Shields                | 80$      |
| Large Shield         | Expertise  | 12     | -      | Shields                | 600$     |
| Pistol (revolver)    | -          | 1      | 60     | Firearms, Projectile   | 600$     |
| Pistol (semi-auto)   | +1 Dom     | 1      | 60     | Firearms, Projectile   | 800$     |
| Rifle                | +2 Dom     | 4      | 90     | Firearms, Projectile   | 1200$    |
| Sniper’s rifle       | +1 Dom     | 6      | 200    | Firearms, Precision    | 1800$    |
| Short Bow            | -          | 1      | 30     | Bows                   | 40$      |
| Bow                  | -          | 1      | 45     | Bows                   | 80$      |
| Long Bow             | +1 Dom     | 2      | 60     | Bows                   | 120$     |
| Crossbow             | -          | 2      | 40     | Bows, Projectile       | 150$     |
| Heavy Crossbow       | +1 Dom     | 4      | 60     | Bows, Projectile       | 200$     |

(*) Two handed weapons.

# APPENDIX: Theorycrafting Elements

In this appendix, you can find some technical elements about the numbers
behind the SIRPAS system.

This is also a place where we store our theory, and check our design
explicitly, to see how it works when the dice start rolling.

## Chance Table

This table gives you the probability to roll a certain number or to beat
a certain value with the sum of 3d6.

The "chance to match" column shows you how likely is to roll exactly the
value on the left column. The "Chance to Beat" is the probability to roll a
number _greater_ than the one on the left. To get the probability to roll
_at least_ the number on the left, add both columns.

| Target Score | Chance to match |  Chance to beat |
|-------------:|----------------:|----------------:|
| 3            |    0.46%        |   99.54%        |
| 4            |    1.39%        |   98.15%        |
| 5            |    4.17%        |   93.98%        |
| 6            |    4.63%        |   89.35%        |
| 7            |    5.56%        |   83.80%        |
| 8            |    8.33%        |   75.46%        |
| 9            |    10.19%       |   65.28%        |
| 10           |    15.28%       |   50.00%        |
| 11           |    15.28%       |   34.72%        |
| 12           |    10.19%       |   24.54%        |
| 13           |    8.33%        |   16.20%        |
| 14           |    5.56%        |   10.65%        |
| 15           |    4.63%        |   6.02%         |
| 16           |    4.17%        |   1.85%         |
| 17           |    1.39%        |   0.46%         |
| 18           |    0.46%        |   0.00%         |

## Contest Table

This table shows how likely is to win, lose or achieve a draw on a contest
roll, given a certain difference in the base.

Suppose the base is the same for both characters; the difference of the bases
is zero. The probability to win or lose is the same, 45%, and there is a
10% probability to roll a draw.

If a character rolls on a base 10, and the other has a base 13, the difference
is 3. The character with the base 10, reads its chances on the -3 row, and the
other uses the row number 3. In this case the advantage character has 70%
chance to win, 22% to lose and 8% to achieve a draw; the position of the
other character is reversed.

|  Difference | Chance to win    | Chance to Lose | Chance to Draw |
|------------:|-----------------:|---------------:|---------------:|
|  -9         |   1.20%          |   97.79%       |     1.00%      |
|  -8         |   2.21%          |   96.16%       |     1.63%      |
|  -7         |   3.84%          |   93.67%       |     2.49%      |
|  -6         |   6.33%          |   90.01%       |     3.66%      |
|  -5         |   9.99%          |   85.13%       |     4.87%      |
|  -4         |   14.87%         |   79.19%       |     5.94%      |
|  -3         |   20.81%         |   72.07%       |     7.12%      |
|  -2         |   27.93%         |   63.88%       |     8.19%      |
|  -1         |   36.12%         |   54.78%       |     9.10%      |
|  0          |   45.22%         |   45.22%       |     9.57%      |
|  1          |   54.78%         |   36.12%       |     9.10%      |
|  2          |   63.88%         |   27.93%       |     8.19%      |
|  3          |   72.07%         |   20.81%       |     7.12%      |
|  4          |   79.19%         |   14.87%       |     5.94%      |
|  5          |   85.13%         |   9.99%        |     4.87%      |
|  6          |   90.01%         |   6.33%        |     3.66%      |
|  7          |   93.67%         |   3.84%        |     2.49%      |
|  8          |   96.16%         |   2.21%        |     1.63%      |
|  9          |   97.79%         |   1.20%        |     1.00%      |

Consider: with a -3 modifier, you have only 1 chance over five to win; 
be very cautious fighting characters with higher bases than you.
