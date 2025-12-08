# Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        result = []
        start = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i]
            
            # Case: consecutive → continue the range
            if current == prev + 1:
                prev = current
            else:
                # Case: range breaks → close previous range
                if start == prev:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(prev))
                
                # Start a new range
                start = current
                prev = current
        
        # Close the final range after loop ends
        if start == prev:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(prev))
        
        return result

 