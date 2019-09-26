# Ctci Ice Cream Parlor

URL - https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of **money** and the **cost** of each flavor for **t** trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a **cost**. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

For example, `n = 5` there are flavors having `cost = [2,1,3,5,6]`. Together they have `money = 5` to spend. They would purchase flavor ID's **1** and **3** for a cost of `2 + 3 = 5`. Use **1** based indexing for your response.

Note:

- Two ice creams having unique IDs **i** and **j** may have the same cost (i.e., `cost[i] == cost[j]`).
- There will always be a unique soluti

## Function Description

Complete the function whatFlavors in the editor below. It must determine the two flavors they will purchase and print them as two space-separated integers on a line.

whatFlavors has the following parameter(s):

- cost: an array of integers representing price for a flavor
- money: an integer representing the amount of money they have to spend
