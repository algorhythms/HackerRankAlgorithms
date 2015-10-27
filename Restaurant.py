# -*- coding: utf-8 -*-
"""
Problem Statement

Martha is interviewing at Subway. One of the rounds of the interview requires her to cut a bread of size l×b into
smaller identical pieces such that each piece is a square having maximum possible side length with no left over piece of
bread.

Input format
The first line contains an integer T. T lines follow. Each line contains two space separated integers l and b which
denote length and breadth of the bread.

Output format

T lines, each containing an integer that denotes the number of squares of maximum size, when the bread is cut as per
the given condition.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        gcd
        :param cipher: the cipher
        """
        l, b = cipher
        r = self.gcd(l, b)
        return (l * b) / (r * r)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
