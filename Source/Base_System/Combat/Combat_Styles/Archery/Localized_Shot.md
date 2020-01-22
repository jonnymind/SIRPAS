### Localized Shot {#BaM-s-localized-shot}


$(dd cm_archery_localized_shot)
{ "Type": "Attack",
	"Modifier": "Variable",
	"Prereq": "Archery 5",
	"DR": "-1",
	"Damage": "__SM__+1",
	"Condition": "(__Cripple__)"
}

Loads and shoot an arrow or a bolt aiming to a specific part of the body.

A _critical success_ will cause automatically
a _localized heavy wound_, crippling that part of the body,
if the damage caused would be otherwise enough to cause at least
a _light wound_.

> Localized heavy wounds can have further negative effects with respect to
normal heavy wounds, as disarming, reducing the movement speed, blinding
and so on.

If the localized shot was aimed at the head, a _critical success_ will cause
a _deadly wound_.

The modifier to be applied depends on the target part of the body:

| Body Part | Modifier |
|:---------:|---------:|
| Arm       | -2       |
| Leg       | -3       |
| Head      | -4       |
