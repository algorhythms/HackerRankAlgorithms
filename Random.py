# -*- coding: utf-8 -*-
"""
Problem Statement

Given an array 'D' with n elements: d[0], d[1], ..., d[n-1], you can perform the following two steps on the array.

Randomly choose two indexes (l, r) with l < r, swap (d[l], d[r])
Randomly choose two indexes (l, r) with l < r, reverse (d[l...r]) (both inclusive)
After you perform the first operation a times and the second operation b times, you randomly choose two indices l & r
with l < r and calculate the S = sum(d[l...r]) (both inclusive).

Now, you are to find the expected value of S.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        # TODO


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    n, a, b = map(int, f.readline().strip().split(' '))
    D = map(int, f.readline().strip().split(' '))
    cipher = n, a, b, D

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
