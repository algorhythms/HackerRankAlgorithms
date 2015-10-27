"""
Problem Statement

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the
order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length,
which is common to both the sequences.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        dp
        f[i][j] = f[i-1][j-1]+1
        f[i][j] = max(f[i-1][j], f[i][j-1])
        :param cipher: the cipher
        """
        m, n, A, B = cipher
        f = [["" for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    # f[i][j] = f[i-1][j-1]+A[i-1]  # otherwise cannot insert space
                    f[i][j] = f[i - 1][j - 1] + " " + A[i - 1]
                else:
                    if len(f[i - 1][j]) > len(f[i][j - 1]):
                        f[i][j] = f[i - 1][j]
                    else:
                        f[i][j] = f[i][j - 1]
        return f[m][n].strip()


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    m, n = map(int, f.readline().strip().split(' '))
    A = f.readline().strip().split(' ')
    B = f.readline().strip().split(' ')
    cipher = m, n, A, B
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
