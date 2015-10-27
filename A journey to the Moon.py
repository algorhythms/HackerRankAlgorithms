"""
Problem Statement

The member states of the UN are planning to send 2 people to the Moon. But there is a problem. In line with their
principles of global unity, they want to pair astronauts of 2 different countries.

There are N trained astronauts numbered from 0 to N-1. But those in charge of the mission did not receive information
about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts
belong to the same country.
"""
__author__ = 'Danyang'


class DisjointSet(object):
    def __init__(self, n):
        self.rank = [1 for _ in xrange(n)]
        self.parent = [i for i in xrange(n)]
        self.n = n

    def find(self, i):
        if i == self.parent[i]:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])  # directly point to ancestor
            return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)

        if x == y: return
        self.parent[x] = y
        self.rank[y] += self.rank[x]

    def card(self):
        card = 0
        for i in xrange(self.n):
            if self.parent[i] == i:
                card += 1
        return card


class Solution(object):
    def solve(self, cipher):
        """
        Disjoint-set data structure

        Union-Find Algorithm
        :param cipher: the cipher
        """
        N, pairs = cipher
        djs = DisjointSet(N)
        for a, b in pairs:
            djs.union(a, b)

        result = 0
        for i in xrange(N):
            if djs.find(i) == i:  # set representative
                # result += (djs.rank[i])*(N-djs.rank[i])/2  # otherwise rounding error
                result += (djs.rank[i]) * (N - djs.rank[i])
        return result / 2


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()

    N, I = map(int, f.readline().strip().split(' '))

    pairs = []
    for i in xrange(I):
        pairs.append(map(int, f.readline().strip().split(' ')))

    cipher = N, pairs
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
