$(--
	SIRPAS - Simple Role Play Adventure System
	Full-lenght base rule manual.

	(C) Giancarlo Niccolai 2018.
	LICENSE: CC-BY-ATTR Share-alike
--)

$(include Introduction)
$(include Basics)



$(-- Section: CHECKS --)

$(include Checks.md)
$(include Checks/Simple_check.md)
$(include Checks/Repeated_attempts.md)
$(include Checks/Ranking_rolls.md)
$(include Checks/Direct_contest.md)
$(include Checks/multi_contest.md)
$(include Checks/Critical_Results.md)


$(-- Section: Injury  --)
$(include Damage_and_injury.md)
$(include Damage_and_injury/Localized_Wounds.md)
$(include Damage_and_injury/Damage_Type.md)
$(include Damage_and_injury/Damage_Type/*.md)
$(include Damage_and_injury/Conditions.md)


$(-- Section: STATISTICS  --)
$(include Skills.md)
$(include Skills/*.md)
$(include Advantages.md)
$(include Advantages/*.md)
$(include Disadvantages.md)
$(include Disadvantages/*.md)
$(include Perks_and_Drags.md)
$(include Perks_and_Drags/*.md)

$(-- Section: COMBAT  --)

$(include Combat.md)
$(include Combat/Simplified_Combat.md)
$(include Combat/Basic_Combat.md)
$(include Combat/Advanced_Combat.md)

$(include Combat/Combat_Styles.md)
$(include Combat/Combat_Styles/Generic_Combat_Skills.md)
$(include Combat/Combat_Styles/Generic_Combat_Skills/*.md)
$(include Combat/Combat_Styles/Archery.md)
$(include Combat/Combat_Styles/Archery/*.md)
$(include Combat/Combat_Styles/Brawl.md)
$(include Combat/Combat_Styles/Brawl/*.md)
$(include Combat/Combat_Styles/Concentration.md)
$(include Combat/Combat_Styles/Concentration/*.md)
$(include Combat/Combat_Styles/Firearms.md)
$(include Combat/Combat_Styles/Firearms/*.md)
$(include Combat/Combat_Styles/Full_Contact.md)
$(include Combat/Combat_Styles/Full_Contact/*.md)
$(include Combat/Combat_Styles/Knife_Fight.md)
$(include Combat/Combat_Styles/Knife_Fight/*.md)
$(include Combat/Combat_Styles/Swordfight.md)
$(include Combat/Combat_Styles/Swordfight/*.md)

$(-- Section: EQUIPMENT  --)

$(include Equipment.md)
$(include Equipment/Adventuring_Equipment.md)
$(include Equipment/Armours.md)
$(include Equipment/Weapons.md)

$(-- Section: TECHNICAL  --)

$(include Technical.md)
