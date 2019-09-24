# acm-icpc-team

URL - https://www.hackerrank.com/challenges/acm-icpc-team/problem

There are a number of people who will be attending [acm-icpc world finals](https://en.wikipedia.org/wiki/acm_international_collegiate_programming_contest). Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.

For example, given three attendees' data as follows:

```
10101
11110
00010
```

These are all possible teams that can be formed:

```
Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]
```

In this case, the first team will know all 5 subjects. They are the only team that can be created knowing that many subjects.

## Function Description

Complete the acmTeam function in the editor below. It should return an integer array with two elements: the maximum number of topics any team can know and the number of teams that can be formed that know that maximum number of topics.

acmTeam has the following parameter(s):

- topicArr: An array of strings of binary digits

## Constraints

- 2 <= n <= 500 (binary string length)
- 1 <= m <= 500 (number of strings)

## Output Format

On the first line, print the maximum number of topics a 2-person team can know.
On the second line, print the number of ways to form a 2-person team that knows the maximum number of topics.
