# -*- coding: utf-8 -*-
"""
Problem Statement

Given a string S, find the number of unordered anagramic pairs of substrings.
"""
import collections

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        collect to map

        https://github.com/derekhh/HackerRank/blob/master/sherlock-and-anagrams.cpp

        :param cipher: the cipher
        """
        d = collections.defaultdict(int)
        lst = list(cipher)
        n = len(lst)
        for i in xrange(n):
            for l in xrange(1, n - i + 1):
                sub = lst[i: i + l]
                sub.sort()
                d["".join(sub)] += 1

        s = 0
        for v in d.values():
            s += v * (v - 1) / 2
        return s


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
