# -*- coding: utf-8 -*-
"""
Help him figure out whether any anagram of the string can be a palindrome or not.
"""
import collections

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        collect to map
        :param cipher: the cipher
        """
        d = collections.defaultdict(int)
        for c in cipher:
            d[c] += 1

        cnt = 0
        for v in d.values():
            if v & 1 == 1:
                cnt += 1
            if cnt > 1:
                return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    cipher = f.readline().strip()

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
