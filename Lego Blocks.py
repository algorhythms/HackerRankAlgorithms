# -*- coding: utf-8 -*-
"""
Problem Statement

You have 4 types of lego blocks, of sizes (1 x 1 x 1), (1 x 1 x 2), (1 x 1 x 3), and (1 x 1 x 4). Assume that you have
an infinite number of blocks of each type.

Using these blocks, you want to make a wall of height N and width M. The wall should not have any holes in it. The wall
you build should be one solid structure. A solid structure can be interpreted in one of the following ways:

(1)It should not be possible to separate the wall along any vertical line without cutting any lego block used to build
the wall.
(2)You cannot make a vertical cut from top to bottom without cutting one or more lego blocks.

The blocks can only be placed horizontally. In how many ways can the wall be built?
"""
__author__ = 'Danyang'
MOD = 1000000007


class Solution(object):
    def __init__(self):
        self.lens = [1, 2, 3, 4]

    def solve(self, cipher):
        """
        f[i][j] represents the number of combinations for size i*j wall, not necessarily solid
        f[i][j] = f[1][j]**i

        s[i][j] represents the number of combinations for size i*j wall, solid

        s[h][w]  = f(h,w) - sum(f[h][w-i]*s[h][i] for i)

        To solve TLE:
        1. s[h][w] not rely on previous h, simplify to s[w]
        2. power takes time, take memory to save time for f[1][j]**i

        :param cipher:
        :return:
        """
        N, M = cipher
        f = [0 for _ in xrange(M + 1)]
        s = [0 for _ in xrange(M + 1)]

        f[0] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 0:
                    f[j] += f[j - l]
                f[j] %= MOD

        f_N = map(lambda x: pow(x, N, MOD), f)

        for j in xrange(1, M + 1):
            s[j] = f_N[j]
            if s[j] <= 0: break
            for k in xrange(1, j):  # sum
                s[j] -= f_N[j - k] * s[k]
                s[j] %= MOD
        return s[M]


class Solution_TLE(object):
    def __init__(self):
        self.lens = [1, 2, 3, 4]

    def solve(self, cipher):
        """
        f[i][j] represents the number of combinations for size i*j, not necessarily solid
        f[i][j] = f[1][j]**i
        s[i][j] represents the number of combinations for size i*j, solid

        s[h][w]  = f(h,w) - sum(f[h][w-i]*s[h][i])

        be careful with TLE
        :param cipher:
        :return:
        """
        N, M = cipher
        f = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]
        s = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]

        f[1][0] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 0:
                    f[1][j] += f[1][j - l]
                    f[1][j] %= MOD

        for i in xrange(2, N + 1):
            for j in xrange(1, M + 1):
                f[i][j] = f[i - 1][j] * f[1][j]
                f[i][j] %= MOD

        for i in xrange(1, N + 1):
            for j in xrange(1, M + 1):
                s[i][j] = f[i][j]
                if s[i][j] <= 0: break
                for k in xrange(1, j):  # sum
                    s[i][j] -= f[i][j - k] * s[i][k]
                    s[i][j] %= MOD
        return s[N][M]

    def solve_error(self, cipher):
        """
        f[i][j] represents the number of combinations for size i*j
        f[i][j+1] = iC1*f[i-1][j]*f[1][j+1]
                  = iC2*f[i-2][j]*f[1][j+1]^2
                  ...
        (need careful math proof of the equivalent points
        :param cipher: the cipher
        """
        N, M = cipher
        f = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]

        f[1][1] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 1:
                    f[1][j] += f[1][j - l]
        for j in xrange(1, M + 1):
            f[1][j] -= f[1][j - 1]

        for i in xrange(2, N + 1):
            for j in xrange(1, M + 1):
                cmb = i
                for l in xrange(1, i + 1):
                    f[i][j] += cmb * f[i - l][j - 1] * (f[1][j] ** i)  # equivalent
                    cmb = cmb * (i - l) / (l + 1)
        return f[N][M]


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
