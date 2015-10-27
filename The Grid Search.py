"""
Problem Statement

Given a 2D array of digits, try to find the location of a given 2D pattern of digits within it. For example, consider
the following 2D matrix.

1234567890
0987654321
1111111111
1111111111
2222222222
If we need to look for the following 2D pattern within it:

876543
111111
111111
If we scan through the original array, we observe, that 2D pattern begins from the second row and the third column of
the larger grid (the 8 in the second row and third column of the larger grid, is the top-left corner of the pattern we
are searching for).

So, a 2D pattern of digits P is said to be present in a larger grid G, if the latter contains a contiguous, rectangular
2D grid of digits matching with the pattern P; similar to the example shown above.

Input Format
The first line contains an integer T, which is the number of tests. T tests follow and the structure of each test is
described below:
The first line contains 2 space separated integers R and C indicating the number of rows and columns in the grid G.
This is followed by R lines, each with a string of C digits each; which represent the grid G.
The second line contains 2 tab separated integers r and c indicating the number of rows and columns in the pattern grid
P.
This is followed by r lines, each with a string of c digits each; which represent the pattern P.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        pre-check pruning

        Typical technique in Matrix (Grid)
        dp[i][j] is the sum of the rect from (0, 0) to (i-1, j-1)

        then them sum of the rect from (a, b) to (i, j) can be calculated
        :param cipher: the cipher
        """
        matrix, pattern = cipher

        R1, C1 = len(matrix), len(matrix[0])
        R2, C2 = len(pattern), len(pattern[0])

        dp = [[0 for _ in xrange(C1 + 1)] for _ in xrange(R1 + 1)]  # note the dummies

        for i in xrange(1, R1 + 1):
            for j in xrange(1, C1 + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]

        pattern_sum = sum([sum(pattern[i]) for i in xrange(R2)])

        for i in xrange(R1 - R2 + 1):
            for j in xrange(C1 - C2 + 1):
                # bottom = i+R2+1 # bugs
                # left = j+C2+1
                bottom = i + R2
                left = j + C2
                candidate_sum = dp[bottom][left] - dp[bottom][j] - dp[i][left] + dp[i][j]

                if candidate_sum == pattern_sum:
                    matched = True
                    for a in xrange(R2):
                        for b in xrange(C2):
                            if matrix[i + a][j + b] != pattern[a][b]:
                                matched = False
                                break
                        if not matched:
                            break
                    if matched:
                        return "YES"
        return "NO"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        matrix = []
        pattern = []
        R, C = map(int, f.readline().strip().split(' '))
        for i in xrange(R):
            matrix.append(map(int, list(f.readline().strip())))
        R, C = map(int, f.readline().strip().split(' '))
        for i in xrange(R):
            pattern.append(map(int, list(f.readline().strip())))

        cipher = matrix, pattern
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
