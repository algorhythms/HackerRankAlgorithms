# -*- coding: utf-8 -*-
"""
Problem Statement

Sherlock is given 2 square tiles, initially both of whose sides have length L placed in an x−y plane; so that the left
bottom of each square coincides with the the origin and their sides are parallel to the axes.

At t=0, both squares start moving along line y=x (along the positive x and y) with velocities S1 and S2.

For each query of form qi, Sherlock has to report the time at which the overlapping area of tiles is equal to qi.
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Physics 101
        (L-vt)^2 = s

        notice the precision problem
        :param cipher: the cipher
        """
        L, S1, S2, qs = cipher
        v = abs(S1 - S2) / math.sqrt(2)
        rets = []
        for q in qs:
            t = (L - math.sqrt(q)) / v
            rets.append(t)
        return "\n".join(map(lambda x: "%f" % x, rets))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    L, S1, S2 = map(int, f.readline().strip().split(' '))
    q = int(f.readline().strip())
    qs = []
    for t in xrange(q):
        qs.append(int(f.readline().strip()))

    # construct cipher
    cipher = L, S1, S2, qs
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
