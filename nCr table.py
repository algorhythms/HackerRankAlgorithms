"""
Problem Statement

Jim is doing his discrete maths homework which requires him to repeatedly calculate nCr(n choose r) for different values
of n. Knowing that this is time consuming, he goes to his sister June for help. June, being a computer science student
knows how to convert this into a computer program and generate the answers quickly. She tells him, by storing the lower
values of nCr(n choose r), one can calculate the higher values using a very simple formula.

If you are June, how will you calculate nCr values for different values of n?

Input Format
The first line contains the number of test cases T.
T lines follow each containing an integer n.
"""
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def solve(self, n):
        """
        main solution function
        :param cipher: the cipher
        """
        result = []

        comb = 1  # 0!
        result.append(comb)
        for i in xrange(1, n + 1):
            comb = comb * (n + 1 - i) / i
            result.append(comb % MOD)

        return " ".join(map(str, result))


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
