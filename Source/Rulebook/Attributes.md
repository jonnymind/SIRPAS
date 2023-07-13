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

Higher level attributes form the **base** of the lower level ones, which are said
to be their **dependent** attributes. Every dependent attribute has a **base value**,
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
so that its **S**=11, its **AW** grows too, as now **AW**= **S**+1 = 12.

The number of character point to be spent in each attribute or skill to train it depends on how
many other attributed are based on that, and on the objective complexity of improving it.

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

$(include /tables/modifiers.md)

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
The system has **affinity** attributes for *earth*, *air*, *water* and *fire*, which
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
base attribute). Rounding is always in defect.
* Average Base: (avg **A**, **B**,...). The **base value** is the average of the listed
values.
* Choice Base: (**A** or **B**). The **base value** is the best between the options listed.

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
