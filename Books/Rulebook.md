# Introduction

SIRPAS stands for "SImple Role Playing Adventure System". It's a generic, modular
and extensible table-top RPG system, that aims to be as simple as needed and
become as complex as you wish.

SIRPAS is organized in the following components:

- The **rulebook** (what you're reading now): bare-bone description of how the
system works. There isn't any list of skills, attributes, or specific 
rendering of the rules in practice. At times we'll use some well known 
skill that may be found in any generic RPG (e.g. *strength* or *climbing*) 
to make some example of how the rules work, but nothing more.
- The **base module**: a basic implementation of the rules, which describes
very generic attributes, skills, damage sources and other concrete aspect of the
system, that should be general enough to be applied to most if not all the
RPG settings you may come up with.
- Additional **modules**: Extension of the base system (which may enrich it or
change it if necessary), particularly adequate to describe some specific world
or setting for your adventures.

All you need is the **base module**. The system will often refer to the rules in this
rulebook, so you will need to know them, but you don't need to know them *upfront*. The
**base module** will briefly explain the relevant rules when possible or point at this
rulebook when necessary. You may wish to read this book in advance, skim over it, or
just ignore it until you feel the need to read some portions of it following the 
**base module**.

> **Experts**: Feel free to skip the rest of this introduction. 
> The only thing an expert
> need to know about is that SIRPAS is generic (setting-less), skill-based, 
> using d6 only (and mostly 3d6) with a fully modular system architecture. Detailed 
> sub-system can be used or ignored, depending on the mood of the night,
> while still having your character set-up count. Also, all the systems are
> inter-playable: you could bring a character from a Cthulu-esque campaign 
> in a cyberpunk settings, and the rules will work just fine.

## What is SIRPAS?

SIRPAS is a "SImple Role Playing Adventure System".

So, we’re talking *adventures* here: a role playing session that can spawn for 
a casual night with friends, or with the family, or with strangers met at a gaming 
club. Systems thought for Role Playing Games are (usually) complex enough for you 
to invest lots of time in creating your characters, play through multiple sessions 
and use some time off to sort your past games out to get fun out of them. 

Some may say that's actually part of the fun itself. If you like the streamlined 
experience of Sirpas gameplay, you can play adventures spawning multiple sessions, 
or multiple adventures with the same characters, in the same world (this is often
referred as *campaign*). 

But you don’t need to. The idea is having as little commitment as necessary to get 
playing, and then, pour in as much commitment as you want if you like it.

## A system for everyone

Sirpas is for everyone: beginners, intermediate and veteran players.

Who reads this manual and has never heard about role playing games
before will encounter many new terms that have a special meaning in RPG,
as *session*, *adventure*, *campaign*, *world*, *setting*, *character*,
etc. Also, they might need on how to prepare, organize, manage, or
even behave during a session. This is important, but it is not covered
in this manual. This rulebook presents the game as succinctly as possible;
all the concepts commonly known in RPG can be easily found in the larger
Internet. 

However, to help the beginners getting on RPG with Sirpas, depending on the
media you’re reading the rulebook, we will:

1.	provide hyperlink to the description of the term. 
2.	highlighting terms with special meaning in RPG. A fast Internet search
for "RPG" and the highlighted word will  bring you to the description of the term.
3.	Add a box named "For Beginners" near the relevant terms, that experienced
readers can skip.

## Feel of the system

Sirpas has the following characteristics:

- Generic: rules are meant to be applicable in any settings you can come up with. More on that later.
- Modular: Sirpas has a lean set of rules called **Base System**. The base system is generic enough
to support any world setting and playing style. On this base system, additional rules (called **modules**)
can be attached to better fit your game world. Want a system to perform mind fights between Asimov inspired psionic 
super-humans? We got you. Want a be a gunslinger involved in western-styled show downs? That can be done too.
A wizard casting magic spells? No problem. An occultist summoning extra-dimensional entities? That's fine.
The system is even flexible enough to merge multiple styles of magic, melee combats, large scale fights
and ranged missile firing in the same session. Yes, you can bring a bow (or a knife) in a gunfight.
- Extensible: Other than designing your own additional modules, you can also modify the base system to fit
your need. For example, there base system has two main attributes called **Body** and **Mind**; if you
want to play as an AI in a virtual world, you may replace **Body** with **MIPS** (millions of operation per second),
and use **Mind** as an expression of the quality of your O.S. and software. The rest of the base system will
still stand and be mostly useful for you to play with.
- Role-play oriented: the system emphasizes the build-up of the character; both the composition of its skill set
in the adventure world, and the makeup of its personality, play a primary role in how the rules unfold.
- Simple as you want: the base system has differently detailed rules to resolve game situations. For example,
combat or any type of confrontation between two opposing parties could be resolved with a single throw of a few
dices (Risk! style), or with the detail of a Warhammer miniature replica battlefield.

All the system is based on multiple rolls of a standard dice with 6 face; however, different modules support other
kind of dices, if that's the vibe you want for your game.

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

Sirpas works the other way around: the combat system is simply the
specialization of the general system. As such, is possible to run adventures or
entire campaign devoid of "combat", and focusing either on other kind of contest
(as i.e. skill battles in virtual worlds), or in other aspects of the role
playing altogether.

Consider, for example, a police drama as a RPG setting. While gunfights might
play an important part in the campaign, the very nature of a gunfight doesn’t
translate into interesting RPG mechanics, while more interesting actions as
sword fights or martial art fights might not fit the setting.

As such, Sirpas focuses on a more differentiated gameplay, which can be as
combat-intensive or combat-devoid as needed.

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

## Attributes

Attributes describe a character as succinctly as possible. 
They are organized in a hierarchy. Higher level attributes are more *generic*:
they describe general aspects of your character. The lower you descend in the
hierarchy, the more detailed the attribute become. At the bottom of the hierarchy
we find **skills**, that are attributes dedicated to performing specific actions.

Attributes and skills are normally expressed as a value between 3 and 18, 
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

Modules can introduce different range and scaling for some or all the attributes; 
for example, in a vampire society an attribute like **Vampire Speed** (shortened as **VS**)
could be measured as a linear scale in a 0-99 range, where a **VS**0 is as
fast as the fastest human, with one point of difference having the same value whether the 
**VS** is 0 or 99.

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

In general, the hierarchy level of the **TT** is specified as a number, so
that **TT**/1 is a train token for the top tier attributes, **TT**/2 is one
for the attributes directly derived from them etc; however, every module can
declare different attribute categories and hierarchies, that aren't necessarily
following the base value chains.

For example, if a module declares a hierarchy of attributes as
```
Primary -> Generic -> Hard Skills -> Easy Skills
```

a **TT**/Primary can be exchanged for 2 **TT**/Generic, 4 **TT**/Hard,
or 8 **TT**/Easy.

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

### Cascade Attributes

Cascade attributes are attributes that can be be trained multiple times, each of them
representing a single attempt in repeated checks.

For example, some combat skills can be used only once per combat turn. To use them
multiple times in a turn, a second version of the same skill must be trained.

In the player sheet, they will be indicated as "Composite skill / 1", "Composite Skill / 2"
and so on. If the composite skill is specialized, it will be indicated as 
"Skill/specialization / 1", "Skill/specialization / 2" and so on.

Composite attributes are still targeted as a single one by attribute-targeting advantages
and disadvantages.

For example, if "Active Mitigation" is a combat specialized and composite attribute,
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
*Drawless Contests* (**ndCNT**). In this cases, when a draw is scored, it is
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
1. Besides each name, write the modifiers for that characters, to be updated 
if the contest is repeated.
1. Unless each GM controlled character is special, the GM always assigns the best outcome 
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

### Styles and maneuvers

In the _advanced combat system_, **Combat skills** are associated with a _style_, 
that is a collection of actions that can be done using the skill (called **maneuvers**).

**Maneuvers** are not stand-alone skills, and they cannot be target of advantages or perks.

The same combat style can also cover different type of weapons, with some
specific maneuvers limited to some weapons. For example, a combat skill may be
**Firearms**, covering any kind of modern firearm, and its style may include maneuvers as 
**rapid reload**, which applies only to pistols, and **sniping**, which applies only to
precision rifles.

Maneuvers have the following statistics:

* Type: can be **attack**, **defense** or **action**.
* Modifier: positive or negative bonus to the combat skill for any type of roll.
* Prerequisite: minimum level of other attributes/skills required to perform this maneuver.
* Diminishing Return: modifier to the roll if using the same maneuver more than once in a row.
* Range: If the combat skill is ranged, the distance at which this maneuver is effective.
* Damage: How many **DP** the maneuver inflicts if successful. Defenses and actions can have
generate damage as well (i.e. counter-attacks or actions causing indirect damage).
* Status: a status alteration of the target if the maneuver is successful (i.e. causing
the target to be *stunned* for 2 turns, and so on).

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
per the _base combat_ rules; _actions_ are
other ways a combat skill can be employed.

### Maneuver modifier

Some maneuvers are more difficult than others; some rely on brute force, others
on finesse of execution. To reflect this, each maneuver can offer different
modifiers to the various combat skill rolls.

### Diminishing Returns

Some maneuvers get a negative modifier if being used repeatedly against the same
target. For example, repeating using a brawl/punch has diminishing returns: your
opponent will read your move, and will be able to better defend against the same
attack. In those situations, you’ll want to be less predictable, and use other
maneuvers, or other styles altogether.

This factor is called __diminishing return__ (**DR**) for a certain maneuver.

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
