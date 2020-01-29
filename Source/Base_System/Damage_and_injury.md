# Damage and Injury {#BaM-m-damage-and-injury}

A critical aspect of any RPG is the set of rules that determine how characters
sustain damage and receive injuries.

SIRPAS has a modular injury system, which can be fitted in any setting and play styles.

It can be used to determine an overall status of a fight, or to determine precisely 
which part of a human body, mechanical robot, flying mount or AI virtual device 
has been damaged, and to what extent it has been incapacitated. 

It can be employed to keep the score of harmless intellectual challenges, 
as well as devastating psychic attacs on the mental sanity of the characters.

## Damage Points {#BaM-m-damage-points}

The *raw damage* a character receives is measured in *damage points* (**DP**).

Damage can come in the way of characters in various forms, and from various
sources; hence, **DP** have also a *quality*, which depends on which source
is generating them.

Physical harm, fatigue, heat, cold, mental stress etc. can be source. The
base system divides them in three main categories: *physical*, *mental* and
*elemental*. These macro-categories further subdivided
in specific *damage sources*, which are defined further down. 

## Effective Damage {#BaM-m-effective-damage}

Incoming *raw damage* is modified through the application of
*defences*, that reduce it in various ways; they are mainly
divided in the following categories:
* *Passive Defences*: reducing the incoming **DP**s of a flat amount (like physical armors),
  or dividing the damage by a certain factor, i.e. 4/5 or 3/4 (like magic or sci-fi shields),
  or eventually by an hybrid formual (as in the case of specific resistances against some
  kind of damage).
* *Active Defences*: the amount of reduced **DP**s depends on the use of a certain
  character ability. 

The way different kind of damages impact on the characters is fully considerd by the way
defences are applied to reduce the incoming **DP**s.

The count of **DP**s left after the defences are applied is called *effective damage* (**ED**), and
is used to evaluate the effect of the damage on the character.

## Wounds and Injury Points {#BaM-m-wounds}

When sustaining a certain amount of damage, the character
receive a certain kind of wound: a *scratch* or a *light*,
*serious* or *heavy* wound, and possibly even *deadly* ones,
according with the following table:

$(include tables/wounds_severity.md)

The severity of the received wound determines the amount of
*injury points* (**IP**) currently sustained by a certain character;
once the **IP**s are above the maximum a character can sustain (its
*injury resistance*),
it becomes *incapacitated*, and it may eventually die, if the wounds
are not treated.

>For example: A human has normally **IR** 9; this means it can sustan 
1 light wound and 2 heavy wounds, or 4 serious wounds, before becoming
unable to act, and possibly unconscious.

>In many RPGs, a form of *health*, *constitution* or similar statistic determines how
how much damage a character can take. In SIRPAS, **IR** serves this purpose,
and it's mostly fixed; more than stacking a single statistic, characters can 
acquire multiple resistances, skills and advantages to become progressively 
less affected by the same amount of damage.

*Scratches* and *deadly wounds* are treated differently.

### Wounds Penalty {#BaM-m-wounds}

A serious wound causes a penalty of -1, and a heavy wound causes a penalty of
-2, on every action.

For example, if a character receives an heavy and a serious wound, every action
requiring a check will be penalized by 3 points.


## Scratches {#BaM-m-scratches}

A character hit by a damage source and
reducing the **ED** to zero receives a **scratch** (although there are
some situations in which a not even a scratch is received).

Scratches are extremely light wounds that, by themselves, don't impact
the character **IP** pool.

However, once received a certain number of scratches, they are considered
as one light wound. This number (namely a **structural statistic**) is called 
*scratch-to-wound* (**StW**), and it's 3, unless differently specified, for any character.
No matter if we're talking of a dragon, a vampire, a god, an AI or a human,
when they receive their equivalent of 3 scratches, they totalize a light wound, 
unless differently specified.

Practically, the players will note down the received scratches, and when they amount
to their *StW*, they will remove the scratches and assign a light wound to themselves.

## Deadly Wounds (optional) {#BaM-m-deadly-wounds}

When a character receives more than 9 *ED* points, it sustains a wound that is
potentially able to kill them immediately.

To avert an immediate death, the character must pass a _simple check_ on the
[resistance](#BaM-s-resistance-source) skill for the specific damage source.

When character can't use any specific resistance skill, the check is performed
on __body__, if the damage is physical, or __mind__, if it's mental.

If the check is successful, the character receives a _heavy wound_.

> Remember that the _resistance check_ has a negative modifier depeding
on the received wounds, as any other action.

## Direct Wounds {#BaM-m-direct-wounds}

In some situation, a character can receive a wound of a certain kind directly,
and not as a consequence of a damage source dealing damage points. For instance,
certain magic spells could cause a heavy wound directly, if the character fails
an attempt to resist them. A overwhelmingly powerful weapon, for example a starship
laser directed against a human, could have the same effect. Explicit actions 
performed on the character when it is unable to defend itself 
(i.e. forms of physical or mental torture) could deal
an arbitrary wound as the attacker seems fit, etc.


