## Attributes {#RB-attributes}

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

$(include /tables/modifiers.md)

Suppose a skill has base declared as **mD**. This means the base of that skill is not **Dexterity**
directly, but the modifier derived from the above table.

### Attribute descriptions

Attribute are described with:
* Their short name (usually an acronym) always in **bold**.
* Their *base* formula, if any
* Their difficulty.

### Training attributes {#RB-training}

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
