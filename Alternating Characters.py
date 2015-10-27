# -*- coding: utf-8 -*-
"""
Problem Statement

Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like
ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this,
he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Greedy deletions
        :param cipher: the cipher
        """
        lst = list(cipher)
        ret = [lst[0]]
        cnt = 0
        for i in xrange(1, len(lst)):
            if lst[i] != ret[-1]:
                ret.append(lst[i])
            else:
                cnt += 1
        return cnt


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
