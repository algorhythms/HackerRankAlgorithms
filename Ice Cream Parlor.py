# -*- coding: utf-8 -*-
"""
Sunny and Johnny together have M dollars and want to spend the amount at an ice cream parlour. The parlour offers N
flavors, and they want to choose 2 flavors so that they end up spending the whole amount.

You are given a list of cost of these N flavors. The cost of ith flavor is denoted by (ci). You have to display the
indices of two flavors whose sum is M.

Input Format

The first line of the input contains T, T test cases follow.
Each test case follows the format: The first line contains M. The second line contains N. The third line contains N
single space separated integers denoting the price of each flavor. Here, ith integer denotes ci.

Output Format

Output two integers, each of which is a valid index of the flavor. The lower index must be printed first. Indices are
indexed from 1 to N.

Constraints

1 ≤ T ≤ 50
2 ≤ M ≤ 10000
2 ≤ N ≤ 10000
1 ≤ ci ≤ 10000
The prices of two items may be same and each test case has a unique solution.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Two sum

        hash
        two pointers
        :param cipher: the cipher
        """
        M, N, C = cipher
        hash_map = {}
        for ind, val in enumerate(C):
            if val in hash_map:
                hash_map[val].append(ind)
            else:
                hash_map[val] = [ind]
        for ind, val in enumerate(C):
            target = M - val
            if target in hash_map:
                i = 0
                while i < len(hash_map[target]) and hash_map[target][i] <= ind:
                    i += 1
                if i != len(hash_map[target]):
                    return "%d %d" % (ind + 1, hash_map[target][i] + 1)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        M = int(f.readline().strip())
        N = int(f.readline().strip())
        C = map(int, f.readline().strip().split(' '))
        cipher = M, N, C
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
