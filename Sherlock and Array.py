# -*- coding: utf-8 -*-
"""
Problem Statement

Watson gives an array A1,A2...AN to Sherlock. Then he asks him to find if there exists an element in the array, such
that, the sum of elements on its left is equal to the sum of elements on its right. If there are no elements to
left/right, then sum is considered to be zero.

Formally, find an i, such that, A1+A2...Ai-1 = Ai+1+Ai+2...AN.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, A = cipher
        f = [0 for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            f[i] = f[i - 1] + A[i - 1]

        for i in xrange(N):
            if f[i] == f[N] - f[i + 1]:
                return "YES"
        return "NO"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
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
