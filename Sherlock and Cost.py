# -*- coding: utf-8 -*-
"""
Array A contains the elements, A1,A2...AN. And array B contains the elements, B1,B2...BN. There is a relationship
between Ai and Bi, ∀ 1 ≤ i ≤ N, i.e.,
any element Ai lies between 1 and Bi.

Let cost S of an array A is defined as:

image

You have to print the largest possible value of S.

Input Format
The first line contains, T, the number of test cases. Each test case contains an integer, N, in first line. The second
line of each test case contains N integers that denote the array B.

Output Format
For each test case, print the required answer in one line.

Constraints
1 ≤ T ≤ 20
1 ≤ N ≤ 105
1 ≤ Bi ≤ 100
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        B = cipher
        N = len(B)
        dp = [[0, 0] for _ in xrange(N + 1)]

        LOW = 0
        HIGH = 1
        for i in xrange(2, N + 1):
            dp[i][LOW] = max(dp[i - 1][LOW], dp[i - 1][HIGH] + abs(1 - B[i - 2]))
            dp[i][HIGH] = max(dp[i - 1][HIGH], dp[i - 1][LOW] + abs(B[i - 1] - 1))

        return str(max(dp[-1][LOW], dp[-1][HIGH]))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
