### 1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Example :
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r

#### Leet code sumbission link : https://leetcode.com/problems/merge-strings-alternately/solutions/7017682/1768-merge-strings-alternately-by-yesesr-csgp 

#### Time complexity: O(m+n)
Where 'm' is the length of word1 and 'n' is the length of word2.
The algorithm iterates through both strings essentially once. In each step, it appends a character (or two) to the result.
The number of operations is directly proportional to the total number of characters in both input strings. Therefore, if word1 has m characters and word2 has n characters, the total operations will be roughly m + n.

#### Space complexity: O(m+n)
The algorithm constructs a new string (or list of characters that is later joined into a string) to store the merged result.
The length of this new string will be m + n (the sum of the lengths of the two input strings).
Therefore, the space required to store the output is directly proportional to the combined length of the input strings.
