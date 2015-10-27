# -*- coding: utf-8 -*-
"""
Problem Statement

You are given two integers, N and M. Count the number of strings of length N under the alphabet set of size M that
doesn't contain any palindromic string of the length greater than 1 as a consecutive substring.
"""
__author__ = 'Danyang'

MOD = 10 ** 9 + 7


class Solution(object):
    def solve(self, cipher):
        """
        Any palindrome, it has a sub-palindrome with length 2 or 3 pivoting at the center.

        To construct a palindrome, the 1st letter has M ways, the 2nd has (M-1) ways, subsequently, there
        are (M-2) ways to choose letters, since it should not be the same as the previous or pre-previous letter;
        otherwise it will form a palindrom with either length 2 or 3.

        Therefore, total = M*(M-1)*(M-2)*(M-2)*(M-2)...

        :param cipher: the cipher
        """
        N, M = cipher
        s = M
        if N > 1:
            s *= (M - 1)
        if N > 2:
            s *= pow(M - 2, N - 2, MOD)  # s *= self._exp(M-2, N-2)
            s %= MOD
        return s % MOD

    def _exp(self, a, b):
        """Alternative to built-in pow()"""
        ret = 1
        b %= MOD
        while b > 0:
            if b & 1 == 0:
                b /= 2
                a *= a
                a %= MOD
            else:
                ret *= a
                ret %= MOD
                b -= 1
        return ret


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
