"""8. String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a
challenge, please do not see below and ask yourself what are the
possible input cases.

Notes: It is intended for this problem to be specified vaguely
(ie, no given input specs). You are responsible to gather all the
input requirements up front.
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str is None or len(str) == 0:
            return 0

        ret, start, isPositive = 0, 0, 1
        include = ["%d" % i for i in range(10)]

        if str[0] == '-' or str[0] == '+':
            isPositive = 1 if str[0] == '+' else -1
            start += 1

        for i in range(start, len(str)):
            if str[i] not in include:
                break
            ret = ret * 10 + int(str[i])

        ret = ret * isPositive
        return max(-2**31, min(2**31 - 1, ret))
