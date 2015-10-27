"""
Louise and Richard play a game. They have a counter set to N. Louise gets the first turn and the turns alternate
thereafter. In the game, they perform the following operations.

If N is not a power of 2, they reduce the counter by the largest power of 2 less than N.
If N is a power of 2, they reduce the counter by half of N.
The resultant value is the new N which is again used for subsequent operations.
The game ends when the counter reduces to 1, i.e., N == 1, and the last person to make a valid move wins.

Given N, your task is to find the winner of the game.

Update If they set counter to 1, Richard wins, because its Louise' turn and she cannot make a move.

Input Format
The first line contains an integer T, the number of testcases.
T lines follow. Each line contains N, the initial number set in the counter.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N = cipher
        turn = 0
        while N > 1:
            turn += 1
            if N & (N - 1) == 0:
                N /= 2
            else:
                num = 1
                while num < N:
                    num <<= 1
                num >>= 1
                N -= num

        if turn & 1 == 0:
            return "Richard"
        else:
            return "Louise"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
