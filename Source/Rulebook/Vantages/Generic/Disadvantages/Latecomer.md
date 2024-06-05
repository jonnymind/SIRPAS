### Latecomer

@(dd latecomer)
{ 
  "*Name": "Latecomer",
  "*Brief": "Reduces all rankings by one place",
  "Category": "Disadvantage",
  "Cost": "2 TT/Secondary",
  "Conflict": "Nimble crowder"
}

Whenever a [ranking]($RulebookAddress#ranking) is performed, the character 
gets one place lower than their scored rank. This is not applied to
[multirankings]($RulebookAddress#multiranking)

If two or more characters with this disadvantage are stacked in consecutive places,
the first character without this disadvantage ranks on top of them.

For example, suppose this is the outcome of an **initiative** ranking to establish
a **combat order**:

| Place | Roll    | Party   | Member |
|------:|---------|---------|--------|
| 1     | 18      |  A      | Warrior|
| 2     | 16      |  A      | Wizard |
| 3     | 12      |  B      | Goblin |
| 4     | 9       |  B      | Gnoll  |

If both the warrior and the wizards have this disadvantage and the goblin hasn't,
the ranking will be modified as:

| Place | Roll    | Party   | Member |
|------:|---------|---------|--------|
| 1     | 12      |  B      | Goblin |
| 2     | 18      |  A      | Warrior|
| 3     | 16      |  A      | Wizard |
| 4     | 9       |  B      | Gnoll  |

This disadvantage conflicts with [nimble crowder](#nimble-crowder), even if that
advantage have a similar effect, that is, being able to reduce the character
position in any ranking at will.
