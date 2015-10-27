"""
Problem Statement

Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the
values thus obtained. Can you help her in this task?

Note : [1,2,3] is contiguous subarray of [1,2,3,4] while [1,2,4] is not.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        consider array 1, 2, 3, 4, 5, 6, 7
        consider 3, number of appearance time in consecutive subset: 1+2+3+3+3+2+1 = 3*(7-(3-1))
        consider 4: 1+2+3+4+3+2+1 = 4*(7-(4-1))
        consider 6: 1+2+2+2+2+2+1 = (7-(6-1))*6

        consider i: 1+2+..i+...+1 = i*(l-(i-1))

        if start from 0:
        (i+1)*(N-i)
        :param cipher: the cipher
        """
        N, A = cipher
        ret = 0
        for i, val in enumerate(A):
            if (i + 1) * (N - i) % 2 == 1:
                ret ^= val
        return ret


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())
    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))

        cipher = N, A
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
