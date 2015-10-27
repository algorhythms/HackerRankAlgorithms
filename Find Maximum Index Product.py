# -*- coding: utf-8 -*-
"""
Problem Statement

You are given a list of n numbers a1,a2,…,an. For each i (1≤i≤n), define LEFT(i) to be the nearest index j before i such
that aj>ai. Note that if j does not exist, we should consider LEFT(i) to be 0. Similarly, define RIGHT(i) to be the
nearest index j after i such that aj>ai. Note that if j does not exist, we should consider RIGHT(i) to be 0.

Define INDEXPRODUCT(i) as the product of LEFT(i) and RIGHT(i). Find the maximum INDEXPRODUCT(i) among all 1≤i≤n.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        dp, chaining

        L[i] represents the index of LEFT(i)
        R[i] represents the index of RIGHT(i)

        L[i]
        0 1 2 3 4
        5 4 3 4 5
        - 0 1 0 -

        :param cipher: the cipher
        """
        A = cipher
        L = [-1 for _ in A]
        for i in xrange(1, len(A)):
            idx = i - 1
            while idx != -1:
                if A[idx] > A[i]:
                    L[i] = idx
                    break
                idx = L[idx]

        R = [-1 for _ in A]
        for i in xrange(len(A) - 2, -1, -1):
            idx = i + 1
            while idx != -1:
                if A[idx] > A[i]:
                    R[i] = idx
                    break
                idx = R[idx]

        maxa = -1
        for i in xrange(len(A)):
            left = L[i] + 1
            right = R[i] + 1
            maxa = max(maxa, left * right)

        return maxa


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    N = int(f.readline().strip())

    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
