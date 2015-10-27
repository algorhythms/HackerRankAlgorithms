# -*- coding: utf-8 -*-
"""
Problem Statement

Welcome to the exciting class of Professor Manasa. In each lecture she used to play some game while teaching a new
concept. Today's topic is Set Theory. For today's game, she had given a set A = {a1, a2, ...aN} of N integers to her
students and asked them to play the game as follows.

At each step of the game she calls a random student and asks him/her to select a non-empty subset from set A such that
this subset had not been selected earlier and the sum of subset should be even. This game ends when all possible subsets
had been selected. Manasa needs your help in counting the total number of times students can be called assuming each
student gives the right answer. While it is given that if two numbers are same in the given set, they have different
colors. It means that if a1 = a2, then choosing a1 and choosing a2 will be considered as different sets.
"""
__author__ = 'Danyang'
MOD = 10 ** 9 + 7


class Solution(object):
    def solve_error(self, cipher):
        """
        count odd number and even number
        :param cipher: the cipher
        """
        N, lst = cipher
        odd_cnt = len(filter(lambda x: x % 2 == 1, lst))
        even_cnt = N - odd_cnt

        a = (2 ** even_cnt) % MOD

        result = 0
        result += a - 1

        i = 2
        comb = (odd_cnt) * (odd_cnt - 1) / (1 * 2)
        while i <= odd_cnt:
            result += comb * a
            result %= MOD
            i += 2
            comb *= (odd_cnt - i + 1) * (odd_cnt - i) / ((i - 1) * i)
            comb %= MOD

        return result

    def solve(self, cipher):
        """
        count odd number and even number
        :param cipher: the cipher
        """
        N, lst = cipher
        odd_cnt = len(filter(lambda x: x % 2 == 1, lst))
        even_cnt = N - odd_cnt

        a = (2 ** even_cnt) % MOD
        b = (2 ** (odd_cnt - 1)) % MOD

        if odd_cnt != 0:
            result = a - 1 + (b - 1) * a
        else:
            result = a - 1

        return result % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())
    lst = map(int, f.readline().strip().split(' '))
    cipher = N, lst
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
