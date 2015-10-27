# -*- coding: utf-8 -*-
"""
Problem Statement

Akash and Akhil are playing a game. They have N balls numbered from 0 to N−1. Akhil asks Akash to reverse the position
of the balls, i.e., to change the order from say, 0,1,2,3 to 3,2,1,0. He further asks Akash to reverse the position of
the balls N times, each time starting from one position further to the right, till he reaches the last ball. So, Akash
has to reverse the positions of the ball starting from 0th position, then from 1st position, then from 2nd position and
so on. At the end of the game, Akhil will ask Akash the final position of any ball numbered K. Akash will win the game,
if he can answer. Help Akash.

Input Format
The first line contains an integer T, i.e., the number of the test cases.
The next T lines will contain two integers N and K.

Output Format
Print the final index in array.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Math
        group into pairs
        :param cipher: the cipher
        """
        N, K = cipher
        if K < N / 2:
            return 2 * K + 1
        else:
            return 2 * (N - 1 - K)


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
