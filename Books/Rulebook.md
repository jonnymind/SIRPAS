

# Introduction

SIRPAS stands for "SImple Role Playing Adventure System". It's a generic, modular
and extensible table-top RPG system, that aims to be as simple as needed and
become as complex as you wish.

SIRPAS is organized in the following components:
* The **rulebook** (what you're reading now): bare-bone description of how the
  system works. There isn't any list of skills, attributes, or specific 
  rendering of the rules in practice. At times we'll use some well known 
  skill that may be found in any generic RPG (e.g. *strength* or *climbing*) 
  to make some example of how the rules work, but nothing more.
* The **base system**: a basic implementation of the rules, which describes
  very generic attributes, skills, damage sources and other concrete aspect of the
  system, that should be general enough to be applied to most if not all the
  RPG settings you may come up with.
* Additional **modules**: Extension of the base system (which may enrich it or
  change it if necessary), particularly adequate to describe some specific world
  or setting for your adventures.

All you need is the **base system**. The system will often refer to the rules in this
rulebook, so you will need to know them, but you don't need to know them *upfront*. The
**base system** will briefly explain the relevant rules when possible or point at this
rulebook when necessary. You may wish to read this book in advance, skim over it, or
just ignore it until you feel the need to read some portions of it following the 
**base system**.

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
* Generic: rules are meant to be applicable in any settings you can come up with. More on that later.
* Modular: Sirpas has a lean set of rules called **Base System**. The base system is generic enough
  to support any world setting and playing style. On this base system, additional rules (called **modules**)
  can be attached to better fit your game world. Want a system to perform mind fights between Asimov inspired psionic 
  super-humans? We got you. Want a be a gunslinger involved in western-styled show downs? That can be done too.
  A wizard casting magic spells? No problem. An occultist summoning extra-dimensional entities? That's fine.
  The system is even flexible enough to merge multiple styles of magic, melee combats, large scale fights
  and ranged missile firing in the same session. Yes, you can bring a bow (or a knife) in a gunfight.
* Extensible: Other than designing your own additional modules, you can also modify the base system to fit
  your need. For example, there base system has two main attributes called **Body** and **Mind**; if you
  want to play as an AI in a virtual world, you may replace **Body** with **MIPS** (millions of operation per second),
  and use **Mind** as an expression of the quality of your O.S. and software. The rest of the base system will
  still stand and be mostly useful for you to play with.
* Role-play oriented: the system emphasizes the build-up of the character; both the composition of its skill set
  in the adventure world, and the makeup of its personality, play a primary role in how the rules unfold.
* Simple as you want: the base system has differently detailed rules to resolve game situations. For example,
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

* **Attributes**: important aspect of the character on which many other mechanics depend. 
  For example *body* (**B**), *mind* (**M**), *health* (**H**) and *will* (**W**).
  **Skills** are special **attributes** used to perform specific actions, 
  as *hacking*, *lock picking*, *running*, *climbing* etc.
* **Statuses**: values that vary fluidly during an adventure; for example,
  to keep track of the current health of a character you can look at its **injury points**.
* **Advantages**/**disadvantages**: Statistics affecting other skills, as example an expert 
  modifier which increase the chance of winning checks against a specific skill. 
* **Perks**/**drags**: distinctive traits setting the character apart from the 
  background people in the setting. Could be things a "famous" or "criminal". 
  They have an impact in the adventure at large, and might also affect indirectly 
  some checks, providing bonuses and penalties at discretion of the game master.

## Character Points

Character Points (**CP**) express the amount of experience of your character, 
and with that, the amount of learning (improvement of its statistics) that 
the character will perform during the adventure, or in between adventures.

Roughly speaking, statistics can be bought, and in some case sold, 
in exchange with character points.

The amount of **CP** that must be spent to increase a certain statistic vary depending 
on the nature of the statistic, and in most cases, also depending on its current level. 
It is easier to increase low scores, and as the statistic gets higher, it becomes harder 
and harder to perfect it further.

Statistics are scored with their base and a specific amount of points assigned to them. 
For example, the skill sprint is based on dexterity. If the current value of dexterity is 10, 
and nothing has been invested in sprint, then sprint will be 10 as well. To buy a point 
of sprint, the character must invest the CP needed to bring it from 10 to 11. Now, if 
at a later time the character increases its dexterity, the sprint skill will increase as well, 
as the points previously spent on sprint represent a bonus with respect to the dexterity base.

This means that it’s usually preferable to invest in the desired skills in the beginning, 
and then increase the base at a later time. On the other hands, later adventures typically 
provide a larger amount of CP per session, so the decision whether to invest on single skills 
or on more powerful bases, while important, is not as critical as it might seem.

The following table describes how many CP must be spent in order to increase a statistic. 
Skills have different costs, depending on the complexity of learning a certain skill.

| Level        | Mains        | Attributes   | Skill/hard   | Skill/normal | Skill/easy   |
|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|
| 4            | 15           | 5            | 1            | 1            | 1            |
| 5            | 18           | 6            | 1            | 1            | 1            |
| 6            | 21           | 7            | 1            | 1            | 1            |
| 7            | 24           | 8            | 1            | 1            | 1            |
| 8            | 27           | 9            | 2            | 1            | 1            |
| 9            | 30           | 10           | 2            | 1            | 1            |
| 10           | 33           | 11           | 3            | 2            | 1            |
| 11           | 36           | 12           | 3            | 2            | 1            |
| 12           | 39           | 13           | 4            | 2            | 2            |
| 13           | 42           | 14           | 4            | 3            | 2            |
| 14           | 45           | 16           | 5            | 3            | 2            |
| 15           | 50           | 18           | 5            | 3            | 2            |
| 16           | 55           | 20           | 6            | 4            | 3            |
| 17           | 60           | 22           | 6            | 4            | 3            |
| 18           | 70           | 25           | 7            | 5            | 4            |



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
considered minimally  functional in the game world — a value below 3 
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

Different settings might introduce different ranges with other scaling rules; 
for example in a vampire society, the Body attribute (**B**) could be measured 
in a 0-100 range, where a B0 for a vampire would be equivalent to a B18 for a human,
and where the difference between B0 and B1 and between B49 and B50 is the same.

### Base Modifiers

In some situation, instead of using a statistic as a direct base, 
the system requires to use a base modifier (represented as **mX** where **X** is the 
base attribute).

This happens when some  statistics are baseless by their own nature, 
but a base statistic influences them nevertheless.

For example, many combat styles are baseless, as you need to learn them from scratch to be good at those, 
but characters with a higher dexterity, or rather strength, are naturally better at it.

| Attribute | Modifier |
|:---------:|---------:|
|    3-5    |       -3 |
|    6-7    |       -2 |
|    8-9    |       -1 |
|   10-11   |        0 |
|   12-13   |       +1 |
| 14-15     |       +2 |
| 16-18     |       +3 |

Suppose a skill has base declared as **mD**. This means the base of that skill is not **Dexterity**
directly, but the modifier derived from the above table.

### Attribute descriptions

Attribute are described with:
* Their short name (usually an acronym) always in **bold**.
* Their *base* formula, if any
* Their difficulty.

### Training attributes

Higher level attributes form the **base** of the lower level ones. This means that,
by default, all the sub-attributes of a top one will have its same value.

A player can increase the value of any attribute by **training** it:
using **Character Points** to improve it. When it does so, 
all the lower level attributes grow with their **base**. Of course, training on a
base attribute is more expensive than training on specific detail attributes.

For example, suppose that in a game world the attribute **Dexterity (D)** is the base
for **Archery (Arc)**. A character that has never learned **Arc**, but has a value of 
**D** 10, has a *default* value of 10 in **Arc** as well. If the character trains
on **Arc**, it may get an extra point and have **D**=10, **Arc**= **D**+1 =11. 
If the character then trains on general **D** (which is harder than specialize in **Arc**),
so that its **D**=11, its **Arc** grows to, as now **Arc**= **D**+1 = 12.

The number of character point to be spent in each attribute or skill to train it depends on how
many other attributed are based on that, and on the objective complexity of improving it.

# Statuses and status points

Characters will sustain negative effects in pools called *statuses*. Most statuses are binary,
i.e. on or off. For example, a character may be *asleep* or *awake*: it's awakeness status may
be on/off.

Some statuses have numeric values, and the character will be negatively affected if the number
increases. For example, the number of [injury points](
the higher the worse.

Finally, there are statuses that start at a certain maximum level, and as the characters use 
their skills, they are used up. This statuses are called *pools*, and various modules and 
sub-systems can define different pools for specific usages. For example, a magic system may
define a *mana pool*, which determines how many spells a character can cast.

# Advantages and Disadvantages

Advantages special conditions that apply to the character in general or to a specific attribute or set
of attribute in particular, and that have a direct effect on some game mechanics.

For example, some advantages may grant you the possibility to automatically win a draw once a day. 
Others may give you extra dice to throw and use in some situation. Others may give you one extra
point to all the skills having a certain base attribute, i.e. improve all the skills based on 
**Dexterity**. Others may reduce the difficulty level of the attempts on a certain skill by one
level, so that i.e. easy pickpocket targets become trivial, normal targets become easy and so on. 

Advantages can also be negative (disadvantages). A character might be given
disadvantages temporarily or permanently, because of what happened during
previous adventures, or as a background flavor. As disadvantages have negative CP costs,
a player can chose to get certain disadvantages in order to gain **CP** to be
spent elsewhere, in other statistics.

While most advantages are simply either active or not, some can have different levels. 
For example, an advantage called i.e. Survival Instinct, which, say, reduce the difficulty level
of all survival checks, may have a level between 1 and 3, each granting a one extra reduced difficulty level. 

In that case, the description of the advantage indicates the initial cost and the cost per additional level. 
The cost of a further level is given by the base cost, plus the additional level cost times the current level. 
For example, if the description indicates the cost in **CP** being 5+2, it means that the first level costs 5, 
the second 5+2*1 = 7, the third 5+2*2 = 9 and so on.

Some advantage could have a pre-requisite that must be fulfilled in order to be acquired. 
For example, they could require having already acquired another advantage, or having a certain 
statistic at a minimum set score.

The GM may allow to get a certain number of advantages and/or disadvantages to taken at character creation,
or may allow to get some of them later on if that's fitting for the setting. For example, in a cyberpunk
setting, many advantages may be granted through body implants, which may be be bought under certain
conditions.

# Perks and Drags

Perks and drags are generic advantages and disadvantages that don’t 
impact the game system directly. They usually give more flavor  in 
terms of roleplaying, and better define a character in its settings.

Being famous, of noble origins, being able to play a certain instrument, 
knowing a certain literature or scientific topic, being rich, and the 
inverse of those are considered perks (or drags). 
 
They can and usually will have an influence in how the adventure plays, 
and some of them can have indirect and direct effect on the rules.

For example, if a certain module has a **Criminal Boss** perk, that may
influence any attempt to **intimidate** specific characters that know 
about the reputation of the character, and have a reason to fear it.


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

| Difficuylty          |  Success Level   |
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

The the fourth
ranked in B, and the fourth and fifth in C are **excluded** and will not contribute to winning.
Nevertheless, the
most numerous group has an advantage in having more chances to score high points 
than the others -- everything else equal.

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
   to the topmost character, so that it can read the ranking results going top to bottom. 

If the GM doesn't have a dice-throwing application handy, which can automate part of the process, it
can use the following procedure to generate multiple scores at once:
1. Roll 2d6 and write down the result.
1. Roll Nd6, where N is the count of character controlled by the *GM*.
1. If more than one 6 is rolled, count them as 7, 8 etc.
1. If more than one 1 is rolled, count them as 0, -1 etc.
1. Add each single rolled result to the previous 2d6 roll.

For example, the GM controls 5 characters.
1. It rolls 2d6 for a total of 7.
1. It now rolls 5d6, one per character; the results are 6, 6, 4, 1, 1.
1. The characters gets the following points, top to bottom: 7+7 = 14, 7+6 = 13, 7+4 = 11, 7+1 = 8 and 7+0 = 7.
1. Now the GM gets the result from the players, and communicates the winning party, 
1. the scoring characters and, if relevant, the negative **SM** of the **succumber** characters.


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

In a *contest* a *critical success* can be 
scored only by the winning party (as the **SM** can be only positive, and
is assigned to the winner); hence, a contest can't determine **critical failures**.

Conversely, **rankings** have only negative **SM**, so they cannot result in 
**critical successes**.

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

It can be used to determine an overall status of a fight, or to determine precisely 
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

* *Passive Defenses*: reducing the incoming **DP**s of a flat amount (like physical armors),
  or dividing the damage by a certain factor, i.e. 4/5 or 3/4 (like magic or sci-fi shields),
  or eventually by an hybrid formula (as in the case of specific resistances against some
  kind of damage).
* *Active Defenses*: the amount of reduced **DP**s depends on the use of a certain
  character ability. 

The way different kind of damages impact on the characters is fully considered by the way
defenses are applied to reduce the incoming **DP**s.

The count of **DP**s left after the defenses are applied is called 
*effective damage* (**ED**).

## Effective Damage and Wounds

When sustaining a certain amount of damage, the character
receive a certain kind of wound, according with the following table:

|**ED** | Wound   | **IP** | 
|------:| -----   | ------:| 
| 0     | Scratch |      - | 
| 1-3   | Light   |      1 | 
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

The number of *IP* that can be received before being incapacitated is
determined by the **resistance** (**Res**) towards that damage source, which is
an attributed defined by each module.

### Wounds Penalty

A character receives a penalty to any check of half the sum total of
**IP**s across all types (rounded down). 

While the type of the wounds its relevant for the amount of damage that
can be sustained, that doesn't matter for how well the character is
performing. You are not going to find a new theorem with a broken
arm, and your fighting style will be less than effective if your
mind is in shambles.

## Scratches

A character receiving an *effective damage* greater than 0, 
but below the amount necessary to generate a wound receives a "scratch".
 
Scratches are extremely light wounds that, by themselves, don't impact
the character **IP** pool.

However, once received a certain number of scratches, they are considered
as one light wound. The number is determined by the **scratch resistance** (**SRes**)
to that damage type, which is defined by each module.

### Non-scratches (optional)

When the damage received is mitigated to the point to be insignificant, 
it doesn't generate a scratch.

Unless the module specifies differently, when the **ED** is -3 or less, 
that isn't accounted as a scratch. However, it may still generate negative effects,
for example apply any form of physical or magical poisoning, inject a virus in an AI
or in a cyber brain and so on.

## Deadly Wounds (optional)

When a character receives more than 9 *ED* points, it sustains a wound that is
potentially able to kill them immediately.

To avert an immediate death, the character must pass a _simple check_ on the
**resistance** (**Res**) to the specific damage source, which is determined by
each module.

When character can't use any specific resistance skill, the check is performed
on __body__, if the damage is physical, or __mind__, if it's mental.

If the check is successful, the character receives a _heavy wound_.

> Remember that the _resistance check_ has a negative modifier of half the
received **IP**s, as any other action.

## Direct Wounds

In some situation, a character can receive a wound of a certain kind directly,
and not as a consequence of a damage source dealing damage points. For instance,
certain magic spells could cause a heavy wound directly, if the character fails
an attempt to resist them. A overwhelmingly powerful weapon, for example a starship
laser directed against a human, could have the same effect. Explicit actions 
performed on the character when it is unable to defend itself 
(i.e. forms of physical or mental torture) could deal
an arbitrary wound as the attacker seems fit, etc.

Direct wounds will immediately apply the relative **injury points** as if they were
received through damage application.

## Localized Wounds

By default, wounds are generally directed in the generic direction of the body,
but some abilities allow to aim a certain specific part of the body.

### Wounds to limbs or periferical devices

When a wound is localized on a specific body part (an arm, a leg), 
any action involving that body part receives the double amount of
penalty from that wound type. For instance, a *heavy wound* localized
on a leg will generate 2 *IP* as normal, generating a penalty of 2 points
to any check, but the penalty will be -4 or any skill involving jumping, 
running and using specifically the legs.

This extends to non human and even virtual body parts as well: and AI receiving
a heavy wound on a virtual device will have a double penalty if it tries to use
that device to perform any action.

### Wounds to the head or control unit

When a wound affects the head (or other target part that is particularly critical
to control the behavior of the target), it generates an additional **injury point**.
*Light wounds* generate 1 *IP*, while *medium* and *heavy wounds* generate 2 and 3
**IP** respectively.

### Curing wounds

As a wound is cured through any mean (medicine, magic, natural healing etc.), 
its **IP** cost is removed.

Scratches not turned into a light wound are removed after a reasonable amount of time
and minimal care adequate to the setting. For example, in a fantasy setting, that may
be spending a few minutes to tend the wounds after a combat. In a cyberpunk setting, 
it may be applying wound-reducing foams. 

**Optional**: in any setting, the equivalent of a day of rest should clear any scratch.


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


