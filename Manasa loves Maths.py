# -*- coding: utf-8 -*-
"""
Problem Statement

You are given an integer N. Is there a permutation of digits of integer that's divisible by 8? A permutation of digits
of integer N is defined as an integer formed by rearranging the digits of N. For example, if the number N = 123, then
{123, 132, 213, 231, 312, 321} are the possible permutations.

Input Format
The first line contains an integer T i.e. number of test cases.
T lines follow, each containing the integer N.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        starting from divided by 2, 4, then 8
        :param cipher: the cipher
        """
        l = len(cipher)
        if l == 1:
            if int(cipher) % 8 == 0:
                return "YES"
            else:
                return "NO"
        elif l == 2:
            if int(cipher) % 8 == 0 or int(cipher[::-1]) % 8 == 0:
                return "YES"
            else:
                return "NO"

        # when there are 3 or more digits
        hm = [0 for _ in xrange(10)]
        for char in cipher:
            hm[int(char)] += 1

        for i in xrange(0, 1000, 8):
            copy = list(hm)
            s = "00" + str(i)
            j = -1
            while j >= -3:  # check 3 digits
                d = int(s[j])
                if copy[d] <= 0: break
                copy[d] -= 1
                j -= 1
            if j == -4:
                return "YES"
        return "NO"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
