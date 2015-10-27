# -*- coding: utf-8 -*-
"""
Problem Statement

The Indian bank issues coins in 4 denominations, ₹1, ₹2, ₹5 and ₹10.

Given a limited supply of each of the above denominations, in how many ways can you sum them up to a total of ₹N?

Input Format
The first line contains an integer T (number of testcases). Each testcase contains 2 lines. The first line contains
integer N (sum to be achieved)
A, B, C and D in the next line, each representing the number of ₹1, ₹2, ₹5 and ₹10 coins respectively.

Output Format
Output the number of ways in which we can achieve the sum N.
"""
__author__ = 'Danyang'


class Solution_TLE(object):
    def __init__(self):
        self.coinage = [10, 5, 2, 1]

    def solve(self, cipher):
        """
        branch & bound
        :param cipher: the cipher
        """
        target, lst = cipher
        lst.reverse()
        result = [0]
        self.dfs(lst, target, result)
        return result[0]

    def dfs(self, seq, remaining, result):
        if remaining < 0:
            return
        if remaining == 0:
            result[0] += 1
            return

        bound = 0
        for i in xrange(4):
            bound += seq[i] * self.coinage[i]
        if bound < remaining:
            return

        for j in xrange(4):
            for i in xrange(seq[j]):
                remaining -= (i + 1) * self.coinage[j]
                self.dfs([0] * (j + 1) + seq[j + 1:], remaining, result)
                remaining += (i + 1) * self.coinage[j]


class Solution(object):
    def __init__(self):
        self.coinage = [1, 2, 5, 10]
        self.count = {}
        self.A = None

    def solve(self, cipher):
        """
        dp
        :param cipher: the cipher
        """
        target, self.A = cipher
        return self.get_count(target, 3)

    def get_count(self, n, k):
        """
        algorithm top-down dp
        bottom-up dp: https://github.com/derekhh/HackerRank/blob/master/coinage.cpp
        :param seq:
        :param n: target
        :param k: current examining coin
        """
        if (n, k) not in self.count:
            if k == 0:
                if n % self.coinage[k] == 0 and self.coinage[k] * self.A[k] >= n:
                    self.count[(n, k)] = 1
                else:
                    self.count[(n, k)] = 0
            else:
                i = 0
                cnt = 0
                while i <= self.A[k] and i * self.coinage[k] <= n:
                    cnt += self.get_count(n - i * self.coinage[k], k - 1)
                    i += 1
                self.count[(n, k)] = cnt

        return self.count[(n, k)]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        target = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(' '))
        cipher = target, lst
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
