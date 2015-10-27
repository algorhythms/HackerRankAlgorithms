"""
Problem Statement

Watson asks Sherlock:
Given a string S of N 0's and M 1's, how many unique permutations of this string start with 1?

Help Sherlock by printing the answer modulo (109+7).

Input Format
First line contains T, the number of test cases.
Each test case consists of N and M separated by a space.
"""
MOD = 10 ** 9 + 7
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Labeled permutation variants
        :param cipher: the cipher
        """
        N, M = cipher
        return math.factorial(N + M - 1) / math.factorial(N) / math.factorial(M - 1) % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
