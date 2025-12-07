# Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ""
        for char in s:
            if char.isalnum():
                result += char.lower()
            else:
                continue
        
        left = 0
        right = len(result) - 1

        while left < right:
            if result[left] != result[right]:
                return False
                
            left += 1
            right -= 1
        return True
