# -*- coding: utf-8 -*-
"""
Problem Statement

Shashank loves to play with arrays a lot. Today, he has an array A consisting of N positive integers. At first, Shashank
listed all the subarrays of his array A on a paper and later replaced all the subarrays on the paper with the maximum
element present in the respective subarray.

For eg: Let us consider the following array A consisting of three elements.

A = {1,2,3}

List of Subarrays:
{1}
{2}
{3}
{1,2}
{2,3}
{1,2,3}

Final List:
{1}
{2}
{3}
{2}
{3}
{3}

Now, Shashank wondered how many numbers in the list are greater than K.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        total number of sub-arrays: N+(N-1)*(N-2)+...+1 = N(N+1)/2

        divide the array into the elements less than or equal K (call S) and large than K (call L)
        we know the total number of sub-arrays, subtract the sub-arrays ONLY consists of S, and the result will be
        sub-arrays with maximum elements in L.

        :param cipher: the cipher
        """
        N, K, A = cipher
        total = N * (N + 1) / 2
        total_only_s = 0
        i = 0
        while i < N:
            if A[i] > K:
                i += 1
            else:
                j = i + 1
                while j < N and A[j] <= K: j += 1
                l = j - i
                total_only_s += l * (l + 1) / 2

                i = j

        return total - total_only_s


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N, K = map(int, f.readline().strip().split(' '))
        A = map(int, f.readline().strip().split(' '))
        cipher = N, K, A
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
