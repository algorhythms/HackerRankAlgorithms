"""
A clique in a graph is set of nodes such that there is an edge between any two distinct nodes in the set. It is well
known that finding the largest clique in a graph is a computationally tough problem and no polynomial time algorithm
exists for it. However, you wonder what is the minimum size of the largest clique in any graph with N nodes and M edges.

Input Format
The first line contains T the number of test cases. Each of the next T lines contain 2 integers : N, M
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Turan's Graph:

        :param cipher: the cipher
        """
        N, M = cipher
        # K_{r+1} free
        # r = 2
        # edge_cnt = 0
        # while edge_cnt<M:
        # edge_cnt = self.Turan(N, r)
        #     r += 1
        #
        # return r-1


        # binary search
        # T(n, r) <= M
        # T(n, r+1) >M
        low = 0
        high = N
        while low + 1 < high:
            mid = (low + high) / 2
            r = self.Turan(N, mid)

            if r < M:
                low = mid
            else:
                high = mid
        return high

    def Turan(self, n, r):
        """
        http://en.wikipedia.org/wiki/Tur%C3%A1n_graph
        """
        return 0.5 * (n ** 2 - (n % r) * (n / r + 1) ** 2 - (r - (n % r)) * (n / r) ** 2)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
