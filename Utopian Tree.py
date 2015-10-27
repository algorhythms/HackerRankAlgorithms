"""
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the monsoon, when it
doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find the height
of the tree after N growth cycles?
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N = int(cipher[0])
        # initial = 1  # wrong var name
        height = 1  # initialization
        for cycle in xrange(N):
            if cycle & 1 == 0:
                height *= 2
            else:
                height += 1

        return height


if __name__ == "__main__":
    import sys
    # f = open("1.in", "r")
    f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
