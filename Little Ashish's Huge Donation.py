# -*- coding: utf-8 -*-
"""
Problem Statement

Little Ashish is doing internship at multiple places. Instead of giving parties to his friends he decided to donate
candies to children. He likes solving puzzles and playing games. Hence he plays a small game. Suppose there are N
children. The rules of the game are:

The ith child gets i2 candies (1≤i≤N).

The yth child cannot get a candy until and unless all the children before him (1≤i<y) gets candies according to rule
number 1.

One of his jealous friends, Pipi, asks him "Given X (the number of candies) how many children will you be able to
serve?". Little Ashish fears calculations and cannot solve this problem so he leaves this problem to the worthy
programmers of the world. Help little Ashish in finding the solution.

Input Format
The first line contains T i.e. number of test cases.
T lines follow, each line containing an integer X.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Bin search + sum of squares
        :param cipher: the cipher
        """
        l = 1
        h = cipher
        while l <= h:
            mid = (l + h) / 2
            if self.sum_of_squares(mid) <= cipher:
                l = mid + 1
            else:
                h = mid - 1

        l -= 1
        return l

    def sum_of_squares(self, n):
        return n * (n + 1) * (2 * n + 1) / 6


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
