"""
Problem Statement

In the Quicksort challenges, you sorted an entire array. Sometimes, you just need specific information about a list of
numbers, and doing a full sort would be unnecessary. Can you figure out a way to use your partition code to find the
median in an array?
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        partial quick sort
        :param cipher: the cipher
        """
        N, A = cipher
        if N % 2 == 1:
            return self.find_kth(A, 0, N - 1, (N - 1) / 2)
        else:
            raise IndexError

    def find_kth(self, A, i, j, k):
        """
        partial quick sort
        """
        p = self.partition(A, i, j)
        if p == k:
            return A[p]
        if p > k:
            return self.find_kth(A, i, p - 1, k)
        else:
            return self.find_kth(A, p + 1, j, k)

    def partition(self, A, i, j):
        if i > j:
            raise IndexError
        if i == j:
            return i

        p = i
        ptr_smaller = p
        for ptr in xrange(p + 1, j + 1):  # 1 for loop
            if A[ptr] < A[p]:
                ptr_smaller += 1
                A[ptr], A[ptr_smaller] = A[ptr_smaller], A[ptr]

        A[p], A[ptr_smaller] = A[ptr_smaller], A[p]
        return ptr_smaller


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    N = int(f.readline().strip())
    A = map(int, f.readline().strip().split(' '))
    cipher = N, A
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
