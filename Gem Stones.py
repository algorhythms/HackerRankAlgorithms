"""
John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a
lowercase latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a
'gem-element' if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format
The first line consists of N, the number of rocks.
Each of the next N lines contain rocks' composition. Each composition consists of lowercase letters of English alphabet.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        return len(reduce(lambda x, y: x & y, [set(list(elt)) for elt in cipher]))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    number = int(f.readline().strip())
    cipher = []
    for t in xrange(number):
        # construct cipher
        cipher.append(f.readline().strip())

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
