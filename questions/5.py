"""5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_str = ""
        isPal = [[0 for j in range(len(s))] for i in range(len(s))]

        if s is None or len(s) == 0:
            return max_str

        for i in range(len(s)):
            j = i
            while(j >= 0):
                if (s[j] == s[i]) and (i - j < 2 or isPal[j + 1][i - 1]):
                    isPal[j][i] = 1
                    lens = i - j + 1
                    if max_len < lens:
                        max_len = lens
                        max_str = s[j: i + 1]
                j -= 1

        return max_str
