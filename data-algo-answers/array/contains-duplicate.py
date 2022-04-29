'''
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
'''

class Solution:
    def containsDuplicate(self, array):
        nums = {}
        for i in array:
            if 'numbers' in nums:
                nums['numbers'] = nums['numbers'], i
            else:
                nums['numbers'] = i
        print(nums)


Solution().containsDuplicate([1,2,3,100])