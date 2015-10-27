# -*- coding: utf-8 -*-
"""
Problem Statement

Chief's bot is playing an old DOS-based game. There are N+1 buildings in the game - indexed from 0 to N and are placed
left-to-right. It is guaranteed that building with index 0 will be of height 0 unit. For buildings with index i
(i∈[1,N]) height will be hi units.

At beginning Chief's bot is at building with index 0. At each step, bot jumps to next (right) building. Suppose bot is
at kth building and his current energy is botEnergy, then in next step he will jump to (k+1)th building. He will
gain/lose energy equal in amount to difference between hk+1 and botEnergy
If hk+1>botEnergy, then he will lose hk+1−botEnergy units of energy.
Otherwise, he will gain botEnergy−hk+1 units of energy.
Goal is to reach Nth building, and during the course bot should never have negative energy units. What should be the
minimum units of energy with which bot should start to successfully complete the game?
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def solve_error(self, cipher):
        """
        E = 2E - h_{k+1}
        E_{i+1} = 2E_i - h_{i+1} > 0

        you can find a mathematical relationship

        forward algorithm got numerical errors

        :param cipher: the cipher
        """
        N, H = cipher
        s = 0
        m = max(H)
        up = math.log(m, 2)
        for i, e in enumerate(H):
            if i > up and i > 1000:
                break
            s += float(e) / 2 ** (i + 1)
        return int(math.ceil(s))

    def solve(self, cipher):
        """
        backward algorithm

        some manipulation of math relationship
        E1N  + (E1N - h1) >= E2N.
        """
        N, H = cipher
        mini = 0
        for i in xrange(N - 1, -1, -1):
            mini = (mini + H[i] + 1) / 2  # ceil, but better than float version of math.ceil
        return mini


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    N = int(f.readline().strip())
    H = map(int, f.readline().strip().split(' '))
    cipher = N, H
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
