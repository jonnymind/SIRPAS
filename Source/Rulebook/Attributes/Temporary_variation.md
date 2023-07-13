### Temporary attribute variations

Normally, the value of dependent attributes is computed only when the base attribute changes
definitively, through a means that improves (or reduces it) permanently. In practice,
this happens every few hours of uninterrupted game.

However, it's possible that an attribute is temporarily altered by various means;
for example by magic, drugs or boosts to cyber implants.

If the attribute is a base for many others, it may be difficult to keep track of the
temporary changes to its dependents. To avoid excessive burden to the game play,
temporary attribute variations are applied to its dependents only if the attribute
is their **direct base**.

Every other case, that is, every case in which a dependent has a complex formula
to determine its base value, is considered as if the value of its base (or bases)
cannot be immediately applied.

For example, an arm wrestler can feel a temporary boost or loss of
strength right away. This will be expressed as the attribute **arm wrestling** 
having the direct base value of *strength*, expressed as "(**S**)".
Conversely, if **lore** has a base value expressed as
"(m**I**)" where **I** stands for **intelligence**, and m**I** is the 
**intelligence** modifier, this means that it takes some effort to learn lores
even for a very intelligent character, and as such, a temporary improvement
of **intelligence** won't be transferred to **lore**.
