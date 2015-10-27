# -*- coding: utf-8 -*-
"""
Problem Statement

Adam is standing at point (a,b) in an infinite 2D grid. He wants to know if he can reach point (x,y) or not. The only
operation he can do is to move to point (a+b,b), (a,a+b), (a-b,b), or (a,a-b) from some point (a,b). It is given that he
can move to any point on this 2D grid,i.e., the points having positive or negative X(or Y) co-ordinates.

Tell Adam whether he can reach (x,y) or not.

Input Format
The first line contains an integer, T, followed by T lines, each containing 4 space separated integers i.e. a b x y

Output Format
For each test case, display YES or NO that indicates if Adam can reach (x,y) or not.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm: math: https://hr-filepicker.s3.amazonaws.com/infinitum-jun14/editorials/2372-possible-path.pdf
        :param cipher: the cipher
        """
        a, b, x, y = cipher
        if self.gcd(a, b) == self.gcd(x, y):
            return "YES"
        else:
            return "NO"

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


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
