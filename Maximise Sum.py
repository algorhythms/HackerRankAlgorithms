# -*- coding: utf-8 -*-
"""
Maximal Sum of Subarray Taking Modulo

Problem Statement

You are given an array of size N and another integer M. Your target is to find the maximum value of sum of subarray modulo M.

Subarray is a continous subset of array elements.

Note that we need to find the maximum value of (Sum of Subarray)%M , where there are N∗(N+1)/2 possible subarrays.

Input Format 
First line contains T , number of test cases to follow. Each test case consists of exactly 2 lines. First line of each 
test case contain 2 space separated integers N and M, size of the array and modulo value M. 
Second line contains N space separated integers representing the elements of the array.

Output Format 
For every test case output the maximum value asked above in a newline.

Constraints 
2 ≤ N ≤ 105 
1 ≤ M ≤ 1014 
1 ≤ elements of the array ≤ 1018 
2 ≤ Sum of N over all test cases ≤ 500000

Sample Input

1
5 7
3 3 9 9 5
Sample Output

6
Explanation

Max Possible Sum taking Modulo 7 is 6 , and we can get 6 by adding first and second element of the array
"""
import bisect

__author__ = 'Daniel'


class Solution(object):
    def solve(self, cipher):
        """
        Brute force: O(N^2)

        sum dp with bisect O(n lg n)
        :param cipher: the cipher
        """
        N, M, A = cipher

        F = []
        s = 0
        maxa = 0
        for a in A:
            s += a
            s %= M
            idx = bisect.bisect_left(F, s)
            F.insert(idx, s)  # BST

            # bisect previous
            idx = min(bisect.bisect_right(F, (s+1)%M), len(F)-1)
            maxa = max(maxa, (s-F[idx])%M, (s-F[idx-1])%M, s%M)

        return maxa

    def solve_brute(self, cipher):
        """TLE"""
        N, M, A = cipher
        F = [0]
        s = 0
        for a in A:
            s = (s+a) % M
            F.append(s)

        maxa = 0
        for i in xrange(1, len(A)+1):
            for j in xrange(i):
                maxa = max(maxa, F[i], (F[i]-F[j])%M)

        return maxa

if __name__ == "__main__":
    import sys
    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N, M = map(int, f.readline().strip().split(' '))
        A = map(int, f.readline().strip().split(' '))
        cipher = N, M, A
        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,