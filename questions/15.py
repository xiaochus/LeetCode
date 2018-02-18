"""15. 3Sum
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        result = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            sub1 = 0 - nums[i]
            d = {}
            for x in nums[i + 1:]:
                sub2 = sub1 - x
                if sub2 in d:
                    result.add((nums[i], sub2, x))
                else:
                    d[x] = 1

        return list(map(list, result))
