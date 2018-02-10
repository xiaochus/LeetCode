"""3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and
not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sub = 0
        start = 0
        last = {}

        if s is None or len(s) == 0:
            return max_sub

        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= start:
                start = last[s[i]] + 1
            last[s[i]] = i
            max_sub = max(max_sub, i - start + 1)

        return max_sub
