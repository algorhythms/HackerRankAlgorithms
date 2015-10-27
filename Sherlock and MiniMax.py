# -*- coding: utf-8 -*-
"""
Watson gives Sherlock an array A1,A2...AN.
He asks him to find an integer M between P and Q(both inclusive), such that, min {|Ai-M|, 1 ≤ i ≤ N} is maximised. If
there are multiple solutions, print the smallest one.

Input Format
The first line contains N. The next line contains space separated N integers, and denote the array A. The third line
contains two space separated integers denoting P and Q.

Output Format
In one line, print the required answer.

Constraints
1 ≤ N ≤ 102
1 ≤ Ai ≤ 109
1 ≤ P ≤ Q ≤ 109

Sample Input

3
5 8 14
4 9

5
12 10 50 24 40
9 16
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        A, P, Q = cipher
        A.sort()

        gmax = -1 << 32
        M = -1
        if P <= A[0] and gmax < A[0] - P:
            gmax = A[0] - P
            M = P
        if Q >= A[-1] and gmax < Q - A[-1]:
            gmax = Q - A[-1]
            M = Q

        for i in xrange(1, len(A)):
            max_cnd = (A[i] - A[i - 1]) / 2  # max_candidate
            if gmax < max_cnd:
                M_cnd = (A[i] + A[i - 1]) / 2
                if P <= M_cnd <= Q:
                    gmax = max_cnd
                    M = M_cnd

                else:  # fall in the middle
                    if M_cnd > Q and A[i - 1] <= Q <= A[i]:
                        max_cnd = min(abs(A[i] - Q), abs(A[i - 1] - Q))
                        if gmax < max_cnd:
                            gmax = max_cnd
                            M = Q
                    if M_cnd < P and A[i - 1] <= P <= A[i]:
                        max_cnd = min(abs(A[i] - P), abs(A[i - 1] - P))
                        if gmax < max_cnd:
                            gmax = max_cnd
                            M = P
        return M


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())


    # construct cipher
    lst = map(int, f.readline().strip().split(" "))
    P, Q = map(int, f.readline().strip().split(" "))
    cipher = lst, P, Q
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
