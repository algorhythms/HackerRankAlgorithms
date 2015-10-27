# -*- coding: utf-8 -*-
"""
Red John has committed another murder. But this time, he doesn't leave a red smiley behind. What he leaves behind is a
puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in.
The puzzle begins as follows.

There is a wall of size 4xN in the victim's house. The victim also has an infinite supply of bricks of size 4x1 and 1x4
in her house. There is a hidden safe which can only be opened by a particular configuration of bricks in the wall. In
every configuration, the wall has to be completely covered using the bricks. There is a phone number written on a note
in the safe which is of utmost importance in the murder case. Gale Bertram wants to know the total number of ways in
which the bricks can be arranged on the wall so that a new configuration arises every time. He calls it M. Since Red
John is back after a long time, he has also gained a masters degree in Mathematics from a reputed university. So, he
wants Patrick to calculate the number of prime numbers (say P) up to M (i.e. <= M). If Patrick calculates P, Teresa
should call Red John on the phone number from the safe and he will surrender if Patrick tells him the correct answer.
Otherwise, Teresa will get another murder call after a week.

You are required to help Patrick correctly solve the puzzle.
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        F(n) = F(n-4)+F(n-1)

        F(0) = 0
        F(1..3) = 1
        F(4) = 2

        :param cipher: the cipher
        """
        return self.sum_prime(self.get_configs(cipher))

    def get_configs(self, N):
        if N < 4:
            return 1

        F = [0 for _ in xrange(N + 1)]
        for i in xrange(1, 4):
            F[i] = 1
        F[4] = 2

        for i in xrange(5, N + 1):
            F[i] = F[i - 4] + F[i - 1]

        return F[N]

    def prime(self, n):
        """
        is_prime[2*j::j] = 0
        Sieve of Eratosthenes
        """
        is_prime = [1 for _ in xrange(n + 1)]
        for i in xrange(2):
            is_prime[i] = 0

        n_max = int(math.sqrt(len(is_prime)))
        for i in xrange(2, n_max + 1):
            for j in xrange(2 * i, len(is_prime), i):
                is_prime[j] = 0

        return sum(is_prime)

    def sum_prime(self, n):
        """
        HackerRank does not support numpy
        Sieve of Eratosthenes
        """
        import numpy as np

        is_prime = np.ones((n + 1,), dtype=bool)
        is_prime[:2] = 0
        N_max = int(np.sqrt(len(is_prime)))  # just to speed up
        for j in xrange(2, N_max):
            is_prime[2 * j::j] = False  # not start from j, since don't clean j itself
        return np.sum(is_prime)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
