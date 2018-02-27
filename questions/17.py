"""17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is
given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        from functools import reduce
        maps = {'2': 'abc', '3': 'def', '4': 'ghi',
                '5': 'jkl', '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}

        return reduce(lambda p, n: [x + y for x in p for y in maps[n]], digits, [''])
