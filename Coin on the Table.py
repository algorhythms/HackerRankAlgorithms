# -*- coding: utf-8 -*-
"""
Problem Statement

You have a rectangular board consisting of N rows, numbered from 1 to N, and M columns, numbered from 1 to M. The top
left is (1,1) and the bottom right is (N,M). Initially - at time 0 - there is a coin on the top-left cell of your board.
Each cell of your board contains one of these letters:

When the coin reaches a cell that has letter '*', it will stay there permanently. When you punch on your board, your
timer starts and the coin moves between cells. Before starting the game, you can make operations to change the board,
such that you are sure that at or before time K the coin will reach the cell having letter '*'. In each operation you
can select a cell with some letter other than '*' and change the letter to 'U', 'L', 'R' or 'D'. You need to carry out
as few operations as possible in order to achieve your goal. Your task is to find the minimum number of operations.
"""
import sys

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.dirs = [(0, 1, 'L'), (0, -1, 'R'), (-1, 0, 'D'), (1, 0, 'U')]

    def solve(self, cipher):
        """
        DP
        f number of operations at point (i, j) BEFORE OR AT time k

        f[k][i][j] = f[k-1][i-1][j]+1 if mat[i-1][j]!='D' else f[k-1][i-1][j]
        f[k][i][j] is taking the min from all directions
        :param cipher: the cipher
        """
        M, N, K, mat = cipher
        i_dest = -1
        j_dest = -1
        for i in xrange(M):
            for j in xrange(N):
                if mat[i][j] == "*":
                    i_dest = i
                    j_dest = j
                    break

        f = [[[sys.maxint for _ in xrange(N)] for _ in xrange(M)] for _ in xrange(K + 1)]
        for k in xrange(K + 1):  # you need zero ops to be at the origin BEFORE time k
            f[k][0][0] = 0

        for k in xrange(1, K + 1):  # when k=0, at origin
            for i in xrange(0, M):
                for j in xrange(0, N):
                    for dir in self.dirs:
                        i_pre = i + dir[0]
                        j_pre = j + dir[1]
                        if 0 <= i_pre < M and 0 <= j_pre < N:
                            if mat[i_pre][j_pre] == dir[2]:
                                f[k][i][j] = min(f[k][i][j], f[k - 1][i_pre][j_pre])
                            else:
                                f[k][i][j] = min(f[k][i][j], f[k - 1][i_pre][j_pre] + 1)

        mini = sys.maxint
        for k in xrange(K + 1):
            mini = min(mini, f[k][i_dest][j_dest])
        return mini if mini != sys.maxint else -1


if __name__ == "__main__":
    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    M, N, K = map(int, f.readline().strip().split(' '))
    mat = []
    for i in xrange(M):
        mat.append(list(f.readline().strip()))

    cipher = M, N, K, mat
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
