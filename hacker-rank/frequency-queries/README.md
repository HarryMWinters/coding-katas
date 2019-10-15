# Frequency Queries

URL - https://www.hackerrank.com/challenges/frequency-queries/problem

You are given **q** queries. Each query is of the form two integers described below:

- 1:x Insert x in your data structure.
- 2:y Delete one occurrence of y from your data structure, if present.
- 3:z Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

The queries are given in the form of a 2-D `queries` array of size `q` where `queries[i][0]` contains the operation, and `queries[i][1]` contains the data element. For example, you are given array `queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]`. The results of each operation are:

```
Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
```

Return an array with the output: `[0, 1]`.

## Function Description

Complete the freqQuery. It must return an array of integers where each element is a 1 if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

- queries: a 2-d array of integers
