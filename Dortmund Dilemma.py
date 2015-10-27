"""
Borussia Dortmund are a famous football (soccer) club from Germany. Apart from their fast-paced style of playing, the
thing that makes them unique is the hard to pronounce names of their players.

The team's coach is your friend. He is in a dilemma as he can't decide how to make it easier to call the players by
name, during practice sessions. So, you advise him to assign easy names to his players. A name is easy to him if

1. It consists of only one word.
2. It consists of only lowercase english letters.
3. It's length is exactly N.
4. It contains exactly K different letters from the 26 letters of English alphabet.
5. At least one of its proper prefixes matches with its proper suffix of same length.

Given, N and K you have to tell him the number of easy names he can choose from modulo (109+9).

Note : A prefix P of a name W is proper if, P!=W. Similarly, a suffix S of a name W is proper if, S!=W.

Input Format
The first line of the input will contain T ( the number of testcases). Each of the next T lines will contain 2 space
separated integers N and K.
"""
__author__ = 'Danyang'
MOD = 10 ** 9 + 9


class Solution(object):
    def __init__(self):
        self.factorials = [0 for _ in xrange(26 + 1)]
        self.factorials[0] = 1
        for i in xrange(1, 26 + 1):
            self.factorials[i] = self.factorials[i - 1] * i


        # cached, rather than calculated eveytime
        N = 10 ** 5
        K = 26

        self.F = [[0 for _ in xrange(K + 1)] for _ in xrange(N + 1)]
        # starting from 1
        for j in xrange(1, K + 1):
            self.F[1][j] = j
            for i in xrange(2, N + 1):
                if i & 1 == 0:
                    self.F[i][j] = (self.F[i - 1][j] * j - self.F[i / 2][j])
                else:
                    self.F[i][j] = (self.F[i - 1][j] * j)
                self.F[i][j] %= MOD

        self.G = [[0 for _ in xrange(K + 1)] for _ in xrange(N + 1)]

        for j in xrange(1, K + 1):
            total = j
            for i in xrange(1, N + 1):
                self.G[i][j] = total - self.F[i][j]  # rather than using j**i
                self.G[i][j] %= MOD

                total *= j
                total %= MOD  # otherwise time out

    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, K = cipher

        P = 0
        if K == 1:
            P += self.G[N][K]
        else:
            for j in xrange(K, 0, -1):
                # P = self.G[N][K]
                # P -= G[j] * (self.factorials[K]/(self.factorials[j]*self.factorials[K-j]))
                # PIE: Principle of Inclusion-Exclusion
                P += (-1) ** (K - j) * self.G[N][j] * (
                    self.factorials[K] / (self.factorials[j] * self.factorials[K - j]))
                P %= MOD

        result = P * (self.factorials[26] / (self.factorials[K] * self.factorials[26 - K]))
        return result % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())
    solution = Solution()
    for t in xrange(testcases):
        # construct cipher
        cipher = map(lambda x: int(x), f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
