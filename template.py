__author__ = 'Danyang'
class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """


if __name__=="__main__":
    import sys
    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')

        # solve
        s = "%s\n"%(Solution().solve(cipher))
        print s,