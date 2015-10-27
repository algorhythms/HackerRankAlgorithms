# -*- coding: utf-8 -*-
"""
Problem Statement

Given a squared sized grid G of size N in which each cell has a lowercase letter. Denote the character in the ith row
and in the jth column as G[i][j].

You can perform one operation as many times as you like: Swap two column adjacent characters in the same row G[i][j]
and G[i][j+1] for all valid i,j.

Is it possible to rearrange the grid such that the following condition is true?

G[i][1]≤G[i][2]≤⋯≤G[i][N] for 1≤i≤N and
G[1][j]≤G[2][j]≤⋯≤G[N][j] for 1≤j≤N
In other words, is it possible to rearrange the grid such that every row and every column is lexicographically sorted?

Note: c1≤c2, if letter c1 is equal to c2 or is before c2 in the alphabet.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        m = len(cipher)
        n = len(cipher[0])
        cipher = map(lambda x: sorted(x), cipher)
        # print cipher
        for j in xrange(n):
            for i in xrange(m - 1):
                if cipher[i][j] > cipher[i + 1][j]:
                    return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        n = int(f.readline().strip())
        cipher = []
        for i in xrange(n):
            cipher.append(list(f.readline().strip()))

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
