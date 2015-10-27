# -*- coding: utf-8 -*-
"""
Problem Statement

Given a list of n integers, A={a1,a2,…,an}, and another integer, k representing the expected sum. Select zero or more
numbers from A such that the sum of these numbers is as near as possible, but not exceeding, to the expected sum (k).

Note

Each element of A can be selected multiple times.
If no element is selected then the sum is 0.
Input Format

The first line contains T the number of test cases.
Each test case comprises of two lines. First line contains two integers, n k, representing the length of list A and
expected sum, respectively. Second line consists of n space separated integers, a1,a2,…,an, representing the elements of
list A.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        repeatable knapsack, dp

        f[i][c] represents the max possible value at the index i given the capacity c
        normally:
        f[i][c] = max{f[i-1][c], f[i-1][c-w_i]+v_i}
        since repeatable:
        f[i][c] = max{f[i-1][c], f[i-1][c-w_i]+v_i, f[i][c-w_i]+v_i}
        since f[i][c] represent the max possible value at i, c; thus only need to consider f[i-1][c-w_i] among others

        :param cipher: the cipher
        """
        n, k, A = cipher
        f = [[0 for _ in xrange(k + 1)] for _ in xrange(n + 1)]  # f[0, :] is dummies
        for i in xrange(n + 1):
            for c in xrange(k + 1):
                f[i][c] = f[i - 1][c]
                temp = c - A[i - 1]
                if temp >= 0:
                    f[i][c] = max(f[i - 1][c], f[i - 1][c - A[i - 1]] + A[i - 1], f[i][c - A[i - 1]] + A[i - 1])

        return f[n][k]


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        n, k = map(int, f.readline().strip().split(' '))
        A = map(int, f.readline().strip().split(' '))
        cipher = n, k, A

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
