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

## Effective Damage and Wounds

When sustaining a certain amount of damage, the character
receive a certain kind of wound, according with the following table:

$(include tables/wounds_severity.md)

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
