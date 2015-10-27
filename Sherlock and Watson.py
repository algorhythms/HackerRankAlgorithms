"""
John Watson performs an operation called Right Circular Rotation on an integer array a0,a1 ... an-1. Right Circular
Rotation transforms the array from a0,a1 ... aN-1 to aN-1,a0,... aN-2.

He performs the operation K times and tests Sherlock's ability to identify the element at a particular position in the
array. He asks Q queries. Each query consists of one integer x, for which you have to print the element ax.

Input Format
The first line consists of 3 integers N, K and Q separated by a single space.
The next line contains N space separated integers which indicates the elements of the array A.
Each of the next Q lines contain one integer per line denoting x.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        algorithm: circular: original_index = (i-k)%N
        :param cipher: the cipher
        """
        N, K, Q, A, q = cipher

        result = []
        for i in q:
            result.append(A[(i - K) % N])

        return "\n".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, K, Q = map(int, f.readline().strip().split(' '))
    A = map(int, f.readline().strip().split(' '))

    q = []
    for i in xrange(Q):
        q.append(int(f.readline().strip()))

    cipher = N, K, Q, A, q


    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
