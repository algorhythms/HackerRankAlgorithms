# -*- coding: utf-8 -*-
"""
Problem Statement

How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need
to efficiently compute the answer.

Problem Statement

Write a program that, given

An amount N and types of infinite available coins M
A list of M coins - C={C1,C2,C3,..,CM}
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        f stands for number of different ways at money k with combination of coins[i: ]
        when lst = [1, 2, 3]
        f[k][i] = f[k-lst[i]][i]+f[k][i+1] ...
        :param cipher: the cipher
        """
        total, n, lst = cipher
        f = [[0 for _ in xrange(n)] for _ in xrange(total + 1)]

        for i in xrange(n):
            if lst[i] < total + 1:
                f[lst[i]][i] = 1  # can only be 1

        for k in xrange(1, total + 1):
            for i in reversed(xrange(n)):
                if k - lst[i] >= 0:
                    f[k][i] += f[k - lst[i]][i]  # pick the current coin i
                if i + 1 < n:
                    f[k][i] += f[k][i + 1]  # skip to the next coin

        return f[total][0]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    N, M = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))

    cipher = N, M, lst
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
