"""
Problem Statement

Sorting is often useful as the first step in many different tasks. The most common task is to make finding things
easier, but there are other uses also.

Challenge
Given a list of unsorted numbers, can you find the numbers that have the smallest absolute difference between them? If
there are multiple pairs, find them all.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, A = cipher
        A.sort()

        diff = 1 << 31
        lst = []
        for i in xrange(N - 1):
            b = A[i + 1]
            a = A[i]
            if abs(a - b) < diff:
                diff = abs(a - b)
                lst = [a, b]
            elif abs(a - b) == diff:
                lst.append(a)
                lst.append(b)

        return " ".join(map(str, lst))


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
