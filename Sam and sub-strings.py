# -*- coding: utf-8 -*-
"""
Problem Statement

Samantha and Sam are playing a game. They have 'N' balls in front of them, each ball numbered from 0 to 9, except the
first ball which is numbered from 1 to 9. Samantha calculates all the sub-strings of the number thus formed, one by one.
If the sub-string is S, Sam has to throw 'S' candies into an initially empty box. At the end of the game, Sam has to
find out the total number of candies in the box, T. As T can be large, Samantha asks Sam to tell T % (109+7) instead.
If Sam answers correctly, he can keep all the candies. Sam can't take all this Maths and asks for your help.
"""
__author__ = 'Danyang'
MOD = 1e9 + 7


class Solution(object):
    def solve_TLE(self, cipher):
        """
        O(N^2)

        :param cipher: the cipher
        """
        A = map(int, list(cipher))
        f = A[0]
        num = A[0]
        sig = 1
        for i in xrange(1, len(A)):
            num = 10 * num + A[i]
            sig *= 10

            temp = num
            temp_sig = sig
            while temp_sig >= 1:
                f += temp
                f %= MOD

                temp %= temp_sig
                temp_sig /= 10

        return int(f)

    def solve(self, cipher):
        """
        O(N)
        example: 1234
        1
        12, 2
        123, 23, 3
        1234, 234, 34, 4
        :param cipher:
        :return:
        """
        pre = [0 for _ in cipher]
        pre[0] = int(cipher[0])
        for i in xrange(1, len(cipher)):
            pre[i] = (pre[i - 1] * 10 + int(cipher[i]) * (i + 1)) % MOD

        s = 0
        for elt in pre:
            s = (s + elt) % MOD

        return int(s)


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()

    # construct cipher
    cipher = f.readline().strip()

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
