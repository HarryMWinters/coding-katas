# Taum and Bday

URL - https://www.hackerrank.com/challenges/taum-and-bday/problem

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy black gifts and white gifts.

The cost of each black gift is **bc** units.
The cost of every white gift is **wc** units.
The cost of converting each black gift into white gift or vice versa is units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

For example, if Taum wants to buy **b = 3** black gifts and **w = 5** white gifts at a cost **bc = 3, wc = 4** of and conversion cost **z = 1**, we see that he can buy a black gift for **3** and convert it to a white gift for **1**, making the total cost of each white gift **4**. That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. Either way, the overall cost is `3*3+5*4 = 29`.

## Function Description

Complete the function taumBday in the editor below. It should return the minimal cost of obtaining the desired gifts.

taumBday has the following parameter(s):

- b: the number of black gifts
- w: the number of white gifts
- bc: the cost of a black gift
- wc: the cost of a white gift
- z: the cost to convert one color gift to the other color

## Output Format

A non negative integer.
