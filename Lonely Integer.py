# -*- coding: utf-8 -*-
"""
There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs
only once.

Input Format

The first line of the input contains an integer N indicating number of integers.
The next line contains N space separated integers that form the array A.

Constraints

1 <= N < 100
N % 2 = 1 ( N is an odd number )
0 <= A[i] <= 100, ∀ i ∈ [1, N]
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        A = cipher

        bit = 0
        for item in A:
            bit ^= item
        return bit


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())


    # construct cipher
    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
