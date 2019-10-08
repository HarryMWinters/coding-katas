# Luck Balance

URL - https://www.hackerrank.com/challenges/luck-balance/problem

Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, **L\[i\]** and **T\[i\]**:

- **L\[i\]** is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by **L\[i\]**; if she loses it, her luck balance will increase by **L\[i\]**.

- **T\[i\]** denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

If Lena loses no more than important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.

## Function Description

Complete the luckBalance function in the editor below. It should return an integer that represents the maximum luck balance achievable.

luckBalance has the following parameter(s):

- k: the number of important contests Lena can lose
- contests: a 2D array of integers where each contains two integers that represent the luck balance and importance of the contest.
