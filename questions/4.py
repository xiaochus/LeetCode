"""4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and
n respectively.

Find the median of the two sorted arrays. The overall run time
complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import sys

        if not nums1 and not nums2:
            return 0
        if not nums1:
            m = self.getMid(len(nums2))
            return (nums2[m[0]] + nums2[m[1]]) / 2
        if not nums2:
            m = self.getMid(len(nums1))
            return (nums1[m[0]] + nums1[m[1]]) / 2

        lens = len(nums1) + len(nums2)
        mid = lens // 2
        p1, p2 = 0, 0
        nums3 = []

        for i in range(lens):
            a = nums1[p1] if p1 < len(nums1) else sys.maxsize
            b = nums2[p2] if p2 < len(nums2) else sys.maxsize

            if a < b:
                nums3.append(a)
                p1 += 1
            else:
                nums3.append(b)
                p2 += 1
            if i == mid:
                break

        m = self.getMid(lens)
        return (nums3[m[0]] + nums3[m[1]]) / 2

    def getMid(self, n):
        if n % 2 == 0:
            return (n // 2 - 1, n // 2)
        else:
            return (n // 2, n // 2)
