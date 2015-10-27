# -*- coding: utf-8 -*-
"""
Problem Statement

You are given two strings, A and B. Find if there is a substring that appears in both A and B.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        a = map(set, cipher)
        ret = a[0].intersection(a[1])
        if len(ret) > 0:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = []
        cipher.append(f.readline().strip())
        cipher.append(f.readline().strip())
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
