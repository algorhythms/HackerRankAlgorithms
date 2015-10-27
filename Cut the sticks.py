"""
Problem Statement

You are given N sticks, where each stick is of positive integral length. A cut operation is performed on the sticks such
that all of them are reduced by the length of the smallest stick.

Suppose we have 6 sticks of length
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

        result = []
        while A:
            result.append(len(A))
            A = map(lambda x: x - A[0], A)
            A = filter(lambda x: x > 0, A)

        return "\n".join(map(str, result))


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
