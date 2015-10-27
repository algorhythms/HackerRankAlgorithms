"""
Problem Statement

How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need
to efficiently compute the answer.
"""
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.combs = {}

    def solve(self, cipher):
        """
        Similar to Coinage with limited supply of coins

        :param cipher: the cipher
        """
        C, N = cipher
        return self.get_combinations(N, C, 0)

    # memoize
    def get_combinations(self, t, lst, k):
        if t == 0:
            return 1

        if t < 0 or k >= len(lst):
            return 0

        if (t, k) not in self.combs:
            cnt = 0
            while t >= 0:
                cnt += self.get_combinations(t, lst, k + 1)
                t -= lst[k]
            self.combs[(t, k)] = cnt

        return self.combs[(t, k)]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    C = map(int, f.readline().strip().split(', '))
    N = int(f.readline().strip())
    cipher = C, N
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
