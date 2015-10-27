"""
Problem Statement

Jigar got a sequence of n positive integers as his birthday present! He likes consecutive subsequences whose sum is
divisible by k. He asks you to write a program to count them for him.
"""
__author__ = 'Danyang'


class Solution_TLE(object):
    def solve(self, cipher):
        """
        brute force O(n^2)
        :param cipher: the cipher
        """
        n, k, a = cipher
        f = [0 for _ in xrange(n + 1)]  # sum dp
        for i in xrange(1, n + 1):
            f[i] = f[i - 1] + a[i - 1]

        result = 0
        for i in xrange(1, n + 1):
            for j in xrange(0, i):
                if (f[i] - f[j]) % k == 0:
                    result += 1
        return result


class Solution(object):
    def solve(self, cipher):
        """
        MOD and combinations
        :param cipher: the cipher
        """
        n, k, a = cipher
        cnts = [0 for _ in xrange(k)]

        s = 0
        cnts[0] = 1  # \phi
        for num in a:
            s += num
            s %= k
            cnts[s] += 1

        result = 0
        for cnt in cnts:
            result += (cnt * (cnt - 1)) / 2  # nC2
        return result


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        n, k = map(int, f.readline().strip().split(' '))
        a = map(int, f.readline().strip().split(' '))
        cipher = n, k, a
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
