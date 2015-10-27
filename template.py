# -*- coding: utf-8 -*-
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """


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