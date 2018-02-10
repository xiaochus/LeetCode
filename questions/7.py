"""7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold
integers within the 32-bit signed integer range. For the purpose
of this problem, assume that your function returns 0 when the
reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        isPositive = 1
        if x < 0:
            isPositive = -1

        x = int(str(isPositive * x)[::-1])
        x = isPositive * x

        if x > 2**31 - 1 or x < -2**31:
            return 0
        else:
            return x
