# -*- coding: utf-8 -*-
"""
Problem Statement

Isaac has to buy a new HackerPhone for his girlfriend Amy. He is exploring the shops in the town to compare the prices
whereupon he finds a shop located on the first floor of a building, that has a unique pricing policy. There are N steps
leading to the shop. A numbered ball is placed on each of the steps.
The shopkeeper gives Isaac a fair coin and asks him to toss the coin before climbing each step. If the result of the
toss is a 'Heads', Isaac should pick up the ball, else leave it and proceed to the next step.

The shopkeeper then asks Isaac to find the sum of all the numbers he has picked up (let's say S). The price of the
HackerPhone is then the expected value of S. Help Isaac find the price of the HackerPhone.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        return sum(cipher) / 2.0


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    N = int(f.readline().strip())

    cipher = []
    for _ in xrange(N):
        # construct cipher
        cipher.append(int(f.readline().strip()))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
