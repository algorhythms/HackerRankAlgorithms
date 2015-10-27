"""
Given two strings a and b of equal length, what's the longest string (S) that can be constructed such that S is a child
of both a and b.

A string x is said to be a child of a string y, if x can be formed by deleting 0 or more characters from y

Input format

Two strings a and b with a newline separating them
"""
__author__ = 'Danyang'


class Solution(object):
    def solve_error(self, cipher):
        """
        dp

        error transition:
        dp[i][j] = dp[i-1][j] + 1 if a[i]==b[j]
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if a[i]!=b[j]
        :param cipher: the cipher
        """
        a, b = cipher
        m = len(a)
        n = len(b)
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  # superset
        return dp[-1][-1]

    def solve(self, cipher):
        """
        dp

        dp longest common sequence
        dp[i][j] = dp[i-1][j-1] + 1 if a[i]==b[j]
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if a[i]!=b[j]
        :param cipher: the cipher
        """
        a, b = cipher
        m = len(a)
        n = len(b)
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  # superset
        return dp[-1][-1]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    cipher = []
    cipher.append(f.readline().strip())
    cipher.append(f.readline().strip())

    s = "%s\n" % (Solution().solve(cipher))
    print s,
