"""
Problem Statement

Elon Musk has succesfully built an automated staircase from Earth to Mars. Many people want to go to Mars, but that's
not possible due to limited capacity of the staircase and logistics involved. Hence, Elon asks interested candidates to
solve a tough challenge. If they solve it, they get a chance to visit Mars, otherwise not. Sam is highly interested in
going to Mars. Can you help him solve the challenge?

The staircase has N steps. It can either go step by step, or at each step, it can take a jump of at most N steps.

Elon is interested to know the number of ways in which you can go to Mars. Since the number of steps in stairs can be
insanely large, Elon is only interested in the first and the last K digits of number of ways from which he can compute
the actual answer with his algorithm.
"""
import math
from decimal import *

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        getcontext().prec = 28

    def solve(self, cipher):
        """
        first K digit of B^N
        http://discuss.codechef.com/questions/15398/first-k-digits-of-nn

        :param cipher: the cipher
        """
        N, K = cipher
        LSB = pow(2, N - 1, 10 ** K)

        # calculate MSB
        MSB = int(str(self.get_MSB(2, N - 1) * 10 ** K)[:K])

        return MSB + LSB

    def get_MSB(self, b, n):
        """
        Use Decimal() otherwise only works for small numbers
        """
        p = Decimal(n) * Decimal(b).log10()
        f = Decimal(p) - Decimal(math.floor(p))
        return Decimal(10) ** f


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
