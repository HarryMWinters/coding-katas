# 2D Array

URL - https://www.hackerrank.com/challenges/2d-array/problem

Given a **6 x 6** 2D Array, _arr_:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

We define an hourglass **A** in to be a subset of values with indices falling in this pattern in _arr_'s graphical representation:

```
a b c
  d
e f g
```

### Function Description

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

- arr: an array of integers

### Input Format

Each of the **6** lines of inputs _arr_**[i]** contains **6** space-separated integers _arr_**[i][j]**.

### Constraints

- -9 <= _arr_**[i][j]** <= 9
- 0 <= i,j <= 5

### Output Format

Print the largest (maximum) hourglass sum found in _arr_.
