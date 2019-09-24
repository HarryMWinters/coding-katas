# Cavity Map

URL - https://www.hackerrank.com/challenges/mark-and-toys

Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if **_prices_ = [1,2,3,4]** and Mark has to spend **_k=7_**, he can buy items **_[1,2,3]_** for **_6_**, or **-[3,4]** for **_7_** units of currency. He would choose the first group of **_3_** items.

## Function Description

Complete the function maximumToys. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

- prices: an array of integers representing toy prices
- k: an integer, Mark's budget

## Constraints

1 <= _n_ <= 10^5
1 <= k <= 10^9
1 <= _prices[i]_ <= 10^9
A toy can't be bought multiple times.

## Output Format

An integer that denotes the maximum number of toys Mark can buy for his son.
