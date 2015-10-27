"""
You are given a list of size N, initialized with zeroes. You have to perform M queries on the list and output the
maximum of final values of all the N elements in the list. For every query, you are given three integers a, b and k and
you have to add value k to all the elements ranging from index a to b(both inclusive).

Input Format
First line will contain two integers N and M separated by a single space.
Next M lines will contain three integers a, b and k separated by a single space.
Numbers in list are numbered from 1 to N.

Output Format
A single line containing maximum value in the final list.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Array, Math, Range
        Range & Complementary Range

        [i , j] plus k == [i, +\infty] plus k with [j+1, +\infty] subtract k

        :param cipher: the cipher
        """
        N, M, queries = cipher

        qry = []
        for query in queries:
            qry.append((query[0], query[2]))
            qry.append((query[1] + 1, -query[2]))

        qry.sort(key=lambda x: (x[0], x[1]))
        # qry.sort(key=lambda x: x[1]) # secondary attribute

        maxa = -1 << 32
        cur = 0
        for q in qry:
            cur += q[1]
            maxa = max(maxa, cur)

        return maxa


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, M = map(int, f.readline().strip().split(' '))

    queries = []
    for t in xrange(M):
        # construct cipher
        queries.append(map(int, f.readline().strip().split(' ')))

    cipher = N, M, queries
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
