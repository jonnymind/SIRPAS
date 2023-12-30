## Active Mitigation 

@(dd active_mitigation)
{ 
  "*Name": "Active Mitigation",
  "*Brief": "Reduce incoming damage once per turn",
  "Callsign": "AM",
  "Category": "Skill/combat",
  "Specialization": "combat style",
  "Cascade": "Yes",
  "Cost": "1 TT/Hard"
}

Once per combat turn, the character can mitigate incoming damage
by an amount equal (or less) than the **Success Margin** on a **Simple Check** on
this skill.

For example, a warrior has **AM/Swordfight** 6, and the advantage **Expert/AM/Swordfight** 
It receives damage for 5 **DP** after passive mitigation.

The Success Level for this simple check is 16 (being an Expert rolling **AM** a 16 after various
modifier, the check results 6+16 = 22, which has **SM** 22 - 21 = 1.

In the end, the fighter receives 5-1 = 4 **DP**.

This is a [cascade skill]($RulebookAddress#cascade-attributes); this means
it's possible to acquire this attribute multiple times to perform multiple
active mitigations per turn.
