"""
Problem Statement

Jim enters a candy shop which has N different types of candies, each candy is of the same price. Jim has enough money to
buy K candies. In how many different ways can he purchase K candies if there are infinite candies of each kind?
"""
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        """
        \binom nk=\binom{n-1}{k-1}+\binom{n-1}k, \text{ for } 0<k<n,
        """
        self.C = [[1 for _ in xrange(2000)] for _ in xrange(2000)]
        for n in xrange(1, 2000):
            for k in xrange(1, n):  # 0<k<n
                self.C[n][k] = self.C[n - 1][k - 1] + self.C[n - 1][k]

    def solve(self, cipher):
        """
        Abstract: N types, K holes, repeatable
        nCk when items are duplicated

        reference:
        dp algorithm: https://github.com/derekhh/HackerRank/blob/master/k-candy-store.cpp

        :param cipher: the cipher
        """
        N, K = cipher
        return self.C[N + K - 1][K] % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())
    solution = Solution()
    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        K = int(f.readline().strip())
        cipher = N, K
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
