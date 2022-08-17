#[EASY]

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        unique_chars_s = dict()
        unique_chars_t = dict()
        
        if len(s) == len(t):
            for i in range(len(s)):
                unique_chars_s[s[i]] = 1 + unique_chars_s.get(s[i], 0)
                unique_chars_t[t[i]] = 1 + unique_chars_t.get(t[i], 0)
            
            
            return unique_chars_s == unique_chars_t
        else :
            return False
