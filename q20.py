# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        
        # mapping closing → opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If closing bracket
            if char in mapping:
                if not stack:
                    return False
                
                top = stack.pop()
                if top != mapping[char]:
                    return False
            else:
                # opening bracket
                stack.append(char)
        
        # if stack empty, all matched correctly
        return len(stack) == 0
