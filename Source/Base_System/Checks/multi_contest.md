## Multi-contests {#BaM-m-multi-contest}

A multi-contest (**mCNT**) is a contest between two or more parties,
each comprising one or more characters. 

In a multi-contest, each party performs a *ranking* on the 
selected skill. Then, the best *check scores* from each party
are compared against each other, and a point is assinged to the
party having the highest *check score* of all. The contest continues
comparing the second-best scores, the third-best scores and so on,
until all the parties have a score to oppose to the others. Draws
are discarded.

The party having scored the higest number of points is the winner;
more than one party has totalized the same number of points, a multi-draw
happens; depending on the context (and on the rules), draw might either
lead to a new situation, or require the whole multi-contest to be repeated.

As there could be negative consequences for the losing parties, each
losing participant will receive a negative *success margin*.

 Notice that a multi-contest between two parties comprising just one 
 character each is almost the same as a *direct contest*, with the 
 difference that, instead of assigning a positive *SM* to the winner, 
 a negative *SM* is assigned to the loser.

**Example**: Three paties, composed of 3, 4 and 5 members respectively,
try to run up a hill before the others. They perform a *multi-contest*
on [running](#BaM-s-running). The rankings in each party result in:
* Party A: 29-23-20
* Party B: 26-25-22-19
* Party C: 28-22-21-18-16

The points are assigned as follows:
* A = 29, B = 26, C = 28 - Point for A
* A = 23, B = 25, C = 22 - Point for B
* A = 20, B = 22, C = 21 - Point for B

Group A has 1 point while group B has 2: group B wins the multi-contest.
However, the first qualified members of group B and C will have a *SM* of
-3 and -1 respectrively, while for what concerns the second qualified,
it's the member of the group A that will have a negative *SM* (-2); also
the second qualified of group C will have a *SM* of -3.

The remaning one member in B and two members in C are not participating in
the *multi-contest*; nevertheless, the most numerous group has an advantage
in having more chances to score high points than the others -- everything else equal.

The effect of the multi-contest in the adventure should reflect its outcome. In this
example, the two highest scores in the ranking might have fumbled on the hill, or grabbed each
other in a brawl, while the two winners of the winning party would have reached the top,
nearly followed by the losers, and at a distance, by the ones excluded from the contest.

## Ranking generation for the **GM** {#BaM-m-ranking-gm}

In a multi-contest, each player rolls its own dice, and performs its own computation, communicating
the final resul to the **GM**; the players may even arrive to order their scores before
doing that, helping out the GM in its task.

However, the GM is alone in rolling the dice for the character it controls; repeating several 3d6 rolls
and adding various modifiers that can change during an action (i.e. because a GM controlled character
gets wound), can be tiresome, and can slow down the pace of the game for the players as well.

To prepare the multi-comparison, the GM should:
1. Write the character he controls on a column of a notepad.
1. Besides each name, it writes the modifiers for that characcters, to be updated 
   if the contest is repeated.
1. Unless each GM controlled character is special, the GM always assigns the best outcome 
   to the topmost character, so that it can read the ranking results going top to bottom. 

If the GM doesn't have a dice-throwing application handy, which can automate part of the process, it
can use the following procedure to generte the scores at once, when it controls more than 3 characters:
1. Roll 2d6 and write down the result.
1. Roll Nd6, where N is the count of character controlled by the *GM*.
1. It is easy now to write the highest rolls on top, and write the others down in order.
1. If more than one 6 is rolled, count them as 7, 8 etc.
1. If more than one 1 is rolled, count them as 0, -1 etc.


For example, the GM controls 5 characters.
1. It rolls 2d6 for a total of 7.
1. It now rolls 5d7; the results are 6, 6, 4, 1, 1.
1. The topmost character on the GM notepad get 7+7 = 14.
1. The others get 7+6 = 13, 7+4 = 11, 7+1 = 8 and 7+0 = 7.
1. Now the GM gets the result from the players, and communitcates
   their respective **SM** to each of them.


