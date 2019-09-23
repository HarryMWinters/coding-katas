# Largest Permutation

URL - https://www.hackerrank.com/challenges/largest-permutation/problem

You are given an unordered array of unique integers incrementing from **1**. You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

For example, if **arr = [1,2,3,4]** and the maximum swaps **k = 1**, the following arrays can be formed by swapping the **1** with the other elements:

```
[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
```

The highest value of the four (including the original) is `[4, 2, 3, 1]`. If , we can swap to the highest possible value:

## Function Description

Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):

- k: an integer that represents the limit of swaps
- arr: an array of integers

## Output Format

Print the lexicographically largest permutation you can make with at most **k** swaps.
