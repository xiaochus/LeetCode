"""1. Two Sum
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
            sub = target - nums[i]
            part = nums[i + 1:]
            if sub in part:
                result = [i, part.index(sub) + len(nums[: i + 1])]
                break

        return result

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            sub = target - x
            if sub in d:
                result = [d[sub], i]
                break
            d[x] = i

        return result
