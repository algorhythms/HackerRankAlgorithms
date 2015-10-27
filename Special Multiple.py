"""
Problem Statement

You are given an integer N. Can you find the least positive integer X made up of only 9's and 0's, such that, X is a
multiple of N?

Update

X is made up of one or more occurences of 9 and zero or more occurences of 0.

Input Format
The first line contains an integer T which denotes the number of test cases. T lines follow.
Each line contains the integer N for which the solution has to be found.

Output Format
Print the answer X to STDOUT corresponding to each test case. The output should not contain any leading zeroes.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N = cipher

        x = 1
        while True:  # shortcut: while int(str(bin(x)[2:]))%N!=0
            binary = bin(x)[2:]
            nine_ary = str(binary).replace("1", "9")
            dec = int(nine_ary)
            if dec % N == 0:
                return dec
            x += 1


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
