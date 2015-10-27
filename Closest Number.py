# -*- coding: utf-8 -*-
"""
Problem Statement

You are given 3 numbers a, b and x. You need to output the multiple of x which is closest to ab. If more than one answer
 exists , display the smallest one.

Input Format
The first line contains T, the number of testcases.
T lines follow, each line contains 3 space separated integers (a, b and x respectively)

Output Format
For each test case , output the multiple of x which is closest to ab

Constraints
1 ≤ T ≤ 105
1 ≤ x ≤ 109
0 < ab ≤ 109
1 ≤ a ≤ 109
-109 ≤ b ≤ 109
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        a, b, x = cipher
        if a > 1:
            result = int((a ** b) / float(x) + 0.5) * x
        else:
            result = 1
        if result != int(result):
            if result > 0.5 and x == 1:
                return 1
            else:
                return 0
        return result


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
