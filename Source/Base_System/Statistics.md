# Statistics {#BaM-gen-statistics}

In SIRPAS, the statistics are all the numeric or quality values that define a characters. 
They are divided in the following categories:

* Attributes: important aspect of the character on which many other mechanics depend. 
  For example *body* (**B**), *mind* (**M**), *health* (**H**) and *will* (**W**).
* Structural Staticstics, or **structs**: A set of statistics that regulate how 
  characters are structurally built; for example, how they receive and resist damage,
  how much stress they can sustain before going deranged, how many times they must feed
  or recharge in a day, and so on.
* Status Statistics: values that vary fluidly during an adventure; for example,
  the amount of **injury points**, **fatigue points** etc. 
* Skills: specific abilities to perform some actions, 
  as *hacking*, *lock picking*, *running*, *climbing* etc. They are divided into
  three categories, depending on the difficulty of learning and improving them: 
  *easy*, *normal* and *hard*.
* Advantages/disadvantages: Statistics affecting other skills, as example an expert 
  modifier which increase the chance of winning checks against a specific skill. 
* Perks/drags: distinctive traits setting the character apart from the 
  background people in the setting. Could be things a “famous” or “criminal”. 
  They have an impact in the adventure at large, and might also affect indirectly 
  some checks, providing bonuses and penalties at discretion of the game master.

Attributes and skills are normally expressed as a value between 3 and 18, 
which is the range of value that can be expressed by summing the 
result of a 3d6 dice throw. A value of 3 represents the minimum skill 
level, or characteristic, that a character could have to be still 
considered minimally  functional in the game world — a value below 3 
would indicate a sub-normal characteristic. A value of 18 would represent 
the apex for the game environment, and the values between 10 and 12 would be 
the most common across the reference population.

The scaling is relative to the game setting. For example, if playing 
a campaign where the characters are Greek or Norse gods, a value of 3 on any 
statistic would probably express a level of proficiency far superior to that of
any human.

Notice that the scaling is not linear: it follows the probability distribution
of the 3d6 dice throw. For example, a character with strength 12 is just marginally 
stronger than one with strength 11, but one with strength 18 is in a totally 
different league than one with strength 17. Similarly, characters with health 
10 and 11 have a very similar constitution, but one with health 3 will 
be much more gracile than one with health 4.

Different settings might introduce different ranges with other scaling rules; 
for example in a vampire society, the Body attribute (**B**) could be measured 
in a 0-100 range, where a B0 for a vampire would be equivalent to a B18 for a human,
and where the difference between B0 and B1 and between B49 and B50 is the same.

## Status Statistics {#BaM-m-status-statistics}

*Status statistics* are a set of values that determines the current status of the
character. The base system defines the following:

* *Injury points* (**IP**): amount of damage currently sustained by a character. Damage
has different effects on different type of charactrs, so **IP** might mean different things
to different type of characters.
* *Fatigue points* (**FgP**): current amount of physical tiredness.
* *Stress points* (**StP**): current amount of mental tiredness.

Other subsystem in this manyual introduce more status statistics; for example different
kind of *magic* systems have *mana points*. 

## Structural Statistics {#BaM-m-structs}

*Structural Statistics*, or more simply **structs**, are special statistics
descrbing the overall structure of the character.

They are defined in the base system as:

* *Injury Reistance* (**IR**): number of *injury points* a character can take 
before becoming *incapacitated*. A normal human has **IR** 9,
which can be slightly increased through advantages.
* *Fatigue Resistance* (**FgR**): number of *fatigue points* a character can take 
before becoming *incapacitated*. A normal human has **FgR** 9,
which can be slightly increased through advantages.
* *Stress Resistance* (**StR**): number of *stress points* a character can take 
before becoming *incapacitated*. A normal human has **FgR** 9,
which can be slightly increased through advantages.

## Base and Specific Values {#BaM-m-base}

Statistcs are organized in a hierarchy, where a lower level statistics (as i.e. a skill)
may depend on a higher level one (i.e. an attribute).

The "parent" statistic provides a "default" value for all its children, called **base**. Other
than the base, each statistic has a **specific value**, which represent a specific training
or ability that the character has acquired on a particular attribute or skill, which makes
it better than what another character with the same **base** would have. 

The actual value of any statistic is the sum of the **base** and the **specific value**. 
 
For example, the skill [hiding](#BaM-s-hiding) is based on the attribute *intelligence*. 
This means that any any character has the ability to hide, and the value of the skill
is the same as its *intelligence*, and if its intelligence increases, so does its hiding ability. 
However, a character may learn some simple tricks to improve its ability to hide without having to 
increase its overall intelligence, which is certainly more difficult.

To reflect this fact, the character sheet, all the information about a character are recorded,
has a place to store the **specific value** besides the actual value of the statistic. In this way,
when a base changes, it's easy to recompute the actual value of each statistic.

In the above example, suppose that a character has learned how to hide better, acquiring 3 points of
**specific value** in [hiding](#BaM-s-hiding); its intelligence is 13, and that gives a total of 16.
Suppose that the character improves its intelligence, which becomes 14. The player will go through the
list of skills for which she has acquired any **specific value**, and that are based on *intelligence*;
knowing that the **specific value** of [hiding](#BaM-s-hiding) is 3, she will update the total value 
from 16 to 17.

### Baseless statistics {#BaM-m-baseless-statistic}

Not every statistics has a base. Some skills can't be "improvised" naturally, and must be learned
specifically. For example, everyone can swing a sword, but learning a style of swordsmanship is 
a completely different matter. 

Statistics without a base can be used only with a specific training: to use them, the character must
have at least one point of **specific value** for them.

### Difficulty and Bases {#BaM-m-difficulty-and-bases}

While some statistics are baseless, not all those have a certain parent have the same base. Some skills
are more difficult than others, and the value of the parent attribute can only provide a minimal basic
proficiency.

Normally, *easy* skills receive the full value of their base, *normal* skills only half of it (rounded down), 
and *hard* skills get a third of their base (again, rounded down); 
special bases could be assigned in particular cases, when the rules specify it.

