
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

