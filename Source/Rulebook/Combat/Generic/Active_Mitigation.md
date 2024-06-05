### Active Mitigation 

@(dd active_mitigation)
{ 
  "*Name": "Active Mitigation",
  "*Brief": "Reduce incoming damage once per turn",
  "Callsign": "AM",
  "Category": "Skill/combat",
  "Specialization": "combat style",
  "Cascade": "Yes",
  "EC": "Shields (opt)",
  "Cost": "1 TT/Hard"
}


Once per combat turn, the character can mitigate incoming damage
by an amount equal (or less) than the **Success Margin** on a **Simple Check** on
this skill. 

This skill can be used also in simplified combat, after the full amount of damage
received by a character is computed.

For example, a warrior has **AM/Swordfight** 6, and the advantage **Expertise/AM/Swordfight** 
It receives damage for 5 **DP** after passive mitigation. Rolling on this skill
4 die (as an expert for **AM** in **Swordfight** style) it obtains 6, 5, 5, 1, for a total
of 6 + 5 + 5 for the roll and 6 for the skill level; the total is 22, so the **SM** is 
22 - 21 = 1.

In the end, the fighter receives 5-1 = 4 **DP**.

**Optional**: Dedicated equipment can change the difficulty of the check. Wearing a shield
or a defensive equivalent for the selected style will make the check *easy*.
In ranged styles, cover will be considered adequate shielding. More advanced technology or
magic may make the check *very easy*.

This is a [cascade skill]($RulebookAddress#cascade-skills); this means
it's possible to acquire this attribute multiple times to perform multiple
active mitigations per turn.
