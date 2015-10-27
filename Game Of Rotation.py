"""
Mark is an undergraduate student and he is interested in rotation. A conveyor belt competition is going on in the town
which Mark wants to win. In the competition, there's A conveyor belt which can be represented as a strip of 1xN blocks.
Each block has a number written on it. The belt keeps rotating in such a way that after each rotation, each block is
shifted to left of it and the first block goes to last position.

There is a switch near the conveyer belt which can stop the belt. Each participant would be given a single chance to
stop the belt and his PMEAN would be calculated.

PMEAN is calculated using the sequence which is there on the belt when it stops. The participant having highest PMEAN is
the winner. There can be multiple winners.

Mark wants to be among the winners. What PMEAN he should try to get which guarantees him to be the winner.

PMEAN=\sumi=1ni\timesa[i]
where a represents the configuration of conveyor belt when it is stopped. Indexing starts from 1.

Input Format
First line contains N denoting the number of elements on the belt.
Second line contains N space separated integers.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Math
        brute O(n^2)
        math O(n)+O(n)
        :param cipher: the cipher
        """
        A = cipher
        N = len(A)
        _sum = sum(A)
        _max = -1 << 65  # 64-bit

        s = 0
        for ind, val in enumerate(A):
            s += (ind + 1) * val

        _max = max(_max, s)
        for i in xrange(N):
            s = s + _sum - N * A[N - 1 - i]
            _max = max(_max, s)

        return _max


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())
    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
