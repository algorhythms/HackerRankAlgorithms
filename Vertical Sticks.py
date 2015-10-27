# -*- coding: utf-8 -*-
"""
Problem Statement

Given an array of integers Y=[y1,y2,…,yn], we have n line segments, such that, the endpoints of ith segment are (i,0)
and (i,yi). Imagine that from the top of each segment a horizontal ray is shot to the left, and this ray stops when it
touches another segment or it hits the y-axis. We construct an array of n integers, [v1,v2,…,vn], where vi is equal to
length of ray shot from the top of segment i. We define V(y1,y2,…,yn)=v1+v2+…+vn.

For example, if we have Y=[3,2,5,3,3,4,1,2], then v1,v2,…,v8=[1,1,3,1,1,3,1,2], as shown in the picture below:

For each permutation p of [1,2,…,n], we can calculate V(yp1,yp2,…,ypn). If we choose a uniformly random permutation p of
[1,2,…,n], what is the expected value of V(yp1,yp2,…,ypn)?
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        approach this problem by independently calculating the expected value of vi for each stick

        http://cs.stackexchange.com/questions/1076/how-to-approach-vertical-sticks-challenge
         Start with a round table with n seats and k people and seat them at random. Distances between individuals
         are obviously i.i.d. with mean n/k.
         Now straighten the table to line, k+1 lines (including the y-axis), and the virtual circle of the line is (n+1)

        Complexity: O(N^2)
        :param cipher: the cipher
        """
        N, A = cipher
        l = N + 1

        E = 0
        for cur in A:
            k = 0
            for a in A:
                if a >= cur:
                    k += 1  # including itself
            E += float(l) / (k + 1)
        return "%.2f" % E


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
