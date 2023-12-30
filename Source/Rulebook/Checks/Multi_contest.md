## Multi-contests

A multi-contest (**mCNT**) is a contest between two or more parties,
each comprising one or more characters. 

In a multi-contest, each party performs a *ranking* on the 
selected skill. Then, the best *check results* from each party
are compared against each other, and a point is assigned to the
party having the highest *check result* among the top scores
in each of them. 

The contest continues
comparing the second-best results, the third-best results and so on,
until all the parties have a score to oppose to the others. Draws
are discarded.

The party having scored the highest number of points is the winner. If
more than one party has totalized the same number of points, a multi-draw
happens; depending on the context (and on the rules), the multi-draw might either
lead to a new situation, or require the whole multi-contest to be repeated.

The characters that have scored points for the winning parties are called
**scorers**; those who have lost their roll (regardless of their party 
having won or not) are called **succumbers**. The ones who couldn't be
matched with a ranking from the other parties are **excluded**.

As there could be negative consequences for the losing parties, each
losing participant will receive the difference between their score
and the winner of their rank as a negative *success margin*, 

Notice that a multi-contest between two parties comprising just one 
character each is almost the same as a *direct contest*, with the 
difference that, instead of assigning a positive *SM* to the winner, 
a negative *SM* is assigned to the loser.

**Example**: Three parties, composed of 3, 4 and 5 members respectively,
try running up a hill before the others. They perform a *multi-contest*
on a skill or attribute used for running. The rankings in each party result in:

* Party A: 29-23-20
* Party B: 26-25-22-19
* Party C: 28-22-21-18-16

The points are assigned as follows:

* A = 29, B = 26, C = 28 - Point for A, **SM** of B = -3, **SM** of C = -1  
* A = 23, B = 25, C = 22 - Point for B, **SM** of A = -2, **SM** of C = -3
* A = 20, B = 22, C = 21 - Point for B, **SM** of A = -2, **SM** of C = -1

Group A has 1 point, while group B has 2: group B wins the multi-contest.

The the fourth ranked in B, and the fourth and fifth in C are **excluded** 
and will not contribute to winning.

Nevertheless, the most numerous group has an advantage in having more chances
to score high points than the others -- everything else equal.

The effect of the multi-contest in the adventure should reflect its outcome. In this
example, as team A had the highest score but ended up losing the race, the two 
characters with the highest scores in parties A and B might have fumbled on the hill, 
or grabbed each other in a brawl, while the two characters having scored points for the 
winning party would have reached the top, nearly followed by the losers, 
and at a distance, by the ones excluded from the contest.

## Ranking generation for the **GM**

In a multi-contest, each player rolls its own dice, and performs its own computation, communicating
the final result to the **GM**; the players may even sort their scores before
doing that, helping out the GM in its task.

However, the GM is alone in rolling the dice for the characters they control; repeating several 3d6 rolls
and adding various modifiers that can change during an action (i.e. because a GM controlled character
gets wounded) can be tiresome, and can slow down the pace of the game for the players as well.

To prepare the multi-contest, the GM should:
1. Write the characters he controls on a column of a notepad.
1. Besides each name, write the modifiers for that characters, to be updated 
   if the contest is repeated.
1. Unless each GM controlled character is special, the GM always assigns the best outcome 
   to the topmost character, so that it can read the ranking results go top to bottom. 

If the GM doesn't have a dice-throwing application handy, which can automate part of the process, it
can use the following procedure to generate multiple scores at once:
1. Roll 2d6 and write down the result.
2. Roll Nd6, where N is the count of character controlled by the *GM*.
3. If more than one 6 is rolled, count them as 7, 8 etc.
4. If more than one 1 is rolled, count them as 0, -1 etc.
5. Add each single rolled result to the previous 2d6 roll.

For example, the GM controls 5 characters.
1. It rolls 2d6 for a total of 7.
1. It now rolls 5d6, one per character; the results are 6, 6, 4, 1, 1.
1. The characters gets the following points, top to bottom: 7+7 = 14, 7+6 = 13, 7+4 = 11, 7+1 = 8 and 7+0 = 7.
1. Now the GM gets the result from the players, and communicates the winning party, 
   the scoring characters and, if relevant, the negative **SM** of the **succumber** characters.

