### Localized Shot


$(dd cm_archery_localized_shot)
{ "Type": "Attack",
	"Modifier": "Variable",
	"Prereq": "Archery 5",
	"DR": "-1",
	"Damage": "__SM__+*D*+6",
	"Condition": "(__Cripple__)"
}

Loads and shoot an arrow or a bolt aiming to a specific part of the body.
A critical success will cripple that part of the body, inflicting a 
permanent negative modifier until healed, and if the localised shot
was aimed at the head, it will cause a deadly wound.

The modifier to be applied depends on the target part of the body:

| Body Part | Modifier |
|:---------:|---------:|
| Arm       | -2       |
| Leg       | -3       |
| Head      | -4       |
