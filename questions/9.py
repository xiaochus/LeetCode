"""9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra
space.
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        a, b = 0, x

        while(b > 0):
            a = a * 10 + b % 10
            b //= 10

        if a == x:
            return True
        else:
            return False
