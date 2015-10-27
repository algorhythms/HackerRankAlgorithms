"""
Problem Statement

You are given a tree (a simple connected graph with no cycles). You have to remove as many edges from the tree as
possible to obtain a forest with the condition that : Each connected component of the forest should contain an even
number of vertices.
"""
__author__ = 'Danyang'


class Solution(object):
    def __init__(self, N, M):
        self.f = [0 for _ in xrange(N + 1)]  # store the number of nodes of a subtree rooted at i
        self.V = [[] for _ in xrange(N + 1)]  # 0 is dummy
        self.E = []

    def solve(self, cipher):
        """
        count the number of subtree with even size
        if a subtree is even, it can be detached from else and maintain the else's even odd Parity

        :param cipher: the cipher
        """
        N, M, E = cipher
        for e in E:
            u, v = e
            self.E.append([u, v])
            self.V[u].append(v)
            self.V[v].append(u)

        self.get_sum(1, 0)

        result = 0
        for i in xrange(2, N + 1):  # excluding root
            if self.f[i] % 2 == 0:
                result += 1
        return result

    def get_sum(self, cur, pi):
        """
        reduce graph to tree
        dp (graph is mostly top-down dp)
        dfs
        """
        if self.f[cur] == 0:
            for nigh in self.V[cur]:
                if nigh != pi:
                    self.f[cur] += self.get_sum(nigh, cur)  # child

            self.f[cur] += 1  # itself

        return self.f[cur]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, M = map(int, f.readline().strip().split(' '))
    solution = Solution(N, M)
    E = []
    for t in xrange(M):
        # construct cipher
        E.append(map(int, f.readline().strip().split(' ')))

    # solve
    cipher = N, M, E
    s = "%s\n" % (solution.solve(cipher))
    print s,
