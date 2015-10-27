# -*- coding: utf-8 -*-
"""
Problem Statement

Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S.
The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

(Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the
absolute value of an integer x)
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        s = cipher
        r = s[::-1]
        s = map(ord, list(s))
        r = map(ord, list(r))
        for i in xrange(1, len(s)):
            if abs(s[i] - s[i - 1]) != abs(r[i] - r[i - 1]):
                return "Not Funny"
        return "Funny"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
