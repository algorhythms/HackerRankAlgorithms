"""
Problem Statement

A series is defined in the following manner:

Given the nth and (n+1)th terms, the (n+2)th can be computed by the following relation
Tn+2 = (Tn+1)^2 + Tn
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        A, B, N = cipher

        a, b = A, B
        cnt = 1
        while cnt < N:
            cnt += 1
            a, b = b, b * b + a

        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()

    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
