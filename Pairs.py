"""
Given N integers, count the number of pairs of integers whose difference is K.

Input Format
The 1st line contains N & K (integers).
The 2nd line contains N numbers of the set. All the N numbers are distinct.

Output Format
An integer that tells the number of pairs of integers whose difference is K.

Constraints:
N <= 10^5
0 < K < 10^9
Each integer will be greater than 0 and at least K smaller than 2^31-1
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, K, lst = cipher

        hm = {}
        for val in lst:
            if val in hm:
                hm[val] += 1
            else:
                hm[val] = 1

        cnt = 0
        for val in lst:
            target = val + K
            if target in hm:
                cnt += hm[target]
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, K = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))
    cipher = N, K, lst
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
