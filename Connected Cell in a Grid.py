# -*- coding: utf-8 -*-
"""
Problem Statement

You are given a matrix with m rows and n columns of cells, each of which contains either 1 or 0. Two cells are said to
be connected if they are adjacent to each other horizontally, vertically, or diagonally. The connected and filled (i.e.
cells that contain a 1) cells form a region. There may be several regions in the matrix. Find the number of cells in the
largest region in the matrix.
"""
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.max = -1
        self.cur_area = 0
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def solve(self, cipher):
        """
        dfs, O(mn)

        :param cipher: the cipher
        """
        m, n, mat = cipher
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and mat[i][j] == 1:
                    self.cur_area = 0
                    self.dfs(visited, mat, i, j, m, n)

        return self.max

    def dfs(self, visited, mat, i, j, m, n):
        visited[i][j] = True
        self.cur_area += 1
        self.max = max(self.max, self.cur_area)

        for dir in self.dirs:
            i1 = i + dir[0]
            j1 = j + dir[1]
            if 0 <= i1 < m and 0 <= j1 < n and not visited[i1][j1] and mat[i1][j1] == 1:
                self.dfs(visited, mat, i1, j1, m, n)


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    m = int(f.readline().strip())
    n = int(f.readline().strip())

    mat = []
    for i in xrange(m):
        mat.append(map(int, f.readline().strip().split(' ')))

    cipher = m, n, mat
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
