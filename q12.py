# Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # count characters in magazine
        char_count = {}
        for ch in magazine:
            char_count[ch] = char_count.get(ch, 0) + 1
        
        # check characters in ransomNote
        for ch in ransomNote:
            if ch not in char_count or char_count[ch] == 0:
                return False
            char_count[ch] -= 1  # use one letter
        
        return True


 
