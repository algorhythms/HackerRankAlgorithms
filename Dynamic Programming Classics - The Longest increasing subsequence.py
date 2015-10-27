"""
Problem Statement

An Introduction to the Longest Increasing Subsequence Problems

The task is to find the length of the longest subsequence in a given array of integers such that all elements of the
subsequence are sorted in ascending order. For example, the length of the LIS for { 15, 27, 14, 38, 26, 55, 46, 65, 85 }
is 6 and the longest increasing subsequence is {15, 27, 38, 55, 65, 85}.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        LIS

        brute force is O(n^3)
        reduced to O(n^2)

        let f[i] denote the LIS ended with A[i]
        f[i] = max(f[j]+1 for j<i and A[j]<A[i])
        :param cipher: the cipher
        """
        N, A = cipher
        maxa = 1
        f = [1 for _ in xrange(N)]
        for i in xrange(1, N):
            for j in xrange(i):
                if A[i] > A[j]:
                    f[i] = max(f[i], f[j] + 1)
            maxa = max(maxa, f[i])
        return maxa


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    N = int(f.readline().strip())

    A = []
    for _ in xrange(N):
        A.append(int(f.readline().strip()))
    cipher = N, A
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
