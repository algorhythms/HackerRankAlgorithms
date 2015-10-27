"""
Problem Statement


Watson gives an integer N to Sherlock and asks him: What is the number of divisors of N that are divisible by 2?.

Input Format
First line contains T, the number of testcases. This is followed by T lines each containing an integer N.
"""
__author__ = 'Danyang'
import math


class Solution(object):
    def solve(self, cipher):
        """
        Brute Force
        :param cipher: the cipher
        """
        N = cipher

        if N % 2 == 1:
            return 0

        cnt = 0
        i = 1
        sq = math.sqrt(N)
        while i <= sq:
            if N % i == 0:
                if i % 2 == 0:
                    cnt += 1
                other = N / i
                if other != i and other % 2 == 0:
                    cnt += 1
            i += 1
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
