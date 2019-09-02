# Cavity Map

URL - hackerrank.com/challenges/cavity-map

You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge. Note, two cells are a diagonal are _not_ adjacent.

Find all the cavities on the map and replace their depths with the uppercase character **X**.

For example, given a matrix:

```
989
191
111
```

You should return:

```
989
1X1
111
```

## Function Description

Complete the `cavityMap` function.. It should return an array of strings, each representing a line of the completed map.

cavityMap has the following parameter:

- grid: an array of strings, each representing a row of the grid

## Input Format

The first line contains an integer _n_, the number of rows and columns in the map.

Each of the following _n_ lines (rows) contains _n_ positive digits without spaces (columns) representing depth at _map_[_row,_ _column_].

## Constraints

1 <= _n_ <= 100

## Output Format

Output an list fo len(_n_) with each element a string denoting a line. Each cavity should be replaced with the character **X**.
