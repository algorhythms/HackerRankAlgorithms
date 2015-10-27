# -*- coding: utf-8 -*-
"""
Problem Statement

Given a word w, rearrange the letters of w to construct another word s in such a way that, s is lexicographically
greater than w. In case of multiple possible answers, find the lexicographically smallest one.

Input Format
The first line of input contains t, number of test cases. Each of the next t lines contains w.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        similar to next permutation
        :param cipher: the cipher
        """
        A = list(cipher)
        A = map(ord, A)
        n = len(A)

        a = -1
        for i in xrange(n - 1, 0, -1):
            if A[i - 1] < A[i]:
                a = i - 1
                break
        else:
            return "no answer"

        b = -1
        for i in xrange(n - 1, a, -1):
            if A[i] > A[a]:
                b = i
                break
        else:
            return "no answer"

        A[a], A[b] = A[b], A[a]  # swap
        A = A[:a + 1] + A[n - 1:a:-1]  # reverse
        return "".join(map(chr, A))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
