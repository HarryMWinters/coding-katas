# Ctci Comparator Sorting

URL - https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

**Name:** a string.
**score:** an integer.

Given an array of **n** Player objects, write a comparator that sorts them in order of decreasing score. If **2** or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns `-1` if `a < b`, `0` if `a == b`, and `1` if `a > b`.

## Function Description

Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

## Constraints

- foo <= bar
- erc.

## Output Format

A lorem ispum dolor data struct.
