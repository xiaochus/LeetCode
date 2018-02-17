"""12. Integer to Roman
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""

        roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["", "M", "MM", "MMM"]]
        result = ""
        dig = 0

        while(num != 0):
            result = roman[dig][num % 10] + result
            num = num // 10
            dig += 1

        return result
