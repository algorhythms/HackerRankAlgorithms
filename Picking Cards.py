"""
Problem Statement

There are N cards on the table and each has a number between 0 and N. Let us denote the number on the ith card by ci.
You want to pick up all the cards. The ith card can be picked up only if at least ci cards have been picked up before
it. (As an example, if a card has a value of 3 on it, you can't pick that card up unless you've already picked up 3
cards previously) In how many ways can all the cards be picked up?
"""
__author__ = 'Danyang'
MOD = 1000000007


class Solution(object):
    def solve(self, cipher):
        """
        Multiplication
        Algorithms to increment the paths
        :param cipher: the cipher
        """
        N, A = cipher
        cnts = [0 for _ in xrange(N + 1)]
        for num in A:
            cnts[num] += 1

        if 0 not in cnts:
            return 0

        # set up
        result = 1
        paths = cnts[0]
        for i in xrange(1, N):
            if paths <= 0:
                return 0
            result *= paths  # Multiplication
            result %= MOD
            paths += cnts[i]
            paths -= 1  # fill the hole

        return result


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
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
