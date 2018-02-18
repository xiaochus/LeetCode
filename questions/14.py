"""14. Longest Common Prefix
Write a function to find the longest common prefix string amongst
an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[: len(prefix) - 1]
                if not prefix:
                    return ""

        return prefix
