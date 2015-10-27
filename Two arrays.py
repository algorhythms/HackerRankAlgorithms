"""
ou are given two integer arrays, A and B, each containing N integers. The size of the array is less than or equal to
1000. You are free to permute the order of the elements in the arrays.

Now here's the real question: Is there an permutation A', B' possible of A and B, such that, A'i+B'i >= K for all i,
where A'i denotes the ith element in the array A' and B'i denotes ith element in the array B'.


Input Format
The first line contains an integer, T, the number of test-cases. T test cases follow. Each test case has the following
format:

The first line contains two integers, N and K. The second line contains N space separated integers, denoting array A.
The third line describes array B in a same format.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, K, A, B = cipher
        A.sort()
        B.sort(reverse=True)  # dynamic typed, then cannot detect list()
        for i in xrange(N):
            if not A[i] + B[i] >= K:
                return "NO"
        return "YES"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N, K = map(int, f.readline().strip().split(" "))
        A = map(int, f.readline().strip().split(' '))
        B = map(int, f.readline().strip().split(' '))
        cipher = N, K, A, B
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
