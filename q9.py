#  Find the Index of the First Occurrence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == " ":
            return 0

        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            if haystack.startswith(needle,i):
                return i
            
        return -1
