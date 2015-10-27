# -*- coding: utf-8 -*-
"""
Problem Statement

Gandalf is travelling from Rohan to Rivendell to meet Frodo but there is no direct route from Rohan (T1) to Rivendell (Tn).

But there are towns T2,T3,T4...Tn-1 such that there are N1 routes from Town T1 to T2, and in general, Ni routes from Ti
to Ti+1 for i=1 to n-1 and 0 routes for any other Ti to Tj for j ≠ i+1

Find the total number of routes Gandalf can take to reach Rivendell from Rohan.
"""
__author__ = 'Danyang'
MOD = 1234567


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        return reduce(lambda x, y: x * y % MOD, cipher)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
