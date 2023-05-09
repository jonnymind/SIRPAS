# Attributes {#BaM-m-attributes}

Attributes describe a character as syntetically as possible. 
They are the most important statistics, on which
many other ones depend directly or indirectly. 

Attributes are organized in hierarchies, with top-level attributes called **mains**.

The base systems defines the following attributes:
* Body (**B**): The phyisical aspect of the character. Body attributes are:
   * Strength (**S**): raw phisical power;
   * Dexterity (**D**): speed, precision and control over actions performed with the body;
   * Health (**H**): Resilience against fatigue, injury and illness.
* Mind (**M**): describes the mental prowess of a character. Mind attributes are:
  * Will (**W**): strength of conviction and assertiveness.
  * Intelligence (**I**): ability to understand and solve complex problems; mental flexibility.
  * Equilibrium (**E**): resilience to mental strain, stress and madness.

Higher level attributes form the **base** of lower level ones. This meanst that the lower
attributes are computed _by difference_ with respect to their base. They start off as having
the same value, and extra point can be bought (or sold) at a "discount price", in order
to increase them specifically.

For example, initially, a character with M12 has also W12, I12 and E12. If the player
buys one point of **will**, it will be now W13. If later on the player decides to 
buy a point of **mind**, the attribute values will now M13, I13 and E13, 
but having bought a point of **will** already, that will now be W14. Of course, the cost
of buying points for higher level attributes is proportionally larger. 

A simple game session might be run by determinging nothing but the **mains**. 
If more time is spent in creating the characters, or as the game progresses, the lower
level statistics can be finetuned and differentiated with respect to their parent
attributes in the hyerarchy.

## Body {#BaM-c-body}

The Body (**B**) is a value that describes your overall physical prowess in terms of
bodily strength, resilience to prolonged efforts, recovery speed, resistance to
illness and so on. For humans, it is measured in the range between 3 and 18 (the
possible outcomes of 3d6). Most adult characters score in the range between 10
and 12, with 18 representing a person with the best possible body (rarely if
ever ill, strong as the strongest wrestler or weight lifter, moving as swift as
a record runner and able to run as long as a marathon champion — all at the same
time), and 3 representing the weakest possible fully formed and barely
functional body.

### Strength {#BaM-c-strength}

Strength (*S*) is the attribute measuring a character physical strength. 
In the default setting, it also indicates how much weight the character 
can transport without being fatigued, or the amount of weight it can 
carry without being slowed down, or that it can lift. There are different
tiers  used in various occasion, all multiple of the value of Strength in 
pounds:

$(include /tables/strength.md)

The name of the tiers match the names of the skill difficulty levels, 
as they are directly applied as a difficulty level in various checks.
However, they also define other effects that are not directly related with skills; 
for example, the transport weight tier is applied directly to the combat movement: 
a character transporting  a “very hard” weight has its movement cut to one third 
of it normal movement

### Dexterity {#BaM-c-dexterity}

Dexterity (**D**) expresses the ability to control one’s own body.
Eye-hand coordination, agility, reaction times and rapidity are all 
components of dexterity. A dexterity of 3 indicates sluggish reaction times, 
18 indicates a martial-art or olympic gymnast level of dexterity, 
with the vast majority of common people stacking around 10-12.

The *dexterity* indicates also the base movement speed of a character.
The actual speed depends on what a character actually is; a cyborg with
*D*12 will probably be faster than any human with *D*18. 

The following table is for humans; you can adapt it to other races
by using the *speed coefficient* of that race (for humans, it's 1).

$(include /tables/dexterity.md)

Notice that the speed for combat turn is not necessarily the sprint speed,
as movement during combat is limited by other factors. Also, the combat
turn here is the standard 10 seconds combat turn of the the base system;
other systems might redefine the duration of a combat turn (and how *dexterity*
works in those contexts).

### Health {#BaM-c-health}

Health (**H**) represents the resistance to fatigue, illness and polluted 
environment (including allergenic agents). It's used to determine how many
*fatigue points* are generated in sitautions where the body is under strain,
and gives the base for all resistance skills 
(i.e. [poison resistance](#BaM-s-poison-resistance)).


## Mind {#BaM-c-mind}

The Mind (**M**) is the overall score of mental abilities in terms of intelligence,dcreativity, 
will power, mental sanity, depth of knowledge and so on. 
A mind level 3 represents a character that is barely functional as an autonomous person (or
creature) in the reference setting, while a 18 represents a character maximally intelligent, 
penetrating, knowledgable, sane and wise. The vast majority of characters (or heroes)
in the reference setting will have a mind between 10 and 12.

### Will {#BaM-c-will}

Will (**W**) is the power of the mind to focus on a certain task, 
perform prolonged mental activity, keep determination in 
adverse situations and so on. It can be roughly thought as the 
equivalent of the strength (*S*) in the mind realm.


### Intelligence {#BaM-c-intelligence}

Intelligence (**I**) is the ability to understand and solve complex problems, 
comprehend difficult study subjects, see through schemes and machinations 
etc. As it measure the flexibility of the mind processes, it can be thought 
as the dexterity (**D**) of the mind.

### Equilibrium {#BaM-c-equilibrium}

Equilibrium (**E**) is the stability of the mind, 
or basically the equivalent of its health (**H**). It determines how much
mental stress a character can sustain before receiving a *stress point*.
 
It indicates how much mental strain a person can take before being debilitated; 
of course, it is also important in those settings where attacks are delivered 
to the mind instead of the body: fantasy, sci-fi and horror settings 
can present as many dangers for the mind as for the body, or more.

