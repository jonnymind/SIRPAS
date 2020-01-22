# APPENDIX: Theorycrafting Elements {#BaM-apx-theorycrafting-elements}


In this appendix, you can find some technical elements about the numbers
behind the SIRPAS system.

This is also a place where we store our theory, and check our design
explicitly, to see how it works when the dice start rolling.

## Chance Table {#BaM-apx-chanche-table}


This table gives you the probability to roll a certain number or to beat
a certain value with the sum of 3d6.

The "chance to match" column shows you how likely is to roll exactly the
value on the left column. The "Chance to Beat" is the probability to roll a
number _greater_ than the one on the left. To get the probability to roll
_at least_ the number on the left, add both columns.

$(include tables/chance_table.md)

## Conflict Table {#BaM-apx-conflict-table}


This table shows how likely is to win, lose or achieve a draw on a contest
roll, given a certain difference in the base.

Suppose the base is the same for both characters; the difference of the bases
is zero. The probability to win or lose is the same, 45%, and there is a
10% probability to roll a draw.

If a character rolls on a base 10, and the other has a base 13, the difference
is 3. The character with the base 10, reads its chances on the -3 row, and the
other uses the row number 3. In this case the advantage character has 70%
chance to win, 22% to lose and 8% to achieve a draw; the position of the
other character is reversed.

$(include tables/contest_table.md)

Consider: with a -3 modifier, you have only 1 chance over five to win --
be very cautious fighting characters with higher bases than you.
