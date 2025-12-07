# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        # If lengths differ, cannot be an anagram
        if len(s) != len(t):
            return False

        # Create frequency count for characters
        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Subtract count using characters from t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
