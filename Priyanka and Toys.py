# -*- coding: utf-8 -*-
"""
Problem Statement

Little Priyanka visited a kids' shop. There are N toys and their weight is represented by an array W=[w1,w2,…,wN]. Each
toy costs 1 unit, and if she buys a toy with weight w′, then she can get all other toys whose weight lies between
[w′,w′+4] (both inclusive) free of cost.

Input Format

The first line contains an integer N i.e. number of toys.
Next line will contain N integers, w1,w2,…,wN, representing the weight array.

Output Format

Minimum units with which Priyanka could buy all of toys.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        A = sorted(cipher)
        cur = -5
        cnt = 0
        for a in A:
            if cur + 4 < a:
                cur = a
                cnt += 1
        return cnt


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    n = int(f.readline().strip())


    # construct cipher
    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
