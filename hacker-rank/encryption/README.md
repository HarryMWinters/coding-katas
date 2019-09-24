# Encryption

URL - https://www.hackerrank.com/challenges/encryption/problem

An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let **L** be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

`floor(sqrt(L)) <= row <= column <= ceil(sqrt(L))`

That is to say the resulting grid should have at least as many columns as rows.

so if `S = "if man was meant to stay on the ground god would have given us roots"` becomes

```
ifmanwas
meanttos
tayonthe
groundgo
dwouldha
vegivenu
sroots
```

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

## Function Description

Complete the encryption function in the editor below. It should return a single string composed as described.
encryption has the following parameter(s):

- s: a string to encrypt

## Constraints

- **s** is comprised only of characters in the range ascii\[a-z\].

## Output Format

Return the encoded message as a string.
