### Localized Shot

$(dd cm_firearm_localized_shot)
{ "Type": "Attack",
	"Modifier": "Variable",
	"Prereq": "Firearms 4",
	"DR": "-1",
	"Damage": "__SM__+12",
	"Condition": "__(Cripple)__"
}

Shoot aiming a part of the body. A critical success will cripple that
part of the body, inflicting a permanent negative modifier until healed,
and if the localised shot was aimed at the head, it will cause a deadly
wound.

The modifier to be applied depends on the target part of the body:

| Body Part  | Modifier |
|:----------:|---------:|
| Arm        | -2       |
| Leg        | -3       |
| Head       | -4       |
