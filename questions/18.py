"""18. 4Sum
Given an array S of n integers, are there elements a, b, c,
and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        n = len(nums)
        result = set()
        nums = sorted(nums)

        for i in range(0, n - 3):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            sub1 = target - nums[i]
            for j in range(i + 1, n - 2):
                sub2 = sub1 - nums[j]
                d = {}
                for x in nums[j + 1:]:
                    sub3 = sub2 - x
                    if sub3 in d:
                        result.add((nums[i], nums[j], sub3, x))
                    else:
                        d[x] = 1

        return list(map(list, result))
