"""
Problem Statement

Manasa was sulking her way through a boring class when suddenly her teacher singled her out and asked her a question.
He gave her a number n and Manasa has to come up with the smallest number m which contains atleast n number of zeros at
the end of m!. Help Manasa come out of the sticky situation.

Input Format
The first line contains an integer T i.e. the number of Test cases.
Next T lines will contain an integer n.
"""
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        import math

        MAX_MULT = int(math.log(10 ** 16) / math.log(5)) + 1
        self.M = [(i, (5 ** i - 1) / 4) for i in reversed(xrange(1, MAX_MULT + 1))]

    def solve_TLE(self, cipher):
        """
        10 = 2*5
        count 5 and count 2
        count 5 since more 2's than 5's
        :param cipher: the cipher
        """
        cnt = 0
        m = 0
        while True:
            if cnt >= cipher:
                break
            else:
                m2 = m
                while m2 != 0 and m2 % 5 == 0:
                    cnt += 1
                    m2 /= 5
                m += 5

        m -= 5
        return m

    def solve_math(self, cipher):
        """
        fastest
        """
        n = cipher
        m = 0
        for i, p in self.M:
            if p <= n:
                cnt = n / p
                n -= cnt * p
                m += cnt * 5 ** i
        return m

    def solve(self, n):
        """
        binary search
        """
        l = 0
        h = 5 * n
        while l <= h:
            mid = (l + h) / 2
            cnt = self.prime_count(5, mid)
            if cnt < n:
                l = mid + 1
            else:
                h = mid - 1
        return l

    def prime_count(self, p, n):
        """
        count number of p in n!'s factors, where p is a prime number

        complexity O(lg n)
        """
        if n < p:
            return 0

        return n / p + self.prime_count(p, n / p)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())
    solution = Solution()
    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
