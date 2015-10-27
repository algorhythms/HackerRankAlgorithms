"""
A 'Decent' Number has -

3 or 5 or both as its digits. No other digit is allowed.
Number of times 3 appears is divisible by 5.
Number of times 5 appears is divisible by 3.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, N):
        """
        mod

        :param cipher: the cipher
        """
        for i in xrange(N / 3 * 3, -1, -3):
            if (N - i) % 5 == 0:
                return "5" * i + "3" * (N - i)

        return "-1"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
