"""
Sherlock is given an array of N integers A0, A1 ... AN-1 by Watson. Now Watson asks Sherlock that how many different
pairs of indices i and j exist such that i is not equal to j but Ai is equal to Aj.

That is, Sherlock has to count total number of pairs of indices (i, j) where Ai = Aj AND i != j.

Input Format
First line contains T, the number of testcases. T test case follows.
Each testcase consists of two lines, first line contains an integer N, size of array.
Next line contains N space separated integers.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Hash
        :param cipher: the cipher
        """
        hm = {}
        cnt = 0
        for ind, val in enumerate(cipher):
            if val in hm:
                cnt += 2 * len(hm[val])
                hm[val].append(ind)
            else:
                hm[val] = [ind]
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = f.readline().strip()
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
