"""
Problem Statement
You are given a number N, you need to print the number of positions where digits exactly divides N.

Input format

The first line contains T (number of test cases followed by T lines each containing N).
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        num = int(cipher)
        cnt = 0
        for char in cipher:
            digit = int(char)
            if digit == 0: continue
            if num % digit == 0:
                cnt += 1

        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
