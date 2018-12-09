## Standard Injury Rule

The Standard Injury Rule describes the most common way in which Damage Points,
Resistance Level, Wounds, Disable Level and Injury Points interacts.

* Damage Points from a certain source are summed up until they get larger than
  the Resistance Level for the source. The excess of Damage Points is noted down,
  and the value is reset to 0.
* The character receives a Wound, which severity is determined by the noted
  excess of Damage Points.
* If the number of Wounds equals or exceeds the Disable Level, the character is
  disabled. 
* The severity of the disable status is determined by the sum of *Injury Points*.

The standard rule covers most cases, but there are settings, situations and
characters that rely on different rules around Injury Statistics.

For example, a zombie cannot become disabled, and is immune to light wounds; a
vampire will flee, if possible, (transforming into myst or in a bat) after
having sustained too much damage; a ghost doesn’t sustain negative effect for
incapacitating damage; an advanced AI not is disabled when it receives a certain
number of wounds, but when the total injury points is larger than a threshold,
etc.


