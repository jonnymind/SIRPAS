# Checks {#BaM-gen-checks}

*Checks* are the nuts and bolts of SIRPAS. Practically every action that 
might succeed or fail requires performing a successful check on a specific
skill, or more rarely, on an attribute.

A *check* consists in throwing a certain amount of dices (normally 3), 
and summing all their values to the value of the checked skill or attribute, 
eventually summing and subtracting various *modifiers* and verify if the 
result is equal or above a certain score, called *success level* (**SL**), or a 
certain roll performed by an opponent.

The total score obtained by summing the dice values, the checked skills and all
the modifiers to be applied is called *check score* (**CS**). The difference between the
*check score* and the value to beat (either a *success level* or a *check score* obtained
by an opponent) is called *success margin* (**SM**), and can be negative in case of
failures.

## Difficulty Modifiers {#BaM-m-difficulty-modifiers}

The following modifiers can be added to the **CS** when actions require extraordinary effort.

$(include /tables/difficulty.md)

This reference values are referenced by the skills description; many of them describe when actions
are to be considered *easy*, *hard* and so on. When the skill description doesn't specify it,
the Game Master can assign a difficulty modifier depending on the situation.

Instead of the generic difficulty level, some skills can assign determined modifiers;
for example, jumping from a height requires a check on [acrobatics](#BaM-s-acrobatis) with a
modifier that depends on how high is the jump.


