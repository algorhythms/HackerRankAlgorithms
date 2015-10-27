"""
Given two strings of length n, P = p1p2...pn and Q = q1q2...qn, we define M(i,j,k) as the number of mismatches between
 p(i), p(i+1), ...p(i+k-1) and q(j), q(j+1)...,q(j+k-1). That is in set notation, M(i,j,k) refers to the size of the set

{0 <= x < k, p[i+x]| != q[j+x]}
Given an integer S, your task is to find the maximum length L, such that, there exists pair of indices (i,j) for which
we have M(i, j, L) <= S. Of course, we should also have i+L-1 <=n and j+L-1 <=n.

Input

The first line of input contains a single integer, T (1 <= T <= 10). T test cases follow.
Each test case consists of an integer, S, and two strings P and Q separated by a single space.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm 0: brutal force
        O(n^3)

        Algorithm 1: dp

        dp[i][j] is L that make the substring diff <= S

        Diagonal relationship:
        dp[i+1][j+1] = dp[i][j] if p[i]==q[i] else dp[i][j]+scan until next difference  # but not O(1)

        dp[i][j] = dp[i+1][j+1] if p[i]==q[i] else shrink  # but not O(1)

        Algorithm 2: sliding window, shrink and expand  # O(1), you do not need the exact intermediate results
        :param cipher: the cipher
        """
        S, p, q = cipher
        n = len(p)
        S = int(S)
        global_max = 0
        for i in xrange(n):  # only need to consider diagonal since scanned by diagonal line
            global_max = max(global_max, self.get_longest(S, p, q, i, 0), self.get_longest(S, p, q, 0, i))

        return global_max

    def get_longest(self, S, p, q, i, j):
        start_i = i
        start_j = j
        local_max = 0
        n = len(p)
        cur_diff = 0
        while i < n and j < n:
            if p[i] != q[j]:
                cur_diff += 1

            if cur_diff > S:  # then shrink the left side of window
                while p[start_i] == q[start_j]:
                    start_i += 1
                    start_j += 1
                start_i += 1
                start_j += 1
                cur_diff -= 1

            local_max = max(local_max, i - start_i + 1)

            i += 1
            j += 1

        return local_max


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
