"""
Shik loves sorted intervals. But currently he does not have enough time to sort all the numbers. So he decided to use
Almost sorted intervals. An Almost sorted interval is a consecutive subsequence in a sequence which satisfies the
following property:

The first number is the smallest.
The last number is the largest.
Please help him count the number of almost sorted intervals in this permutation.

Input Format
The first line contains an integer N.
The second line contains a permutation from 1 to N.
"""
__author__ = 'Danyang'
class Solution(object):
    def solve(self, cipher):
        """
        :type cipher: list
        :param cipher
        """
        #TODO


    def solve_error(self, cipher):
        """
        sliding window, error.
        :param cipher: the cipher
        """
        A = cipher
        N = len(A)
        start = 0
        end = 1 # [0, 1)
        cnt = 0
        while end<N:
            if A[end]>A[end-1]:
                end += 1
            else:
                cnt += self.count(start, end)
                start = end
                end += 1

        cnt += self.count(start, end)
        return cnt

    def count(self, start, end):
        l = end-start
        return (l+1)*l/2




if __name__=="__main__":
    import sys
    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())


    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n"%(Solution().solve(cipher))
    print s,