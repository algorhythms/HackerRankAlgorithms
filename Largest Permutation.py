# -*- coding: utf-8 -*-
"""
Problem Statement

You are given an array of N integers which is a permuation of the first N natural numbers. You can swap any two elements
 of the array. You can make at most K swaps. What is the lexicographically largest permutation you can make?

Input Format
The first line of the input contains two integers, N and K, the size of the input array and the maximum swaps you can
make, respectively. The second line of the input contains a permutation of the first N natural numbers.

Output Format
Print the lexicographically largest permutation you can make with at most K swaps.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, K, lst = cipher
        for i in xrange(len(lst)):
            if K <= 0:
                break
            maxa, idx = -1, 0
            for j in xrange(i, len(lst)):
                if lst[j] > maxa:
                    maxa = lst[j]
                    idx = j
            if idx != i:
                K -= 1
                lst[idx], lst[i] = lst[i], lst[idx]

        return " ".join(map(str, lst))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()

    N, K = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))
    cipher = (N, K, lst)
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
