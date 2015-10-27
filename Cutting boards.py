"""
lice gives a wooden board composed of M X N wooden square pieces to Bob and asks him to find the minimal cost of
breaking the board into square wooden pieces. Bob can cut the board along horizontal and vertical lines, and each cut
divides the board in smaller parts. Each cut has a cost depending on whether the cut is made along a horizontal or a
vertical line.

Let us denote the costs of cutting it along consecutive vertical lines with x1, x2, ..., xn-1, and the cost of cutting
it along horizontal lines with y1, y2, ..., ym-1. If a cut (of cost c) is made and it passes through n segments, then
total cost of this cut will be n*c.

The cost of cutting the whole board into single squares is the sum of the cost of successive cuts used to cut the whole
board into square wooden pieces of size 1x1. Bob should compute the minimal cost of breaking the whole wooden board into
squares of size 1x1.

Bob needs your help to find the minimal cost. Can you help Bob with this challenge?

Input Format
A single integer in the first line T, stating the number of test cases. T testcases follow.
For each test case, the first line contains two positive integers M and N separated by a single space. In the next line,
there are integers y1, y2, ..., ym-1, separated by spaces. Following them are integers x1, x2, ..., xn-1, separated by
spaces.
"""
MOD = 10 ** 9 + 7
__author__ = 'Danyang'


class Cost(object):
    def __init__(self):
        self.cost = 0

    def __iadd__(self, other):
        self.cost = (self.cost + other % MOD) % MOD
        return self


class Solution(object):
    def solve(self, cipher):
        """
        Greedy approach

        Fixed #6 - #11 Wrong Answer due to Cost class
        :param cipher: the cipher
        """
        M, N, Y, X = cipher

        y = list(Y)
        x = list(X)

        y.sort()
        x.sort()
        cost = Cost()
        while x and y:
            x_max = x[-1]
            y_max = y[-1]
            if x_max > y_max:
                cost += x.pop() * (M - len(y))
            elif y_max > x_max:
                cost += y.pop() * (N - len(x))
            else:
                if sum(x) > sum(y):
                    cost += x.pop() * (M - len(y))
                else:
                    cost += y.pop() * (N - len(x))
        while x:
            cost += x.pop() * (M - len(y))
        while y:
            cost += y.pop() * (N - len(x))
        return cost.cost


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        M, N = map(int, f.readline().strip().split(" "))
        Y = map(int, f.readline().strip().split(" "))
        X = map(int, f.readline().strip().split(" "))
        cipher = [M, N, Y, X]
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
