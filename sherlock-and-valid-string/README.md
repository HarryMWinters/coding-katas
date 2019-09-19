# Sherlock and Valid String

URL - https://www.hackerrank.com/challenges/sherlock-and-valid-string

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if **s = abc** , it is a valid string because frequencies are **{a: 1, b: 1, c: 1}**. So is **s = abcc** because we can remove one and have of each character in the remaining string. If however, **s = abccc** the string is not valid as we can only remove occurrence of . That would leave character frequencies of .

## Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

- s: a string

## Constraints

- 1 <= s <= 10^5
- s[i] are ascii[a-z] characters

## Output Format

Return true if valid, else false.
