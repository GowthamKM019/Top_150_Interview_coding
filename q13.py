#  Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):

            # If c1 is already mapped but mapped to a different char → conflict
            if c1 in s_to_t and s_to_t[c1] != c2:
                return False

            # If c2 already mapped from a different char → conflict
            if c2 in t_to_s and t_to_s[c2] != c1:
                return False

            # Create new mapping if not exists
            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True
