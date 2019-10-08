# Count Triplets

URL - https://www.hackerrank.com/challenges/count-triplets/problem

You are given an array and you need to find number of tripets of indices `(i, j, k)` such that the elements at those indices are in geometric progression for a given common ratio **r** and `i < j < k`.

For example, `arr =[1, 4, 16, 64]`. If `r = 4`, we have `[1, 4, 16]` and `[4, 16 ,64]` at indices `(1, 2, 3)` and `(0, 1, 2)`.

## Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given `r` as an integer.

countTriplets has the following parameter(s):

- arr: an array of integers
- r: an integer, the common ratio
