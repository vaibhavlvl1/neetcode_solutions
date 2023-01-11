"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


def containsDuplicate(nums):
    d = {}
    for numbers in nums:
        d[numbers] = d.get(numbers,0)+1

    for values in d.values():
        if values >1:
            return True
    return False

# print(containsDuplicate([1,2,3,1]))



# leetcode - using dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for numbers in nums:
            d[numbers] = d.get(numbers,0)+1

        for value in d.values():
            if value >1:
                return True
        return False




# ideal solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for number in nums:
            if number in d:
                return True
            d[number]='it exists'
        return False 
