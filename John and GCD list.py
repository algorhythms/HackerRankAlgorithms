# -*- coding: utf-8 -*-
"""
Problem Statement

John is new to Mathematics and does not know how to calculate GCD of numbers. So he wants you to help him in a few GCD
calculations. John has a list A of numbers, indexed 1 to N. He wants to create another list B having N+1 numbers,
indexed from 1 to N+1, and having the following property:

GCD(B[i], B[i+1]) = A[i], ∀ 1 ≤ i ≤ N

As there can be many such lists, John wants to know the list B in which sum of all elements is minimum. It is guaranteed
that such a list will always exist.

Input Format
The first line contains an integer T, i.e., the number of the test cases. T testcases follow.
The first line of each test case contains an integer N, i.e., the number of elements in the array.
The second line of each test case contains N space separated integers that denote the elements of the list A.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        gcd and scf
        :param cipher: the cipher
        """
        A = cipher
        B = []
        B.append(A[0])
        for i in xrange(1, len(A)):
            B.append(A[i] * A[i - 1] / self.gcd(A[i], A[i - 1]))
        B.append(A[-1])

        return " ".join(map(str, B))

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
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
