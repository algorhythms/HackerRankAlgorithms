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
        left[i] : the nearest (first) position left to i and with value larger than a[i] .
        right[i] : the nearest (first) position right to i and with value smaller than a[i] .
        use stack to find it.

        interval tree

        :param cipher:
        :return:
        """
        # TODO


    def solve_time_out(self, cipher):
        """
        chaining >, dp
        similar to find Find Maximum Index Product

        L[i] is the nearest item on the right larger than A[i]
        S[i] is the nearest item on the right smaller than A[i]
        :type cipher: list
        :param cipher
        """
        A = cipher
        L = [-1 for _ in A]
        S = [-1 for _ in A]
        for i in xrange(len(A) - 2, -1, -1):
            idx = i + 1
            while idx != -1:
                if A[idx] < A[i]:
                    idx = L[idx]
                else:
                    break
            L[i] = idx

            idx = i + 1
            while idx != -1:
                if A[idx] > A[i]:
                    idx = S[idx]
                else:
                    break
            S[i] = idx

        cnt = 0
        for i in xrange(len(A)):
            cnt += 1
            l = L[i]
            s = S[i]
            while l != -1 and (s == -1 or s > l):
                cnt += 1
                l = L[l]

        return cnt

    def solve_error(self, cipher):
        """
        sliding window, error.
        :param cipher: the cipher
        """
        A = cipher
        N = len(A)
        start = 0
        end = 1  # [0, 1)
        cnt = 0
        while end < N:
            if A[end] > A[end - 1]:
                end += 1
            else:
                cnt += self.count(start, end)
                start = end
                end += 1

        cnt += self.count(start, end)
        return cnt

    def count(self, start, end):
        l = end - start
        return (l + 1) * l / 2


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())

    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
