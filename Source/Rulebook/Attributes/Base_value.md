
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
