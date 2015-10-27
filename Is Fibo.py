"""
You are given an integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.

The first few elements of fibonacci sequence are 0,1,1,2,3,5,8,13.... A fibonacci sequence is one where every element is
 a sum of the previous two elements in the sequence. The first two elements are 0 and 1.

Formally:

fib0 = 0
fib1 = 1
fibn = fibn-1 + fibn-2 \forall n > 1

Input Format
The first line contains T, number of test cases.
T lines follows. Each line contains an integer N.
"""
__author__ = 'Danyang'
fib = lambda n: reduce(lambda x, n: [x[1], x[0] + x[1]], xrange(n), [0, 1])[0]


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        num = int(cipher)
        n = 0
        while fib(n) < num:
            n += 1
        if fib(n) == num:
            return "IsFibo"
        else:
            return "IsNotFibo"


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
