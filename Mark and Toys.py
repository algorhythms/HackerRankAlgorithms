# -*- coding: utf-8 -*-
"""
Mark and Jane are very happy after having their first kid. Their son is very fond of toys, so Mark wants to buy some.
There are N different toys lying in front of him, tagged with their prices, but he has only $K. He wants to maximize the
number of toys he buys with this money.

Now, you are Mark's best friend and have to help him buy as many toys as possible.

Input Format
The first line contains two integers, N and K, followed by a line containing N space separated integers indicating the
products' prices.

Output Format
An integer that denotes maximum number of toys Mark can buy for his son.

Constraints
1<=N<=105
1<=K<=109
1<=price of any toy<=109
A toy can't be bought multiple times.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        1D binpacking
        main solution function
        :param cipher: the cipher
        """
        n, K, A = cipher
        A.sort()
        cnt = 0
        for elt in A:
            K -= elt
            if K >= 0:
                cnt += 1
            else:
                break
        return cnt


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    n, K = map(int, f.readline().strip().split(' '))

    # construct cipher
    A = map(int, f.readline().strip().split(' '))

    cipher = n, K, A
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
