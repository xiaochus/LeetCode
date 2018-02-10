"""6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or numRows < 2 or len(s) <= numRows:
            return s

        per = ["" for x in range(numRows)]
        init = 0
        direct = 1

        for i in range(len(s)):
            per[init] += s[i]
            init += direct

            if init >= numRows:
                init = numRows - 2
                direct = -1
            if init < 0:
                init = 1
                direct = 1

        rets = ""
        for p in per:
            rets += p

        return rets
