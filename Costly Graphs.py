# -*- coding: utf-8 -*-
"""
Problem Statement

Let's define the cost of a simple undirected graph as the sum of the costs of its nodes. The cost of a node is defined
as D^K, where D is its degree.

You are given N and K. You need to find the sum of the costs of all possible simple undirected graphs with N nodes.
As this number may be very large, output the sum modulo 1005060097.
"""
__author__ = 'Danyang'

MOD = 1005060097


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, K = cipher
        # TODO


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
