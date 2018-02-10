"""10. Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        len_s = len(s)
        len_p = len(p)

        dp = [[False for i in range(len_p + 1)] for j in range(len_s + 1)]
        dp[0][0] = True

        for j in range(1, len_p):
            if p[j] == '*':
                dp[0][j + 1] = dp[0][j - 1]
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = (dp[i - 1][j - 2] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')) or \
                        dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[len_s][len_p]
