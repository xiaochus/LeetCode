"""16. 3Sum Closest
Given an array S of n integers, find three integers in S such that the
sum is closest to a given number, target. Return the sum of the three
integers. You may assume that each input would have exactly one
solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) < 3:
            return 0

        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]
        diff = abs(target - closest)

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while(left < right):
                sums = nums[i] + nums[left] + nums[right]
                tmpDiff = abs(target - sums)
                if tmpDiff < diff:
                    diff = tmpDiff
                    closest = sums
                if sums < target:
                    left += 1
                else:
                    right -= 1

        return closest
