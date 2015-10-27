# -*- coding: utf-8 -*-
"""
You are given a hexagonal grid of size 2xN. Your task is to construct the grid with 2x1 dominoes. The dominoes can be
arranged in any of the three orientations shown below. To add to the woes, certain cells of the hexogonal grid are
blackened i.e., no domino can occupy that cell. Can you construct such a hexagonal grid?
"""
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.delta = [(0, 1), (1, 0), (1, -1)]  # dominoes delta, coordinate: x downward, y rightward,
        # need consistent directions

    def solve(self, cipher):
        """
        recursive solution, brute force, starting from top left
        :param cipher: the cipher
        """
        ret = self.rec(cipher)
        if ret:
            return "YES"
        else:
            return "NO"

    def rec(self, grid):
        changed = False
        m = len(grid)
        n = len(grid[0])

        for i in xrange(m):
            for j in xrange(n):
                if not changed:  # control the start from top, left
                    if grid[i][j] == 0:
                        changed = True
                        grid[i][j] = 1
                        for d in self.delta:
                            i2 = i + d[0]
                            j2 = j + d[1]
                            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                                grid[i2][j2] = 1
                                if self.rec(grid):
                                    return True
                                grid[i2][j2] = 0
                        grid[i][j] = 0
        if not changed:
            return True


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())
    for t in xrange(testcases):
        # construct cipher
        int(f.readline().strip())
        cipher = []
        for _ in xrange(2):
            cipher.append(map(int, list(f.readline().strip())))

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
