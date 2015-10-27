"""
You and your friend decide to play a game using a stack consisting of N bricks. In this game, you can alternatively
remove 1, 2 or 3 bricks from the top, and the numbers etched on the removed bricks are added to your score. You have to
play so that you obtain the maximum possible score. It is given that your friend will also play optimally and you make
the first move.

Input Format
First line will contain an integer T i.e. number of test cases. There will be two lines corresponding to each test case:
first line will contain a number N i.e. number of elements in the stack and next line will contain N numbers i.e.
numbers etched on bricks from top to bottom.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm: dp
        Current score is affect by the 3 moves and the previous corresponding scores
        Starting from the bottom of the stack (rather than top as the gaming sequence)
        A: f[i][0]
        B: f[i][1]

        index starting from 0:

        f[i][0] = max(sum(w[i-k+1, i]) + sum(w[1..i-k]) - f[i-k][1]) w.r.t k
        f[i][1] = max(sum(w[i-k+1, i]) + sum(w[1..i-k]) - f[i-k][0]) w.r.t k

        for f[i][1], i>=1
        :param cipher: the cipher
        """
        N, v = cipher
        v.reverse()  # start from the bottom
        # sum dp
        s = [0 for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            s[i] = s[i - 1] + v[i - 1]

        f = [[0, 0] for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            # f[i][0]
            local_max = 0
            for k in xrange(1, 4):
                if i - k >= 0:
                    local_max = max(local_max, s[i] - s[i - k] + s[i - k] - f[i - k][1])
            f[i][0] = local_max

            # if i==1: continue  # starting from the bottom
            # f[i][1]
            local_max = 0
            for k in xrange(1, 4):
                if i - k >= 0:
                    local_max = max(local_max, s[i] - s[i - k] + s[i - k] - f[i - k][0])
            f[i][1] = local_max

        return f[-1][0]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        lst = map(lambda x: int(x), f.readline().strip().split(" "))
        cipher = [N, lst]
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
