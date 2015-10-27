# -*- coding: utf-8 -*-
"""
Problem Statement

Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange
Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any
transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Buy one, sell many

        dp: get the largest from right
        f[i] = max(a_i, f[i+1])
        :param cipher: the cipher
        """
        N, A = cipher
        f = [0 for _ in A]
        f[N - 1] = A[N - 1]
        for i in xrange(N - 2, -1, -1):
            f[i] = max(A[i], f[i + 1])

        profit = 0
        for i in xrange(N - 1):
            profit += max(0, f[i + 1] - A[i])

        return profit


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
