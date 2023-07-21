## Unlucky

@(dd Unlucky)
{ 
  "*Name": "Unlucky",
  "*Brief": "Has a chance to worsen every check",
  "Category": "Disadvantage",
  "Cost": "2 TT/Main"
}

The character performs every check (except direct **resistance checks**) 
rolling an additional, separate six-face dice (suggest using a 
differently colored one, if possible).

If the separate roll scores 1, the *worst* roll of the other die in the check
(*after* applying other advantages) is substituted with 1.

For example: a character with **expert**/*lockpicking* attempts opening a lock.
As they have the advantage [expert](#expert) on lock-picking, they will roll 4d6 
and select the best 3 rolls. However,
they also must roll for **unlucky**. Suppose the roll for the check gives
2, 3, 3 and 4, and the **expert** advantage allows to discard the lower roll (2),
resulting in 3, 3 and 4. However, the unlucky dice rolls 1: 
the lowest roll after applying **expert** (3) must be discarded
and changed into 1, so the check result will now be 1 + 3 + 4 = 8 instead of
3 + 3 + 4 = 10.

Of course, nothing happens when the separate dice rolls 1 but one of the
normal dice rolls is 1 already.

This penalty is **not** applied on any **resistance check**. Also, any
temporary effect improving the natural rolls will temporarily disable
this disadvantage as a side-effect.
