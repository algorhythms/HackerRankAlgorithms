# -*- coding: utf-8 -*-
"""
A strange grid has been recovered from an old book. It has 5 columns and infinite number of rows. The bottom row is
considered as the first row. First few rows of the grid are like this:

..............

..............

20 22 24 26 28

11 13 15 17 19

10 12 14 16 18

 1  3  5  7  9

 0  2  4  6  8
The grid grows upwards forever!

Your task is to find the integer in cth column in rth row of the grid.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        r, c = cipher
        r, c = r - 1, c - 1

        return r / 2 * 10 + r % 2 + c * 2


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()

    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
