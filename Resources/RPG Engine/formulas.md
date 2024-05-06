# Formulas and resources for the RPG Engine

The **RPG Engine** is a Virtual Tabletop Software that helps keeping track of statistics, dice rolls
and results during on-site and remote game sessions.

This document contains resources used to build the game experience.



## Modifier formula

This is the formula to compute the modifiers on attributes (A is the source cell, modifying accordingly)

```
with(A, if(it>18,4,if(it>=16,3,if(it>=14,2,if(it>=12,1,if(it<3,-4,if(it<=4,-3,if(it<=6,-2,if(it<=8,-1,0)))))))))
```

